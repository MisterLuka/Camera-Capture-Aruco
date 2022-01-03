import cv2
import numpy as np

filepath = './aruco_photo/'
markersX = 1  # X轴上标记的数量
markersY = 1  # Y轴上标记的数量
markerLength = 100  # 标记的长度，单位是像素
markerSeparation = 20  # 每个标记之间的间隔，单位像素
margins = markerSeparation  # 标记与边界之间的间隔
borderBits = 10  # 标记的边界所占的bit位数
showImage = True


width = markersX * (markerLength + markerSeparation) - markerSeparation + 2 * margins
height =markersY * (markerLength + markerSeparation) - markerSeparation + 2 * margins


dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)  # 生成标记的字典ID
board = cv2.aruco.GridBoard_create(markersX, markersY, float(markerLength), float(markerSeparation), dictionary)
print(cv2.aruco_GridBoard.getGridSize(board))
img = cv2.aruco_GridBoard.draw(board, (500, 500), 1)
cv2.imwrite(filepath + '1.png', img)
