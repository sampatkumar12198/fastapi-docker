from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI running in Docker 🚀, This is new change222"}

@app.get("/health")
def health():
    return {"status": "ok............11"}
