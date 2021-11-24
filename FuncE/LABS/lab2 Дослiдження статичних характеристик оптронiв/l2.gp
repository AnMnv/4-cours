
set terminal png size 1920,1280
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","

set output 'd1.png';

set xtics font ", 15"
set ytics font ", 15"
set ylabel font ", 20" 'I_{вих}, мкА' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 20" 't, c' textcolor lt 8 offset 2,-1,0
set key font ",15"
set key bottom left
plot  "tab1.csv" using 2:1  notitle with points lw 4,\
      "tab1.csv" using 2:1  notitle smooth csplines  lw 2

 