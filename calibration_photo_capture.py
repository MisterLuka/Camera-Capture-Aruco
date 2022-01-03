import cv2
import os


def caliPhotoCap(videoFile, writePath0, width, height, i):
    # right = 0, left = 1
    imageCapture = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    imageCapture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    imageCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
    # cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)

    while True:
        ret, frame = imageCapture.read()
        if ret:
            cv2.resize(frame, (width, height), interpolation=cv2.INTER_CUBIC)
            cv2.imshow("Image", frame)
            key = cv2.waitKey(1)
            if key == ord(' '):
                writePath = os.path.join(writePath0 + videoFile + '/' + str(i) + '.jpg')
                cv2.imwrite(writePath, frame)
                print(i)
                i += 1
            if i > 17:
                break
    imageCapture.release()

if __name__ == "__main__":
    videoFile = 'left'
    writePath0 = './cali_photos/'
    i = 1
    width = 1280
    height = 960
    caliPhotoCap(videoFile, writePath0, width, height, i)







