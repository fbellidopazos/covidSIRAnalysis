import csv

allCities = {}



def indexedNumbers(row):
    fechaField=-1
    observedField=-1
    infectedField=-1
    countryField = -1
    for i in range(0,len(row)):
        if(row[i]=="date"):
            fechaField = i
        elif(row[i]=="confirmed_infections_data_type"):
            observedField = i
        elif(row[i]=="confirmed_infections"):
            infectedField = i
        elif(row[i]=="location_name"):
            countryField=i
    return fechaField,countryField,observedField,infectedField
    
def checkLong(allCities):
    long = 0
    k = 0
    for i in allCities:
        if(k==0):
            long = len(allCities[i])
        else:
            if(long != len(allCities[i])):
                print("Error")
            else:
                continue
    print("Evrything in order")

def getCity(name):
    with open('../Data/datosCovid.csv',encoding="UTF8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        fecha = "" # Var Init
        line_count = 0
        
        # Index for Vals
        fechaField=-1
        countryField = -1
        observedField=-1
        infectedField=-1


        for row in csv_reader: 
            if line_count == 0:
                # Get the indexes
                fechaField,countryField,observedField,infectedField = indexedNumbers(row)
                if(fechaField==-1 or countryField ==-1 or observedField==-1 or infectedField==-1):
                    # If any of them = -1 then BREAK
                    print(f'FechaField{fechaField}\tCountryField{countryField}\tObservedField{observedField}\tInfectedField{infectedField}')
                    break
                line_count += 1
                continue
            else:
                if(not row[countryField] in allCities): # We create the key in Dict
                    allCities[row[countryField]] = []
                if(row[observedField] == 'observed'): # Only get "Observed" Data
                    if(fecha==row[fechaField]):
                        print(f'FECHA REPETIDA\t{fecha}\tJUMP to Next') # Skip the date if are equal
                    else:
                        par = (row[fechaField],round(float(row[infectedField])))
                        allCities[row[countryField]].append(par)
                    fecha = row[fechaField]
            line_count += 1
        checkLong(allCities)
    return allCities[name]









