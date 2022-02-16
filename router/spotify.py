import schemas
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from db.database import get_db
from db import models
from pydantic import BaseModel
from db.models import User_details



app=APIRouter()

@app.post('/spotify_token') 
def spotify_token(spotify_user_token:schemas.Spotify_token,db: Session = Depends(get_db)):

    user_spotify=db.query(models.User_details).filter(models.User_details.id == spotify_user_token.user_id).first()

    update_data = {"token":spotify_user_token.token}

    for name,value in update_data.items():
     setattr(user_spotify,name,value)

    db.add(user_spotify)

    db.commit()
    user_spotify=db.query(models.User_details).filter(models.User_details.id == spotify_user_token.user_id).first() 

    return  {"response":f'successfully updated',"user_details":user_spotify}