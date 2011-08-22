import numpy as np
import cv
import time


def sobel(image, axis=None, output=None):
    """
    OpenCV implementation of the sobel operator.
    """
    if not image.flags["C_CONTIGUOUS"]:
        image = np.ascontiguousarray(image)
    if image.dtype == np.uint8:
        output_type = np.int16
    elif image.dtype == np.float32:
        output_type = np.float32
    else:
        raise TypeError, "Input type of uint8 or float32 expected."
    # magnitude of edges
    if axis is None:
        dx = np.empty(image.shape, dtype=np.float32)
        dy = np.empty(image.shape, dtype=np.float32)
        cv.Sobel(image, dx, 0, 1, 3)
        cv.Sobel(image, dy, 1, 0, 3)
        cv.Pow(dx, dx, 2)
        cv.Pow(dy, dy, 2)
        cv.Add(dx, dy, dx)
        cv.Pow(dx, dx, 0.5)        

        if output:
            output[:] = dx
            return output
        else:
            return dx
    else:
        if not output:
            output = np.zeros(image.shape, dtype=output_type)
        # horizontal edges
        if axis == 0:
            cv.Sobel(image, output, 0, 1, 3)
        # vertical edges
        elif axis == 1:
            cv.Sobel(image, output, 1, 0, 3)
        return output