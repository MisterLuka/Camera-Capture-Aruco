import numpy as np
import cv2
import cv2.aruco as aruco
import sys, time, math

# Define Tag
id_to_find = 0
marker_size = 10

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

# set aruco dictionary
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()

# get the frame
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# set the window size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# show the text
front = cv2.FONT_HERSHEY_PLAIN

while True:
    # read camera frame
    ret, frame = cap.read()
    # convert in gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # find all the aruco markers in the frame
    corners, ids, rejected = aruco.detectMarkers(image=gray, dictionary=aruco_dict, parameters=parameters,
                                                 cameraMatrix=camera_matrix, distCoeff=camera_distortion)

    if ids != None:
        ret = aruco.estimatePoseSingleMarkers(corners, marker_size, camera_matrix, camera_distortion)
        rvec, tvec = ret[0][0, 0, :], ret[1][0, 0, :]
        print(rvec)
        print(tvec)
        # draw
        aruco.drawDetectedMarkers(frame, corners)
        aruco.drawAxis(frame, camera_matrix, camera_distortion, rvec, tvec, 10)
        # print the tag position
        str_position = "MARKER Position x=%4.0f  y=%4.0f  z=%4.0f"%(tvec[0], tvec[1], tvec[2])
        cv2.putText(frame, str_position, (0, 100), front, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('img', frame)
    key = cv2.waitKey(1)
    if key == ord(' '):
        cap.release()
        cv2.destroyAllWindows()
        break

