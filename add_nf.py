import sqlite3
from pathlib import Path
from defs import gerar_num_nf, gerar_data_emissao, gerar_cnpj, gerar_fornecedor, gerar_valor_nf

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

def menu():
    while True:
        print('Bem vindo(a)! Por favor, escolha o modo de adição das notas:')
        decisao = input('[M]anual ou [A]utomático: ')
        decisao = decisao.upper()
        try:
            if decisao.upper() == 'M':
                numero = input('Número da NF: ')
                data_emissao = input('Data de emissão: ')
                cnpj = input('CNPJ: ')
                fornecedor = input('Fornecedor: ')
                valor = input('Valor da nota: ')
                cnpj = cnpj[:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + cnpj[8:12] + '-' + cnpj[12:14]

                exec_sql = f'INSERT INTO {TABLE_NAME} (numero, data_emissao, cnpj, fornecedor, valor) VALUES (?, ?, ?, ?, ?)',
                (numero, data_emissao, cnpj, fornecedor, valor)                    
                
                cursor.execute(exec_sql)
                

            elif decisao == 'A':
                def auto_add_dados():
                    try:
                        quantidade_dados = input('Quantos registros você deseja adicionar no banco de dados? ')
                        quantidade_dados = int(quantidade_dados)
                        for i in range (quantidade_dados):
                            numero = gerar_num_nf()     
                            data_emissao = gerar_data_emissao()
                            cnpj = gerar_cnpj()
                            fornecedor = gerar_fornecedor()
                            valor = gerar_valor_nf()                   

                            cursor.execute(f'INSERT INTO {TABLE_NAME} (numero, data_emissao, cnpj, fornecedor, valor) VALUES (?, ?, ?, ?, ?)',
                            (numero, data_emissao, cnpj, fornecedor, valor))

                            connection.commit()
                    except NameError:
                        ...

            auto_add_dados()
        except NameError:
            print('Digite APENAS uma das opções disponibilizadas.')
            menu()
        except ValueError, UnboundLocalError:
            print('Digite APENAS números.')
        print('Nota(s) fiscal(is) adicionada(s) com sucesso')
        continuar = input('Deseja cadastrar outra nota? '
        '\n[S]im/[N]ão: ')
        if continuar.upper() == 'N':
            break

menu()

cursor.close()
connection.close()