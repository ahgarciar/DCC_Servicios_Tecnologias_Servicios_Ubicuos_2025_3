from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Ejemplo: clases reales y predichas
y_true = [0, 1, 2, 2, 0, 1, 0, 2]
y_pred = [0, 0, 2, 2, 0, 1, 1, 2]

# Matriz de confusión
cm = confusion_matrix(y_true, y_pred)

# Mostrar en consola
print(cm)

# Visualización gráfica
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
#disp.plot(cmap=plt.cm.Blues)
disp.plot()
plt.show()


from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred, target_names=["Clase A", "Clase B", "Clase C"]))

"""
Accuracy (global): proporción de aciertos sobre el total.
Precision, Recall y F1 por clase
    Para cada clase se calcula como si fuera un caso binario (uno contra todos).
"""