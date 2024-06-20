import serial
import serial.tools.list_ports
import sqlite3
from datetime import datetime


# Listar todas as portas disponíveis
ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"Porta disponível: {port.device}")

connection = sqlite3.connect("controle_horas.db")

porta = 'COM8'
# Configura a porta serial (ajuste conforme necessário)
try:
    #ser = serial.Serial('COM12', 9600, timeout=1)
    ser = serial.Serial(porta, 9600, timeout=1)
    print("Conexão com a porta '{0}' bem-sucedida".format(porta ))
except serial.SerialException as e:
    print(f"Erro ao tentar conectar na porta: {e}")

# Nome do arquivo onde os UIDs serão gravados
filename = 'UIDs.txt'


# Loop para ler e gravar os UIDs
if 'ser' in locals() and ser.is_open:
    with open(filename, 'a') as file:
        while True:
            line = ser.readline().decode('utf-8').strip()
            cursor1 = connection.cursor()
            cursor2 = connection.cursor()

            puxaid = "Select RFID FROM aluno where RFID = " + line + ""
            cursor2.execute(puxaid)
            RFIDpuxado = cursor2.fetchall()

            if line in RFIDpuxado:
                if line:
                    tempo_agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    linha_formatada = f'"{line}";"{tempo_agora}"'
                    ano = tempo_agora.year
                    mes = tempo_agora.month
                    dia = tempo_agora.day
                    hora = tempo_agora.hour
                    minuto = tempo_agora.minute
                    segundo = tempo_agora.seconds
                    #sql = "INSERT into log_entrada_saida(matricula,ano,mes,dia,hora,minuto,segundo,RFID) values("
                    sql = "INSERT into log_entrada_saida(ano,mes,dia,hora,minuto,segundo,RFID) values(" + ano + "," + mes + "," + dia + "," + hora + "," + minuto + "," + segundo + line + ");"
                    cursor1.execute(sql)
                    print(f"UID e data/hora recebidos: {linha_formatada}")
                    file.write(f"{linha_formatada}\n")
                    file.flush()
connection.commit()
connection.close()