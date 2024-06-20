import csv
import sqlite3

conexao=sqlite3.connect("controle_horas.db")
sql = "CREATE TABLE IF NOT EXISTS log_entrada_saida(matricula TEXT,ano TEXT,mes TEXT,dia TEXT,hora TEXT,minuto TEXT,segundo TEXT,tipo TEXT)"
cursor=conexao.cursor()
cursor.execute(sql)
sql="CREATE TABLE IF NOT EXISTS aluno(matricula TEXT, nome TEXT)"
cursor.execute(sql)
conexao.close()

with open('alunos.csv', 'r') as arquivo:
    leitor_aluno = csv.reader(arquivo)
    for linha_aluno in leitor_aluno:
        print(linha_aluno)

def inserir_dados():
    conexao = sqlite3.connect("controle_horas.db")
    cursor1 = conexao.cursor()

    with open('log_entrada_saida.txt', 'r') as arquivo_log:
        log_e_s = csv.reader(arquivo_log, delimiter='\t')

        for linha_log in log_e_s:
            if 'matricula' not in linha_log:
                string = "INSERT into log_entrada_saida(matricula,ano,mes,dia,hora,minuto,segundo,tipo) values("
                for campo in linha_log:
                    string += f"'{campo}',"
                string = string[:-1] + ')'  # Remover a última vírgula
                cursor1.execute(string)
        print("Inserido!")

    conexao.commit()
    conexao.close()

inserir_dados()


def inserir_log_alunos():
    conexao = sqlite3.connect("controle_horas.db")
    cursor2 = conexao.cursor()

    with open('alunos.csv', 'r') as arquivo_log:
        log_e_s = csv.reader(arquivo_log, delimiter='\t')

        for linha_log in log_e_s:
            if 'matricula' not in linha_log:
                string = "INSERT into aluno(matricula,nome) values("
                for campo in linha_log:
                    string += f"'{campo}',"
                string = string[:-1] + ')'  # Remover a última vírgula
                cursor2.execute(string)
        print("Inserido Log!")

    conexao.commit()
    conexao.close()

inserir_log_alunos()
