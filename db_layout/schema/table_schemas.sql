CREATE TABLE catalogs (
	catalogID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    stocks INT,
    ref VARCHAR(150)
);

CREATE TABLE accounts (
	accountID INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,	
    passcode VARCHAR(50) NOT NULL,
    privilege ENUM('Basic', 'Student', 'Instructor', 'Staff') DEFAULT ('Basic') 
);

CREATE TABLE transacts (
	transactID INT AUTO_INCREMENT PRIMARY KEY,
    accountID INT,
    catalogID INT,
    borrowStocks INT,
    borrowDate DATETIME,
    returnDate DATETIME,
    FOREIGN KEY (accountID) REFERENCES accounts(accountID),
    FOREIGN KEY (catalogID) REFERENCES catalogs(catalogID)
);
