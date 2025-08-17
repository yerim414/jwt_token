from pydantic import BaseModel, Field

class ToDoBase(BaseModel):
    TITLE: str = Field(min_length=1, max_length=50)
    DESCRIPTION : str | None = Field(default=None, max_length=255)

class TodoCreate(ToDoBase):
    pass

class TodoUpdate(BaseModel):
    TITLE: str | None = None
    DESCRIPTION: str | None = None
    COMPLETED: bool | None = None

class TodoResponse(ToDoBase):
    ID: int
    COMPLETED: bool

    # NOTE : orm 객체를 dict처럼 읽어서 변환
    class Config:
        orm_mode = True