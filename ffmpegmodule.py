import os
import subprocess
with open('output.txt') as file_object:
    content = file_object.read()
    convert='ffmpeg -f lavfi -i color=c=blue:s=320x240:d=0.5 -vf \
    "drawtext=fontfile=/path/to/font.ttf:fontsize=30: \
    fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:text=content" \
    output.mp4'
    #os.system(convert)
    subprocess.call(convert,shell = True)
