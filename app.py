# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

#from config import username, password

#engine = create_engine(os.environ.get('DATABASE_URL', ''))

#engine = create_engine(f'postgresql://{username}:{password}@localhost:5433/petpals')
engine = create_engine("sqlite:///db.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Pet = Base.classes.pets

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():

    session = Session(engine)

    if request.method == "POST":
        name = request.form["petName"]
        lat = request.form["petLat"]
        lon = request.form["petLon"]

        pet = Pet(name=name, lat=lat, lon=lon)
        session.add(pet)
        session.commit()

        session.close()

        return redirect("/", code=302)

    return render_template("form.html")


@app.route("/api/pals")
def pals():

    session = Session(engine)

    results = session.query(Pet.name, Pet.lat, Pet.lon).all()

    names = [result[0] for result in results]
    lat = [result[1] for result in results]
    lon = [result[2] for result in results]

    pet_data = {
        "latitude": lat,
        "longitude": lon,
        "hover_text": names
    }

    session.close()

    return jsonify(pet_data)


if __name__ == "__main__":
    app.run()
