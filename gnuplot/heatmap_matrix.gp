set terminal push
set terminal png
set output "heatmap.png"

# set title "Heat Map generated from a file containing Z values only"

#set xrange [-5:70]
#set yrange [-5:210]

#set xlabel "paragraph pos in doc"
#set ylabel "doc id"

set palette rgbformula 2,-7,-7
# plot 'log.dat' matrix with image
# plot 'for_heatmap2.txt' matrix with image
# plot 'for_heatmap3.txt' matrix with image title "paragraph similarity per doc"
plot '3vals.txt' using 2:1:3 with image

set output
set terminal pop
