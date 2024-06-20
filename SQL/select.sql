--PRATICANDO SELECT
--selecionando todos os registros da tabela "usuarios"
SELECT * FROM usuarios;

--selecionando apenas o nome e o email dos usuários
SELECT nome, email FROM usuarios;

--selecionando os usuários que possuem o nome "João Silva"
SELECT * FROM usuarios WHERE nome = 'João Silva';

--selecionando os usuários que nasceram antes de uma determinada data
SELECT * FROM usuarios WHERE data_nascimento < '1990-01-01';
