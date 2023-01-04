from flask import Flask, request,render_template
from sqlalchemy import create_engine, func
import pandas as pd

app = Flask(__name__)

@app.route("/")   # route to  main index page
def index():
    return render_template("index.html")

@app.route("/showmap")   # route to map page linking to showmapt html and logic js for map visualization
def home():
    protocol = "postgresql"
    username = "postgres"
    host = "localhost"
    port = 5432
    database_name = "project3"
    Password ="root"
    connection_string = f"{protocol}://{username}:{Password}@{host}:{port}/{database_name}"
    engine = create_engine(connection_string)  
    df = pd.read_sql("SELECT * FROM hospitals", con=engine)
    df = df[["latitude", "longitude","organisationname","county","city"]].dropna()
    cord = [{"latitude": lat, "longitude": lon, "oname":oname,"county":county,"city":city} for lat, lon,oname,county,city in zip(df['latitude'], df['longitude'],df['organisationname'],df['county'],df['city']) ]
    return render_template("showmapt.html", cord=cord)

@app.route("/showcountyplot") 
def showcountyplot():
    protocol = "postgresql"
    username = "postgres"
    host = "localhost"
    port = 5432
    database_name = "project3"
    Password ="root"
    connection_string = f"{protocol}://{username}:{Password}@{host}:{port}/{database_name}"
    engine = create_engine(connection_string)  
    df = pd.read_sql("SELECT distinct county  FROM hospitals", con=engine)
    #df = df[["latitude", "longitude","organisationname","county","city"]].dropna()
    data = [{"county":county} for county in zip(df['county'])]
    return render_template("showcountyplot.html", cord=data)


@app.route("/showcc", methods =["GET", "POST"])
def showcc():
    protocol = "postgresql"
    username = "postgres"
    host = "localhost"
    port = 5432
    database_name = "project3"
    Password ="root"
    connection_string = f"{protocol}://{username}:{Password}@{host}:{port}/{database_name}"
    engine = create_engine(connection_string)
    if request.method == "POST":
       # getting input with name = fname in HTML form
      county = request.form.get("c")
    df = pd.read_sql("SELECT distinct latitude, longitude, organisationname, county  FROM hospitals where county='" + county +"'", con=engine)
    #df = df[["latitude", "longitude","organisationname","county","city"]].dropna()
    data = [{"x": lat, "y": lon, "oname":oname,"county":county} for lat, lon,oname,county in zip(df['latitude'], df['longitude'],df['organisationname'],df['county']) ]
    cord=  [{
		"type": "scatter",
		"toolTipContent": "<b>Lattitude: </b>{x}<br/><b>Longitude: </b>{y}<br/><b>Name: </b>{oname}",
		"dataPoints": data}]
    return render_template("spcc.html",county=county, cord=cord)

@app.route("/showcounty")
def showcounty():
    protocol = "postgresql"
    username = "postgres"
    host = "localhost"
    port = 5432
    database_name = "project3"
    Password ="root"
    connection_string = f"{protocol}://{username}:{Password}@{host}:{port}/{database_name}"
    engine = create_engine(connection_string)  
    df = pd.read_sql("SELECT distinct county  FROM hospitals", con=engine)
    #df = df[["latitude", "longitude","organisationname","county","city"]].dropna()
    data = [{"county":county} for county in zip(df['county'])]
    return render_template("showcounty.html", cord=data)

@app.route("/showgov", methods =["GET", "POST"])
def showgov():
    protocol = "postgresql"
    username = "postgres"
    host = "localhost"
    port = 5432
    database_name = "project3"
    Password ="root"
    connection_string = f"{protocol}://{username}:{Password}@{host}:{port}/{database_name}"
    engine = create_engine(connection_string)
    if request.method == "POST":
       # getting input with name = fname in HTML form
      county = request.form.get("c")
    df = pd.read_sql("SELECT count(sector) as seccount  FROM hospitals where county='" + county + "' and sector='Independent Sector'", con=engine)
    #df = df[["latitude", "longitude","organisationname","county","city"]].dropna()
    data = [{"y":cnt,"label":"Independent Sector"} for cnt in zip(df['seccount'])]
    dff = pd.read_sql("SELECT count(sector) as seccount  FROM hospitals where county='" + county + "' and sector!='Independent Sector'", con=engine)
    #df = df[["latitude", "longitude","organisationname","county","city"]].dropna()
    data = data + [{"y":cnt,"label":"Non - Independent Sector"} for cnt in zip(dff['seccount'])]
    return render_template("showgovc.html",county=county, cord=data)


if __name__ == "__main__":
    app.run(debug=True)
