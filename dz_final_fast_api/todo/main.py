from fastapi import FastAPI
import database
import schemas

app = FastAPI()

database.init_db()

@app.get("/")
def homework_api():
    return {"message": "!!!HOMEWORK!!!"}

@app.get("/items")
def get_items():
    items = database.get_all()
    return {"items": items}

@app.post("/items")
def add_item(item: schemas.ItemCreate):
    item_id = database.add_item(item.title, item.description, item.completed)
    return {
        "id": item_id,
        "title": item.title,
        "description": item.description,
        "completed": item.completed
    }

@app.put("/items/{id}")
def update_item(id: int, done: int):
    database.update_item(id, done)
    return {"updated": id, "done": done}

@app.delete("/items/{id}")
def delete_item(id: int):
    database.delete_item(id)
    return {"deleted": id}