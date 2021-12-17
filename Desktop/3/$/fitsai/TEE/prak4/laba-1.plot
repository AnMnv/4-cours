set terminal png size 1920,1280
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","

set output '3.png';

set xtics font ", 22"
set ytics font ", 22"
set ylabel font ", 23" 'С, пФ' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 23" 'U, B' textcolor lt 8 offset 2,-1,0
set key font ",15"
plot  "1.csv" using 2:3 title"200нм" smooth bezier lw 4, \
       "1.csv" using 6:7 title"200нм" smooth bezier lw 4, \


