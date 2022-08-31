from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import datetime
from database import Base, SessionLocal, engine


class Post(Base):
    __tablename__ = "post"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, name="id")
    text = Column(String, name="text")
    topic = Column(String, name="topic")


if __name__ == "__main__":
    session = SessionLocal()
    results = (
        session.query(Post)
        .filter(Post.topic == "business")
        .order_by(Post.id.desc())
        .limit(10)
        .all()
    )
    re = []
    for x in results:
        re.append(x.id)
    print(re)
