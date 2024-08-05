from aula8_etl import pipeline_calcular_kpi_vendas

pasta = "aula8_dados"
# data_frame = extrair_dados_e_consolidar(path=pasta)
# df_calculado = calcular_kpi_de_total_vendas(data_frame)
formato_saida: list = ["csv"]
# carregar_dados(df_calculado,formato_saida)

pipeline_calcular_kpi_vendas(pasta, formato_saida)
