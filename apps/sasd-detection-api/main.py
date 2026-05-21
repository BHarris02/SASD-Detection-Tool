"""
main.py
"""

import sys

sys.dont_write_bytecode = True

from src import create_app

if __name__ == "__main__":
    create_app().run(host="localhost", port=5000)
