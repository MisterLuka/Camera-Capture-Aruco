import numpy as np

txt = open('./camera_parameter/mtx_dist_left.txt', 'r')
lines = txt.readline()
lines = lines.split(' ')

l_camera_matrix = np.zeros((1, 9))
l_camera_distortion = np.zeros((1, 5))

for i, string in enumerate(lines):
    # print(str(i) + ' ' + string)
    if i <= 8:
        l_camera_matrix[0][i] = float(string)
    else:
        j = i - 9
        l_camera_distortion[0][j] = float(string)


l_camera_matrix.resize((3, 3))
print(l_camera_matrix)
print(l_camera_distortion)
