import cv2
import numpy as np

video_path = './video/'
count = 1
width = 640
height = 480

def videoCapture(filepath, count, width, height):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    out1 = cv2.VideoWriter(filepath + str(count) + '_r.avi', fourcc, 25, (width, height))
    out2 = cv2.VideoWriter(filepath + str(count) + '_l.avi', fourcc, 25, (width, height))
    while True:
        # 采集
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        frame1 = cv2.resize(frame1, (width, height), interpolation=cv2.INTER_LINEAR)
        frame2 = cv2.resize(frame2, (width, height), interpolation=cv2.INTER_LINEAR)
        if ret1 & ret2:
            # 横向拼接图像
            frameUp = np.hstack([frame1, frame2])
            cv2.imshow('input', frameUp)
            # cv2.imshow('input1', frame1)
            # cv2.imshow('input2', frame2)
            out1.write(frame1)
            out2.write(frame2)
            if cv2.waitKey(1) & 0xFF == ord(' '):
                break
        else:
            break

    cap1.release()
    out1.release()
    cap2.release()
    out2.release()
    cv2.destroyAllWindows()

    return print('Video capture success!')

if __name__ == '__main__':
    videoCapture(video_path, count, width, height)
