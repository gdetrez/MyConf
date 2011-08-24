#!/bin/bash

width="400"
height="200"
bgcolor="none"
textcolor="red"
fontsize="42"
centerOfGravity="center"
angle="337.5"
xmargin=0
ymargin=0
text="Sessions have ended"
filename="bg_past.png"

convert -size ${width}x${height} xc:${bgcolor} -fill ${textcolor} -pointsize ${fontsize} -gravity ${centerOfGravity} -draw "rotate ${angle} text ${xmargin},${ymargin} '${text}'" ${filename}
