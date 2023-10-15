#flipping the image

from PIL import Image

#opening the image
img=Image.open('download.jpeg')

#transposing,image in matrix
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)

#save it to file in human understandable format
transposed_img.save('corrected.jpeg')

print('done flipping')