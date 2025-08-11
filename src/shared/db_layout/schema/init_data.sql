INSERT INTO catalogs (title, author, genre, stocks, ref)
VALUES
	('How to Basics', 'Zedric', 'Comedy', 2, 'https://www.ebooks.com/How_to_Basics'),
    ('Cats and Dogs', 'James Neil', 'Novel', 1, 'https://novelty.com/cats_and_dogs'),
    ('Art of Hacking', 'Baiza', 'Coding', 1, 'https://www.ebooks.com/Art_of_Hacking'),
    ('Basics of Assembly', 'Arthur Kent', 'Coding', 4, 'https://books.com/011204'),
    ('Lemons', 'Kenshi Yonezu', 'Romance', 2, 'https://jcatalogs.com/lemons');
	
INSERT INTO accounts (username, passcode, privilege)
VALUES
	('Zedric', 'secret', 'Student'),
    ('Von', 'library', 'Basic');

INSERT INTO transacts (accountID, catalogID, borrowStocks, borrowDate, returnDate)
VALUES
	(1, 2, 1, '2025-07-14 15:31:38', '2025-08-14 15:31:38'),
	(1, 4, 2, '2025-07-14 15:31:38', '2025-08-14 15:31:38'),
	(2, 1, 1, '2025-07-14 15:31:38', '2025-08-14 15:31:38');