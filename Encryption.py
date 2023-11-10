from numpy.core.arrayprint import printoptions
from ImageSteg import ImageSteg
from PIL import Image
import pandas as pd
import numpy as np


img = ImageSteg()

img.encrypt_text_in_image("test.jpeg","THIS IS MY SECERT  MESSAGE ","project/")
