# Write your MySQL query statement below
SELECT score,
    @rank := (@rank + (@prev <> (@prev := score))) `Rank`
FROM Scores,
    (
        SELECT @rank := 0,
            @prev := -1
    ) init
ORDER BY score DESC