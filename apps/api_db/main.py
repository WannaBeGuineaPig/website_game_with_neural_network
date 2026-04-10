import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import topics

app = FastAPI()

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(topics.router)

@app.get("/")
def read_root():
    return 'Hello to API Deal With Pixel!'

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)