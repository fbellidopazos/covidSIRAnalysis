# SIR Model
## Índice
1. [Uso](#Uso)
    * [SIR España](#SIR-España)
    * [SIR Hipotético](#Modelo-Hipotético)
1. [Creditos](#Créditos)
## Uso
Para ejecutar todo el Notebook, arriba en el menu:
    Cell > RunAll
### SIR España 
- [Pincha aqui acceder a SIRNotebook](http://jupyter-fbell.herokuapp.com/notebooks/Modelizacion/SIRNotebook.ipynb)

Parametros a cambiar 

* initDay : dia inicial desde el cual queremos que empiece el ajuste 
* day : Numero de dias desde initDay para ajustar, en caso de que el numero de dias sea mayor que el numero de datos del que disponemos a partir de initDay se recogeran solo los datos                 reales hasta el final
* yearsFuture : Numero de años a visualizar con los parametros beta y gamma obtenidos
* predictionNumber : Numero de dias de prediccion a simular 

* export2Tex : True si se quiere exportar a Latex, caso contrario False

### Modelo Hipotético
- [Pincha aqui acceder a SIRNotebook](http://jupyter-fbell.herokuapp.com/notebooks/Modelizacion/hipoteticalCase.ipynb)

- N : Tamaño poblacion inicial
- I0 : Infectados Iniciales
- S0 : Susceptibles Iniciales
- vals : Listado de tuplas <beta, gamma>
- export2Tex : Si quieres documento en latex (True), caso contrario (False)

## Créditos (6 ects)
Este proyecto ha sido realizado por:
- Angel Escudero Iglesias
- Sara Beatriz Alonso Fernandez
- Alejandro Diaz Tiburon
- Fernando Bellido Pazos
