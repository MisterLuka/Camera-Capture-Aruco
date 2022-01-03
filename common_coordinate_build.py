import numpy as np
import cv2

# 初始化参数
x, y, z = (0, 0, 0)
k1, k2, k3, p1, p2 = (0, 0, 0, 0, 0)
u, v = (0, 0)

# 初始点
a = np.array([0, 0, 0], np.float32)  # 单位为cm
a = a.reshape((3, 1))
# 相机内参和畸变参数
# right
camera_matrix = np.array([[483.66122704, 0, 294.36945346],
                          [0, 482.33257692, 241.16306069],
                          [0., 0., 1.0]], np.float32)
camera_distortion = np.array([0.20584962, -1.03123574, 0.00249221, -0.00923714, 1.5690956])
# left
# camera_matrix = np.array([[1.52679648e+03, 0, 4.43963526e+02],
#                           [0, 1.52431485e+03, 5.31947919e+01],
#                           [0., 0., 1.0]], np.float32)
# camera_distortion = np.array([-0.26349966, 0.22469013, -0.01087704, 0.00316442, 1.02499707])
# 旋转矩阵和平移矩阵
# right
rvec = np.mat([2.69388039, 0.11938388, -0.75018929])
tvec = np.mat([4.29959139, 22.97151224, 84.65340775])
# left
# rvec = np.array([2.69958659, -0.01900416, -1.4484283])
# tvec = np.array([-8.17194703, 7.41425144, 68.73805529])

vec = np.mat([0, 0, 0, 1])

# # 构造相机外参
# R, j = cv2.Rodrigues(rvec)
# T = np.transpose(tvec)
# W = np.c_[R, T]
# W = np.r_[W, vec]
#
# # 计算中间变量
# point_1 = W * a
#
# print(point_1)
# for i in range(len(point_1)):
#     if i == 0:
#         x = point_1[i].item()
#     elif i == 1:
#         y = point_1[i].item()
#     elif i == 2:
#         z = point_1[i].item()
#     else:
#         break
#
# # 计算畸变结果
# x_1 = x/z
# y_1 = y/z
# r = np.sqrt(x_1**2 + y_1**2)
# print(x_1, y_1)
# for j in range(5):
#     if j == 0:
#         k1 = camera_distortion[j].item()
#     elif j == 1:
#         k2 = camera_distortion[j].item()
#     elif j == 2:
#         p1 = camera_distortion[j].item()
#     elif j == 3:
#         p2 = camera_distortion[j].item()
#     elif j == 4:
#         k3 = camera_distortion[j].item()
# # 反求畸变
# gama = 1 + k1*r**2 + k2*r**4 + k3*r**6
# x_2 = x_1*gama + 2*p1*x_1*y_1 + p2*(r**2 + 2*x_1**2)
# y_2 = y_1*gama + p1*(r**2 + 2*y_1**2) + 2*p2*x_1*y_1
# print(x_2, y_2)
# point_2 = np.transpose(np.mat([x_2, y_2, 1]))
#
# # 求解像素坐标系下的点
# point = camera_matrix * point_2
# print(point)
# for k in range(len(point)):
#     if k == 0:
#         u = point[k].item()
#     elif k == 1:
#         v = point[k].item()
#     else:
#         break

point, jac = cv2.projectPoints(a, rvec, tvec, camera_matrix, camera_distortion)
print(point)
u = point[0,0,0]
v = point[0,0,1]


# 绘图保存
img = cv2.imread('E:\Gaze_Project\GazeProgram_m\cameraCapture_aruco/video_frame/coor/r.jpg')
point_size = 1
point_color = (0, 0, 255)
thickness = 5
cv2.circle(img, (int(u), int(v)), point_size, point_color, thickness)
cv2.imwrite('E:\Gaze_Project\GazeProgram_m\cameraCapture_aruco/video_frame\coor/r_.jpg', img)
cv2.imshow('image', img)
cv2.waitKey(0)

