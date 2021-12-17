set terminal png size 1024,768
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","
set output 'd1.png';
plot "Data for lab 1.csv" using 7:8:5:6 with xyerrorbars
set output 'd2.png';
plot "Data for lab 1.csv" using 15:16:13:14 with xyerrorbars
set output 'd1r.png';
plot "Data for lab 1.csv" using 24:25:22:23 with xyerrorbars
set output 'd2r.png';
plot "Data for lab 1.csv" using 33:34:31:32 with xyerrorbars
