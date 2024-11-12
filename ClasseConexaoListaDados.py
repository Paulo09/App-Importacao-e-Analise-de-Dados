import psycopg2
import json
import pandas as pd
from datetime import datetime

# Função para conectar ao banco de dados PostgreSQL
# @PauloCastro

def conectar_db():
    try:
        conn = psycopg2.connect(
            dbname="analises_db",  # Nome do banco de dados
            user="seu_usuario",    # Nome do usuário
            password="sua_senha",  # Senha do banco de dados
            host="localhost",      # Endereço do servidor (localhost ou IP do servidor)
            port="5432"            # Porta do PostgreSQL
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para salvar a análise no banco de dados
def salvar_analise(nome_analise, resultado_analise):
    conn = conectar_db()
    if conn is None:
        return

    # Convertendo o resultado para JSON
    resultado_json = json.dumps(resultado_analise)

    # Comando SQL para inserir os dados
    try:
        cursor = conn.cursor()

        # Verificando se a análise já foi salva para o mesmo nome e data
        cursor.execute("""
            SELECT 1 FROM resultados_analises
            WHERE nome_analise = %s AND data_analise::date = %s
        """, (nome_analise, datetime.now().date()))

        if cursor.fetchone() is None:
            # Inserir nova análise
            cursor.execute("""
                INSERT INTO resultados_analises (nome_analise, resultado)
                VALUES (%s, %s)
            """, (nome_analise, resultado_json))

            conn.commit()
            print(f"Análise '{nome_analise}' salva com sucesso.")
        else:
            print(f"Análise '{nome_analise}' já foi salva para hoje.")

        cursor.close()
    except Exception as e:
        print(f"Erro ao salvar análise: {e}")
    finally:
        conn.close()

# Função para ler as análises e salvar no banco
def ler_e_salvar_analises(caminho_arquivo):
    # Análises sejam armazenadas em um arquivo CSV
    try:
        df = pd.read_csv(caminho_arquivo)

        for index, row in df.iterrows():
            nome_analise = row['nome_analise']
            resultado_analise = row.to_dict()

            # Persistência dos Dados
            salvar_analise(nome_analise, resultado_analise)
    except Exception as e:
        print(f"Erro ao ler arquivo de análises: {e}")

# Importar os dados *.csv para Banco de dados
if __name__ == "__main__":
    caminho_arquivo = 'analises.csv' 
    ler_e_salvar_analises(caminho_arquivo)
