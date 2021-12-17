set terminal png size 1920,1280
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","

set output '1.png';
set xtics font ", 26" offset 0,-1,0
set ytics font ", 26" offset 0,-1,0
set ylabel font ", 33" 'e_{f}' textcolor lt 8 offset 1.5,0,0
set xlabel font ", 33" 'L, m' textcolor lt 8 offset 2,-2,0
set key font ",25"
plot  "data.csv" using 1:2 notitle w l lw 4, \
      "data.csv" using 1:2 with points notitle lw 4, \
      "data.csv" using 3:4  w l notitle lw 4, \
