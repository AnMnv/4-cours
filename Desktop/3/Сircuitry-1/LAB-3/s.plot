set terminal png size 1920,1280
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","

set output 'q.png';

set xtics font ", 22"
set ytics font ", 22"
set ylabel font ", 23" 'U_2, B' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 23" 'U_1, B' textcolor lt 8 offset 2,-1,0
set key font ",15"
plot  "111.csv" using 1:2 with linespoints lw 4, \

