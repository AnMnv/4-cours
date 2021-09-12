set terminal png size 1280, 720
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","

set output 'fortab1.png';

set xtics font ", 15"
set ytics font ", 15"
set ylabel font ", 20" 'U_1, B' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 20" 'U_2, B' textcolor lt 8 offset 2,-1,0
set key font ",15"
set key bottom left
plot  "tab1.csv" using 1:2  notitle with points lw 4,\
      "tab1.csv" using 1:2  title"U_2 (П1-П4)" smooth csplines  lw 2, \
      "tab1.csv" using 1:3 notitle with points lw 4, \
      "tab1.csv" using 1:3  title"U_2, для VD_1 (П1)" smooth csplines lw 2, \
      "tab1.csv" using 1:4 notitle with points lw 4, \
      "tab1.csv" using 1:4  title"U_2,  для C_1 (П2)" smooth csplines lw 2, \
      "tab1.csv" using 1:5 notitle with points lw 4,\
      "tab1.csv" using 1:5  title"U_2, для R_7 (П4)" smooth mcsplines   lw 2

set output 'fortab2.png';

set xtics font ", 15"
set ytics font ", 15"
set ylabel font ", 20" 'U_2, B' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 20" 'U_1, B' textcolor lt 8 offset 2,-1,0
set key font ",15"
set key bottom left
plot  "tab1.csv" using 1:2  notitle with points lw 4,\
      "tab1.csv" using 1:2  notitle smooth csplines  lw 2, \




