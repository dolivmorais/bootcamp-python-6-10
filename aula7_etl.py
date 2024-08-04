import csv

path_arquivo = "vendas_aula7.csv"


def ler_csv(nome_arquivio: str) -> list[dict]:
    """
    função que lê arquivo csv
    """
    lista = []
    with open(nome_arquivio, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


def filtrar_produtos_nao_entrgues(lista: list[dict]) -> list[dict]:
    """
    funcao que filtra entrgue = false
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados


def somar_valor_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("price"))
    return valor_total
