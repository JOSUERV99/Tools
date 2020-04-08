""" 
@objective Convert a image into a black and white image     
@author: josuerv99
@since: 6/4/2020
"""
import cv2 # pip install opencv-python

image_path = 'Image1.png' # (R, G, B, A)
black_and_white_image_path = 'b&w.png'

def processingImage(imagePath):  
    image = cv2.imread(imagePath)
    adjustColors(image)
    return image

def adjustColors(image):
    width, height, pixels_length = image.shape[0], image.shape[1], image.shape[2]
    for x in range(width):
        for y in range(height):
            image[x,y] = [ sum(image[x,y])/pixels_length for z in range(pixels_length) ]
    return image

def showImage(image, title='img1'):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def saveImage(image, filename='img_b&w.png'):
    cv2.imwrite(filename, image)
    print("Saved!")

print('Processing image...')
black_and_white_image = processingImage(image_path)
showImage(black_and_white_image, title='Black and White Image')
saveImage(black_and_white_image, filename=black_and_white_image_path )
