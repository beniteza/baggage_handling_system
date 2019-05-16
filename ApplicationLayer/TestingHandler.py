from flask import request, jsonify
from DomainLayer.Testing import Testing


class TestingHandler:
    def test_checkInBag(self):
        passengerId = request.form['passengerId']
        flightId = request.form['flightId']
        weight = request.form['weight']
        classService = request.form['classService']
        bag = Testing().test_checkInBag(passengerId, flightId, weight, classService)
        return jsonify(bag)
