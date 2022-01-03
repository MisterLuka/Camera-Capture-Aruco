import os
import cv2

def video_cut(video_path, f_save_path):
    # return the file list
    videos = os.listdir(video_path)
    for video_name in videos:  # 依次读取视频文件
        file_name = video_name.split('.')[0]  # 去除后缀
        folder_name = f_save_path + file_name  # 保存图片的上级目录+对应每条视频名称
        os.makedirs(folder_name, exist_ok=True)
        vc = cv2.VideoCapture(video_path + video_name)
        # get the fps
        fps = vc.get(cv2.CAP_PROP_FPS)
        # print(fps)
        rval = vc.isOpened()  # 判断视频是否打开  返回True或Flase
        c = 1
        while rval:
            ret, frame = vc.read()
            pic_path = folder_name + '/'
            if ret:
                # if (c % round(fps) == 0):
                cv2.imwrite(pic_path + str(round(c)) + '.jpg', frame)
                # print(str(round(c)) + '.jpg')
                c += 1
            else:
                break
        vc.release()
        print('save success ' + folder_name)

if __name__ == '__main__':
    video_path = './video/'
    f_save_path = './video_frame/'
    video_cut(video_path, f_save_path)
