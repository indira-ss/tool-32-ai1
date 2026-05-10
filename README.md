# AI Service API

## Overview
AI-powered Flask backend using Groq API.

## Features
- AI report generation
- Health endpoint
- Docker support
- Render deployment

## Run Project

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
python app.py
```

## API Endpoints

### Root
GET /

### Health
GET /health

### Generate Report
POST /generate-report

Example request:

```json
{
  "text": "AI in healthcare"
}
```

## Deployment
Hosted on Render.