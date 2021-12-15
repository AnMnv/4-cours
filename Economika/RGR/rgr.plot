set terminal png size 1920,1280
set xzeroaxis
set yzeroaxis

set datafile separator ";"

#set decimalsign ","

set output '1111.png';
set xtics font ", 22"  
set ytics font ", 22"
set ylabel font ", 23" 'Виторг, Дохів, грн' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 23" 'Обсяг виробництва, шт' textcolor lt 8 offset 2,-1,0
set linetype 1 dashtype 2
set key font ",15"
plot  "t1.csv" using 1:2 title"Qp" smooth bezier lw 4, \
      "t1.csv" using 1:3 title"Cp" smooth bezier lw 4, \
      "t1.csv" using 4:5  title"b*Cpov*X" smooth bezier lw 2, \


