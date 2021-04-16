import csv


with open('Spain - Data - Coronavirus.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'\t{row[1]} ------- {row[44]} ------- {row[27]}') # fecha infectados muertos --> titulo
            line_count += 1
        else:
            if(row[44] != ''): # a partir de este momento no hay mas infectados observados y las muertes son una proyeccion -> no los imprimo
                print(f'\t{row[1]} ------- {round(float(row[44]))} ------- {round(float((row[27])))}') # fecha infectados muertos --> datos redondeados
            line_count += 1


    print(f'Processed {line_count} lines.')