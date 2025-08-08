DELIMITER //
CREATE PROCEDURE changePrivilege(IN accountID INT, IN privID INT, IN passcode VARCHAR(50))
BEGIN
	UPDATE accounts
    SET accounts.privID = privID
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