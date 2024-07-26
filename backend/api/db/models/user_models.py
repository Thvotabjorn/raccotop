from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (Mapped,  # relationship
                            mapped_column)
from sqlalchemy.types import DateTime, Integer, String, Text, Boolean

from models.base_model import BaseModel


class User(BaseModel):
    __table_name__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(String(64))
    nickname: Mapped[str] = mapped_column(String(64))
    name: Mapped[str] = mapped_column(String(256))
    password: Mapped[str] = mapped_column(String(256))
