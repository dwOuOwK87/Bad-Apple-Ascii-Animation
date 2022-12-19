import cv2
import os
from time import sleep
from time import time

class AsciiAnimator:
    def __init__(self, input_folder : str):
        self.input_folder = input_folder
        self.ascii_sheet = ("@ ","& ","$ ","% ","# ","= ","! ","+ ")

    def read_images(self, folder : str):
        # return an error when the folder not found.
        if os.path.isdir(folder) == False:
            return False

        image_list = []
        for filename in os.listdir(folder):
            image = cv2.imread(f"{folder}/{filename}", cv2.IMREAD_GRAYSCALE)
            image_list.append(image)
        return image_list

    def resize_images(self, target : str, scale : tuple):
        image_list = self.read_images(self.input_folder)

        # stop the process when occuring problem.
        if image_list == False:
            print("Folder Not Found Error!")
            return

        # create a target folder when it has not created yet.
        if os.path.isdir(target) == False:
            os.mkdir(target)

        index = 0
        length = len(image_list)
        for index in range(length):
            image = cv2.resize(image_list[index], scale, interpolation=cv2.INTER_AREA)
            cv2.imwrite(f"{target}/clip_{index:05d}.png", image)
    
    def show_animation(self, frame_rate : int):
        def deltaTime_decorator(function):
            def inner_function(*args):
                t1 = time()
                function(*args)
                t2 = time()
                return t2-t1
            return inner_function

        @deltaTime_decorator
        def print_ascii_image(image):
            row = len(image)
            col = len(image[0])
            for i in range(row):
                for j in range(col):
                    index = image[i][j] // 32
                    print(self.ascii_sheet[index], end="")
                print()

        image_list = self.read_images(self.input_folder)

        # stop the process when occuring problem.
        if image_list == False:
            print("Folder Not Found Error!")
            return

        for image in image_list:
            deltaTime = print_ascii_image(image)
            sleep(1/frame_rate - deltaTime)
