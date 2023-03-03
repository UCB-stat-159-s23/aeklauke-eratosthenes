import sys
import math
import numpy as np
from sieve_tools import *

def test_erat_first():
    obs = erat_first(10)
    exp = [2,3,5,7]
    assert obs == exp
    

    