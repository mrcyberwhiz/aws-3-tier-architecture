show DATABASES;

use threetadatabase;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO users (username, password, email) 
VALUES 
('Dhanush', 'Dhanush123#', 'dhanush@example.com'),
('Mithran', 'Mithran123#', 'Mithran@example.com'),
('Kamal', 'Kamal123#', 'kamal@example.com'),
('Raj', 'Raj123#', 'raj@example.com');

SELECT * FROM users;