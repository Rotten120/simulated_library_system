DROP PROCEDURE IF EXISTS updateStocks;

DELIMITER //
-- positive deltaStocks: returning copies
-- negative deltaStocks: borrowing copies
CREATE PROCEDURE updateStocks (IN cid INT, IN deltaStocks INT)
BEGIN
	DECLARE availableStocks INT;
    DECLARE updatedStocks INT;
	
	-- CHECKS FIRST IF THE COPIES TO BORROW ARE LOWER THAN THE AVAILABLE COPIES
    
	SELECT stocks INTO availableStocks
    FROM catalogs WHERE catalogID = cid;
    
    SET updatedStocks = availableStocks + deltaStocks;
    
    IF updatedStocks < 0 THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'You are borrowing more stocks than what is available';
    END IF;
    
    -- IF SO, THEN UPDATE THE CATALOG STOCKS
    
    UPDATE catalogs
    SET stocks = updatedStocks
    WHERE catalogID = cid;
END
// DELIMITER ;