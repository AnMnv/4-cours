set terminal png size 1920,1280
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","


set output '1.png';
set xtics font ", 18"
set ytics font ", 18"
set ylabel font ", 23" 'I_{ C}, мА' textcolor lt 8 offset 2,0,0
set xlabel font ", 23" 'U_{ 3}, B' textcolor lt 8 offset 2,-1,0
set key font ", 20"
set key bottom right
plot "t1.csv" using 1:2:(13/1000):3   with xyerrorbars notitle,\
     "t1.csv" using 1:2 title"U = 0.3 B"  smooth bezier lw 4,\
     "t1.csv" using 4:5:(13/1000):6   with xyerrorbars notitle,\
     "t1.csv" using 4:5 title"U = 0.6 B"  smooth bezier lw 4,\
     "t1.csv" using 7:8:(13/1000):9   with xyerrorbars notitle,\
     "t1.csv" using 7:8 title"U = 0.9 B"  smooth bezier lw 4,\
     "t1.csv" using 10:11:(13/1000):12   with xyerrorbars notitle,\
     "t1.csv" using 10:11 title"U = 1.2 B"  smooth bezier lw 4,\


 set output '2.png';
 set xtics font ", 18"
 set ytics font ", 18"
 set ylabel font ", 23" 'I_{ C}, мА' textcolor lt 8 offset 2,0,0
 set xlabel font ", 23" 'U_{ C}, B' textcolor lt 8 offset 2,-1,0
 set key font ", 20"
 set key top right
 plot "t2.csv" using 1:2:(13/1000):14   with xyerrorbars notitle,\
      "t2.csv" using 1:2 title"U = 3.5 B"  smooth bezier lw 4,\
      "t2.csv" using 3:4:(13/1000):14   with xyerrorbars notitle,\
      "t2.csv" using 3:4 title"U = 4 B"  smooth bezier lw 4,\
      "t2.csv" using 5:6:(13/1000):14   with xyerrorbars notitle,\
      "t2.csv" using 5:6 title"U = 4.5 B"  smooth bezier lw 4,\
      "t2.csv" using 7:8:(13/1000):14   with xyerrorbars notitle,\
      "t2.csv" using 7:8 title"U = 5 B"  smooth bezier lw 4,\
      "t2.csv" using 9:10:(13/1000):14   with xyerrorbars notitle,\
      "t2.csv" using 9:10 title"U = 5.6 B"  smooth bezier lw 4,\
      "t2.csv" using 11:12:(13/1000):14   with xyerrorbars notitle,\
      "t2.csv" using 11:12 title"U = 6 B"  smooth bezier lw 4,\


set output '3.png';
set xtics font ", 18"
set ytics font ", 18"
set ylabel font ", 23" 'I_{ C}, мА' textcolor lt 8 offset 2,0,0
set xlabel font ", 23" 'U_{ 3}, B' textcolor lt 8 offset 2,-1,0
set key font ", 20"
set key bottom right
plot "t1.csv" using 1:(sqrt($2)):(13/1000):3   with xyerrorbars notitle,\
     "t1.csv" using 1:(sqrt($2)) title"U = 0.3 B"  smooth bezier lw 4,\
     "t1.csv" using 4:(sqrt($5)):(13/1000):6   with xyerrorbars notitle,\
     "t1.csv" using 4:(sqrt($5)) title"U = 0.6 B"  smooth bezier lw 4,\
     "t1.csv" using 7:(sqrt($8)):(13/1000):9   with xyerrorbars notitle,\
     "t1.csv" using 7:(sqrt($8)) title"U = 0.9 B"  smooth bezier lw 4,\
     "t1.csv" using 10:(sqrt($11)):(13/1000):12   with xyerrorbars notitle,\
     "t1.csv" using 10:(sqrt($11)) title"U = 1.2 B"  smooth bezier lw 4,\
