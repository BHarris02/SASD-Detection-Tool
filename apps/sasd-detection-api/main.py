"""
main.py
"""
import sys

from src import create_app

sys.dont_write_bytecode = True

if __name__ == "__main__":
    print("[sasd-detection-api] Running...")
    create_app().run(host="localhost", port=5000, debug=True)
