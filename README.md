# gym_booking_system

This is a system for a gym to help them manage memberships, and register members for classes. The project uses the Python Flask framework and PostgreSQL for the database.
The project does not include any Javascript. Feedback always welcome.

### Link to app hosted on Heroku
https://tranquil-everglades-14428.herokuapp.com/

## Usage
Fork this project, or download it as a zip file then import into your IDE of choice. You will need Python, PostgreSQL and Flask to run this.

#### Install Flask using pip
```
pip install -U Flask
```

#### Create Gym Database
```
createdb gym
```

#### Run Gym SQL File
```
psql -d gym -f db/gym.sql
```

#### Run Console File
```
python3 console.py
```

#### Run Flask
```
flask run
```
#### App will run on localhost:5000




