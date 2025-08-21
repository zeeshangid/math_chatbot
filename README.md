# math_chatbot

A simple FastAPI-based chatbot that solves math questions step by step. It can
accept direct text questions or extract math problems from uploaded PDF or image
files.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running

Start the web server:

```bash
uvicorn app:app --reload
```

## Usage

- `POST /solve` with JSON `{ "question": "x + 1 = 3" }`
- `POST /upload` with a PDF or image file containing a math problem
