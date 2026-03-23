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

📸 PRINT:
(cole aqui o print)

Descrição:
O serviço de pedidos retornou corretamente os dados do pedido junto com as informações do usuário.

---

### ❌ 2. Pedido inexistente

📸 PRINT:
<img width="713" height="751" alt="Captura de tela 2026-03-23 171126" src="https://github.com/user-attachments/assets/9b142b48-e488-4ef3-8865-98327935231c" />


Descrição:
Foi feita uma requisição com um ID inválido e o sistema retornou erro informando que o pedido não foi encontrado.

---

### 🔥 3. Falha de comunicação entre serviços

📸 PRINT:
(cole aqui o print)

Descrição:
O serviço de usuários foi desligado, e o serviço de pedidos retornou erro ao tentar se comunicar.

---

### 🐢 4. Teste de latência

📸 PRINT:
(cole aqui o print)

Descrição:
Foi adicionado um atraso no serviço de usuários utilizando `time.sleep()`, aumentando o tempo de resposta do sistema.

---

## ⚠️ Problemas Identificados

* Forte acoplamento entre os serviços
* Dependência direta entre microsserviços
* Falha em cascata quando um serviço para
* Aumento de latência devido à comunicação HTTP
* Possibilidade de timeout

---

## 📚 Conclusão

Este projeto demonstra como a comunicação síncrona entre microsserviços pode impactar o desempenho e a disponibilidade do sistema, evidenciando a necessidade de soluções mais robustas em cenários reais.

---

## 🛑 Parar os Serviços

```bash
docker-compose down
```
