import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from table_user import User
from table_post import Post
from table_feed import Feed
from database import SessionLocal
from schema import UserGet, PostGet, FeedGet
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
import yaml
app = FastAPI()


def config():
    with open("params.yaml", "r") as f:
        return yaml.safe_load(f)


def get_db():
    with SessionLocal() as db:
        return db


@app.get('/user/{id}', response_model=UserGet)
def users_08(id, db: Session = Depends(get_db)):
    results = (db.query(User).filter(User.id == id).one_or_none())
    if not results:
        raise HTTPException(status_code=404, detail="user not found")
    else:
        return results


@app.get('/post/{id}', response_model=PostGet)
def users_08(id, db: Session = Depends(get_db)):
    results = (db.query(Post).filter(Post.id == id).one_or_none())
    if not results:
        raise HTTPException(status_code=404, detail="post not found")
    else:
        return results


@app.get('/post/{id}/feed', response_model=List[FeedGet])
def users_08(id, limit: int = 10, db: Session = Depends(get_db)):
    results = (db.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit).all())
    if not results:
        raise HTTPException(status_code=200, detail=[])
    else:
        return results


@app.get('/user/{id}/feed', response_model=List[FeedGet])
def users_08(id, limit: int = 10, db: Session = Depends(get_db)):
    results = (db.query(Feed).filter(Feed.user_id == id).order_by(Feed.time.desc()).limit(limit).all())
    if not results:
        raise HTTPException(status_code=200, detail=[])
    else:
        return results


@app.get('/post/recommendations/')  #, response_model=List[FeedGet])
def users_08(id: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    results = (db.query(Post.id, Post.text, Post.topic)
            .join(Feed, Feed.post_id == Post.id)
            .filter(Feed.action == 'like')
            .group_by(Post.id, Feed.post_id)
            .order_by(func.count("*").desc())
            .limit(limit).all())
    if not results:
        raise HTTPException(status_code=200, detail=[])
    else:
        return results


if __name__ == "__main__":
    uvicorn.run(app)
