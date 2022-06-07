import cv2
from PIL import Image, ImageOps, ImageFilter

# imgInput = input('请输入需要转换的图片文件路径：')
imgInput = r'D:\code\python_\demo\demo.jpeg'
# a = input('请输入图片的模糊参数值（奇数，数值越大越模糊，风景类推荐值29，肖像类推荐值7）：')
a = 7
# b = input('请输入图片的线条参数值（大于零时数值越小线条越明显，小于零时图片为暗色，风景类推荐值5，肖像类推荐值4）：')
b = 4
imgPath = imgInput.split(".")[0] + '_cartoon.' + imgInput.split(".")[1]
img_initial = cv2.imread(imgInput)
img_vague = cv2.medianBlur(img_initial, int(a))
img_gray = cv2.cvtColor(img_vague, cv2.COLOR_RGB2GRAY)
img_line = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=int(a),
                                 C=int(b))
img_line = cv2.cvtColor(img_line, cv2.COLOR_GRAY2RGB)
imgOutput = cv2.bitwise_and(img_vague, img_line)
cv2.imwrite(imgPath, imgOutput)
print('文件保存在' + imgPath)
print('\n更改参数以获得最佳效果\n')
