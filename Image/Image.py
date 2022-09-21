import cv2
import torch
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
from torch.autograd import Variable

from pathlib import Path

class Image():

    # Constructor
    def __init__(self, path):

        """ Initialise with path only"""

        # Store image path
        self.path = Path(path)
        
        # Extract name
        self.name = self.path.name
                
        # Read image
        self.read()


    def read(self):

        """ Read image """

        # Read image
        image = cv2.imread(self.path, -1)

        # Image is already greyscale and just has width x height
        if len(image.shape) < 3: 

            self.grey  = True
            self.array = image
            
        # Image is of the form (height, width, 1)
        elif image.shape[2]  == 1:
            image = image.reshape((image.shape[0], image.shape[1]))
            self.grey  = True
            self.array = image

        # Image has 3 channels
        else:
            # Extract BGR value
            b,g,r = image[:,:,0], image[:,:,1], image[:,:,2]

            # If all channels are equal is greyscale
            if (b==g).all() and (b==r).all():
                image = image[:, :, :1]
                self.grey  = True
                self.array = image

            # RGB image
            else:
                self.grey  = False
                self.array = image

    def plot(self):

        """ Plot image """

        figsize = (10, 10)

        plt.figure(figsize=figsize)
        plt.imshow(self.image)
        plt.axis("off")
        plt.show()

