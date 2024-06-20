# -*- coding: utf-8 -*-
"""Cópia de Cópia de IOT_Aula_23042024 (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jvzkgs_4xHcU376KqQr1VWja8vY1sUyy

#Conexão sqlite - Importação de Arquivos CSV - Atualização da tabela de log.
"""

linha = '21.837.213;2024;3;26;18;47;17;21;29;15'

print(linha.split(";"))

conexao=sqlite3.connect("controle_horas.db")
def inserir_hora(hora,minuto,segundo):

def soma(a,b):
   soma = a+b
   return soma
minha_soma= soma(5,5)
print(minha_soma)



import csv
import sqlite3
conexao=sqlite3.connect("controle_horas.db")

cursor3=conexao.cursor()

conexao=sqlite3.connect("controle_horas.db")
# sql='Select * From aluno'
sql ='Select * From log_entrada_saida'
cursor3.execute(sql)
lista_alunos=cursor3.fetchall()
conexao.close()
print(lista_alunos)

conexao=sqlite3.connect("controle_horas.db")
cursor2=conexao.cursor()

sql='DELETE FROM log_entrada_saida'
cursor2.execute(sql)
conexao.commit()
conexao.close()

sql='Select * From log_entrada_saida'
cursor3.execute(sql)
log_entrada_saida=cursor3.fetchall()
conexao.close()
print(log_entrada_saida)

sql1="CREATE TABLE IF NOT EXISTS log_entrada_saida(matricula text, ano text, mes	text, dia text, hora_in text, min_in text, seg_in text, hora_out text, min_out	text,seg_out text)"
cursor3=conexao.cursor() #executar um comando #Presta Atenção
cursor3.execute(sql1)
conexao.close()

import csv
import sqlite3
conexao=sqlite3.connect("controle_horas.db")

cursor1=conexao.cursor() #executar um comando #Presta Atenção
cursor1.execute(sql)

sql="CREATE TABLE IF NOT EXISTS aluno(matricula TEXT, nome TEXT)"
cursor1=conexao.cursor() #executar um comando #Presta Atenção
cursor1.execute(sql)

with open('alunos.csv', 'r') as arquivo:
    leitor_aluno = csv.reader(arquivo)
    for linha_aluno in leitor_aluno:
        print(linha_aluno)

'21.837.213;2024;3;26;18;47;17;21;29;15'

print(linha.split(";"))

conexao=sqlite3.connect("controle_horas.db")
cursor1=conexao.cursor()
sql='Select * From log_entrada_saida'
cursor1.execute(sql)
log_entrada_saida=cursor1.fetchall()
conexao.close()
print(log_entrada_saida)
for registro in log_entrada_saida:
  print(registro)

conexao=sqlite3.connect("controle_horas.db")
cursor1=conexao.cursor()

import csv
import sqlite3


def inserir_dados():
    conexao = sqlite3.connect("controle_horas.db")
    cursor1 = conexao.cursor()

    cursor1.execute(sql)

    with open('log_entrada_saida.txt', 'r') as arquivo_log:
        log_e_s = csv.reader(arquivo_log, delimiter='\t')

        for linha_log in log_e_s:
            if 'matricula' not in linha_log:
                string = "INSERT into log_entrada_saida(matricula,ano,mes,dia,hora,minuto,segundo,tipo) values("
                for campo in linha_log:
                    string += f"'{campo}',"
                string = string[:-1] + ')'  # Remover a última vírgula
                cursor1.execute(string)

    conexao.commit()
    conexao.close()

inserir_dados()

import csv
import sqlite3

def inserir_dados():
    # Conectar ao banco de dados
    conexao = sqlite3.connect("controle_horas.db")
    cursor = conexao.cursor()

    with open('log_entrada_saida.txt', 'r') as arquivo_log:
        log_e_s = csv.reader(arquivo_log, delimiter='\t')  # Defina o delimitador como '\t' para CSVs com tabulação
        for linha_log in log_e_s:
            if 'matricula' not in linha_log:
                # Converta os valores da linha em uma lista de strings formatadas corretamente
                valores = [f"'{valor}'" for valor in linha_log]
                valores_str = ','.join(valores)

                # Crie a consulta SQL para inserir os dados
                sql = f"INSERT INTO log_entrada_saida(matricula, ano, mes, dia, hora, minuto, segundo, tipo) VALUES ({valores_str})"

                # Execute a consulta SQL
                cursor.execute(sql)

    # Faça commit das alterações e feche a conexão
    conexao.commit()
    conexao.close()

