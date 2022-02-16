import schemas
import uuid
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from db.database import get_db
from db import models
from typing import List
from pydantic import BaseModel
from db.models import User_details
from hash.hash import Hasher

app=APIRouter()

#To signup a user
@app.post("/signup")
def user_signup(user_input:schemas.User, db: Session = Depends(get_db)):
    user_register=db.query(models.User_details).filter(models.User_details.email == user_input.email).first()
    
    if user_register is None:
        new_user=models.User_details(
            id=uuid.uuid4(),
            full_name=user_input.full_name,
            email=user_input.email,
            password=Hasher.get_hash_password(user_input.password),
            age=user_input.age,
            spotify_artist_profile=user_input.spotify_artist_profile,
            favourite_music_style=user_input.favourite_music_style,
            favourite_music_mood=user_input.favourite_music_mood,
            yourown_music= user_input.yourown_music,
            favourite_music_topic= user_input.favourite_music_topic,
            master= user_input.master,
            publish_control=user_input.publish_control,
            outside_income=user_input.outside_income,
            established_artist=user_input.established_artist,
            company=user_input.company,
            linkedin_profile=user_input. linkedin_profile,
            project_seek_music=user_input.project_seek_music,
            turn_around_time=user_input.turn_around_time,
            project_budject=user_input.project_budject,
            syncs_seek=user_input.syncs_seek,
            token=user_input.token,
            user_role=user_input.user_role
        )
        db.add(new_user)
        
        db.commit() 
    
       
        return  {"response":f'successfully registerd'}
    else:
        return {"response":" name already taken"}

@app.post('/login')
def login(user:schemas.UserLogin, db: Session = Depends(get_db)):

    user_login=db.query(models.User_details).filter(models.User_details.email == user.email).first()

    if user_login is  None:

            return {"response":"Invalid Email"}

    if not Hasher.verify_password(user.password, user_login.password):

            return {"response":"Invalid password"}

    return  {"response":f'successfully login',"user_id":user_login.id,"token":user_login.token,"user_role":user_login.user_role}

