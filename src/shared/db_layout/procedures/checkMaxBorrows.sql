DELIMITER //
CREATE PROCEDURE checkMaxBorrows(IN aid INT, IN borrowed INT)
BEGIN
	DECLARE maxBorrows INT;
    DECLARE accBorrows INT;
    
    SELECT accPrivs.maxBorrows INTO maxBorrows
    FROM accounts
		INNER JOIN accPrivs
        ON accounts.privID = accPrivs.privID
	WHERE accounts.accountID = aid;
    
    SELECT SUM(transacts.borrowStocks) + borrowed INTO accBorrows
    FROM transacts WHERE transacts.accountID = aid;
    
    IF accBorrows > maxBorrows THEN
		SIGNAL SQLSTATE '45000'
        SET
			MESSAGE_TEXT = 'Exceed allowed borrow count',
            MYSQL_ERRNO = 50008;
	END IF;
END
// DELIMITER ;