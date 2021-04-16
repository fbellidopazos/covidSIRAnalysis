import csv

dates = []
infected = []

with open('Data/datosCovid.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    fecha = ""
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'\t{row[1]} ------- {row[44]} ------- {row[27]}') # fecha infectados muertos --> titulo
            line_count += 1
        else:
            if(row[3]=='Spain'):
                if(row[43] == 'observed'): # para comprobar que los datos son observados y no proyecciones
                    if(fecha==row[1]):
                        print(f'HOLA')
                        break
                    fecha= row[1]
                    print(f'\t{row[1]} ------- {round(float(row[44]))} ------- {round(float((row[27])))}') # fecha infectados muertos --> datos redondeados
                    dates.append(row[1])
                    infected.append(round(float(row[44])))
            line_count += 1
print(dates)
print(infected)