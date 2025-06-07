const int trigPin = 5;
const int echoPin = 18;

// Variáveis simuladas
float temperatura = 28.0;
float umidade = 60.0;
float pressao = 1005.0;

void setup() {
  Serial.begin(115200);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  randomSeed(analogRead(0));
}

float simularVariacao(float valorAtual, float min, float max, float passo = 2.0) {
  valorAtual += random(-10, 11) * (passo / 10.0);
  if (valorAtual < min) valorAtual = min;
  if (valorAtual > max) valorAtual = max;
  return valorAtual;
}

float lerDistancia() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duracao = pulseIn(echoPin, HIGH, 30000);
  if (duracao == 0) return -1;

  float distancia = duracao * 0.034 / 2;
  return distancia;
}

void loop() {
  // Simulação dos dados com variações suaves
  temperatura = simularVariacao(temperatura, 25.0, 35.0);
  umidade = simularVariacao(umidade, 70.0, 90.0);
  pressao = simularVariacao(pressao, 980.0, 1020.0);

  float distancia = lerDistancia();

  Serial.print("🌡️ Temp: "); Serial.print(temperatura); Serial.println(" °C");
  Serial.print("💧 Umidade: "); Serial.print(umidade); Serial.println(" %");
  Serial.print("🌪️ Pressão: "); Serial.print(pressao); Serial.println(" hPa");

  if (distancia >= 0) {
    Serial.print("📏 Distância: "); Serial.print(distancia); Serial.println(" cm");
  } else {
    Serial.println("📏 Distância: erro de leitura.");
  }

  // Avaliação da condição de tempestade
  bool riscoTempestade = (pressao < 1005 && umidade > 70 && temperatura > 27);

  if (riscoTempestade) {
    Serial.println("⚠️ RISCO DE TEMPESTADE!");
  } else {
    Serial.println("✅ Sem risco de tempestade no momento.");
  }

  // Alerta de objeto próximo
  if (distancia >= 0 && distancia < 20) {
    Serial.println("⚠️ Objeto muito próximo detectado!");
  }

  Serial.println("------------------------------");
  delay(100);
}
