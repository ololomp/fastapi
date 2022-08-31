from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String, MetaData, func
from sqlalchemy.orm import relationship
import datetime
from database import Base, SessionLocal, engine
from table_user import User
from table_post import Post


class Feed(Base):
    __tablename__ = "feed_action"
    __table_args__ = {"schema": "public"}
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True,  name="user_id")
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True,  name="post_id")
    action = Column(String, name="action")
    time = Column(TIMESTAMP, name="time")
    user = relationship("User")
    post = relationship("Post")


if __name__ == "__main__":

    session = SessionLocal()
    results = (
        session.query(Post.id, Post.text, Post.topic)
            .join(Feed, Feed.post_id == Post.id)
            .filter(Feed.action == 'like')
            .group_by(Post.id, Feed.post_id)
            .order_by(func.count("*").desc())
            .limit(2).all()


    )
    re = []
    for x in results:
        print(x)
