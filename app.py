"""Minimal FastAPI app for the math chatbot.

FastAPI is optional; if it's not installed the module will still import but the
web API won't be available.
"""

try:  # pragma: no cover - optional dependency
    from fastapi import FastAPI, File, UploadFile
except Exception:  # pragma: no cover - optional dependency
    FastAPI = None  # type: ignore
    File = UploadFile = None  # type: ignore

from solver import solve_equation
from extractors import extract_text_from_pdf, extract_text_from_image
import io

if FastAPI:
    app = FastAPI(title="Math Chatbot")

    @app.post("/solve")
    async def solve(question: dict):
        text = question.get("question", "")
        return solve_equation(text)

    @app.post("/upload")
    async def upload(file: UploadFile = File(...)):
        data = await file.read()
        buf = io.BytesIO(data)
        if file.filename.lower().endswith(".pdf"):
            text = extract_text_from_pdf(buf)
        else:
            text = extract_text_from_image(buf)
        return solve_equation(text)
else:
    app = None
