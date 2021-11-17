set terminal png size 1920,1080 fontscale 3 
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","

set output 'tr.png';

#set term pdfcairo font "Times-New-Roman-Italic,12"
set xtics font ", 15"
set ytics font ", 15"
set ylabel font ", 16" 'I, мкА' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 16" 'U, B' textcolor lt 8 offset 2,0,0
set key font ",15"
set key bottom left
plot  "l5.csv" using 1:2  notitle with points lw 4,\
      "l5.csv" using 1:2  notitle smooth bezie  lw 2, \
      "l5.csv" using ($3/-1):($4/-1) notitle with points lw 4, \
      "l5.csv" using ($3/-1):($4/-1)  notitle smooth bezie  lw 2, \

set output 'td.png';

#set term pdfcairo font "Times-New-Roman-Italic,12"
set xtics font ", 15"
set ytics font ", 15"
set ylabel font ", 16" 'I, мкА' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 16" 'U, B' textcolor lt 8 offset 2,0,0
set key font ",15"
set key bottom left
plot  "l5.csv" using 6:7  notitle with points lw 4,\
      "l5.csv" using 6:7  notitle smooth sbezier     lw 2, \
      "l5.csv" using ($8/-1):($9/-1) notitle with points lw 4, \
      "l5.csv" using ($8/-1):($9/-1)  notitle smooth  csplines    lw 2, \


set output 'lax.png';

#set term pdfcairo font "Times-New-Roman-Italic,12"
set xtics font ", 15"
set ytics font ", 15"
set ylabel font ", 16" 'I, мкА' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 16" 'E_v, лк' textcolor lt 8 offset 2,0,0
set key font ",15"
set key bottom left
set linestyle 8 lt 6 lw 3
plot  "l5.csv" using 11:12  title "резистивний" with lines lw 4,\
       "l5.csv" using 11:13  title "діодний" linetype 4 lw 20, \
       "l5.csv" using 11:13  notitle with lines lw 4,
