import os
import sys

# Make sure the project root is on the import path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Import your Flask app from main.py
from main import app  # assumes main.py defines `app = Flask(__name__)`
