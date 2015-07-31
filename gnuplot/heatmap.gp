set terminal push
set terminal png
set output "heatmap.png"

plot 'for_heatmap.txt' matrix with image

set output
set terminal pop
