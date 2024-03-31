import sqlalchemy
from fastapi import FastAPI, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

from my_program.src.database.db import get_db
from my_program.src.entity.models import Build
from src.schemas.build import HomeResponse, HomeSchema

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Application v0.0.1"}


@app.get("/homes", response_model=list[HomeResponse], tags=["homes"])
async def get_homes(db: Session = Depends(get_db)):
    homes = db.query(Build).all()
    return homes


@app.get("/homes/{build_id}", response_model=HomeResponse, tags=["homes"])
async def get_home_by_level(build_id: int = Path(ge=1), db: Session = Depends(get_db)):
    home = db.query(Build).filter_by(id=build_id).first()
    if home is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return home


@app.post("/homes", response_model=HomeResponse, tags=["homes"])
async def create_home(body: HomeSchema, db: Session = Depends(get_db)):
    home = db.query(Build).filter_by(level=body.level).first()
    if home:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This level is existing!")
    home = Build(
        name=body.name, level=body.level, gold=body.gold, tree=body.tree, stone=body.stone, corn=body.corn,
        iron=body.iron, crystals=body.crystals
    )
    db.add(home)
    db.commit()
    return home


@app.put("/homes/{build_id}", response_model=HomeResponse, tags=["homes"])
async def update_home(body: HomeSchema, build_id: int = Path(ge=1), db: Session = Depends(get_db)):
    home = db.query(Build).filter_by(id=build_id).first()
    if home is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    home.name = body.name
    home.level = body.level
    home.gold = body.gold
    home.tree = body.tree
    home.stone = body.stone
    home.corn = body.corn
    home.iron = body.iron
    home.crystals = body.crystals
    db.commit()
    return home


@app.delete("/homes/{build_id}", response_model=HomeResponse, tags=["homes"])
async def delete_home(build_id: int = Path(ge=1), db: Session = Depends(get_db)):
    home = db.query(Build).filter_by(id=build_id).first()
    if home is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    db.delete(home)
    db.commit()
    return home


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        # Make request
        result = db.execute(sqlalchemy.text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")