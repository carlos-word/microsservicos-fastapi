# 📦 Microsserviços com FastAPI

## 📋 Descrição

Este projeto implementa dois microsserviços utilizando FastAPI, com comunicação síncrona via HTTP. O objetivo é demonstrar como serviços se comunicam entre si e analisar problemas como latência, falhas e dependência entre eles.

---

## 🏗️ Arquitetura do Sistema

O sistema é composto por dois microsserviços:

### 🔹 Users Service (Serviço de Usuários)

* Endpoint: `/users/{id}`
* Porta: 8001
* Retorna dados simulados de usuários

### 🔹 Orders Service (Serviço de Pedidos)

* Endpoint: `/orders/{id}`
* Porta: 8002
* Retorna pedidos e consome o Users Service

---

## 🔗 Comunicação entre os Serviços

O Orders Service realiza chamadas HTTP para o Users Service para obter informações dos usuários.

Essa comunicação é síncrona, ou seja, o serviço de pedidos depende da resposta do serviço de usuários para finalizar a requisição.

---

## 🛠️ Tecnologias Utilizadas

* Python (FastAPI)
* REST API (HTTP)
* Docker
* Docker Compose

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone <SEU_LINK_AQUI>
cd <SEU_PROJETO>
```

### 2. Executar os serviços

```bash
docker-compose up --build
```

---

## 🌐 Endpoints

### Users Service

```
http://localhost:8001/users/1
```

### Orders Service

```
http://localhost:8002/orders/1
```

---

## 🧪 Testes Realizados

### ✅ 1. Comunicação normal

<img width="716" height="740" alt="Captura de tela 2026-03-23 171031" src="https://github.com/user-attachments/assets/53f0094d-c456-4eb9-b57f-2c2dc3ac8f4a" />

**Descrição:**  
O serviço de pedidos retornou corretamente os dados do pedido junto com as informações do usuário, demonstrando comunicação bem-sucedida entre os microsserviços.

**Como reproduzir:**

1. Iniciar os serviços:

```
docker-compose up --build
```

2. Acessar:

```
http://localhost:8002/orders/1
```

---

### ❌ 2. Pedido inexistente

<img width="713" height="751" alt="Captura de tela 2026-03-23 171126" src="https://github.com/user-attachments/assets/9b142b48-e488-4ef3-8865-98327935231c" />

**Descrição:**  
Foi feita uma requisição com um ID inválido e o sistema retornou erro informando que o pedido não foi encontrado.

**Como reproduzir:**

```
http://localhost:8002/orders/999
```

---

### 🔥 3. Falha de comunicação entre serviços

<img width="712" height="739" alt="Captura de tela 2026-03-23 171206" src="https://github.com/user-attachments/assets/65e38844-34c5-4b4f-840d-b8aa3ea45f1a" />

**Descrição:**  
O serviço de usuários foi desligado, e o serviço de pedidos retornou erro ao tentar se comunicar.

**Como reproduzir:**

1. Iniciar os serviços:

```
docker-compose up --build
```

2. Parar apenas o serviço de usuários:

```
docker-compose stop users-service
```

3. Fazer a requisição:

```
http://localhost:8002/orders/1
```

---

### 🐢 4. Teste de latência

<img width="780" height="746" alt="Captura de tela 2026-03-23 173711" src="https://github.com/user-attachments/assets/3f67b0bb-0c68-49c7-a830-91c6605e8aca" />

**Descrição:**  
Foi adicionado um atraso no serviço de usuários utilizando `time.sleep()`, aumentando o tempo de resposta do sistema.

**Como reproduzir:**

1. Inserir no código do Users Service:

```python
import time
time.sleep(5)
```

2. Reiniciar:

```
docker-compose up --build
```

3. Acessar:

```
http://localhost:8002/orders/1
```

---

### ✅ 5. Teste do Users Service

<img width="719" height="737" alt="Captura de tela 2026-03-23 174608" src="https://github.com/user-attachments/assets/02e55ec3-3ffc-453c-bf70-87839b2f2640" />

**Descrição:**  
Foi realizada uma requisição direta ao serviço de usuários para verificar se ele está operando corretamente de forma independente.

**Como reproduzir:**

```
http://localhost:8001/users/1
```

---

### ✅ 6. Teste do Orders Service

<img width="716" height="741" alt="Captura de tela 2026-03-23 174545" src="https://github.com/user-attachments/assets/24092820-d58e-4ca8-842b-25b4417fb0d9" />

**Descrição:**  
Foi realizada uma requisição direta ao serviço de pedidos para verificar se o endpoint está ativo e funcionando.

**Como reproduzir:**

```
http://localhost:8002/orders/1
```

---

### 🔍 7. Buscar User específico

<img width="718" height="762" alt="Captura de tela 2026-03-23 175603" src="https://github.com/user-attachments/assets/24058b1e-0528-4da4-a3c3-c09a491411fa" />

**Descrição:**  
Foi realizada a busca de um usuário específico pelo seu ID no serviço de usuários.

**Como reproduzir:**

```
http://localhost:8001/users/1
```

---

## ⚠️ Problemas Identificados

* Forte acoplamento entre os serviços  
* Dependência direta entre microsserviços  
* Falha em cascata quando um serviço para  
* Aumento de latência devido à comunicação HTTP  
* Possibilidade de timeout  

---

## ❓ Problemas da comunicação síncrona entre microsserviços

Neste tipo de implementação, os serviços dependem diretamente uns dos outros para responder às requisições. Caso o serviço de usuários fique indisponível, o serviço de pedidos também falha, mesmo estando operacional.

Além disso, atrasos na resposta do serviço dependente aumentam o tempo total de resposta do sistema, podendo causar timeout e degradação da experiência do usuário. Essa dependência também dificulta a escalabilidade e aumenta o acoplamento entre os componentes, tornando o sistema mais vulnerável a falhas.

---

## 📚 Conclusão

Este projeto demonstra como a comunicação síncrona entre microsserviços pode impactar o desempenho e a disponibilidade do sistema, evidenciando a necessidade de soluções mais robustas em cenários reais.

---

## 🛑 Parar os Serviços

```bash
docker-compose down
```
