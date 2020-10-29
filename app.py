from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

from controllers.members_controller import members_blueprint
from controllers.activities_controller import activities_blueprint
from controllers.bookings_controller import bookings_blueprint

app = Flask(__name__)
# db = SQLAlchemy(app)

app.register_blueprint(members_blueprint)
app.register_blueprint(activities_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()