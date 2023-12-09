# routers/stock_price_router.py
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from ..controllers.stock_price_controller import get_stock_price_data, save_upload_file

stock_price_router = APIRouter(
    prefix="/api",
    tags=["stock_prices"],
)

# Get the stock price data
@stock_price_router.get("/stock_prices/")
def get_stock_prices():
    file_path = "data/prices.csv"
    try:
        stock_prices = get_stock_price_data(file_path)
        return stock_prices
    except HTTPException as e:
        raise e

# Route to receive the uploaded CSV file
@stock_price_router.post("/stock_prices/")
def upload_stock_prices(file: UploadFile = File(...)):
    try:
        # Save the uploaded CSV file
        save_upload_file(file, "data/prices.csv")
        return {"message": "File uploaded successfully"}
    except HTTPException as e:
        raise e

