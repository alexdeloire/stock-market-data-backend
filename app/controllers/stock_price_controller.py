# controllers/formations_controller.py
from fastapi import HTTPException
import pandas as pd
import shutil

def get_stock_price_data(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Initialize an empty dictionary to store the formatted data
    formatted_data = {'dates': list(df['Date'])}

    # Iterate through each column (excluding the 'Date' column) and add it to the dictionary
    for column in df.columns[1:]:
        formatted_data[column] = list(df[column])

    return formatted_data

def save_upload_file(file, destination):
    try:
        # Open the file in write mode
        with open(destination, "wb") as buffer:
            # Write the contents of the uploaded file to the destination
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))