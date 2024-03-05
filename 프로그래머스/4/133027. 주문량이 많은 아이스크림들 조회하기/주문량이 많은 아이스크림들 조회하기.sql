SELECT F.FLAVOR
FROM FIRST_HALF AS F JOIN JULY AS J USING(FLAVOR)
GROUP BY F.FLAVOR
ORDER BY (F.TOTAL_ORDER + SUM(J.TOTAL_ORDER)) DESC
LIMIT 3