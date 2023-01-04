# Bad-Apple-Ascii-Animation

## Tips
Clicking "start.py" can start the animation.   
The program will ask you the scale of ASCII animation.  
I recommend you to set it less than 100 both width and height with the same ratio as the original video.

## Need python3 and opencv
```
pip install opencv-python
```

## Links
[Video here.](https://youtu.be/kolcMueYQMw)  
For people who just want to easily use, exe file [here](https://drive.google.com/drive/folders/10Mv6SztT0jr-yEC20ksxw8jAXGUmQwd9?usp=sharing).  

## How to make this
>I'll easily talk about how I made this.  
>Thanks to opencv since it helped me make it simpler.  
>By the way, forgiving my incomprehensible English XD. After all, I am not a native English speaker. Most sentences come from google translate.  
>And ugly images come form MS paint.

To make the program read the video, we need to split it to images frame by frame.  
```
capturer = cv2.VideoCapture(video_path)
while capturer.isOpened():
    is_reading, frame_image = capturer.read()
    if is_reading == False:
        break
    #process
```  
And we process the image during spliting it, make it gray and resized.  
```
processed_image = cv2.cvtColor(
                  cv2.resize(frame_image, scale, interpolation=cv2.INTER_AREA),
                  cv2.COLOR_RGB2GRAY
                  )
```
![alt 001](/image/001.png)



After we got processed image list, we print it out pixel by pixel in a image by using the formula.
```
space = int(256 / length of the ASCII sheet)
index = int(a pixel in frame / space)
```
Then compare the index with that in the ASCII sheet: (".", "+", "=", "#", "%", "$", "@", "M")  
![alt 002](/image/002.png)



Then print the video image by image!, done!
