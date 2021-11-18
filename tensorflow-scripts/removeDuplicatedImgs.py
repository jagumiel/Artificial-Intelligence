import os
import PIL
import glob
import numpy
import shutil
import imagehash

from PIL import Image

# This script can be modified to delete any duplicated file or look for other extensions.


# Get images into "files" array.
files = glob.glob('*.jpg')

# Get a file and calculate its' hash.
for file1 in files:
    img1=Image.open(file1)
    hash1=imagehash.average_hash(img1)

    # Comprobate if any other file on the list has the same hash. If they coincide, the image is repeated.
    for file2 in files:
        # Avoid to compare the same file.
        if(file1!=file2):
            img2=Image.open(file2)
            hash2=imagehash.average_hash(img2)
            if (hash1==hash2):
                print("{} image found similar to {}. Moving it to another folder".format(file1, file2))
                # Creates a folder if it doesn't exist. Moves the duplicated file to the folder. (It also may be deleted instead, commented.)
                os.makedirs("duplicated", exist_ok=False)
                #os.remove(file2)
                shutil.move(file2, "duplicated/"+file2)
                files.remove(file2) # Deletes file2 from arraylist.