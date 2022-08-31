from sqlalchemy import TIMESTAMP, Column, func, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import datetime
from database import Base, SessionLocal, engine


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, name="id")
    gender = Column(Integer, name="gender")
    age = Column(Integer, name="age")
    country = Column(String,  name="country")
    city = Column(String,  name="city")
    exp_group = Column(Integer,  name="exp_group")
    os = Column(String, name="os")
    source = Column(String,  name="source")


if __name__ == "__main__":
    session = SessionLocal()
    results = (
        session.query(User)
        .filter(User.exp_group == 3)
        .with_entities(User.country, User.os, func.count())
        .group_by(User.os, User.country)
        .having(func.count() > 100)
        .order_by(func.count().desc())
        .all()
    )
    re = []
    for x in results:
        re.append(x)
    print(re)




