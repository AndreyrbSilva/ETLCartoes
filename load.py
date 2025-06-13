import pandas as pd
import sqlite3
from sqlalchemy import create_engine

def salvar_csv(df: pd.DataFrame, nome_arquivo: str, separador: str = ';', decimal: str = ','):
    """
    Salva um DataFrame como CSV com configurações regionais brasileiras.

    Parâmetros:
    - df: DataFrame a ser salvo
    - nome_arquivo: nome do arquivo de saída (ex: "dados.csv")
    - separador: separador de colunas (padrão: ';')
    - decimal: separador decimal (padrão: ',')
    """
    try:
        df.to_csv(nome_arquivo, index=False, sep=separador, decimal=decimal)
        print(f"[✔] CSV salvo em: {nome_arquivo}")
    except Exception as e:
        print(f"[✖] Erro ao salvar CSV: {e}")


def salvar_sqlite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):
    """
    Salva um DataFrame em uma tabela SQLite.

    Parâmetros:
    - df: DataFrame a ser salvo
    - nome_banco: caminho do arquivo SQLite (ex: "dados.db")
    - nome_tabela: nome da tabela de destino
    """
    try:
        conn = sqlite3.connect(nome_banco)
        df.to_sql(nome_tabela, conn, if_exists='replace', index=False)
        conn.close()
        print(f"[✔] Dados salvos em SQLite: {nome_banco} → {nome_tabela}")
    except Exception as e:
        print(f"[✖] Erro ao salvar no SQLite: {e}")


def salvar_mysql(df: pd.DataFrame, usuario: str, senha: str, host: str, banco: str, nome_tabela: str):
    """
    Salva um DataFrame em uma tabela MySQL.

    Parâmetros:
    - df: DataFrame a ser salvo
    - usuario, senha, host, banco: credenciais e conexão
    - nome_tabela: nome da tabela no banco MySQL
    """
    try:
        engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")
        df.to_sql(nome_tabela, con=engine, if_exists='replace', index=False)
        print(f"[✔] Dados salvos em MySQL: {banco}.{nome_tabela}")
    except Exception as e:
        print(f"[✖] Erro ao salvar no MySQL: {e}")