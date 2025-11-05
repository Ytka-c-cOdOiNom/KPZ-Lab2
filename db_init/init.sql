
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE
);


INSERT INTO users (username)
SELECT 'Alice'
WHERE NOT EXISTS (SELECT 1 FROM users WHERE username = 'Alice');

INSERT INTO users (username)
SELECT 'Bob'
WHERE NOT EXISTS (SELECT 1 FROM users WHERE username = 'Bob');

INSERT INTO users (username)
SELECT 'Charlie'
WHERE NOT EXISTS (SELECT 1 FROM users WHERE username = 'Charlie');