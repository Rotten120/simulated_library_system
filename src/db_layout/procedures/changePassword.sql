DELIMITER //
CREATE PROCEDURE changePassword(IN accountID INT, IN newPasscode VARCHAR(50), IN oldPasscode VARCHAR(50))
BEGIN
	UPDATE accounts
    SET accounts.passcode = newPasscode
    WHERE
		accounts.accountID = accountID AND
        accounts.passcode = oldPasscode;
	
    IF ROW_COUNT() = 0 THEN
		SIGNAL SQLSTATE '45000'
        SET
			MESSAGE_TEXT = 'Incorrect Password',
            MYSQL_ERRNO = 50006;
    END IF;
END
// DELIMITER ;