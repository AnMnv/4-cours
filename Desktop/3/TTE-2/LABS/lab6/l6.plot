set terminal png size 1920,1280
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","

set output 'd1.png';
set xtics font ", 18"
set ytics font ", 18"
set ylabel font ", 23" 'I_{ C}, мкА' textcolor lt 8 offset 2,0,0
set xlabel font ", 23" 'U_{ CB}, B' textcolor lt 8 offset 2,-1,0
set xrange [-0.1:1.6]
set yrange [0:350]

set key font ", 20"
set key bottom right

#unset key
plot  "data.csv" using 1:2 title"4,5 В"  with points lw 4,\
      "data.csv" using 3:4 title"5 В"  with linespoints lw 4,\
      "data.csv" using 5:6 title"5,5 В"  with linespoints lw 4,\
      "data.csv" using 7:8 title"6 В"  with linespoints lw 4,\
      "data.csv" using 9:10 title"6,5 В"  with linespoints lw 4,\
      "data.csv" using 11:12 title"7 В"  with linespoints lw 4,\
      "data.csv" using 13:14 title"7,5 В"  with linespoints lw 4,\


set output 'd2.png';
set xtics font ", 18"
set ytics font ", 18"
set ylabel font ", 23" 'I_{ C}, мА' textcolor lt 8 offset 2,0,0
set xlabel font ", 23" 'U_{ CB}, B' textcolor lt 8 offset 2,-1,0
set xrange [-0.1:12]
set yrange [0:18]

set key font ", 20"
set key bottom right

#unset key
plot  "data2.csv" using 1:2 title"R_n"  with linespoints lw 4,\
      "data2.csv" using 3:4 title"T_y"  with linespoints lw 4,\
      "data2.csv" using 5:6 title"T_n"  with linespoints lw 4,\
