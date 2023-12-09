from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from dotenv import load_dotenv
from contextlib import asynccontextmanager

# Load the environment variables from the .env file
#load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executed on startup
    print("Startup")
    yield
    # Executed on shutdown
    print("Shutdown")

# Create a FastAPI app
app = FastAPI(
    title="Stock Market Data API",
    description="Stock Market Data API",
    version="0.1.0",
    docs_url="/docs",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://stock-market-data-frontend.onrender.com/", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Define a root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, World"}

# Import the routers
from app.routers.stock_price_router import stock_price_router

app.include_router(stock_price_router)


if __name__ == "__main__":
    import uvicorn

    # Run the application using Uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)