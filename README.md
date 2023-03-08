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

## How to make this
>I'll easily talk about how I made this.  
>Thanks to opencv since it helped me make it simpler.  
>By the way, forgiving my incomprehensible English XD. After all, I am not a native English speaker. Most sentences come from google translate.  

To make the program read the video, we need to split it to images frame by frame.  
I used VideoCapture class to let me easy to split.
```
capturer = cv2.VideoCapture(video_path)
while capturer.isOpened():
        is_reading, frame_image = capturer.read()
        if is_reading == False:
                break
        ...
```  
And we make the image gray and resized during spliting it.  
cvtColor and resize method are both powerful tools.
```
processed_image = cv2.cvtColor(
                  cv2.resize(frame_image, scale, interpolation=cv2.INTER_AREA),
                  cv2.COLOR_RGB2GRAY
                  )
```
After we got processed image list, we print it out pixel by pixel in a image by using the formula.
```
space = ceiling(256 / length of the ASCII sheet)
index = int(a pixel in frame / space)
```
Use the formula, and compare the index with that in the ASCII sheet: (".", "+", "=", "#", "%", "$", "@", "M"),  
Like following code:
```
image_string = ""
for i in range(row):
        for j in range(col):
                index = int(image[i][j] / math.ceil(256/len(ascii_sheet)))
                image_string += ascii_sheet[index] + " "
        image_string += "\n"
print(image_string, end="")
```
Then print the video image by image.
```
for image in image_array:
        print_ascii_image(image, ascii_sheet)
```
Done!
