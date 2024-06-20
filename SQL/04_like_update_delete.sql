--PRATICANDO LIKE
SELECT * FROM usuarios WHERE nome LIKE '%Silva%';
SELECT * FROM usuarios WHERE nome LIKE 'Jo_o%';

--PRATICANDO UPDATE
UPDATE usuarios SET endereco = 'Nova Rua, 123' WHERE email = 'joao@example.com';

--PRATICANDO DELETE
DELETE FROM reservas WHERE status = 'cancelada';
