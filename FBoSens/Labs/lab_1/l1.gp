set terminal png size 1920,1080 fontscale 3 
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","

set output '11.png';


set term pdfcairo font "Times-New-Roman-Italic,12"
set xtics font ", 15"
set ytics font ", 15"
set ylabel font ", 16" 'R, МОм' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 16" 'l, см' textcolor lt 8 offset 2,0,0
set key font ",15"
set key bottom left
plot  "l1.csv" using 1:2  notitle with points lw 4,\
      "l1.csv" using 1:2  notitle smooth bezie  lw 2, \