# Chame a função para inserir os dados no banco de dados
inserir_dados()

print(inserir_dados())

select

with open('log_entrada_saida.txt', 'r') as arquivo_log:
    log_e_s = csv.reader(arquivo_log)
    for linha_log in log_e_s:
        lista_linha = linha_log[0].split('\t')
        if 'matricula' not in lista_linha:
            # Inicializa a string da instrução SQL
            string = 'INSERT INTO log_entrada_saida(matricula, ano, mes, dia, hora, minuto, segundo, tipo) VALUES('

            # Loop pelos campos da linha e adiciona os valores à string da instrução SQL
            for campo in lista_linha:
                string += f"'{campo}', "

            # Remove a vírgula extra no final e fecha os parênteses
            string = string[:-2] + ')'

            # Imprime a instrução SQL final
            print(string)

print(string)

if not 'maricula' in teste:
  print(teste)

linha_log

if not 'maricula' in teste:
  print (teste[4])

len(linha)

type(log_e_s)

type(linha)

sql="INSERT into log_entrada_saida(maricula,ano,mes,dia,hora,minuto,segundo,tipo)"
cursor1=conexao.cursor() #executar um comando #Presta Atenção
cursor1.execute(sql)

insert into log_entrada_saida(maricula,ano,mes,dia,hora,minuto,segundo,tipo)
values('123','2025','8','16','10','40','0','1')

print(log_entrada_saida)




import sqlite3
import csv
from datetime import datetime

def calcular_tempo_no_local(registros):
    tempo_total = {}
    for registro in registros:
        matricula, ano, mes, dia, hora, minuto, segundo, tipo = registro
        chave = (matricula, ano, mes, dia)
        if chave not in tempo_total:
            tempo_total[chave] = {'entrada': None, 'saida': None, 'tempo_total': 0}

        data_registro = datetime(int(ano), int(mes), int(dia), int(hora), int(minuto), int(segundo))
        if tipo == '1':
            tempo_total[chave]['entrada'] = data_registro
        elif tipo == '0':
            if tempo_total[chave]['entrada']:
                tempo_total[chave]['saida'] = data_registro
                tempo_total[chave]['tempo_total'] += (data_registro - tempo_total[chave]['entrada']).seconds / 3600
                tempo_total[chave]['entrada'] = None

    return tempo_total

# Função para inserir dados do aluno no banco de dados SQLite
def inserir_dados_aluno():
    conexao = sqlite3.connect("controle_horas.db")
    cursor = conexao.cursor()

    with open('alunos.csv', 'r') as arquivo_aluno:
        alunos = csv.reader(arquivo_aluno)

        for linha_log in alunos:
            if 'matricula' not in linha_log:
                string = "INSERT INTO aluno(matricula, nome, dt_nascimento) VALUES ("
                for campo in linha_log:
                    string += f"'{campo}',"
                string = string[:-1] + ")"  # Remover a última vírgula
                cursor.execute(string)

    conexao.commit()
    conexao.close()

# Função para ler registros do banco de dados SQLite
def ler_registros_sqlite():
    conexao = sqlite3.connect("controle_horas.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM log_entrada_saida")
    registros = cursor.fetchall()
    conexao.close()
    return registros

# Exemplo de uso
inserir_dados_aluno()  # Inserir dados dos alunos no banco de dados

registros = ler_registros_sqlite()  # Ler registros do banco de dados
tempo_total = calcular_tempo_no_local(registros)  # Calcular tempo total no local

# Mostrar resultados
for chave, valor in tempo_total.items():
    matricula, ano, mes, dia = chave
    tempo = valor['tempo_total']
    #print(f"Matrícula {matricula}: {tempo:.2f} horas no local (Data: {ano}/{mes}/{dia})")
    print(f"Matricula {matricula}:\n Data: {dia}/{mes}/{ano}\n Tempo no local: {tempo:.2f}\n")


