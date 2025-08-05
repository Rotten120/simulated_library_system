CREATE VIEW accountDetails AS
SELECT
	accounts.accountID,
    accounts.username,
    REPEAT('*', LENGTH(accounts.passcode)) AS 'passcode',
    accPrivs.privType as 'privilege'
FROM accounts
	INNER JOIN accPrivs
    ON accounts.privID = accPrivs.privID;