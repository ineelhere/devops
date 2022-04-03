from fastapi import FastAPI
from enum import Enum
import pandas as pd
import random

app = FastAPI()

@app.get("/get_quotes/")
async def get_quotes():
    df = pd.read_csv("data.csv")
    return ((df.loc[df.id == random.randint(0,len(df))])["comb"])