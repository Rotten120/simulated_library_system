DELIMITER //
CREATE PROCEDURE changeUsername(IN accountID INT, IN username VARCHAR(100), IN passcode VARCHAR(50))
BEGIN
	UPDATE accounts
    SET accounts.username = username
    WHERE
		accounts.accountID = accountID AND
        accounts.passcode = passcode;
	
    IF ROW_COUNT() = 0 THEN
		SIGNAL SQLSTATE '45000'
        SET
			MESSAGE_TEXT = 'Incorrect Password',
            MYSQL_ERRNO = 50002;
    END IF;
END
// DELIMITER ;