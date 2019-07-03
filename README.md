# Pitches

## Description
This is a web application that allows users to sign up, log in ad post pitches which other users can ccomment on, upvote or downvote. They can choose which category to write a pitch in and can view and comment on other users' pitches.

### By: ANTONY MWANIKI

## Prerequisites
1. python3.6
2. pip
3. Virtual environment(virtualenv)

## Cloning and running
Clone the application using git clone(this copies the app onto your device). In your terminal:

    $ git clone https://github.com/amwaniki/pitches.git
    $ cd pitches
    
Creating the virtual environment

    $ python3.6 -m venv --without-pip virtual
    $ source virtual/bin/env
    $ curl https://bootstrap.pypa.io/get-pip.py | python
    
Installing Flask and other Modules

    $ python3.6 -m pip install Flask
    $ python3.6 -m pip install Flask-Bootstrap
    $ python3.6 -m pip install Flask-Script
    
Run the application:

    $ chmod a+x start.sh
    $ ./start.sh
    
Testing the Application
To run the tests for the class files:

    $ python3.6 manage.py test
    
## Technologies Used
1. Python 3.6
2. Flask

## BDD
|Behaviour	             | Input	                         | Output                                                |
|------------------------|---------------------------------|-------------------------------------------------------|
|View Categories	       | Click on category               | A list of pitches in that category is displayed       |
|Add a new pitch         | click on pitch                  | Authentification page is displayed and user can pitch |
|Add a comment           | Click on comment                | Comment form is displayed and user can comment        |
|Upvote pitch            | Click on upvote                 | Pitch gets +1 upvote                                  |
|Downvote pitch          | Click on downvote               | Pitche gets +1 downvote                               |

## Contact Information
For any questions, troubleshooting or contributions, find me on:
Email: amwaniki180@gmail.com


## License
MIT License Copyright (c) {2019} ANTONY MWANIKI
