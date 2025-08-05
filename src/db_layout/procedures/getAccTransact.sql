DELIMITER //
CREATE PROCEDURE getAccTransact(IN aid INT)
BEGIN
	SELECT
		t.transactID AS 'Transaction ID',
        c.title AS 'Title',
        c.author AS 'Author',
        t.borrowStocks AS 'Copies Borrowed',
        t.borrowDate AS 'Borrow Date',
        t.returnDate AS 'Return Date',
        borrowStatus(t.borrowDate, t.returnDate) AS 'Status',
        fineBalance(t.transactID) AS 'Fine'
	FROM transacts t
		INNER JOIN accounts a
			ON t.accountID = a.accountID
		INNER JOIN catalogs c
			ON t.catalogID = c.catalogID
	WHERE t.accountID = aid
	ORDER BY
		'Return Date';
END
// DELIMITER ;