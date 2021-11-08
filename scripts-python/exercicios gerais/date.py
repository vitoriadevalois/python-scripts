#Utilizando informações de data, horário e relacionando datas diferentes
from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.month)
    print(data_atual.hour)
    tupla = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2021, 10, 18, 22, 14, 30)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2021 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=18)
    print(nova_data)

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y') #utilizamos strftime para converter à norma que desejamos
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)

if __name__ == '__main__':
    # trabalhando_com_date() #para executar o def trabalhando_com_date
    # trabalhando_com_time() #para executar o def trabalhando_com_time
    trabalhando_com_datetime()