DELIMITER //
CREATE FUNCTION verifyPasscode(aid INT, pass VARCHAR(50))
RETURNS BOOLEAN
DETERMINISTIC
BEGIN
	DECLARE idExists BOOLEAN;
	DECLARE isPassValid BOOLEAN;
    DECLARE accountPass VARCHAR(50);
        
    SELECT passcode, COUNT(*) <>  1 INTO accountPass, idExists
    FROM accounts WHERE accountID = aid;
    
    SET isPassValid = (accountPass = pass);
    
    IF idExists THEN RETURN isPassValid;
    ELSE RETURN FALSE;
    END IF;
END 
// DELIMITER ;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

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

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

DELIMITER //
CREATE FUNCTION borrowStatus(borrowDate DATETIME, returnDate DATETIME)
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
	CASE
		WHEN CURDATE() < DATE(returnDate) THEN RETURN 'Not Due';
		WHEN CURDATE() = DATE(returnDate) THEN RETURN 'Due';
		ELSE RETURN 'Overdue';
    END CASE;
    RETURN 'Good';
END
// DELIMITER ;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --