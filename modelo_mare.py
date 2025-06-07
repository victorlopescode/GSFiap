# modelo_mare.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Carregar base real
df = pd.read_csv("ativacoes_desastres.csv")
df = df.fillna("")

# Criar coluna 'risco_mare' com base no tipo de evento
def classificar_risco(row):
    tipos_de_risco = ["Storm", "Flood", "Coastal Flood", "Hurricane"]
    if row["type of event"].strip().title() in tipos_de_risco:
        return 1
    return 0

df["risco_mare"] = df.apply(classificar_risco, axis=1)

# Criar features simples a partir da data e hora
df["mes"] = pd.to_datetime(df["date of charter Activation"], errors="coerce").dt.month
df["hora"] = pd.to_datetime(df["Time of charter Activation"], errors="coerce").dt.hour

# Remover linhas com datas inválidas
df = df[df["mes"].notna() & df["hora"].notna()]

# Selecionar features e alvo
X = df[["mes", "hora"]]
y = df["risco_mare"]

# Treinar modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Avaliar
y_pred = model.predict(X_test)
print("Acurácia:", accuracy_score(y_test, y_pred))

# Salvar modelo
with open("modelo_mare.pkl", "wb") as f:
    pickle.dump(model, f)