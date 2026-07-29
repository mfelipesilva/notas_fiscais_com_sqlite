import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db_nfs.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'Notas_Fiscais'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '
    '('
    'numero INTEGER PRIMARY KEY, '
    'data_emissao TEXT, '
    'cnpj TEXT, '
    'fornecedor TEXT, '
    'valor REAL '
    ')'
)
connection.commit()

while True:
    print('Bem vindo(a)! Por favor, adicione os dados da NF')
    decisao = input('[I]nseir, [S]air: ')
    if decisao == 'i':
        numero = input('Número da NF: ')
        data_emissao = input('Data de emissão: ')
        cnpj = input('CNPJ: ')
        fornecedor = input('Fornecedor: ')
        valor = input('Valor da nota: ')
    elif decisao == 's':
        break