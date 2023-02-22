#!/usr/bin/env python3
"""
Additional functionality


"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

from pathlib import Path
import pyreadstat
import dask.dataframe as dd
from dask.delayed import delayed




def dask_sas_reader(dir_or_file_path, chunksize):
    """Read SAS file(s) into Dask DataFrame

    * solution proposed in [github issue](https://github.com/dask/dask/issues/1233)
    * ex:
    ``` 
    dd_df = dask_sas_reader('my_sas_file.sas7bdat', chunksize=800000)
    dd_df.head()
    ```
    """
    #helper functions
    SAS_DATA_FILE_EXTENSIONS = ['.sas7bdat']

    def is_sas_file(filepath):
        rslt = None
        if filepath.is_file():
            #fixed_filepath = filepath.resolve()
            ext = filepath.suffix
            if ext in SAS_DATA_FILE_EXTENSIONS:
                rslt = True
            else:
                rslt = False
        else:
            rslt = False
        return rslt
            
    def get_sas_metadata(filepath):
        #read metadata only of the SAS file in order to find out the number of rows
        _, meta = pyreadstat.read_sas7bdat(filepath, disable_datetime_conversion=True, metadataonly=True)
        return meta
    
    def read_sas_chunk(offset):
        #reads a chunk of the sas file
        df, _ = pyreadstat.read_sas7bdat(filepath, disable_datetime_conversion=True, row_offset=offset, row_limit=chunksize)
        return df
    
    def get_list_of_sas_file_chunks(filepath, chunksize):
        #read chunks of a sas file and add to list
        meta = get_sas_metadata(filepath)

        #parallelize reading of chunks using `delayed()` and combine these in a dask dataframe
        dfs = []
        for chunk in range(0, meta.number_rows, chunksize):
            tmp_df = delayed(read_sas_chunk)(chunk)
            dfs.append(tmp_df)
        return dfs
    

    #workflow
    dir_or_file_path = Path(dir_or_file_path)
    check1 = dir_or_file_path.is_file()
    check2 = dir_or_file_path.is_dir()

    if check1:
        filepath = dir_or_file_path.resolve().__str__()
        dfs = get_list_of_sas_file_chunks(filepath, chunksize)
    elif check2:
        dirpath_files = dir_or_file_path.glob('**/*')
        sas_files = [file for file in dirpath_files if is_sas_file(file)]
        dfs = []
        for file in sas_files:
            filepath = file.resolve().__str__()
            dfs_lst = get_list_of_sas_file_chunks(filepath, chunksize)
            dfs.extend(dfs_lst)
    else:
        print(f'ERROR: `{ str(dir_or_file_path.resolve()) }` is not a sas file or directory of sas files')

    ddf = dd.from_delayed(dfs)
    return ddf