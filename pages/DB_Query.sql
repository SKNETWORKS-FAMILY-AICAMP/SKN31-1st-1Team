-- faq table
CREATE TABLE IF NOT EXISTS car_faq (
    faq_id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    site VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS car_info (
	car_id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(50), 
    model VARCHAR(50), 
    car_year INT NOT NULL, 
    mileage INT NOT NULL, 
    price INT NOT NULL
);