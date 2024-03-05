SELECT O.ANIMAL_ID, O.NAME
# SELECT *
FROM ANIMAL_INS AS I RIGHT JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL AND O.ANIMAL_ID IS NOT NULL
ORDER BY I.ANIMAL_ID