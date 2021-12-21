
#set terminal png size 1920,1000
set encoding utf8
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","
set terminal pdf

#set output '1.pdf';



set ylabel font ", 10" '' textcolor lt 8  
#set ylabel "qqq"   rotate by 0
set ylabel offset 0.5,10,0

#set xlabel font ", 10" 'qqq' textcolor lt 8 offset 2,-1,-10
set xlabel offset 31,-0.5,0

set key font ",10"
set key left top

 
set xtics font ", 10"
set ytics font ", 10"

#set yrange [-4.5:14.5]
#set xrange [0:300]

set arrow 1 lw 1.2 from 0,60 to 0,77.5
set arrow 2 lw 1.2 from 0,60 to 640,60

set tmargin 5
set rmargin 10

set border 3



set tics nomirror
set xtics
set ytics

#plot  "1.csv" using 1:2  notitle pt 7 ps 0.2 ,\
 #     "1.csv" using 1:2  title "{/Symbol a}(T)" smooth csplines    dt 2 lw 1 ,\
 #     "1.csv" using 3:4  title "{/Symbol D}V(T)" smooth csplines     lw 3 ,\
 #     "1.csv" using 3:4  notitle pt 7 ps 0.2 ,\
 
set output '123.pdf';
 plot "3c.csv" using 1:3 notitle "3" smooth unique    lc 8  lw 3 ,\
      "3c.csv" using 1:3  notitle lc 8 pt 0 ps 0.0 ,\
      "c1.csv" using 1:3  notitle "1" smooth unique   lc 8  lw 3 ,\
      "c1.csv" using 1:3  notitle lc 8 pt 0 ps 0.0 ,\
      "c2.csv" using 1:3  notitle "2" smooth unique   lc 8  lw 3 ,\
      "c2.csv" using 1:3  notitle lc 8 pt 0 ps 0.0 ,\
      "c4.csv" using 1:3  notitle "4" smooth unique   lc 8  lw 3 ,\
      "c4.csv" using 1:3  notitle lc 8 pt 0 ps 0.0 ,\

 