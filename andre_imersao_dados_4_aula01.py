import pandas as pd

dados = pd.read_csv("dados_imoveis.csv")

head = dados.head()
#print(head)

sample = dados.sample(10)
#print(sample)

info = dados.info()
#print(info)

#printa a coluna bairro da linha 6522
aux = dados["Bairro"][6522]
#print(aux)

mediana_metragem = dados.Metragem.mean()
#print(mediana_metragem)

soma = sum((dados["Bairro"] == "Vila Mariana"))
#print(soma)

#verifica quais bairros são da Vila Mariana e coloca "true" ou "false" em uma tupla
tem_imoveis_vila =(dados["Bairro"] == "Vila Mariana")
#print(tem_imoveis_vila)

#busca em dados pelo id onde tenha true em tem_imoveis_vila
imoveis_vila_mariana = dados[tem_imoveis_vila]
#print(imoveis_vila_mariana)

n_bairros = dados["Bairro"].value_counts()
print(n_bairros)

n_imoveis_bairro = dados["Bairro"].value_counts()
n_imoveis_bairro.head(10).plot.bar()