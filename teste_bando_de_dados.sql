USE teste_banco_de_dados;
CREATE TABLE IF NOT EXISTS cliente (id_nome smallint primary key auto_increment, nome VARCHAR(100) NOT NULL, sexo char(1) NOT NULL check (sexo IN ('m','f')), nascimento datetime) auto_increment = 1, ENGINE=InnoDB;
show tables;
select * from cliente;