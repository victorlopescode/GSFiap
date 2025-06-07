# previsao.py
import numpy as np
import pickle

# Carrega o modelo salvo
with open("../models/modelo_risco_tempestade.pkl", "rb") as f:
    modelo_carregado = pickle.load(f)

# Exemplo de novo dado (temp, umidade, pressao, distancia)
novo_dado = np.array([[28.5, 72.3, 1002.5, 400.0]])

# Faz a previsão
previsao = modelo_carregado.predict(novo_dado)

# Resultado
if previsao[0] == 1:
    print("⚠️ RISCO DE TEMPESTADE PREVISTO!")
else:
    print("✅ Sem risco de tempestade previsto.")
