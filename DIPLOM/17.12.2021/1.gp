
#set terminal png size 1920,1000
set encoding utf8
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","
set terminal pdf

set output '1.pdf';


set xtics font ", 5"
set ytics font ", 5"
#set ylabel font ", 20" 'R, кОм' textcolor lt 8 offset 0.5,0,0
#set xlabel font ", 20" 'I_{свд}, мA' textcolor lt 8 offset 2,-1,0
set key font ",10"
set key left top

 


plot  "1.csv" using 1:2  notitle pt 7 ps 0.2 ,\
      "1.csv" using 1:2  title "{/Symbol a}(T)" smooth csplines    dt 2 lw 1 ,\

 

