CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE roles (
    id INTEGER PRIMARY KEY,
    rolename TEXT UNIQUE
);

INSERT INTO roles (id, rolename) VALUES (1, 'admin');
INSERT INTO roles (id, rolename) VALUES (2, 'tutor');
INSERT INTO roles (id, rolename) VALUES (3, 'fresher');

CREATE TABLE users_roles (
    user_id INTEGER REFERENCES users,
    role_id INTEGER REFERENCES roles
);
