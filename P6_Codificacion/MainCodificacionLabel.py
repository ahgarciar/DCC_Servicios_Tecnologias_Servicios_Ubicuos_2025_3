import pandas as pd
from sklearn.preprocessing import LabelEncoder

instancia = pd.read_csv("../Archivos/Instancia.csv")
print(instancia.head())

encoder_Outlook = LabelEncoder()
encoder_Temperature = LabelEncoder()
encoder_Humidity = LabelEncoder()
encoder_Wind = LabelEncoder()

instancia["label_Outlook"] = encoder_Outlook.fit_transform(instancia["Outlook"])
instancia["label_Temperature"] = encoder_Temperature.fit_transform(instancia["Temperature"])
instancia["label_Humidity"] = encoder_Humidity.fit_transform(instancia["Humidity"])
instancia["label_Wind"] = encoder_Wind.fit_transform(instancia["Wind"])

instancia = instancia.drop(["Outlook","Temperature","Humidity","Wind"], axis=1)

columnas = list(instancia.columns) #encabezados - nombres de las columnas


print("Instancia:")
print(columnas) #encabezados
for i in range(0, len(instancia)):
    registro = instancia.loc[i].tolist()
    print(str(registro))

