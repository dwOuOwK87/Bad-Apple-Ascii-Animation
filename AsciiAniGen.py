import cv2
from math import ceil
from time import time
from time import sleep

class ASCII_Animation:
    def make_video_array(self, video_path: str, scale: tuple):
        capturer = cv2.VideoCapture(video_path)
        video_array = []

        fps = capturer.get(cv2.CAP_PROP_FPS)

        while capturer.isOpened():
            is_reading, frame_image = capturer.read()

            if not is_reading:
                break

            processed_image = cv2.cvtColor(
                cv2.resize(frame_image, scale, interpolation=cv2.INTER_AREA),
                cv2.COLOR_RGB2GRAY
            )
            video_array.append(processed_image)
        
        capturer.release()
        
        return fps, video_array

    def deltaTime_decorator(function):
        def inner_function(*args):
            t1 = time()
            function(*args)
            t2 = time()
            return t2-t1
        return inner_function

    @deltaTime_decorator
    def print_ascii_image(self, image: list, ascii_sheet: str):
        image_string = ""
        for row in image:
            for gray_level in row:
                index = int(gray_level / ceil(256/len(ascii_sheet)))
                image_string += ascii_sheet[index] + " "
            image_string += "\n"
        print(image_string, end="")
        
    def show_animation(self, video_path: str, scale: tuple, ascii_sheet: str = " .,:;!~+-xmo*#W&8@"):
        fps, image_array = self.make_video_array(video_path, scale)

        for image in image_array:
            deltaTime = self.print_ascii_image(image, ascii_sheet)
            sleep(1/fps - deltaTime)