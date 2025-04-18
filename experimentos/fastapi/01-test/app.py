from typing import Annotated, Dict, List
from fastapi import FastAPI, HTTPException, Path, Query
from models.test_model import TestModel
import uuid

fake_db:Dict[uuid.UUID, TestModel] = {}

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#test/33'
@app.get("/test/{arg}")
async def test1(arg:int):
    return {"arg": arg}

#test2/algo'
@app.get("/test2/{arg}")
async def test2(arg:str):
    return {"arg": arg}

#test3?arg=true'
@app.get("/test3")
async def test3(arg:bool):
    return {"arg": arg}

@app.post("/test4")
async def test4(arg:int, arg2:float):
    return {
        "suma": arg+arg2
    }

@app.post("/test5")
async def test5(test_model:TestModel) -> uuid.UUID:
    id = uuid.uuid4()

    fake_db[id]=test_model

    return id

@app.get("/test6/{test_model_id}")
async def test6(test_model_id:Annotated[uuid.UUID, Path(description="El Id del elemento")]) -> TestModel:
    if not test_model_id in fake_db:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")

    return fake_db[test_model_id]

@app.get("/test7")
async def test7() -> List[TestModel]:
    return fake_db.values()


@app.get("/test8/{num}")
async def test8(num:Annotated[float, Query(ge=-3, le=3), Path(description="Un numero entre -3 y 3")]) -> int:
    return num

