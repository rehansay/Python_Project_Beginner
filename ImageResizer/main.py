import cv2
import os

current_dir = os.path.dirname(__file__)

source = os.path.join(current_dir, "batman.jpeg")
destination = os.path.join(current_dir, "newImage.png")

scale_percent=50



src=cv2.imread(source, cv2.IMREAD_UNCHANGED)




#percent by which the image is resized


#calculate the 50 percent of original dimensions
width=int(src.shape[1] * scale_percent /100)

height=int(src.shape[0]* scale_percent/100)

#dsize

dsize=(width, height)

#resize image

output=cv2.resize(src, dsize)

cv2.imwrite(destination, output)
