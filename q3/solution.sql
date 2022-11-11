SELECT *
FROM article_id as a INNER JOIN category_artical_mapping as cam INNER JOIN category as c INNER Join owner as o
    ON a.owner_id = o.owner_id AND a.article_id = cam.article_id AND cam.category_id = c.category_id
GROUP BY article_id
ORDER BY COUNT DISTINCT catergory_id