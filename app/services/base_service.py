from math import ceil
from typing import Type, TypeVar, Generic, List
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.core.pagination import paginate

ModelType = TypeVar("ModelType")


class BaseService(Generic[ModelType]):
    model: Type[ModelType] = None  # 반드시 상속 클래스에서 지정

    def __init__(self, db: Session):
        self.db = db

    # 단건 조회
    def get(self, id: int) -> ModelType:
        obj = self.db.query(self.model).get(id)
        if not obj:
            raise HTTPException(status_code=404, detail="데이터를 찾을 수 없습니다.")
        return obj

    # 전체 조회
    def get_all(self) -> List[ModelType]:
        return self.db.query(self.model).all()

    # 생성
    def create(self, obj_in: dict) -> ModelType:
        obj = self.model(**obj_in)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    # 수정
    def update(self, id: int, obj_in: dict) -> ModelType:
        obj = self.get(id)

        for field, value in obj_in.items():
            setattr(obj, field, value)

        self.db.commit()
        self.db.refresh(obj)
        return obj

    # 삭제
    def delete(self, id: int):
        obj = self.get(id)
        self.db.delete(obj)
        self.db.commit()

    def get_query(self):
        return self.db.query(self.model)

    def paginate(self, query, page: int, size: int):
        total = query.count()

        items = (
            query
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )

        total_pages = ceil(total / size) if total > 0 else 0

        return {
            "items": items,
            "page": page,
            "size": size,
            "total": total,
            "total_pages": total_pages
        }