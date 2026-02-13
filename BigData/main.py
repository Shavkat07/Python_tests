from database import SessionLocal
from models import *

db = SessionLocal()

artists = db.query(Customer)

print(artists)
# for a in artists:
#     print(a.ArtistId, a.Name)

db.close()
