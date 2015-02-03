set terminal push
set terminal png
set output "histogram.png"

set style data histogram
set style fill solid border -1
set xtics rotate
plot "data/toy.dat" u 3:xtic(1) ti col, "" u 12 ti col