
set terminal png size 1080,720
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","

set output '1.png';

set xtics font ", 15"
set ytics font ", 15"
set ylabel font ", 20" 'R, кОм' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 20" 'I_{свд}, мA' textcolor lt 8 offset 2,-1,0
set key font ",15"
set key right top
plot  "1.csv" using 3:2  notitle with points lw 4,\
      "1.csv" using 3:2  title "Білий " smooth  bezier       lw 2,\
      "1.csv" using 6:5  notitle with points lw 4,\
      "1.csv" using 6:5  title "Зелений" smooth   bezier      lw 2,\
 

set output '2.png';

set xtics font ", 15"
set ytics font ", 15"
set ylabel font ", 20" 'R, кОм' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 20" 'I_{свд}, мA' textcolor lt 8 offset 2,-1,0
set key font ",15"
set key right top
plot  "1.csv" using 9:8  notitle with points lw 4,\
      "1.csv" using 9:8  title "Червоний" smooth   bezier       lw 2,\


set output '3.png';

set xtics font ", 15"
set ytics font ", 15"
set ylabel font ", 20" 'I_{ф}, мкА' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 20" 'I_{свд}, мA' textcolor lt 8 offset 2,-1,0
set key font ",15"
set key right top
plot  "2.csv" using 3:2  notitle with points lw 4,\
      "2.csv" using 3:2  title "Білий " smooth  bezier       lw 2,\
      "2.csv" using 6:5  notitle with points lw 4,\
      "2.csv" using 6:5  title "Зелений" smooth   bezier      lw 2,\
      "2.csv" using 9:8  notitle with points lw 4,\
      "2.csv" using 9:8  title "Червоний"   smooth  acsplines    lw 2,\