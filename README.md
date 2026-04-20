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

## ⚙️ Como executar o projeto

Clonando o projeto

```bash
git clone https://github.com/geissianeassuncao/projeto-final-dev-soft.git
cd projeto-final-dev-soft
```

Abrir no Vs Code (opcional)
```bash
code .
```

Para esse projeto, são necessários dois terminais:

- um para o Backend (Django)
- outro para o WebRTC (Node.js)

### 🔹 Backend (Django)

```bash

# Criar ambiente virtual
python -m venv venv

# (Windows) liberar execução de scripts (caso necessário)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Ativar ambiente virtual
.\venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Entrar na pasta do backend
cd backend

# Rodar migrações
python manage.py migrate

# Rodar servidor
python manage.py runserver

```

## 👤 Acesso ao sistema

```bash
# Entrar na pasta do backend
cd backend

# Criar usuário administrador
python manage.py createsuperuser
```

Acesse:

http://127.0.0.1:8000/admin/

Crie usuários e vincule-os como:

- paciente
- médico

🔹 WebRTC (Node.js)

```bash

# Entrar na pasta do WebRTC
cd webrtc

# Instalar dependências
npm install

# Rodar servidor
npm start

```

Agora só precisa voltar a tela de login e entrar como médico ou paciente. Em seguida, clicar na opção iniciar chamada

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

