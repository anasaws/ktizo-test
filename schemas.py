from pydantic import BaseModel
import uuid
from pydantic.networks import EmailStr

class User(BaseModel):
    full_name:str
    email:str
    password:str
    age:int=None
    spotify_artist_profile:str=None
    favourite_music_style:str=None
    favourite_music_mood:str=None
    yourown_music:str=None
    favourite_music_topic:str=None
    master:str=None
    publish_control:str=None
    outside_income:str=None
    established_artist:str=None
    company :str=None
    linkedin_profile:str=None
    project_seek_music:str=None
    turn_around_time:str=None
    project_budject:str=None
    syncs_seek:str=None
    token:str=None
    user_role:str
class UserLogin(BaseModel):
    email:str
    password:str
class Spotify_token(BaseModel):
    user_id:uuid.UUID
    token:str=None
