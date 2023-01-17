import os
from AsciiAniGen import ASCII_Animation

class ErrorHandler:
    def reply_process(self, message):
        reply = input(message)
        if reply in ("n", "N", "no", "No"):
            return False
        return True

class AnimationHandler:
    def __init__(self, path):
        self.path = path

    def make_videos_folder(self):
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

    def get_videos_list(self):
        try:
            videos_list = os.listdir(self.path)
            if len(videos_list) == 0:
                assert False
            return videos_list

        except AssertionError:
            if len(videos_list) == 0:
                retry = ErrorHandler().reply_process(
                    "Videos not found in the folder \"videos\", retry? (y/n) "
                    )
                if retry:
                    return self.get_videos_list()
                else:
                    os._exit()

class User:
    def __init__(self, path):
        self.animation_handler = AnimationHandler(path)
        
    def get_user_input_filename(self, videos_list):
        print(f"Found videos: {videos_list}.")
        print("Please input the filename of video which you would like to play...")
        try:
            video_name = input("Video name: ")
            if video_name not in videos_list:    
                assert False
            return video_name
                
        except AssertionError:
            retry = ErrorHandler().reply_process(
                    "Videos not found, retry? (y/n) "
                    )
            if retry:
                return self.get_user_input_filename(videos_list)
            else:
                os._exit()
    
    def get_user_setting_scale(self):
        print("Ascii Animation Setting:")
        try:
            width = int(input("width: "))
            height = int(input("height: "))
            return width, height

        except ValueError:
            retry = ErrorHandler().reply_process(
                "Please input integers, retry? (y/n) "
                )
            if retry:
                return self.get_user_setting_scale()
            else:
                os._exit()

    def process(self):
        self.animation_handler.make_videos_folder()
        videos_list = self.animation_handler.get_videos_list()
        filename = self.get_user_input_filename(videos_list)
        scale = self.get_user_setting_scale()

        os.system(f"mode con cols={scale[0] * 2 + 30} lines={scale[1]}")
        ASCII_Animation().show_animation(f"{self.animation_handler.path}/{filename}", scale)

user = User("Videos")
user.process()
input("End!")
