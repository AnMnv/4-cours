
#set terminal png size 1920,1000
set encoding utf8
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","
set terminal pdf

#set output '1.pdf';



set ylabel font ", 10" '' textcolor lt 8  
set ylabel "{/Times-Italic{ {/Symbol D}V}\n {/Times-Italic та}\n {/Times-Roman{ {/Symbol a}}}"   rotate by 0
set ylabel offset 0.5,10,0

set xlabel font ", 10" '{/Times-Italic T, K}' textcolor lt 8 offset 2,-1,-10
set xlabel offset 31,-0.5,0

set key font ",10"
set key left top

 
set xtics font ", 10"
set ytics font ", 10"

set yrange [-4.5:14.5]
set xrange [0:300]

set arrow 1 from 0,0 to 0,14.5
set arrow 2 from 0,0 to 300,0

set tmargin 5
set rmargin 10

set border 2



set tics nomirror
unset xtics
unset ytics

#plot  "1.csv" using 1:2  notitle pt 7 ps 0.2 ,\
 #     "1.csv" using 1:2  title "{/Symbol a}(T)" smooth csplines    dt 2 lw 1 ,\
 #     "1.csv" using 3:4  title "{/Symbol D}V(T)" smooth csplines     lw 3 ,\
 #     "1.csv" using 3:4  notitle pt 7 ps 0.2 ,\
 
set output '2.pdf';
 plot "3.csv" using 1:2  notitle "{/Symbol a}(T)" smooth csplines     lw 3 ,\
      "3.csv" using 1:2  notitle pt 7 ps 0.2 ,\
      "3.csv" using 3:4  notitle "{/Symbol D}V(T)" smooth csplines     lw 3 ,\
      "3.csv" using 3:4  notitle pt 7 ps 0.2 ,\

 