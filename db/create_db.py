from database import Base,engine
from models import User_data

Base.metadata.create_all(engine)