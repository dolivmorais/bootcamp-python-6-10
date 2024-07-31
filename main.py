"""
criar o repositorio no github
pyenv local 3.11.5
poetry init
poetry env use 3.11.5
power shell

estrutura e corrigir codigo:
poetry add black -- arruma o codigo
poetry add blue -- irmao do black
poetry add isort
poetry add flake8 -- dica para vc arrumar

poetry add taskipy -- roda black flake8 isort

poetry remove black
----------
pre commit

poetry add pre-commit
bandit

poetry run pre-commit install
"""


# funcoes
# %%
def cadastrar_produto():
    produto = input("Digite um produto: ")
    produto = produto.casefold()
    return produto


produto = cadastrar_produto()
print(f"produto {produto}")


# %%
def minha_soma(n1, n2, n3):
    p = n1 + n2 + n3
    return p


var_soma = minha_soma(12, 3, 6)
print(var_soma)
# %%
produtos = [
    "Beb2131",  # Água Mineral
    "Beb2132",  # Suco de Laranja
    "beb2133",  # Refrigerante de Cola
    "beb2134",  # Chá Gelado
    "beb2135",  # Cerveja
    "beb2136",  # Vinho Tinto
    "beb2137",  # Água de Coco
    "beb2138",  # Energético
    "beb2139",  # Café
    "BEB2140",  # Iogurte Líquido
    "bsa4561",  # Biscoito de Chocolate
    "bsa4562",  # Biscoito Salgado
    "bsa4563",  # Biscoito Recheado
    "bsa4564",  # Amendoim Salgado
    "bsa4565",  # Batata Chips
    "bsa4566",  # Pipoca
    "bsa4567",  # Biscoito de Maisena
    "bsa4568",  # Crackers
    "Bsa4569",  # Pretzels
    "Bsa4570",  # Mix de Castanhas
]


def avaliacao_produto(produto, categoria):
    produto = produto.upper()
    if categoria in produto:
        return True
    else:
        False


for produto in produtos:
    if avaliacao_produto(produto, "BSA"):
        print(produto)

# %%
# funcao para calculo de indicadores

# stockout
vendas = {
    "ve001": (911, "concluido", ""),
    "ve002": (912, "cancelado", "cancelado pelo cliente"),
    "ve003": (913, "cancelado", "cancelado pelo cliente"),
    "ve004": (914, "concluido", ""),
    "ve005": (915, "cancelado", "cancelado pelo cliente"),
    "ve006": (916, "cancelado", "cancelado pelo cliente"),
    "ve007": (917, "concluido", ""),
    "ve008": (918, "cancelado", "cancelado pelo cliente"),
    "ve009": (919, "cancelado", "cancelado pelo cliente"),
    "ve010": (920, "cancelado", "estoque em falta"),
    "ve011": (921, "cancelado", "cancelado pelo cliente"),
    "ve012": (922, "cancelado", "cancelado pelo cliente"),
    "ve013": (923, "concluido", ""),
    "ve014": (924, "cancelado", "estoque em falta"),
    "ve015": (925, "cancelado", "cancelado pelo cliente"),
}


def calculo_stockout(dicionario_vendas):
    numerador = 0
    denominador = 0
    for i in dicionario_vendas:
        valor, status, motivo = dicionario_vendas[i]
        if status == "concluido":
            denominador += valor
        elif status == "cancelado" and motivo == "estoque em falta":
            denominador += valor
            numerador += valor
    return numerador / denominador if denominador != 0 else 0


print(calculo_stockout(vendas))


# %%
clientes_devedores = [
    ("00.000.000/0001-91", 1000, 26),
    ("11.111.111/1111-11", 2000, 22),
    ("22.222.222/2222-22", 1500, 15),
    ("33.333.333/3333-33", 3000, 11),
    ("44.444.444/4444-44", 2500, 2),
    ("55.555.555/5555-55", 1800, 6),
    ("66.666.666/6666-66", 2200, 11),
    ("77.777.777/7777-77", 2700, 25),
    ("88.888.888/8888-88", 3100, 21),
    ("99.999.999/9999-99", 3500, 22),
    ("12.345.678/9012-34", 4000, 30),
    ("23.456.789/0123-45", 4500, 20),
    ("34.567.890/1234-56", 5000, 15),
    ("45.678.901/2345-67", 5500, 2),
    ("56.789.012/3456-78", 6000, 10),
]


def inadimplentes(lista, valar, dias):
    lista_inadimplente = []
    for cnpj, valor, dia in clientes_devedores:
        if valor > valar and dia >= dias:
            lista_inadimplente.append(cnpj)
    return lista_inadimplente


print(inadimplentes(clientes_devedores, 3000, 15))

# %%
# DESAFIO
precos_imoveis = [
    350000.00,
    450000.00,
    275000.00,
    320000.00,
    500000.00,
    610000.00,
    420000.00,
    390000.00,
    520000.00,
    480000.00,
    750000.00,
    810000.00,
    670000.00,
    290000.00,
    360000.00,
]

tamanhos_imoveis = [
    75,  # 75 m²
    120,  # 120 m²
    90,  # 90 m²
    60,  # 60 m²
    150,  # 150 m²
    200,  # 200 m²
    110,  # 110 m²
    85,  # 85 m²
    140,  # 140 m²
    130,  # 130 m²
    180,  # 180 m²
    220,  # 220 m²
    160,  # 160 m²
    70,  # 70 m²
    100,  # 100 m²
]


def separar_listas(precos, tamanhos, fator=0.1):
    if len(precos_imoveis) == len(tamanhos_imoveis):
        i = int((1 - fator) * len(precos_imoveis))
        preco_imoveis_treino = precos[:i]
        preco_imoveis_teste = precos[i:]
        tamanhos_imoveis_treino = tamanhos[:i]
        tamanhos_imoveis_teste = tamanhos[i:]
        return (
            preco_imoveis_treino,
            preco_imoveis_teste,
            tamanhos_imoveis_treino,
            tamanhos_imoveis_teste,
        )
    else:
        print("As lista possuem tamanhos diferentes!")
        return


print(len(precos_imoveis))
print(separar_listas(precos_imoveis, tamanhos_imoveis))
