from fastapi import FastAPI, Query
from pydantic import BaseModel
import Pycodz.ai as nova
from fastapi.middleware.cors import CORSMiddleware

bot = nova.PHIND()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/blackhat")
def chat(
    request: str= Query(..., title="Prompt", description="Prompt for the chatbot")
    ):
    # Teach and control the bot to respond as NOVA GPT with additional rules
    rules = [
        "You are NOVA GPT, an advanced AI developed by @medjahdi.",
        "Always provide accurate and concise information.",
        "Be polite and professional in your responses.",
        "If you don't know the answer, say so.",
        "Do not start responses with unnecessary preamble.",
        "Provide direct and professional responses."
    ]
    prompt = "\n".join(rules) + "\n" + request
    return {
        "response": bot.chat(prompt=prompt)
    }
