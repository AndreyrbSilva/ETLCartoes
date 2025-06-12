import requests
import pandas as pd

def extrair_dados_estoque_cartoes(trimestre: str) -> pd.DataFrame:
    """
    Extrai os dados da API pública do Banco Central sobre estoque de cartões.

    Os dados referem-se à quantidade de cartões emitidos e ativos por bandeira,
    função (crédito, débito etc.) e tipo de produto, no trimestre informado.

    Parâmetros:
    - trimestre: string no formato 'YYYYT' (ex: '20241')

    Retorna:
    - DataFrame com os dados da API
    """
    url = (
        "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/"
        f"Quantidadeetransacoesdecartoes(trimestre=@trimestre)?@trimestre='{trimestre}'"
        "&$top=100&$format=json&$select=trimestre,nomeBandeira,nomeFuncao,produto,"
        "qtdCartoesEmitidos,qtdCartoesAtivos"
    )

    try:
        req = requests.get(url)
        req.raise_for_status()
        dados = req.json()
        df = pd.json_normalize(dados["value"])
        return df
    except requests.exceptions.RequestException as e:
        print(f"[✖] Erro ao extrair dados da API: {e}")
        return pd.DataFrame()


def transformar_dados_cartoes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica transformações nos dados de estoque de cartões.

    - Converte nomes de colunas para minúsculas
    - Garante tipo string na coluna trimestre
    - Ordena os dados por bandeira e função

    Parâmetros:
    - df: DataFrame original

    Retorna:
    - DataFrame transformado
    """
    if df.empty:
        print("[!] DataFrame vazio — nenhuma transformação aplicada.")
        return df

    df.columns = [col.lower() for col in df.columns]
    df["trimestre"] = df["trimestre"].astype(str)
    df = df.sort_values(by=["nomebandeira", "nomefuncao"])
    return df
