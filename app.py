from flask import Flask, render_template
from sqlalchemy import create_engine, func
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    protocol = "postgresql"
    username = "postgres"
    host = "localhost"
    port = 5432
    database_name = "project3"
    Password ="postgres"
    connection_string = f"{protocol}://{username}:{Password}@{host}:{port}/{database_name}"
    engine = create_engine(connection_string)  
    df = pd.read_sql("SELECT * FROM hospitals", con=engine)
    df = df[["Latitude", "Longitude"]].dropna()
    cord = [{"latitude": lat, "longitude": lon} for lat, lon in zip(df['Latitude'], df['Longitude']) ]
    return render_template("index.html", cord=cord)

if __name__ == "__main__":
    app.run(debug=True)