# %%
import csv


# %%
def getDateAndInfected():
    allCities = {}

    with open('Data/datosCovid.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        fecha = "" # Var Init
        line_count = 0
        for row in csv_reader: 
            if line_count == 0:
                line_count += 1
                continue
            else:
                if(not row[3] in allCities):
                    allCities[row[3]] = []
                if(row[43] == 'observed'): # Data is Actual not predicted
                    if(fecha==row[1]):
                        print(f'FECHA REPETIDA')
                        break
                    par = (row[1],round(float(row[44])))
                    allCities[row[3]].append(par)
            line_count += 1
    return allCities

