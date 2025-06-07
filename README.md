# 🌊 Previsão de Risco de Maré de Tempestade com ESP32 + Machine Learning

Projeto desenvolvido para a **Global Solution 2025.1** do curso de Inteligência Artificial da **FIAP**, com o objetivo de prever riscos ambientais com apoio de sensores e algoritmos de Machine Learning.

---

## 🎯 Objetivo

Criar um sistema de previsão de **risco de maré de tempestade** com base em variáveis ambientais simuladas, utilizando:

- Leitura de sensores (temperatura, umidade, pressão e distância);
- Dispositivo ESP32 simulado via [Wokwi](https://wokwi.com);
- Algoritmo de Machine Learning para classificação de risco;
- Análise automatizada dos dados e retorno com previsões.

- 📊 Dados Utilizados
Importante: O modelo não utiliza diretamente os dados da disasterscharter.org, pois essa fonte não possui variáveis ambientais em tempo real que se conectem com sensores físicos.

Em vez disso, dados simulados de sensores via ESP32 foram usados para gerar o CSV dados_meteorologicos.csv, contendo:

temperatura_c

umidade_percent

pressao_hpa

distancia_cm

risco_tempestade (variável-alvo com base em lógica condicional)

---

## 🗂️ Estrutura do Projeto

```bash
gs_fiap_modelo_ml/
├── data/
│   └── dados_meteorologicos.csv         # Dados simulados do ESP32
├── models/
│   └── modelo_risco_tempestade.pkl      # Modelo ML treinado
├── src/
│   ├── treino_modelo.py                 # Treina e salva o modelo
│   └── previsao.py                      # Usa o modelo para prever risco
├── modelo_mare.ipynb                    # Notebook com o fluxo completo
├── README.md
└── .gitignore



