import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    print("Inverting colors...")
    inverted_array = 255 - array
    return inverted_array


def ft_red(array: np.ndarray) -> np.ndarray:
    """Filters the image to show only the Red channel."""
    
    red_array = array.copy()
    print("Filtering to Red...")
    red_array[:, :, 1] = red_array[:, :, 1] * 0 
    red_array[:, :, 2] = red_array[:, :, 2] * 0 
    return red_array