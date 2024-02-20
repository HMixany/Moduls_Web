from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/notes/new")
async def read_new_note():
    return {"message": "Return new notes"}


# @app.get("/notes/{note_id}")
# async def read_note(note_id: int = Path()):
#     return {"note": note_id}


@app.get("/notes/{note_id}")
async def read_note(note_id: int = Path(description="Identifier of the note", gt=0, le=3)):
    return {"note": note_id}