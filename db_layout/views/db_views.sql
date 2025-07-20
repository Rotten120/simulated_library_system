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