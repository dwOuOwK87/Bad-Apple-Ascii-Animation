import cv2
from time import time
from time import sleep

class ASCII_Animation:
    def make_vedio_array(self, vedio_path: str, scale: tuple):
        try:
            capturer = cv2.VideoCapture(vedio_path)
            vedio_array = []

            fps = capturer.get(cv2.CAP_PROP_FPS)

            while capturer.isOpened():
                is_reading, frame_image = capturer.read()

                if is_reading == False:
                    break

                processed_image = cv2.cvtColor(
                    cv2.resize(frame_image, scale, interpolation=cv2.INTER_AREA),
                    cv2.COLOR_RGB2GRAY
                )
                vedio_array.append(processed_image)
            
            capturer.release()
            
            return fps, vedio_array

        except:
            return -1

    def deltaTime_decorator(function):
        def inner_function(*args):
            t1 = time()
            function(*args)
            t2 = time()
            return t2-t1
        return inner_function

    @deltaTime_decorator
    def print_ascii_image(self, image, ascii_sheet):
        image_string = ''
        row = len(image)
        col = len(image[0])
        for i in range(row):
            for j in range(col):
                index = image[i][j] // (256//len(ascii_sheet))
                image_string += ascii_sheet[index] + " "
            image_string += '\n'
        print(image_string)
        
    def show_animation(self, vedio_path: str, scale: tuple, ascii_sheet: tuple = (".","+","=","#","%","$","@","M")):
        try:
            fps, image_array = self.make_vedio_array(vedio_path, scale)
            if image_array == -1:
                assert False, "Error!"

            for image in image_array:
                deltaTime = self.print_ascii_image(image, ascii_sheet)
                sleep(1/fps - deltaTime)
    
        except AssertionError as message:
            print(message)
            return