import random
import sys, os
sys.path.append(os.path.join(sys.path[0],'../..'))
from src.config import symbols

def test_random():
    a = random.choice(symbols)
    b = random.choice(symbols)

    assert a != b