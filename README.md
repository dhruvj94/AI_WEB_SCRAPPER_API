This API will help you to use Streamlit with selenium to scrape websites using Google Chrome

we have used pandas to scrape tables out of the website

## Steps for manual implementation
- download chromedriver of same version as of your google chrome browser version and add to your project directory
- make sure you have miniconda or anaconda downloaded and set path in environment variables
- use that to create new python environment in your ide Example: VS code (Visual Studio code)
- activate environment
- make a requirements.txt file and add all packages that are needed
- pip install uv for fast download and installation of packages
- Install all packages using "uv pip install -r requirements.txt"
- make scrape.py file and add code
- make main.py add code
- open cmd for windows and run command "streamlit run main.py"
- add your website in streamlit app opened in chrome and click scrape
- maggic starts

### Adding to gitub repository
-add .gitignore file in your folder and
- create new github repo
- use all suggested commands in your cmd/bash from github repo
-all done

## Experimentations

### 1
Here we first we used scrape.py where we scrapped website and  with help of for loop got table 0 from website in file good.txt

### 2
Next we used scrape1.py where we deleted headers and droped NA plus we printed all the tables in terminal

### 3 
We used scrape2.py to get good2.txt where we get all the tables with table number but not the names of the tables

### 4
We used scrape3.py to get good3.txt where we get all the tables but with names of table using bs4 to scrape the names of tables got error
#### IndexError: list index out of range