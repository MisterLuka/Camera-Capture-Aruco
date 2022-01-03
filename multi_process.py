import numpy as np
import cv2
import multiprocessing
from multiprocessing import Queue
import time

CAMERA_COUNT = 2  # 摄像头个数
q = Queue()


def video_read(id):
    camera_id = id
    # 摄像头0
    if camera_id == 0:
        cap = cv2.VideoCapture(0)

    # 使用外置的摄像头
    if camera_id == 1:
        cap = cv2.VideoCapture(1)

    # 获取每一个视频的尺寸
    width = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    height = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print(width, height)

    while (cap.isOpened()):
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_CUBIC)
        isEmpty = q.empty()
        print(isEmpty)
        if isEmpty == True:
            print('队列中无数据！')
            q.put(frame)
            time.sleep(0.001)

        else:
            print('队列中有数据！')
            Frame = q.get(frame)
            time.sleep(0.002)
            frameUp = np.hstack(frame, Frame)#左右合并
        # frameUp = np.vstack((frameLeftUp, frameRightUp))#上下合并

        cv2.imshow('camera' + str(id), frameUp)
        key = cv2.waitKey(10)
        if int(key) == 113:
            break

    cap.release()

if __name__ == '__main__':
    print("主进程开始启动！")
    for index in range(CAMERA_COUNT):
        print('摄像头的索引号是：', index)
        p = multiprocessing.Process(target=video_read, args=(index,))
        p.start()
    print('程序结束！')