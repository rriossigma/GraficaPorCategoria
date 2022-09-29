import pandas as pd
import matplotlib.pyplot as plot

df = pd.read_csv('clean_students_complete.csv')

df['reading_score_cat'] = pd.cut(df.reading_score, bins =[0,69,float('Inf')] , labels=['Reprobado','Aprobado'])
df['math_score_cat'] = pd.cut(df.reading_score, bins =[0,69,float('Inf')] , labels=['Reprobado','Aprobado'])

totalesAprobadosReading = df.value_counts("reading_score_cat")
etiquetas = df["reading_score_cat"].value_counts().keys()

graficaAprobadosReading = totalesAprobadosReading.plot.pie(figsize=(10,10) ,labels=etiquetas,autopct="%0.5f" )
plot.show()


