# Catalog-App
A web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users should have the ability to post, edit, and delete their own items.

# Instructions
## Prerequisites
* VirtualBox
* Vagrant
* Python 2.7

## Setup
* Install VirtualBox
* Install Vagrant
* Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
* Change the working directory to vagrant directory within newly created FSND-Virtual-Machine directory.
* Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here and unzip it and copy the file newsdata.sql into the  vagrant directory.
* Run the command vagrant up.
* Run command vagrant ssh to log in to the installed Linux VM.

## To Run
* Navigate to `cd/vagrant` as instructed in terminal
* The app imports requests which is not on this vm. Run sudo pip install requests
* Clone or download this repository and change the directory.
* Run python database_setup.py to create the database.
* Run Python items.py to add items
* Run python 'project.py'
* Open your webbrowser and visit http://localhost:8000/

# Components
- Routing and Templating done using Flask.
- Uses SQLAlchemy to communicate with the back-end database.
- RESTful API endpoints that return json files
- Uses Google Login to authenticate users
  - authenticated users can create, edit and delete their own items.
  
## JSON Endpoints
* Catalog JSON: `/catalog/JSON`
    - Displays the whole catalog. Categories and all items.
* Category Items JSON: `/catalog/<int:category_id>/items/JSON`
    - Displays items for a specific category    
