set terminal push
set terminal png
set output "example.png"

# plot 'data/data.dat' u 0:1 w lp ti col

# plot 'data/data.dat' u 2 smooth csplines w lp ti col, "" u 1 w lp ti col

plot sin(x) w lp lc rgb "orange"

set output
set terminal pop