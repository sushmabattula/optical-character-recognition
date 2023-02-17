
"""
Task: Use any online magazine to draw bounding boxes around paragraph and use any OCR tool to extract the text

User Story: As a user I should specify the path to Pdf and the program should automatically identify texts/paragraphs
and draw bounding boxes around it. In the second step program should extract the texts.

Libraries used - pytesseract, openCV

Task 1 submission provided by Resolute AI internship

Rules
- This code can only take PDFs with single page
- If you have an image, please convert that image file into pdf file.

This code can be further modifiable by assigning an ifelse statement to check whether the input file is
PDF format of image format

How to use this program?
- copy the path of the pdf u want to extract text from
- paste it below specified
- run the code
"""

import cv2
import pytesseract
from pdf2image import convert_from_path

# COPY AND PASTE THE PDF PATH UNDER THIS LINE
path = '/home/solomon/Documents/Python_Codes/OCR/example.pdf'
images = convert_from_path(path)

# SAVE THE PDF FILE INTO PNG FILE
for i in range(len(images)):
    images[i].save('1' + '.png', 'PNG')


pytesseract.pytesseract.tesseract_cmd = 'tesseract'

# READ THE NEWLY CREATED PNG FILE INTO CV2
converted_image = cv2.imread('1.png')

# PRINT THE STRINGS PRESENT IN THAT PDF
print(pytesseract.image_to_string(converted_image))

# CONVERT THE COLOR FORMAT FROM BGR TO RGB
converted_image = cv2.cvtColor(converted_image, cv2.COLOR_BGR2RGB)


# CODE TO DETECT THE TEXTS FROM THE PNG AND FORM A BOX AROUND THE TEXTS
boxes = pytesseract.image_to_data(converted_image)
for a, b in enumerate(boxes.splitlines()):
    if a != 0:
        b = b.split()
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(converted_image, (x, y), (x + w, y + h), (255, 50, 50), 2)


# FULL SCREEN OUTPUT
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
final_image = cv2.resize(converted_image, (1600, 750))

# SHOW OUT THE OUTPUT
cv2.imshow("window",final_image)

cv2.waitKey(0)

