from sqlalchemy import Column, Integer, String

# from sqlalchemy.orm import relationship
# from sqlalchemy.sql.schema import ForeignKey

from . import database


class BaseMixin:
    sysId = Column(String, primary_key=True, index=True)


class User(BaseMixin, database.Base):
    __tablename__ = "user"

    # quiz_id = Column(Integer, ForeignKey("quiz.id"), nullable=True)
    sysId = Column(String(50), primary_key=True, nullable=False)
    userId = Column(String(20))
    userName = Column(String(45))
    nickName = Column(String(50))
    email = Column(String(45), default=None)
    phone = Column(String(45), default=None)
    grade = Column(Integer(), default=None)
