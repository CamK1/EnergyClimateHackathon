from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow your React frontend to talk to this backend
origins = [
    "http://localhost:3000",  # common React dev server
    "http://localhost:5173",  # common Vite dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "FastAPI backend is running"}

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI"}

@app.post("/api/add")
async def add_numbers(data: dict):
    a = data.get("a", 0)
    b = data.get("b", 0)
    return {"result": a + b}