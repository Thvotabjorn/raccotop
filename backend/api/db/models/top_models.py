from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (Mapped,  # relationship
                            mapped_column)
from sqlalchemy.types import DateTime, Integer, String, Text, Boolean

from models.base_model import BaseModel


class CustomList(BaseModel):
    __table_name__ = "custom_lists"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text)
    is_numbered: Mapped[bool] = mapped_column(Boolean)


class ListItem(BaseModel):
    __table_name__ = "list_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text)
    serial_number: Mapped[int] = mapped_column(Integer, nullable=True)
    custom_list: Mapped[int] = mapped_column(ForeignKey("custom_lists.id"))
