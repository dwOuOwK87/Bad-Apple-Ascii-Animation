import os
from AsciiAniGen import ASCII_Animation

path = "videos"

def process():
    try:
        videos_in_path = os.listdir(path)
        if len(videos_in_path) == 0:
            assert False, "Videos not found in the videos folder, retry? (y/n)"

        for filename in videos_in_path:
            front, suffix =  os.path.splitext(filename)
            if suffix == ".mp4":
                video_path = f"{path}/{front}{suffix}"
                break
        
        print("Ascii Animation Setting:")
        width = int(input("width: "))
        height = int(input("height: "))
        
        os.system(f"mode con cols={width * 2 + 30} lines={height}")
        ASCII_Animation().show_animation(video_path, (width, height))

        input("End!")

    except AssertionError as message:
        reply = input(message)
        if reply in ("y", "Y", "yes", "Yes"):
            process()
        elif reply in ("n", "N", "no", "No"):
            return
        else:
            process()

    except:
        os.mkdir(path)
        process()

process()
