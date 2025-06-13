import os
from src.extractTransform import extrair_dados_estoque_cartoes, transformar_dados_cartoes
from src.load import salvar_csv, salvar_sqlite

def run_etl(trimestre: str):
    print(f"[→] Iniciando ETL de estoque de cartões para o trimestre {trimestre}")

    df_raw = extrair_dados_estoque_cartoes(trimestre)
    if df_raw.empty:
        print("[!] Nenhum dado extraído. Processo encerrado.")
        return

    df_clean = transformar_dados_cartoes(df_raw)

    os.makedirs("datasets", exist_ok=True)

    nome_arquivo_csv = f"datasets/estoque_cartoes_{trimestre}.csv"
    nome_sqlite = "datasets/estoque_cartoes.db"
    nome_tabela_sqlite = "estoque_cartoes"

    salvar_csv(df_clean, nome_arquivo_csv, separador=';', decimal=',')
    salvar_sqlite(df_clean, nome_sqlite, nome_tabela_sqlite)

    print("[✓] ETL de estoque de cartões finalizada com sucesso.")


if __name__ == "__main__":
    run_etl("20241")
