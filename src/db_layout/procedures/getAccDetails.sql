DELIMITER //
CREATE PROCEDURE getAccDetails(IN aid INT)
BEGIN
	SELECT
		accountID,
        username,
        passcode,
        privType
	FROM accounts
		INNER JOIN accprivs
        ON accounts.privID = accprivs.privID
	WHERE accountID = aid;
END
// DELIMITER ;