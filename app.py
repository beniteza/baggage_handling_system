from flask import render_template, jsonify
from ApplicationLayer.ClerkHandler import ClerkHandler
from ApplicationLayer.LoaderHandler import LoaderHandler
from ApplicationLayer.TechnicianHandler import TechnicianHandler
from ApplicationLayer.CBSControllerHandler import CBSControllerHandler
from InfrastructureLayer.DBconfig import DatabaseConfig
import os
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


@app.route('/')
def index():
    return jsonify('Welcome to the Software Design Project: Baggage Handling System')


@app.route('/checkInBag', methods=['POST'])
def checkInBag():
    return ClerkHandler().checkInBag()


@app.route('/placeBagIntoCB', methods=['POST'])
def placeBagIntoCB():
    return ClerkHandler().placeBagIntoCB()


@app.route('/scanBagTag', methods=['POST'])
def scanBag():
    return LoaderHandler().scanBagTag()


@app.route('/bagsInLoadingArea', methods=['POST'])
def getAllBagsInAirlineLoadingArea():
    return LoaderHandler().getAllBagsInAirlineLoadingArea()


@app.route('/getJammedSignal')
def getJammedSignal():
    return TechnicianHandler().getJammedSignal()


@app.route('/sendUnjammedSignal', methods=['POST'])
def sendUnjammedSignal():
    return TechnicianHandler().sendUnjammedSignal()


@app.route('/routeBags', methods=['POST'])
def routeBags():
    return CBSControllerHandler().routeBags()


@app.route('/jammed', methods=['POST'])
def jammed():
    return CBSControllerHandler().jammed()


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
