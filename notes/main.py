from fastapi import FastAPI, Depends, HTTPException
from typing import List
import json
import os
from .models import Note
from .auth import get_current_user
from .yandex_speller import check_spelling

app = FastAPI()

notes: List[dict] = []
try:
    with open("data/notes.json", "r", encoding="utf-8") as f:
        notes = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    notes = []


@app.post("/notes/", response_model=Note)
def add_note(note: Note, user: str = Depends(get_current_user)) -> Note:
    errors = check_spelling(note.text)
    if errors:
        raise HTTPException(
            status_code=400,
            detail={"message": "Spelling errors detected!", "errors": errors},
        )

    note_dict = note.model_dump()
    note_dict["user"] = user
    notes.append(note_dict)

    if not os.path.exists("data"):
        os.makedirs("data")

    with open("data/notes.json", "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)

    return note


@app.get("/notes/", response_model=List[Note])
def get_notes(user: str = Depends(get_current_user)) -> List[Note]:
    return [Note(**note) for note in notes if note.get("user") == user]
