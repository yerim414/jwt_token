from sqlalchemy.orm import Session
from models.todo_model import ToDo
from schemas.todo_schemas import TodoCreate, TodoUpdate


def create_todo(db: Session, id: str, todo: TodoCreate):
    new_todo = ToDo(**todo.model_dump(), ID=id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def get_todos(db: Session, id: str = None, seq: int = None, title: str = None):
    query = db.query(ToDo)

    if id:
        query = query.filter(ToDo.ID == id)

    if seq:
        query = query.filter(ToDo.SEQ == seq)

    if title:
        # NOTE Like 검색으로..
        query = query.filter(ToDo.TITLE.like(f"%{title}%"))

    return query.all()


def update_todo(db: Session, seq: int, todo_data: TodoUpdate, id: str):
    todo = db.query(ToDo).filter(ToDo.ID == id, ToDo.SEQ == seq).first

    if not todo:
        return None

    for key, value in todo_data.model_dump(exclude_unset=True).items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, seq: int, id: str):
    todo = db.query(ToDo).filter(ToDo.ID == id, ToDo.SEQ == seq).first

    if not todo:
        return None

    db.delete(todo)
    db.commit()
    return todo
