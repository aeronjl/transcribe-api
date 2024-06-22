from fastapi import FastAPI
import precisetranscribe as at

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}