import csv
import os

from flask import Flask, jsonify, request

app = Flask(__name__)

DATA_PATH = os.environ.get("PROPERTY_DATA_PATH", "rets_property_sample.csv")


def load_properties():
    with open(DATA_PATH, newline="") as f:
        return list(csv.DictReader(f))


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/properties")
def list_properties():
    city = request.args.get("city")
    rows = load_properties()

    if city:
        rows = [
            r for r in rows
            if r.get("L_City", "").lower() == city.lower()
        ]

    return jsonify(rows[:50])


@app.route("/properties/<listing_id>")
def get_property(listing_id):
    rows = load_properties()

    match = next(
        (r for r in rows if r.get("L_ListingID") == listing_id),
        None
    )

    if not match:
        return jsonify(error="not found"), 404

    return jsonify(match)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


"""
CSV property data
      ↓
Python Flask app (python framework that allows python to become web server / API -> can respond when someone visits a URL) 
    app = Flask(__name__) -> create a web application using Flask. 
      ↓
API endpoints
    exposes 3 API endpoints: @app.route... 
        http://localhost:8080/health -> if someone visits they get status ok, can ask AWS to use /health to ask -> Is this server still alive? 
        if visit http://localhost:8080/properties -> reads csv and returns first 50 listings as JSON 
        if @app.route("/properties/<listing_id>") -> can do /properties/R100234 -> L_ListingID == "R100234" returns property if dosen't exist returns HTTP 404 Not Found Error 
        
      ↓
AWS infrastructure


Flask
= turns Python into a web/API application

@app.route(...)
= creates a URL endpoint

request
= receives information from the user/request

jsonify()
= sends JSON back

app.run(...)
= starts the server

"""
