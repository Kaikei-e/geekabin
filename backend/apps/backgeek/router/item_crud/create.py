from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/item/create", tags=["item"])
async def create_item(item_info: Request):
    return {"item_info": item_info}
