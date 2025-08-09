DELIMITER //
CREATE PROCEDURE deleteAccount(IN accountID INT, IN passcode VARCHAR(50))
BEGIN
	DECLARE borrowStocks INT;
	
    SELECT SUM(transacts.borrowStocks) INTO borrowStocks
    FROM transacts WHERE transacts.accountID = aid;
    
    IF borrowStocks <> 0 THEN
		SIGNAL SQLSTATE '45000'
        SET
			MESSAGE_TEXT = 'Cannot delete. Account has unreturned catalogs',
			MYSQL_ERRNO = 50012;
    END IF;
    
    DELETE FROM accounts
    WHERE
		accounts.accountID = accountID AND
        accounts.passcode = passcode;
        
	IF ROW_COUNT() = 0 THEN
		SIGNAL SQLSTATE '45000'
        SET
			MESSAGE_TEXT = 'Incorrect Password',
            MYSQL_ERRNO = 50006;
    END IF;
END
// DELIMITER ;