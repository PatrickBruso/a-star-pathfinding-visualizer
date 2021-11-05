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

# Color constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE= (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)



