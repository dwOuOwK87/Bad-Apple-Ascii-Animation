import os
from AsciiAniGen import ASCII_Animation

def process():
    try:
        path = "./videos"
        videos_in_path = os.listdir(path)
        if len(videos_in_path) == 0:
            assert False, "Videos not found in the folder: videos/..."

        for filename in videos_in_path:
            front, suffix =  os.path.splitext(filename)
            if suffix == ".mp4":
                video_path = f"{path}/{front}{suffix}"
                break

    except AssertionError as message:
        input(message)

    else:
        print("Ascii Animation Setting:")
        width = int(input("width: "))
        height = int(input("height: "))
        
        os.system(f"mode con cols={width * 2 + 30} lines={height}")
        ASCII_Animation().show_animation(video_path, (width, height))

        input("End!")
    
process()
