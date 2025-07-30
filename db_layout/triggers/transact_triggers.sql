DROP TRIGGER IF EXISTS delTransacts;
DROP TRIGGER IF EXISTS addTransacts;
DROP TRIGGER IF EXISTS editTransacts;

DELIMITER //
CREATE TRIGGER delTransacts BEFORE DELETE ON transacts FOR EACH ROW
BEGIN
	CALL updateStocks(OLD.catalogID, OLD.borrowStocks);
END
// DELIMITER ; 

DELIMITER //
CREATE TRIGGER addTransacts BEFORE INSERT ON transacts FOR EACH ROW
BEGIN
	IF NEW.borrowDate IS NULL THEN
		SET NEW.borrowDate = CURRENT_TIMESTAMP();
        SET NEW.returnDate = ADDDATE(NEW.borrowDate, INTERVAL 1 MONTH);
	END IF;
    
    IF NEW.borrowStocks IS NULL THEN
		SET NEW.borrowStocks = 1;
	ELSEIF NEW.borrowStocks <= 0 THEN
		SIGNAL SQLSTATE '45000'
		SET
			MESSAGE_TEXT = 'Invalid value to borrow',
            MYSQL_ERRNO = 50003;
    END IF;

	CALL checkMaxBorrows(NEW.accountID, NEW.borrowStocks);
	CALL updateStocks(NEW.catalogID, -NEW.borrowStocks);
END
// DELIMITER ; 

DELIMITER //
CREATE TRIGGER editTransacts BEFORE UPDATE ON transacts FOR EACH ROW
BEGIN
	IF NEW.borrowStocks <= 0 THEN
		SIGNAL SQLSTATE '45000'
		SET
			MESSAGE_TEXT = 'Invalid value to borrow',
            MYSQL_ERRNO = 50003;
	END IF;
    
    IF NEW.catalogID <> OLD.catalogID THEN
		SIGNAL SQLSTATE '45000'
        SET
			MESSAGE_TEXT = 'CatalogID cannot be changed',
            MYSQL_ERRNO = 50004;
	ELSE
		CALL updateStocks(OLD.catalogID, OLD.borrowStocks - NEW.borrowStocks);
	END IF;
END
// DELIMITER ;