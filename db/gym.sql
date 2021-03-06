DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS activities;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    membership VARCHAR(255),
    status VARCHAR(255)
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    day_of_week VARCHAR(255),
    time VARCHAR(255),
    capacity INT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id SERIAL REFERENCES members(id),
    activity_id SERIAL REFERENCES activities(id) ON DELETE CASCADE
);