# PythonFinal3500
Hannah's Python Final For Audubon Blue Bird Observations

# About Application
This application was designed for the use of the Eastern Blue Bird volunteer observers for the Audubon Society of Miami Valley. This app was developed for observers to be able to add, edit and delete observations. All users should be able to add information but will need specific permissions to edit or delete. There is also a graph and table to show an accumlated presentation of recent observation findings from 2017-2020. There is a table for users to see Recent Entries as well.

# Download Application
To download this application, click the green code button in the upper right hand corner. You can choose the download zip option or if you have you git clone set-up you may download it that way but copying the link, and pasting it in your terminal GitBash folder like so: git clone url link.

# Get Started
To use this application you will need to create a virtual environment. To help you set up your virutal environment here are two links for Mac users and Windows. As well as a link for downloading and installing PyCharm. You will also need to download Bulma. Bulma is used as a styling guide for this application. This application utilizes MySql Database. You will need to download mysql as well.
- Mac: https://opensource.com/article/19/6/python-virtual-environments-mac
- Windows: https://docs.python.org/3/library/venv.html
- Pycharm: https://www.jetbrains.com/help/pycharm/installation-guide.html
- Bulma: https://bulma.io/
- MySql:https://www.mysql.com/

After you have your virtual env going, Open up your Pycharm and start a New Project. You will then place or open up your downloaded code. You can than start the application. To start the application, in the terminal in pycharm type this:

## Windows
set FLASK_APP=project
set FLASK_DEBUG=1
flask run

## Mac
export FLASK_APP=project
export FLASK_DEBUG=1
flask run

# Application File Structure
flask_auth_app/
## project/
  ## static/
    ## styles/
         custom.css
         custom.css.map
    graphs.js
    small_logo_tr.png
    bird2.png
    bird3.png
    bird4.png
    bird5.png
   
 ## templates/
    - _formhelpers.html
    - base.html
    - edit-entry.html
    - entry.html
    - graph.html
    - helpuser.html
    - index.html
    - login.html
    - profile.html
    - signup.html
    - tables.html
##  __init__.py
- auth.py
- forms.py
- main.py
- models.py
- table.py

# Database Structure
Create database named flask and schema flask.
## user/
  - id
  - email
  - password
  - name
## entries/
  - bhid
  - date
  - id
  - numeggspres
  - alive
  - dead
  - activespecies
  - cowbird
  - repairs
  - comments
  - entryId
