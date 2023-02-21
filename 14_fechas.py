# import datetime

from datetime import datetime
from datetime import time
from datetime import date
ahora = datetime.now()
print(ahora.day)
print(datetime.now().hour)
print(ahora.timestamp())
print(datetime(1967,5,25))
nueva_fecha = datetime(2023,2,2, 10,58)
print(nueva_fecha)
hora_actual = time(11,30,25)
print(hora_actual)
print(time(12,45,35).hour)
fecha_nueva = date(1985,12,31)
print(fecha_nueva)
fecha_nueva = date.today()
print(fecha_nueva)
ano = fecha_nueva.year
mes = fecha_nueva.month
dia = fecha_nueva.day
print(ano, mes, dia)
mes += 1
print(ano, mes, dia)
nueva_fecha = date(2023, 2, 24)
print(f"{nueva_fecha} // {fecha_nueva}")
resto_fecha = nueva_fecha - fecha_nueva
print(resto_fecha)
