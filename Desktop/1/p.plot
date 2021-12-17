set terminal png size 1024,768
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","

set output 'd1.png';
set ylabel 'I _d, мА' textcolor lt 8
set xlabel 'U _d, мB' textcolor lt 8
plot "Data for lab 1.csv" using 7:8:5:6 title"ВАХ дiода D1 за прямого змiщення" with xyerrorbars


set output 'd2.png';
set ylabel 'I _d, мА' textcolor lt 8
set xlabel 'U _d, мB' textcolor lt 8
plot "Data for lab 1.csv"  using  15:16:13:14 title"ВАХ дiода D2 за прямого змiщення" with xyerrorbars

set output 'd1r.png';
set ylabel 'I _d, мА' textcolor lt 8
set xlabel 'U _d, мB' textcolor lt 8
plot "Data for lab 1.csv" using 24:25:22:23 title"ВАХ дiода D1 за зворотного змiщення" with xyerrorbars

set output 'd2r.png';
set ylabel 'I _d, мА' textcolor lt 8
set xlabel 'U _d, мB' textcolor lt 8
plot "Data for lab 1.csv" using 33:34:31:32 title"ВАХ дiода D2 за зворотного змiщення" with xyerrorbars
