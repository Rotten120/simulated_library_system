DELIMITER //
CREATE PROCEDURE getCatDetails(IN cid INT)
BEGIN
	SELECT
		catalogs.catalogID,
        title,
        author,
        releaseYear,
        GROUP_CONCAT(genre ORDER BY genreID SEPARATOR ', ') as 'genres',
        media,
        stocks,
        ref
	FROM catalogs
		INNER JOIN genres
        ON catalogs.catalogID = genres.catalogID
	WHERE catalogs.catalogID = cid
	GROUP BY catalogs.catalogID;
END
// DELIMITER ;