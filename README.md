# AI for Banking and Finance

This uses conda environments not typical pipenv vms.

## TOC

_DS Tools_

* Fundamentals of computing
  - 
* Dataframe structure
  - R / Py
  - Differences
  - Oddities
* Data visualization
  - Background
  - Ggplot
  - Extensions
* Big data and frameworks
  - Spark
  - Dask
* Migrating from legacy tools
  - AWS
  - Different file formats
  - SAS
  - Alternatives to SQL


_Data and Domains_

* Economic data sources 
  - FRED
  - NBER
  - BLS
  - FFIEC

* Financial data
  - SEC
  - CFTC


_Theory and Mathematics_





## Install and Build

This project is focused on conda venv (pip may not work):

* create a conda virtual environment with: `conda create --name base --file requirements.txt`
* start the environment with: `source activate base`
* use in conda env by: `conda list -e > requirements.txt`
* use in pip env by: `pip list --format=freeze > requirements.txt`


### Review Book theme

Written with MyST Markdown, [ref](https://sphinx-book-theme.readthedocs.io/en/stable/tutorials/get-started.html)


### Build SSG Book

```
jupyter-book build mybookname/
```


### Build PDF

Install pyppeteer for html to [pdf workflow](https://jupyterbook.org/en/stable/advanced/pdf.html)
```
pip install pyppeteer
```

Install pyppeteer dependencies
```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update 
sudo apt install google-chrome-stable
sudo apt install libxss1
```

Build pdf
```
jupyter-book build mynewbook/ --builder pdfhtml
```


## Previously Used Materials

* notes_Data_Pandas-Basic.ipynb
* notes_Data_Pandas-Plots.ipynb
* notes_Data_Pandas-Rpy.ipynb
* blog_ds-intro_numpy_pandas.ipynb
* blog_ds-dataframe_r_and_pandas


## TODO

* cells should have key-val for display/hide with respect to what will be added to jupyterbook