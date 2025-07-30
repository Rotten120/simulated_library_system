CREATE VIEW transactDetails AS
SELECT
    transactID AS 'Transaction ID',
    accounts.username AS 'Username',
    catalogs.title AS 'Title',
    borrowStocks AS 'Copies Borrowed',
    borrowDate AS 'Borrow Date',
    returnDate AS 'Return Date',
    borrowStatus(borrowDate, returnDate) AS 'Status'
-- NOT SURE IF IT SHOULD BE INNER OR LEFT JOIN
FROM transacts
	INNER JOIN accounts
		ON transacts.accountID = accounts.accountID
	INNER JOIN catalogs
		ON transacts.catalogID = catalogs.catalogID
ORDER BY
    'Username',
    'Borrow Date';
    
    
CREATE VIEW catalogDetails AS
SELECT
	catalogs.catalogID,
    title,
    author,
    releaseYear,
    GROUP_CONCAT(genre ORDER BY genreID SEPARATOR ', ') AS 'genres',
    media,
    stocks,
    ref
FROM catalogs
	INNER JOIN genres
    ON catalogs.catalogID = genres.catalogID
GROUP BY catalogs.catalogID;


CREATE VIEW accountDetails AS
SELECT
	accounts.accountID,
    accounts.username,
    REPEAT('*', LENGTH(accounts.passcode)) AS 'passcode',
    accPrivs.privType as 'privilege'
FROM accounts
	INNER JOIN accPrivs
    ON accounts.privID = accPrivs.privID;