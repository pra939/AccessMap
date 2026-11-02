from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

JAVA_DIR = os.path.join(BASE, "java")
C_DIR = os.path.join(BASE, "c")

places = [
    "Main Gate",
    "Main Building",
    "Library",
    "Canteen",
    "Auditorium",
    "Parking Area"
]


@app.route("/")
def home():

    return """
    <html>
    <head>
        <title>AccessMap</title>
    </head>

    <body style="text-align:center; font-family:Arial;">

        <h1>ACCESSMAP</h1>

        <h3>Accessible Campus Navigation</h3>

        <form action="/route" method="post">

            <h3>Find Your Route</h3>

            Starting Location:
            <select name="start">
                """ + "".join(
                    f"<option>{p}</option>" for p in places
                ) + """

            </select>

            <br><br>

            Destination:
            <select name="end">
                """ + "".join(
                    f"<option>{p}</option>" for p in places
                ) + """

            </select>

            <br><br>

            <button type="submit">Find Route</button>

        </form>

        <hr>

        <h3>Accessibility Checker</h3>

        <form action="/score" method="post">

            <label>Ramp Available (1=Yes, 0=No)</label>
            <input type="number" name="ramp" min="0" max="1">

            <br><br>

            <label>Lift Available (1=Yes, 0=No)</label>
            <input type="number" name="lift" min="0" max="1">

            <br><br>

            <label>Accessible Washroom (1=Yes, 0=No)</label>
            <input type="number" name="toilet" min="0" max="1">

            <br><br>

            <button type="submit">Calculate Score</button>

        </form>

    </body>
    </html>
    """


@app.route("/route", methods=["POST"])
def route():

    start = request.form["start"]
    end = request.form["end"]

    result = subprocess.run(
        ["java", "-cp", JAVA_DIR,
         "RouteFinder", start, end],
        capture_output=True,
        text=True
    )

    return "<h2>Suggested Campus Route</h2><h3>" + \
           result.stdout + "</h3><a href='/'>Go Back</a>"


@app.route("/score", methods=["POST"])
def score():

    ramp = request.form["ramp"]
    lift = request.form["lift"]
    toilet = request.form["toilet"]

    executable = os.path.join(
        C_DIR,
        "accessibility.exe"
        if os.name == "nt"
        else "accessibility"
    )

    result = subprocess.run(
        [executable, ramp, lift, toilet],
        capture_output=True,
        text=True
    )

    return "<h2>Accessibility Result</h2><h3>" + \
           result.stdout + "</h3><a href='/'>Go Back</a>"


if __name__ == "__main__":
    app.run(debug=True)