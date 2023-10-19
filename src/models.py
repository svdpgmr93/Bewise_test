from sqlalchemy import Column, Integer, String, DateTime, sql
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Test(Base):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    outer_id = Column(Integer, unique=True)
    question = Column(String)
    answer = Column(String)
    create_time = Column(DateTime(timezone=True), server_default=sql.func.now())

    def to_json(self):
        data = {'id': self.id, 'question': self.question, 'answer': self.answer, 'create_time': self.create_time}
        return data
