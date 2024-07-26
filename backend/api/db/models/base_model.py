from sqlalchemy import TIMESTAMP, func
from sqlalchemy.types import DateTime
from sqlalchemy.orm import (DeclarativeBase, Mapped, declared_attr,
                            mapped_column)


class BaseModel(DeclarativeBase):
    __abstarct__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[DateTime] = mapped_column(default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        TIMESTAMP(timezone=True),
        default=func.now(),
        onupdate=func.now()
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"