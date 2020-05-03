#Python 3
#Retornar a data do dia anterior
from datetime import datetime
def diaAnterior(data):
    meses = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    ano = data.year
    mes = data.month
    dia = data.day
    if dia == 1:
        if mes == 1:
            ano-=1
            return datetime(ano,12,31)
        else:
            mes-=1
            #ano bissexto
            if ano % 4 == 0 and mes == 2:
                return datetime(ano,mes,meses[mes]+1)
            else:
                return datetime(ano,mes,meses[mes])
    else:
        return datetime(ano,mes,dia-1)
def main():
    data = datetime(2019,3,25)
    print(diaAnterior(data))

if __name__ == "__main__":
    main()