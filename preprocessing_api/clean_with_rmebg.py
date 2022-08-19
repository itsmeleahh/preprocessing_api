from typing_extensions import assert_type
import matplotlib.pyplot as plt
import os
import shutil
import sys

from datetime import datetime
from IPython.display import display
from pathlib import Path
from PIL import Image, ImageEnhance

import numpy as np
from rembg import remove

# Check the python version to be compatible with rembg
assert sys.version > 3.9, 'Please update your Python version to 3.9'


# Remove the background from the directory.
def remove_bg(input_dirpath, output_dirpath, output_name,
              input_type='jpg', output_type='jpg'):

    assert (input_dirpath and output_dirpath).is_dir(), "It's not a directory."

    # Load the files
    c_train = Path(input_dirpath)
    imgcnames = sorted([f for f in c_train.iterdir() if input_type in f.suffix])

    print(f"There's {len(imgcnames)} pics in the directory.")
    print(f"Image path looks like: {imgcnames[0]}")

    for img in imgcnames:
        output_path = os.path.join(output_path, output_name, '.'+output_type)
        try:
            with open(img, 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)
        except FileNotFoundError:
            pass
