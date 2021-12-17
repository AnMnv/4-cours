set terminal png size 1920,1280
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","

set output '50-100_Na.png';
set multiplot layout 2,1 rowsfirst
set xtics font ", 22"
set ytics font ", 22"
set ylabel font ", 23" 'I, А' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 23" 'U, B' textcolor lt 8 offset 2,-1,0
set key font ",15"
plot  "data1.csv" using 1:2 title"200нм" smooth bezier lw 4, \
      "data1.csv" using 1:3 title"400нм" smooth bezier lw 4, \
      "data1.csv" using 1:4 title"650нм" smooth bezier lw 4, \
      "data1.csv" using 1:5 title"700нм" smooth bezier lw 4

plot  "data1.csv" using 1:6 title"200нм" smooth bezier lw 4, \
      "data1.csv" using 1:7 title"400нм" smooth bezier lw 4, \
      "data1.csv" using 1:8 title"650нм" smooth bezier lw 4, \
      "data1.csv" using 1:9 title"700нм" smooth bezier lw 4
unset multiplot

set output '50-100_Zn.png';
set multiplot layout 2,1 rowsfirst
set xtics font ", 22"
set ytics font ", 22"
set ylabel font ", 23" 'I, А' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 23" 'U, B' textcolor lt 8 offset 2,-1,0
set key font ",15"
plot  "Zn_csv.csv" using 1:2 title"200нм" smooth bezier lw 4, \
      "Zn_csv.csv" using 1:3 title"400нм" smooth bezier lw 4, \
      "Zn_csv.csv" using 1:4 title"650нм" smooth bezier lw 4, \
      "Zn_csv.csv" using 1:5 title"700нм" smooth bezier lw 4

plot  "Zn_csv.csv" using 1:6 title"200нм" smooth bezier lw 4, \
      "Zn_csv.csv" using 1:7 title"400нм" smooth bezier lw 4, \
      "Zn_csv.csv" using 1:8 title"650нм" smooth bezier lw 4, \
      "Zn_csv.csv" using 1:9 title"700нм" smooth bezier lw 4
unset multiplot

set output '50-100_Cu.png';
set multiplot layout 2,1 rowsfirst
set xtics font ", 22"
set ytics font ", 22"
set ylabel font ", 23" 'I, А' textcolor lt 8 offset 0.5,0,0
set xlabel font ", 23" 'U, B' textcolor lt 8 offset 2,-1,0
set key font ",15"
plot  "Cu_csv.csv" using 1:2 title"200нм" smooth bezier lw 4, \
      "Cu_csv.csv" using 1:3 title"400нм" smooth bezier lw 4, \
      "Cu_csv.csv" using 1:4 title"650нм" smooth bezier lw 4, \
      "Cu_csv.csv" using 1:5 title"700нм" smooth bezier lw 4

plot  "Cu_csv.csv" using 1:6 title"200нм" smooth bezier lw 4, \
      "Cu_csv.csv" using 1:7 title"400нм" smooth bezier lw 4, \
      "Cu_csv.csv" using 1:8 title"650нм" smooth bezier lw 4, \
      "Cu_csv.csv" using 1:9 title"700нм" smooth bezier lw 4
unset multiplot

  ########################################
 ###                2                ###
#######################################
set output '2Na.png';
set xtics font ", 26" offset 0,-1,0
set ytics font ", 26"
set ylabel font ", 33" 'I, А' textcolor lt 8 offset 1.5,0,0
set xlabel font ", 33" 'Інтенсивність, %' textcolor lt 8 offset 2,-2,0
set key font ",25"
plot  "2Na_csv.csv" using 1:2 title"200нм" smooth bezier lw 4, \
      "2Na_csv.csv" using 1:3 title"400нм" smooth bezier lw 4, \
      "2Na_csv.csv" using 1:4 title"440нм" smooth bezier lw 4, \



  ########################################
 ###                3                ###
#######################################
set output '3part.png';
set xtics font ", 26" offset 0,-1,0
set ytics font ", 26"
set ylabel font ", 33" 'Енергія, еВ' textcolor lt 8 offset 1.5,0,0
set xlabel font ", 33" 'Частота, 10^{15} Гц' textcolor lt 8 offset 2,-2,0
set key font ",25"
plot  "3.csv" using 1:2 title"Na" smooth bezier lw 4, \
      "3.csv" using 4:5 title"Zn" smooth bezier lw 4, \
      "3.csv" using 7:8 title"Cu" smooth bezier lw 4, \
      "3.csv" using 10:11 title"Pl" smooth bezier lw 4, \
      "3.csv" using 13:14 title"Ka" smooth bezier lw 4, \
      "3.csv" using 16:17 title"Mg" smooth bezier lw 4, \
