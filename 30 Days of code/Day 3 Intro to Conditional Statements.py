#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    assert 1<=N<=100, "Error!"
    if N % 2 != 0:
        print("Weird")
    # If  is even and in the inclusive range of  to , print Not Weird
    if N % 2 == 0:
        if 2 <= N <= 5:
            print("Not Weird")
        if 6 <= N <= 20:
            print("Weird")
        if N > 20:
            print("Not Weird")
