set terminal push
set terminal png
set output "myplot.png"

plot 'data.dat' u 0:1 w lp ti col

plot 'data.dat' u 2 smooth csplines w lp ti col, "" u 1 w lp ti col

plot sin(x) w lp lc rgb "orange"

set output
set terminal pop