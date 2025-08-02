from fastapi import FastAPI;
from pydantic import BaseModel;
from typing import List;

app = FastAPI()

# defining a model for tea items
class Tea(BaseModel):
    id: int
    name: str
    origin: str 
    price: float

# defining a list to hold tea items
teas: List[Tea] = []

# decorator for the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea house!!"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return {"message": "Tea added successfully", "tea": tea}

@app.put("/teas/{tea_id}")
def update_tea(tea_id:int, update_tea:Tea):
    for index, tea in enumerate(teas):
        if tea.id== tea_id:
            teas[index]=update_tea
            return update_tea
    return {"error":"Tea not found"}

@app.delete("/teas/{teas_id}")
def delete_tea(tea_id:int):
    for index, tea in enumerate(teas):
        if tea.id==tea_id:
            deleted = teas.pop(index)
            return deleted
    return {"error":"Tea not found"}


            