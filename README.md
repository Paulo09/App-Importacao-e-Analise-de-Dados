** Criar uma arquitetura de armazenamento de dados **

As análises anteriores foram feitas acessando diretamente as base de dados de
origem, agora faz-se necessário a criação de uma arquitetura de armazenamento
de dados desacoplada dos dados de origem.
1 - Criar um banco de dados para armazenar os resultados da análises.
2 - Desenvolver código python para ler as análises e salvar na nova estrutura dedados.
3 - Os códigos deverão estar num arquivo de extensão .py
4 - A execução de forma repetitiva não pode duplicar os dados

Instalação Pandas
# pip install pandas

* Criar Database - Postgres

-- Database: analises_db

-- DROP DATABASE analises_db;

CREATE DATABASE analises_db
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'Portuguese_Brazil.1252'
       LC_CTYPE = 'Portuguese_Brazil.1252'
       CONNECTION LIMIT = -1;

# Cirar Tabela : 

-- Table: resultados_analises

-- DROP TABLE resultados_analises;

CREATE TABLE resultados_analises
(
  nome_analise "char"[],
  data_analise date[]
)
WITH (
  OIDS=FALSE
);
ALTER TABLE resultados_analises
  OWNER TO postgres;
