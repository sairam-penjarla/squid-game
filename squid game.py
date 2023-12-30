import cv2
from pygame import mixer
import numpy as np
from playsound import playsound
import time

cap = cv2.VideoCapture(0)
mixer.init()
mixer.music.load("doll.mp3")
mixer.music.set_volume(0.7)
img2 = cv2.imread('2.png')
img1 = cv2.imread('1.png')
img3 = cv2.imread('1.png')
img4 = cv2.imread('2.png')
height, width, channels = img1.shape
width_len = width
end = False
h, w, c = img3.shape
length = w


def func1():
    global end
    global length
    global img1
    global img2
    k = 0
    wait = 0
    start_time = time.time()
    while not end:
        play_again = 0
        wait += 1
        mixer.music.play()
        print('.')
        while -1 < k < 75:
            w = width - length
            cv2.rectangle(img1, (0, height - 100), (w, height), (0, 0, 255), thickness=10)
            cv2.rectangle(img2, (0, height - 100), (w, height), (0, 0, 255), thickness=10)
            print('.')
            if 0 < wait < 60:
                length -= 5
            elif wait > 60:
                wait = -80
            cv2.imshow("Squid Game", img1)
            cv2.waitKey(1)
            k += 1
        if k == 75:
            k = 0
        cv2.imshow("Squid Game", img2)
        cv2.waitKey(1)
        _, a = cap.read()
        i = 0
        while i < 160:
            print('.')
            i += 1
            _, b = cap.read()
            error = (np.mean(a != b)) * 100
            if error > 93:
                end_time = time.time()
                end = True
                playsound('gun.mp3')
                while play_again == 0:
                    img2 = cv2.imread('3.png')
                    cv2.putText(img2, 'DEAD', (int(img2.shape[1] / 2) - 500, int(img2.shape[0] / 2)-200), cv2.FONT_ITALIC, 10, (255, 255, 255), 40)
                    cv2.putText(img2, 'DEAD', (int(img2.shape[1] / 2) - 500, int(img2.shape[0] / 2) - 200), cv2.FONT_ITALIC, 10, (0, 0, 255), 20)
                    text = (('you lasted for '+ str(round(end_time - start_time))+ ' seconds'))

                    cv2.putText(img2, text, (int(img2.shape[1] / 2) - 1200, int(img2.shape[0] / 2) + 300 - 200), cv2.FONT_ITALIC, 6, (0, 0, 0), 20)
                    cv2.putText(img2, text, (int(img2.shape[1] / 2) - 1200, int(img2.shape[0] / 2) + 300 - 200), cv2.FONT_ITALIC, 6, (0, 0, 255), 10)
                    text = "Press 'q' to Play Again"

                    cv2.putText(img2, text, (int(img2.shape[1] / 2) - 900, int(img2.shape[0] / 2) + 600 - 200), cv2.FONT_ITALIC, 6, (0, 0, 0), 20)
                    cv2.putText(img2, text, (int(img2.shape[1] / 2) - 900, int(img2.shape[0] / 2) + 600 - 200), cv2.FONT_ITALIC, 6, (0, 0, 255), 10)
                    cv2.imshow("Squid Game", img2)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        play_again = 1
                        k = 0
                        wait = 0
                        end = False
                        img1 = img3
                        img2 = img4
                        h, w, c = img3.shape
                        length = w
                        start_time = time.time()
                break


func1()
