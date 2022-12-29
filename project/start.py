from os import system
from AsciiAniGen import ASCII_Animation

system("mode con cols=150 lines=48")
ASCII_Animation().show_animation("vedio.mp4", (64, 48))