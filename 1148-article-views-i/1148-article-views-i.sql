# Write your MySQL query statement below
SELECT author_id as id FROM Views
where author_id = viewer_id
GROUP BY id
ORDER BY id asc