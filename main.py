"""
A* search algorithm implemented in pygame using Euclidean distance
"""

import pygame as pg
import math
from queue import PriorityQueue

# Initialize pygame window and caption
WIDTH = 800
WIN = pg.display.set_mode((WIDTH, WIDTH))
pg.display.set_caption("A* Path Finding Algorithm")


