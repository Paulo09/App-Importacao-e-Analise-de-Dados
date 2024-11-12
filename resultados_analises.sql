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
