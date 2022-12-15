import cv2

# links must end with '.jpg or .jpeg or png


image = cv2.imread(
    r"C:\Users\IVORY CATCH VENTURES\Downloads\Images_into_Sketch\images\WIN_20210109_23_27_16_Pro.jpg")
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=280)

cv2.imwrite("sketch.png", sketch)
