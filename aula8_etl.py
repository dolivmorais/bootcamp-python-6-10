import pandas as pd
import os
import glob


def extrair_dados_e_consolidar(path: str) -> pd.DataFrame:
    """funcao de le e consolida os json"""
    arquivos_json = glob.glob(os.path.join(path, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


def calcular_kpi_de_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["total"] = df["quantidade"] * df["venda"]
    return df


def carregar_dados(df: pd.DataFrame, formato_saida: list):
    """parametro que vai ser ou csv ou parquet ou os dois"""
    for formato in formato_saida:
        if formato == "csv":
            df.to_csv("dados.csv")
        if formato == "parquet":
            df.to_parquet("dados.parquet")


def pipeline_calcular_kpi_vendas(pasta, formato_saida):
    data_frame = extrair_dados_e_consolidar(pasta)
    df_calculado = calcular_kpi_de_total_vendas(data_frame)
    carregar_dados(df_calculado, formato_saida)
