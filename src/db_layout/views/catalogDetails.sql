CREATE VIEW catalogDetails AS
SELECT
	catalogs.catalogID,
    title,
    author,
    releaseYear,
    GROUP_CONCAT(genre ORDER BY genreID SEPARATOR ', ') AS 'genres',
    media,
    stocks,
    ref
FROM catalogs
	INNER JOIN genres
    ON catalogs.catalogID = genres.catalogID
GROUP BY catalogs.catalogID;