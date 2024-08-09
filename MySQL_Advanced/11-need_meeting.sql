-- SQL script that creates a view need_meeting that lists all students 
-- with a score under 80 (strict) and either no last_meeting or a last_meeting 
-- more than 1 month ago.
DROP VIEW IF EXISTS need_meeting;

CREATE VIEW need_meeting AS
SELECT name 
FROM students
WHERE score < 80 
AND (last_meeting IS NULL 
OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
