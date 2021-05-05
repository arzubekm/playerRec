# playerec
Player recommendation (playerec) project is build using [Flask](http://flask.pocoo.org/). It is a simple FIFA21 player recommendation application which shows five similar players that could replace your inputted player (overall rating >= 66). The application model uses K-nearest algorithm (KNN) based on [FIFA21 kaggle] (https://www.kaggle.com/stefanoleone992/fifa-21-complete-player-dataset?select=players_21.csv) dataset.

## Setup
### Install and initialize virtual environment
```
pip install virtualenv
python -m venv env
source env/bin/activate
```
### Install required libraries
```
pip install -r requirements.txt
```
### Clone the project
```
git clone https://github.com/arzubekm/playerRec.git
```
### Run the app
```
cd playerRec
export FLASK_APP=app.py
flask run
```
### Access the app
You can open the app in your browser by typing http://127.0.0.1:5000/

Also, it is hosted on Heroku: [https://player-rec.herokuapp.com/](https://player-rec.herokuapp.com/)
