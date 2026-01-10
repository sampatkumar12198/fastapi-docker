from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI running in Docker 🚀, ========="}

@app.get("/health")
def health():
    return {"status": "Helth is ok==============="}

@app.get('/test')
def hellow():
    return {'message':'Hellow World!..New text'}
