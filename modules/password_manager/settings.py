import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv()


BASE_DIR = Path.cwd()

engine = create_engine(os.getenv('PasswordManagerEngine', '')) # I'll confige it later
Session = sessionmaker(engine)
