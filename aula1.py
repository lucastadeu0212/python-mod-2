import os
import pandas as pd
import plotly.express as px
import win32com.client as win32

lista_arquivo = os.listdir("C:/Projeto/Vendas/")

print(lista_arquivo)

tabela_total = pd.DataFrame()


for arquivo in lista_arquivo:
  if "Vendas" in arquivo:
    tabela = pd.read_csv(f"C:/Projeto/Vendas/{arquivo}")
    tabela_total = pd.concat([tabela_total, tabela])
    print(tabela_total)

print(tabela_total)
tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by = "Quantidade Vendida", ascending = False)
print(tabela_produtos)


tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]


tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by = "Faturamento", ascending = False)
print(tabela_faturamento)


tabela_loja = tabela_total.groupby("Loja").sum()
tabela_loja = tabela_loja[["Faturamento"]]
print(tabela_loja)


grafico = px.bar(tabela_loja, x = tabela_loja.index, y = "Faturamento")
grafico.show()
grafico_path = 'C:/Projeto/Vendas/grafico.png'
grafico.write_image(grafico_path)

'''
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'millasool@gmail.com'
mail.Subject = 'Relatório'
mail.HTMLBody = 

<p>Produtos</p> 
{tabela_produtos.to_html()}

<p>Faturamento</p>
{tabela_faturamento.to_html()}

<p>Lojas</p>
{tabela_loja.to_html()}


# To attach a file to the email (optional):
# attachment  = "Path to the attachment"
# mail.Attachments.Add(attachment)

mail.Send()

'''

print('Email enviado!')
