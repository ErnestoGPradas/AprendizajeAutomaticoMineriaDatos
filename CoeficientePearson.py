import pandas as pd
import math

#Cargamos los datos del csv y los metemos en un dataframe
df = pd.read_csv('estaciones_madrid_202111.csv', sep=",")

#Extraemos en un dataframe todos los registros de la estación 4 (por ejemplo)
dfEstacion4 = df[df['ESTACION'] == 4]
#Extraemos en un dataframe todos los registros de la estación 4 en el mes de Junio (6)
dfEstacion4IntervaloTiempo = dfEstacion4[dfEstacion4['MES'] == 6]
#Extraemos en un dataframe todos los registros seleccionados solo con las columnas que nos interesan
df2 = dfEstacion4IntervaloTiempo[['ESTACION','MES','DIA','SO2','CO']]

#Realizamos los cálculos necesarios para posteriormente introducirlos en la fórmula de correlacion de Pearson
df2['(SO2*CO)'] = df2['SO2'] * df2['CO']
df2['SO2^2'] = df2['SO2'] * df2['SO2']
df2['CO^2'] = df2['CO'] * df2['CO']
print(df2)


totalSO2 = df2['SO2'].sum()
print("El total de la Columna SO2 es: ", totalSO2)
totalCO = df2['CO'].sum()
print("El total de la Columna CO es: ", totalCO)
totalSO2porCO = df2['(SO2*CO)'].sum()
print("El total de la columna SO2*CO es: ", totalSO2porCO)
totalSO2Cuadrado =  df2['SO2^2'].sum()
print("El total de la Columna SO2 al cuadrado es: ", totalSO2Cuadrado)
totalCOCuadrado =  df2['CO^2'].sum()
print("El total de la Columna CO al cuadrado es: ", totalCOCuadrado)

#Calculamos el coeficiente de correlación de Pearson
#n es el número de registros, como es el mes de Junio son 30 días
n = 30
#Fórmula matemática para calcular la correlación de Pearson. Introducimos todos los datos calculados
correlacionPearson = ((n * totalSO2porCO) - (totalSO2 * totalCO)) / (math.sqrt(n * totalSO2Cuadrado - (totalSO2 * totalSO2))) * (math.sqrt(n * totalCOCuadrado - (totalCO * totalCO)))

print("La correlación de Pearson entre SO2 y CO es: ", correlacionPearson)
