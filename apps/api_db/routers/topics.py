from fastapi import APIRouter
from models.table_topic import *

router = APIRouter(
    prefix="/topics",
    tags=["Topics"]
)

@router.get('')
def get_topics():
    return get_all_topic()