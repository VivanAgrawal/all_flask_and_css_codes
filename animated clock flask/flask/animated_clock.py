import os
from flask import Flask, render_template, request, jsonify
import pytz
from datetime import datetime
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        country_name = request.form.get("country_name")
        try:
            timezone = pytz.timezone(country_name)
            return render_template("index.html", country_name=country_name, timezone=timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            return "Invalid country name or timezone not found."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
