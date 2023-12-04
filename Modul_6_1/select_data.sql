SELECT id, name as fullname
FROM contacts c 
WHERE favorite != TRUE 
ORDER BY fullname
LIMIT 5;

SELECT name, email
FROM users u 
WHERE age IN (20, 30, 40)
ORDER BY name;

SELECT name, email
FROM users u 
WHERE age BETWEEN 32 AND 40
ORDER BY name;

SELECT name, email
FROM users u 
WHERE age NOT BETWEEN 32 AND 40
ORDER BY name;

SELECT name, email
FROM users u 
WHERE age >= 32 AND age <= 40
ORDER BY name;

SELECT name, email
FROM contacts c  
WHERE name LIKE "%L%"
ORDER BY name;

SELECT name, email
FROM contacts c  
WHERE name LIKE "_y%"
ORDER BY name;

SELECT name, email
FROM contacts c  
WHERE name LIKE "% R%"
ORDER BY name;

SELECT COUNT(user_id) as total, user_id 
FROM contacts c  
GROUP BY user_id;

--Знайти всі контакти для користувачів вік яких меньше 35 років
SELECT *
FROM contacts c 
WHERE user_id IN (
	SELECT id 
	FROM users u 
	WHERE age < 35
);

SELECT c.name comtact_name, c.email contact_email, c.phone contact_phone, u.name , u.email 
FROM contacts c 
JOIN users u ON u.id = c.user_id;

SELECT c.name comtact_name, c.email contact_email, c.phone contact_phone, u.name , u.email 
FROM contacts c 
LEFT JOIN users u ON u.id = c.user_id;

UPDATE contacts SET user_id = 3 WHERE id = 5;