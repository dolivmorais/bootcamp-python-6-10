from aula7_etl import ler_csv, filtrar_produtos_nao_entrgues, somar_valor_dos_produtos

path_arquivo = "vendas_aula7.csv"

lista_de_produtos = ler_csv(path_arquivo)
produtos_nao_entrgues = filtrar_produtos_nao_entrgues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valor_dos_produtos(produtos_nao_entrgues)
print(valor_dos_produtos_entregues)
