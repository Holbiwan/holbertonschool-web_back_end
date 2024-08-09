-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and stores the average score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER |

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    
    SET avg_score = (
        SELECT AVG(score)
        FROM corrections AS C
        WHERE C.user_id = user_id
    );
    
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END
|

DELIMITER ;

-- The procedure takes an integer user_id as input, updates the 
-- average_score field of the user with this id.
-- The average score is computed as the average of the scores of all 
-- the corrections of the user.
-- The procedure should be called with the id of the user for which the
-- average score should be computed.
-- The procedure should update the average_score field of the user with 
-- the computed average score.
-- The procedure should not return anything.

