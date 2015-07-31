set terminal push
set terminal png
set output "heatmap.png"

set palette rgbformula -7,2,-7
plot 'for_heatmap.txt' matrix with image

set output
set terminal pop
