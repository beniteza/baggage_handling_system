from flask import render_template, jsonify
from ApplicationLayer.CheckInAreaUserHandler import CheckInAreaUserHandler
from ApplicationLayer.AirlineLoadingAreaUserHandler import AirlineLoadingAreaUserHandler
from ApplicationLayer.TechnicianAreaUserHandler import TechnicianAreaUserHandler
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
    return CheckInAreaUserHandler().checkInBag()


@app.route('/placeBagIntoCB', methods=['POST'])
def placeBagIntoCB():
    return CheckInAreaUserHandler().placeBagIntoCB()


@app.route('/scanBagTag', methods=['POST'])
def scanBag():
    return AirlineLoadingAreaUserHandler().scanBagTag()


@app.route('/bagsInLoadingArea')
def getAllBagsInAirlineLoadingArea():
    return AirlineLoadingAreaUserHandler().getAllBagsInAirlineLoadingArea()


@app.route('/getJammedSignal')
def getJammedSignal():
    return TechnicianAreaUserHandler().getJammedSignal()


@app.route('/sendUnjammedSignal', methods=['POST'])
def sendUnjammedSignal():
    return TechnicianAreaUserHandler().sendUnjammedSignal()


@app.route('/bagsReachedLoadingArea', methods=['POST'])
def bagsReachedLoadingArea():
    return CBSControllerHandler().bagsReachedLoadingArea()


@app.route('/jammed', methods=['POST'])
def jammed():
    return CBSControllerHandler().jammed()


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
