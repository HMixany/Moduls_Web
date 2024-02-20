from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/")
async def get_todos():
    pass


@router.get("/{todo_id}")
async def get_todo():
    pass


@router.post("/")
async def create_todo():
    pass


@router.put("/{todo_id}")
async def update_todo():
    pass


@router.delete("/{todo_id}")
async def delete_todo():
    pass
