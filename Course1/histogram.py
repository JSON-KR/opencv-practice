import cv2 as cv
import matplotlib.pyplot as plt

fileSource = r'Resources'
fileCategory = r'\Photos'
fileName = r'\cats.jpg'
nameReadImg = fileSource + fileCategory + fileName

img = cv.imread(nameReadImg)  
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# ! Gray Hist
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.show()

# ! 마스킹도 가능

# ! RGB Hist
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)