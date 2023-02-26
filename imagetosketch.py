import cv2
from google.colab.patches import cv2_imshow
image= cv2.imread('r.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray_image,(5,5),0)
edges = cv2.Canny(blur,50,150)
sketch = cv2.bitwise_not(edges)
cv2_imshow(sketch)

cv2.destroyAllWindows()