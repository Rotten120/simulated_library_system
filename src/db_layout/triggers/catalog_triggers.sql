DROP TRIGGER IF EXISTS rmvCatalog;

DELIMITER //
CREATE TRIGGER rmvCatalog BEFORE DELETE ON catalogs FOR EACH ROW
BEGIN
	DELETE FROM transacts
	WHERE catalogID = OLD.catalogID;
    
    DELETE FROM genres
    WHERE catalogID = OLD.catalogID;
END
// DELIMITER ;
