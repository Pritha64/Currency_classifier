import cv2
import os

def save_image(name):
    file_name=name.split('.')[0]
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    arr = os.listdir(file_name)
    image_number=len(arr)
    print(image_number)
    cam=cv2.VideoCapture('Videos/'+name)
    while cam.isOpened():
        ret,frame=cam.read()
        if not ret:
            break
        try:
            frame=cv2.resize(frame,(256,117))
            cv2.imwrite(file_name+'/'+str(image_number)+'.png',frame)
            image_number+=1
        except:
            pass
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()


'''_______________________________________________________'''
'''code runs from here'''
save_image('5.0.mp4')