DELIMITER //
CREATE FUNCTION getAccountID(accname VARCHAR(100), pass VARCHAR(50))
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE userid INT;
    DECLARE userpassword VARCHAR(50);
    
	SELECT accountID, passcode INTO userid, userpassword
    FROM accounts WHERE username = accname;
    
    IF userid IS NULL THEN
		SIGNAL SQLSTATE '45000'
        SET
			MESSAGE_TEXT = "Username does not exist",
            MYSQL_ERRNO = 50001;
	ELSEIF NOT pass = userpassword THEN
		SIGNAL SQLSTATE '45000'
        SET
			MESSAGE_TEXT = "Incorrect password",
            MYSQL_ERRNO = 50002;
	ELSE
		RETURN userid;
	END IF;
END
// DELIMITER ;