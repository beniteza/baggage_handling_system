from flask import render_template, jsonify
from ApplicationLayer.CheckInAreaUserHandler import CheckInAreaUserHandler
from ApplicationLayer.AirlineLoadingAreaUserHandler import AirlineLoadingAreaUserHandler
from InfrastructureLayer.DBconfig import DatabaseConfig
import os

app = DatabaseConfig()


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


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
