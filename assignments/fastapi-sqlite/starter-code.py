import sqlite3

from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_NAME = "tasks.db"

app = FastAPI()


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""
    completed: bool = False


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )


create_table()


@app.get("/")
def root():
    return {"message": "Implement the Task API"}
