-- 코드를 입력하세요
SELECT P2.ID, P2.NAME, P2.HOST_ID
FROM PLACES as P2
WHERE P2.HOST_ID IN ( SELECT P.HOST_ID
                    FROM PLACES as P
                    GROUP BY P.HOST_ID
                    HAVING COUNT(*) >= 2)
ORDER BY P2.ID;