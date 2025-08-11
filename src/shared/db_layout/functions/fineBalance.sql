DELIMITER //
CREATE FUNCTION fineBalance (transactID INT)
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE borrowDate DATETIME;
    DECLARE returnDate DATETIME;
    DECLARE dateStatus VARCHAR(20);
    DECLARE borrowStocks INT;
    DECLARE lateFine INT;
    
    SELECT
		accprivs.lateFine,
		transacts.borrowDate,
        transacts.returnDate,
        transacts.borrowStocks
    INTO
		lateFine,
		borrowDate,
        returnDate,
        borrowStocks
    FROM transacts
		INNER JOIN accounts
			ON transacts.accountID = accounts.accountID
        INNER JOIN accprivs
			ON accounts.privID = accprivs.privID
    WHERE transacts.transactID = transactID;
    
    IF dateStatus = 'Overdue' THEN
		RETURN DATEDIFF(returnDate, borrowDate) * lateFine * borrowStocks;
    END IF;
    
    RETURN 0;
END
// DELIMITER ;