CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO items (name)
SELECT 'Item 1 (from Database)'
WHERE NOT EXISTS (SELECT 1 FROM items WHERE name = 'Item 1 (from Database)');

INSERT INTO items (name)
SELECT 'Item 2 (from Database)'

WHERE NOT EXISTS (SELECT 1 FROM items WHERE name = 'Item 2 (from Database)');
