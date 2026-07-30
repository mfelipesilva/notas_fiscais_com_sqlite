import random

def gerar_num_nf():
    numero = random.randrange(1,9999)
    return numero
gerar_num_nf()

def gerar_data_emissao():
    dia = str(random.randrange(1,31))
    mes = str(random.randrange(1,12))
    ano = '2026'

    juntar = dia + '/' + mes + '/' + ano
    return juntar
gerar_data_emissao()

def gerar_cnpj():
    junta = []
    for i in range(14):
        numeros_cnpj = random.randrange(0,9,1)
        junta.append(str(numeros_cnpj))
        formatados = ''.join(junta)
        formatados = formatados[:2] + '.' + formatados[2:5] + '.' + formatados[5:8] + '/' + formatados[8:12] + '-' + formatados[12:14]
    return formatados
gerar_cnpj()

def gerar_fornecedor():
    fornecedores =[
        ["Range Veículos LTDA"],
        ["Beni Armazenagens"],
        ["Atlas Automóveis S/A"],
        ["ERP Fort Systems LTDA"],
        ["Chico Eletrônicos"],
        ["Scarabolos"]
    ]
    escolha_fornecedor = random.choice(fornecedores)
    return str(*escolha_fornecedor)
gerar_fornecedor()

def gerar_valor_nf():
    valor = random.randrange(1,100000)
    return valor
gerar_valor_nf()