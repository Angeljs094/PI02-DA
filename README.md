
# P02- Siniestros Viales en CABA

## Inroducción

En este proyecto, adoptamos el papel de un Analista de Datos en el equipo de una consultora, encargado de responder a la solicitud del Observatorio de Movilidad y Seguridad Vial (OMSV), un organismo vinculado a la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires (CABA), para llevar a cabo un análisis de datos.

## Objetivo
El objetivo principal es proporcionar información que permita a las autoridades locales implementar medidas destinadas a reducir el número de víctimas mortales en accidentes de tránsito ocurridos en CABA. Con este fin, trabajamos con un conjunto de datos que abarca los homicidios relacionados con siniestros viales ocurridos en la Ciudad de Buenos Aires durante el período 2016-2021.

Los siniestros viales, también conocidos como accidentes de tráfico o accidentes de tránsito, son eventos que involucran vehículos en las vías públicas y pueden tener diversas causas, desde colisiones entre automóviles, motocicletas, bicicletas o peatones hasta atropellos o choques con objetos fijos. Estos incidentes pueden causar desde daños materiales hasta lesiones graves o fatales para los involucrados.

En la Ciudad Autónoma de Buenos Aires (CABA), situada en Argentina, los siniestros viales son una preocupación importante debido al alto volumen de tráfico y la densidad poblacional. Con una población de 3,120,612 habitantes en una superficie de aproximadamente 200 km², y un registro de 12,437,735 vehículos transitando por las autopistas de acceso en julio de 2023, la prevención y la implementación de políticas efectivas son esenciales para abordar este problema adecuadamente.

En Argentina, los siniestros viales representan una preocupación nacional, con alrededor de 4,000 muertes anuales. Según el Sistema Nacional de Información Criminal (SNIC), entre 2018 y 2022 se registraron 19,630 muertes en siniestros viales en todo el país, lo que equivale a un promedio de 11 personas fallecidas por día. Buenos Aires, la capital del país, cuenta con una densidad de población de más de 15,000 habitantes por kilómetro cuadrado, y en 2022 se registraron 3,828 muertes fatales en siniestros viales. Por lo tanto, el estudio y la prevención de los siniestros viales son de vital importancia para las autoridades locales y nacionales.

## Desarrollo

### ETL (Extract, Transform, Load)
El proceso ETL (Extract, Transform, Load) es fundamental para la preparación de los datos antes de realizar el análisis. A continuación, se presenta el flujo de trabajo ETL realizado para este proyecto:

Importar librerías: Se importan las bibliotecas necesarias, incluyendo pandas, numpy y funciones personalizadas.

Carga de Datos: Se cargan los datos de los archivos "homicidios.xlsx" y "lesiones.xlsx" en DataFrames utilizando la biblioteca pandas.

### EDA

Se realizo una exploración inicial de los datos para comprender su estructura y contenido.
Se identifican y se tratan los valores nulos y duplicados.
Se eliminan columnas irrelevantes o con una gran cantidad de valores nulos.
Se renombran las columnas para mejorar la legibilidad y se convierten los valores a minúsculas.
Se convierten algunas columnas a tipos de datos más adecuados y se categorizan según sea necesario.
Combinar Datos: Se combinan los datos de los homicidios y las víctimas en un único DataFrame utilizando la función merge de pandas.

Modificaciones y Transformaciones Adicionales: Se realizan ajustes finales, como la eliminación de filas con valores nulos o vacíos.

Almacenamiento y Unión de Datos: Finalmente, se guarda el DataFrame limpio en un archivo CSV para su posterior análisis y se proporciona una versión combinada de los datos.

Este proceso de ETL proporciona una base sólida para el análisis posterior de los datos sobre siniestros viales en CABA, permitiendo a las autoridades locales tomar medidas efectivas para abordar este importante problema de seguridad vial.

Exploración de Datos: Mi Enfoque

Importando Librerías: Para comenzar mi análisis, importo las bibliotecas necesarias, como Pandas para manipulación de datos, Seaborn y Matplotlib para visualización, y otras utilidades como Numpy y Calendar.

Cargando Datos: A continuación, cargo mis conjuntos de datos relevantes, en este caso, los datos de homicidios limpios. Defino los tipos de datos para cada columna y aseguro que las fechas sean interpretadas correctamente.

Explorando los Datos: Observo los primeros registros de mis datos usando head() para tener una idea inicial de su estructura. También reviso la forma del DataFrame y utilizo info() para obtener información sobre los tipos de datos y la cantidad de valores nulos en cada columna.

Análisis de Valores Nulos: Realizo un análisis de los valores nulos, contando la cantidad de nulos por columna y calculando su porcentaje en relación con el tamaño total del DataFrame.

Creación de Nuevas Características: Para enriquecer mi análisis, creo nuevas columnas a partir de la columna de fecha, como el día, la semana, el mes, el semestre y el año.

Resumen Estadístico: Utilizo la función describe() para obtener un resumen estadístico de las características seleccionadas, como el número de víctimas, la franja horaria, la comuna, la edad, entre otros.

Matriz de Correlación: Calculo la matriz de correlación entre las características seleccionadas y visualizo las correlaciones usando un heatmap, identificando posibles relaciones entre las variables.

Manejo de Outliers: Identifico y visualizo outliers en las variables relevantes, como el número de víctimas y la edad, utilizando gráficos de dispersión y de caja.

Frecuencia por Comuna: Investigando la frecuencia de siniestros fatales por comuna, lo cual proporciona información sobre las áreas con mayores desafíos en términos de seguridad vial.

Análisis por Tipo de Calle: Examino la cantidad de accidentes por tipo de calle para entender qué tipos de vías son más propensas a accidentes.

Tendencias Temporales: Analizo las tendencias temporales, como la cantidad de víctimas por año y por mes, para comprender cómo han variado los accidentes a lo largo del tiempo.

Distribución de Accidentes por Horario: Exploro la distribución de accidentes a lo largo del día, identificando las horas en las que ocurren la mayoría de los siniestros.

Categorización del Tiempo: Categorizo las horas del día en franjas horarias para comprender mejor cuándo ocurren la mayoría de los accidentes.

Conclusiones Preliminares: Basado en estos análisis preliminares, puedo identificar patrones, tendencias y posibles áreas de enfoque para futuros análisis y acciones preventivas.

### Vizualizaciones en Power BI

Aca podemos ver unos graficos realizados para ver como esta la situacion con respecto a los accidentes de transito
[Analisis Temporal]("Imagenes/Analisis_Temporal.png")

[Analisis Categorico]("Imagenes/Analisis_Categorico.png")

[Indicadores]("Imagenes/Indicadores.png")
