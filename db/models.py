from db.database import Base
from sqlalchemy import Integer,String,Column,Boolean,DateTime
from sqlalchemy_utils import URLType, UUIDType


class User_details(Base):
    __tablename__='user'
    __table_args__ = {'extend_existing': True}
    id = Column(UUIDType, primary_key=True)
    full_name=Column(String(255),unique=True)
    email=Column(String(255),unique=True)
    password=Column(String(255))
    age = Column(Integer)
    spotify_artist_profile=Column(String(255))
    favourite_music_style=Column(String(255))
    favourite_music_mood=Column(String(255))
    yourown_music=Column(String(255))
    favourite_music_topic=Column(String(255))  
    master=Column(String(255))
    publish_control=Column(String(255))
    outside_income=Column(String(255))
    established_artist=Column(String(255))
    company=Column(String(255))
    linkedin_profile=Column(String(255))
    project_seek_music=Column(String(255))
    turn_around_time=Column(String(255))
    project_budject=Column(String(255))
    syncs_seek=Column(String(255))
    token =Column(String(255),nullable=True)
    user_role=Column(String(255),nullable=False)
    
   
