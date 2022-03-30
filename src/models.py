from fastapi import Query
from pydantic import BaseModel, validator
import re

class CalcGetRequest(BaseModel):
    expression: str = Query(None, max_length=50)


class CalcPostRequest(BaseModel):
    first: int
    last: int
    operator: str
    @validator('operator')
    def onlySimpleMath(cls, v):
        if v == '*' or v == '/' or v == '-' or v == '+':
            return v
        raise ValueError('Возможен только простой математический запрос.')


class CalcResponce(BaseModel):
    result: str = None
    operation: str = None