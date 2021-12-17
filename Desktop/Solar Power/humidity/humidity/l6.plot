set terminal png size 1920,1280
set xzeroaxis
set yzeroaxis

set datafile separator "\t"
#set decimalsign ","

set output 'd1.png';
set xtics font ", 18"
set ytics font ", 18"
#set ylabel font ", 23" 'I_{ C}, мкА' textcolor lt 8 offset 2,0,0
#set xlabel font ", 23" 'U_{ CB}, B' textcolor lt 8 offset 2,-1,0


set key font ", 20"
set key bottom right

#unset key
plot  "output1.txt" using 1:2 title"Влажность"  with linespoints lw 4,\
      "output1.txt" using 1:3 title"Температура"  with linespoints lw 4,\
