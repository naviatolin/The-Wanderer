from SimpleCV import Display, Image
display = Display()
print"Display opening..."

# Loop until window is closed
while display.isNotDone():
    # Capture image
    os.system(‘raspistill –n –w 500 –h 500 –o image.jpg’)
    img = Image(‘image.jpg’)
    # Here’s where you’d put any image processing
    img.show()

print"Display closed"