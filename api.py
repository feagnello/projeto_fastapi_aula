import uvicorn
from fastapi import FastAPI

app = FastAPI()

def example() -> str:
    return "Olá Mundo"

if __name__ == "__main__":
    print(example())
    uvicorn.run(app, port=8088)
    
    
