# Projeto para atendimeto médico online ao idoso

Sistema web para gerenciamento de consultas médicas com suporte a videochamadas em tempo real, desenvolvido com Django e WebRTC.

---

## 📌 Sobre o projeto

O projeto é uma plataforma voltada para facilitar o acesso de idosos a atendimentos médicos remotos, permitindo:

- Agendamento de consultas
- Gerenciamento de médicos e pacientes
- Videochamadas em tempo real
- Troca de mensagens durante consultas

---

##  Tecnologias utilizadas

###  Backend
- Django
- Django REST Framework
- SQLite
- Python

###  Frontend
- HTML
- CSS
- JavaScript

###  Comunicação em tempo real
- WebRTC
- Socket.IO
- Node.js
- Express

### 🛠️ Ferramentas
- Git
- GitHub
- VS Code / PyCharm

---

## 🧠 Arquitetura

O sistema segue uma arquitetura baseada em **API REST**, onde:

- O **Django** gerencia o backend e o banco de dados
- O **Django REST Framework** expõe os endpoints
- O **Node.js + Socket.IO** realizam a sinalização
- O **WebRTC** permite comunicação P2P (vídeo e chat)

---

## 📊 Funcionalidades

### 👤 Usuários
- Cadastro de pacientes e médicos
- Autenticação personalizada (Custom User)

### 📅 Agendamentos
- Criação de agendas médicas
- Geração automática de horários
- Controle de disponibilidade

### 🎥 Videochamada
- Conexão P2P com WebRTC
- Áudio e vídeo em tempo real
- Chat entre usuários

---

## 🔁 Fluxo da aplicação

1. Usuário acessa o sistema
2. Realiza login (paciente ou médico)
3. Agenda uma consulta
4. Entra na sala de videochamada
5. Conexão é estabelecida via WebRTC

---


---

## ⚙️ Como executar o projeto

Para esse projeto, são necessários dois terminais, um para a aplicação Backend(Django) e outro para aplicação WebRTC

### 🔹 Backend (Django)

```bash

## Entrar na pasta do servidor
cd ProjetoFinalDS

# Ative o ambiente virtual (Windows)
.\venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Rodar servidor
python manage.py runserver

```

🔹 WebRTC (Node.js)

```bash

# Entrar na pasta do servidor
cd webrtc-server

# Instalar dependências
npm install

# Rodar servidor
node server.js

```

## ⚠️ Observações

- Ative primeiramente o backend
- Certifique-se de que o backend e o servidor WebRTC estejam rodando simultaneamente
- Para ver a aplicação Web RTC funcionar, é necessário que seu computador ou notbook tenha câmera
---


## Destaques técnicos

- Modelagem relacional eficiente com Django ORM
- Uso de AbstractUser para autenticação personalizada
- Geração automática de horários baseada em períodos
- Comunicação P2P com WebRTC (baixa latência)
- Uso de Socket.IO para sinalização

