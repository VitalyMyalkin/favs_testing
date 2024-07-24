from typing import TypedDict


class Favorite(TypedDict):
    id: int
    title: str
    lat: float
    lon: float
    color: str | None
    created_at: str


class ErrorModel(TypedDict):
    id: int
    title: str
