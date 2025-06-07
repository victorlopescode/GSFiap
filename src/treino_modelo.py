# src/treino_modelo.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

def carregar_dados(caminho_csv):
    df = pd.read_csv(caminho_csv)

    # Regra para determinar risco de tempestade
    df["risco_tempestade"] = (
        (df["pressao_hpa"] < 1005) &
        (df["umidade_percent"] > 70) &
        (df["temperatura_c"] > 27)
    ).astype(int)

    return df

def treinar_modelo(df):
    X = df[["temperatura_c", "umidade_percent", "pressao_hpa", "distancia_cm"]]
    y = df["risco_tempestade"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)
    print(f"Acurácia do modelo: {acuracia:.2f}")

    return modelo

def salvar_modelo(modelo, caminho_pkl):
    with open(caminho_pkl, "wb") as f:
        pickle.dump(modelo, f)

if __name__ == "__main__":
    df = carregar_dados("data/dados_meteorologicos.csv")
    modelo = treinar_modelo(df)
    salvar_modelo(modelo, "models/modelo_risco_tempestade.pkl")