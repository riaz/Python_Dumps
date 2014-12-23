from simpleCV import Camera

#Initializing the camera
cam = Camera()

#Loop to continuously get images
while True:

    #get image from camera
    img = cam.getImage()

    #make the image black and white
    ing = img.binarize()

    #draw the text "Hello World" on the image
    img.drawText("Hello World!")

    #Show the image
    img.show()
