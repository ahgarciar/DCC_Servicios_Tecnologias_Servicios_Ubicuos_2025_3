import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from keras import Sequential, layers, optimizers, callbacks
from sklearn.model_selection import StratifiedKFold, StratifiedShuffleSplit
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
from joblib import dump
#########################################################################################################
semilla = 7
np.random.seed(semilla)
tf.random.set_seed(semilla)
#########################################################################################################
from P05_KNN_Modularizado import CargaInstancia
instancia = CargaInstancia.cargarInstancia("../Archivos/iris/iris.csv")
#########################################################################################################
##SEPARA LA INSTANCIA
#copia para asegurar no alterar a la instancia original al hacer ajustes en X e y
X = instancia.iloc[:, :-1].copy()
y = instancia.iloc[:, -1].copy() # nominales
#########################################################################################################
##CODIFICA LAS CLASES
encoder = LabelEncoder() #ordinalizacion (Label)
y_int = encoder.fit_transform(y)
#########################################################################################################
##CALCULA EL TTOTAL DE CLASES Y DE ATRIBUTOS
n_clases = len(encoder.classes_)
n_feats = X.shape[1]
#########################################################################################################
# CREACION DEL MODELO
def create_model(input_dim, n_classes):
    model = Sequential([
        layers.Input(shape=(input_dim,)),

        layers.Dense(8, activation="relu"),
        layers.Dropout(0.1),

        # layers.Dense(4, activation="relu"),
        # layers.Dropout(0.1),

        layers.Dense(n_classes, activation="softmax")  # IDEAL PARA MULTICLASES
    ])
    opt = optimizers.Adam(learning_rate=1e-3)
    model.compile(
        optimizer=opt,
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )
    return model

early = callbacks.EarlyStopping(
    patience=20, restore_best_weights=True, monitor="val_loss"
)
#########################################################################################################
# VALIDACIÓN CRUZADA
N_SPLITS = 10 #folds
skf = StratifiedKFold(n_splits=N_SPLITS, shuffle=True, random_state=semilla)
# Resumen de resultados
fold_metrics = []
cm_accum = np.zeros((n_clases, n_clases), dtype=int)
#########################################################################################################
# Directorio de salida
OUT_DIR = "salidas_cv"
os.makedirs(OUT_DIR, exist_ok=True)

# Guarda el encoder
dump(encoder, os.path.join(OUT_DIR, "label_encoder.joblib"))

for fold, (train_index, test_index) in enumerate(skf.split(X, y_int), start=1):
    print(f"\nFold {fold}/{N_SPLITS}")

    X_train_full, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train_full, y_test = y_int[train_index], y_int[test_index]

    # Split interno estratificado (15%) para validación
    sss = StratifiedShuffleSplit(n_splits=1, test_size=0.15, random_state=semilla)
    train_idx_sub, val_idx_sub = next(sss.split(X_train_full, y_train_full))

    X_train = X_train_full.iloc[train_idx_sub]
    y_train = y_train_full[train_idx_sub]
    X_val   = X_train_full.iloc[val_idx_sub]
    y_val   = y_train_full[val_idx_sub]

    # Escalado(fit SOLO con train)
    x_scaler = StandardScaler().fit(X_train)
    X_train_s = x_scaler.transform(X_train)
    X_val_s   = x_scaler.transform(X_val)
    X_test_s  = x_scaler.transform(X_test)

    # Modelo por fold
    model = create_model(n_feats, n_clases)

    history = model.fit(
        X_train_s, y_train,
        validation_data=(X_val_s, y_val),
        epochs=300,
        batch_size=7,
        callbacks=[early],
        verbose=0
    )

    # Evaluación en el test del fold
    test_loss, test_acc = model.evaluate(X_test_s, y_test, verbose=0)
    y_pred = model.predict(X_test_s, verbose=0).argmax(axis=1)

    # Métricas
    acc  = accuracy_score(y_test, y_pred)
    f1_m = f1_score(y_test, y_pred, average="macro")
    f1_w = f1_score(y_test, y_pred, average="weighted")

    print(f"Fold {fold} - Loss: {test_loss:.4f} | Acc: {acc:.4f} | F1-macro: {f1_m:.4f} | F1-weighted: {f1_w:.4f}")

    # Matriz de confusión acumulada
    cm = confusion_matrix(y_test, y_pred, labels=np.arange(n_clases))
    cm_accum += cm

    # Modelo y scaler del fold
    model_path  = os.path.join(OUT_DIR, f"modelo_fold{fold}_acc{acc:.3f}.keras")
    scaler_path = os.path.join(OUT_DIR, f"x_scaler_fold{fold}.joblib")
    model.save(model_path)
    dump(x_scaler, scaler_path)

    # Métricas por fold
    fold_metrics.append({
        "fold": fold,
        "test_loss": float(test_loss),
        "accuracy": float(acc),
        "f1_macro": float(f1_m),
        "f1_weighted": float(f1_w),
        "model_path": model_path,
        "scaler_path": scaler_path
    })

# RESUMEN FINAL
metrics_df = pd.DataFrame(fold_metrics)
print("\nResumen CV")
print(metrics_df[["fold", "test_loss", "accuracy", "f1_macro", "f1_weighted"]])

print("\nPromedios:")
print(metrics_df[["test_loss", "accuracy", "f1_macro", "f1_weighted"]].mean())

print("\nDesviaciones estándar:")
print(metrics_df[["test_loss", "accuracy", "f1_macro", "f1_weighted"]].std())

# Matriz de confusión acumulada (sobre todos los folds)
cm_df = pd.DataFrame(cm_accum, index=encoder.classes_, columns=encoder.classes_)
print("\nMatriz de confusión acumulada (rows=true, cols=pred):")
print(cm_df)