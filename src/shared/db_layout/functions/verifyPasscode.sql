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