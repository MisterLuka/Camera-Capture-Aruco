import numpy as np
import cv2
import cv2.aruco as aruco
import sys, time, math, os

# Define frames path
framePath = './video_frame/'
frameDirName = 'coor/'

marker_size = 10

# # 相机内参和畸变参数
# right
r_camera_matrix = np.array([[483.66122704, 0, 294.36945346],
                          [0, 482.33257692, 241.16306069],
                          [0., 0., 1.0]], np.float32)
r_camera_distortion = np.array([0.20584962, -1.03123574, 0.00249221, -0.00923714, 1.5690956])
# left
l_camera_matrix = np.array([[1.52679648e+03, 0, 4.43963526e+02],
                          [0, 1.52431485e+03, 5.31947919e+01],
                          [0., 0., 1.0]], np.float32)
l_camera_distortion = np.array([-0.26349966, 0.22469013, -0.01087704, 0.00316442, 1.02499707])

# set aruco dictionary
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()

# show the text
front = cv2.FONT_HERSHEY_PLAIN

images = os.listdir(framePath + frameDirName)

for image in images:
    count = 0
    # read the frame
    frame = cv2.imread(framePath + frameDirName + image)
    i = image.split('.')[0]
    # convert in gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # find all the aruco markers in the frame
    corners, ids, rejected = aruco.detectMarkers(image=gray, dictionary=aruco_dict, parameters=parameters,
                                                 cameraMatrix=camera_matrix, distCoeff=camera_distortion)
    if ids != None:
        # deliver the rotation matrix and translation matrix to a document
        txt = open('./video_frame/analysis_txt/' + i + '.txt', 'w')
        ret = aruco.estimatePoseSingleMarkers(corners, marker_size, camera_matrix, camera_distortion)
        rvec, tvec = ret[0][0, 0, :], ret[1][0, 0, :]
        txt.write(i + ' ' + str(rvec) + ' ' + str(tvec))
        txt.close()
        # draw
        aruco.drawDetectedMarkers(frame, corners)
        aruco.drawAxis(frame, camera_matrix, camera_distortion, rvec, tvec, 10)
        # print the tag position
        str_position = "MARKER Position x=%4.0f  y=%4.0f  z=%4.0f"%(tvec[0], tvec[1], tvec[2])
        cv2.putText(frame, str_position, (0, 100), front, 1, (0, 255, 0), 2, cv2.LINE_AA)

        count += 1

        cv2.imwrite(framePath + 'analysis_image/' + image, frame)
        cv2.imshow('img', frame)
        cv2.waitKey(1)
        if (count >= (len(images) - 1)):
            break
    else:
        print(image)

