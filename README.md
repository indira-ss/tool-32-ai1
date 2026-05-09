<<<<<<< HEAD
# Tool-32 AI Service

AI-powered microservice built using Flask and Groq API.

## Features

- AI procedure description generation
- Recommendation generation
- Report generation
- Health monitoring endpoint
- Input validation and sanitization
- Error handling and fallback responses
- Docker support

---

# Tech Stack

- Python
- Flask
- Groq API
- REST API
- Docker

---

# Project Structure

```bash
ai-service/
│
├── routes/
├── services/
├── prompts/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/indira-ss/tool-32-ai1.git
```

---

## 2. Move Into Project

```bash
cd tool-32-ai1
```

---

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

---

## 4. Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Create .env File

```env
GROQ_API_KEY=your_api_key_here
```

---

## 7. Run Server

```bash
python app.py
```

---

# API Endpoints

## Health

```http
GET /health
```

---

## Describe

```http
POST /describe
```

Example:

```json
{
  "text": "how to install python"
}
```

---

## Recommend

```http
POST /recommend
```

Example:

```json
{
  "text": "how to improve laptop performance"
}
```

---

## Generate Report

```http
POST /generate-report
```

Example:

```json
{
  "text": "AI in education"
}
```

---

# Docker Run

## Build Image

```bash
docker build -t tool-32-ai .
```

## Run Container

```bash
docker run -p 5000:5000 tool-32-ai
```

---

# Author

Indira S Gowda
=======
# Procedure Documentation Tool
>>>>>>> cf09fba610074f81d293e542eba3de193027b72c
