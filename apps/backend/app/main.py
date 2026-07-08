from fastapi import FastAPI

app = FastAPI(
    title="TradeForge API",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "message": "Welcome to TradeForge API 🚀"
    }