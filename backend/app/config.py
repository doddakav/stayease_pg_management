from dotenv import load_dotenv
import os

load_dotenv()

# These are not used yet (no JWT/bcrypt login today).
# They are kept here so auth can be added later without
# having to set up config again. Safe defaults are used
# so this file does not crash if it gets imported.

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key-later")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))