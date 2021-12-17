set terminal png size 1080,720
set xzeroaxis
set yzeroaxis

set datafile separator ";"
#set decimalsign ","

set output '1.png';
set xtics font ", 18"
set ytics font ", 18"
set ylabel font ", 23" 'I _{вх}, мкА' textcolor lt 8 offset 0.5,1,0
set xlabel font ", 23" 'U _{вх}, B' textcolor lt 8 offset 2,-1,0

#unset key
set key
plot "vax_vx.csv" using 1:2:3:4 title "Uвых = 0 В" with xyerrorbars, \
     "vax_vx.csv" using 5:6:7:8 title "Uвых = 8 В" with xyerrorbars

set terminal png size 1920,1200
set output '2.png';
set ylabel font ", 23" 'I _{вих}, мкА' textcolor lt 8 offset 0.5,1,0
set xlabel font ", 23" 'U _{вих}, B' textcolor lt 8 offset 2,-1,0
plot"vax_exit.csv" using 1:2:3:4 notitle with xyerrorbars, \
    "vax_exit.csv" using 1:2 title"3 мкА"    smooth bezier lw  4,\
    "vax_exit.csv" using 5:6:7:8 notitle with xyerrorbars, \
    "vax_exit.csv" using 5:6 title"6 мкА"    smooth bezier lw  4,\
    "vax_exit.csv" using 9:10:11:12 notitle with xyerrorbars, \
    "vax_exit.csv" using 9:10 title"9 мкА"     smooth bezier lw  4, \
    "vax_exit.csv" using 13:14:15:16 notitle  with xyerrorbars, \
    "vax_exit.csv" using 13:14 title"12 мкА"    smooth bezier lw  4, \
    "vax_exit.csv" using 17:18:19:20 notitle with xyerrorbars, \
    "vax_exit.csv" using 17:18 title"15 мкА"    smooth bezier lw  4, \
    "vax_exit.csv" using 21:22:23:24 notitle with xyerrorbars, \
    "vax_exit.csv" using 21:22 title"18 мкА"    smooth bezier lw  4, \
    "vax_exit.csv" using 25:26:27:28 notitle with xyerrorbars, \
    "vax_exit.csv" using 25:26 title"21 мкА"    smooth bezier lw  4, \
    "vax_exit.csv" using 29:30:31:32 notitle with xyerrorbars, \
    "vax_exit.csv" using 29:30 title"24 мкА"    smooth bezier lw  4, \
    "vax_exit.csv" using 33:34:35:36 notitle with xyerrorbars, \
    "vax_exit.csv" using 33:34 title"27 мкА"    smooth bezier lw  4, \
    "vax_exit.csv" using 37:38:39:40 notitle with xyerrorbars, \
    "vax_exit.csv" using 37:38 title"30 мкА"    smooth bezier lw  4, \
    "vax_exit.csv" using 41:42:43:44 notitle with xyerrorbars, \
    "vax_exit.csv" using 41:42 title"33 мкА"    smooth bezier lw  4, \
    "vax_exit.csv" using 45:46:47:48 notitle with xyerrorbars, \
    "vax_exit.csv" using 45:46 title"36 мкА"    smooth bezier lw  4, \
    "vax_exit.csv" using 49:50:51:52 notitle with xyerrorbars, \
    "vax_exit.csv" using 49:50 title"39 мкА"    smooth bezier lw  4, \
    "vax_exit.csv" using 53:54:55:56 notitle with xyerrorbars, \
    "vax_exit.csv" using 53:54 title"42 мкА"    smooth bezier lw  4, \
    "vax_exit.csv" using 57:58:59:60 notitle with xyerrorbars, \
    "vax_exit.csv" using 57:58 title"45 мкА"    smooth bezier lw  4, \
    "vax_exit.csv" using 61:62:63:64 notitle with xyerrorbars, \
    "vax_exit.csv" using 61:62 title"48 мкА"    smooth bezier lw  4, \

    set xrange [0:0.3]
    set output '3.png';
    plot"vax_exit.csv" using 1:2:3:4 notitle with xyerrorbars, \
        "vax_exit.csv" using 1:2 title"3 мкА"    smooth bezier lw  4,\
        "vax_exit.csv" using 5:6:7:8 notitle with xyerrorbars, \
        "vax_exit.csv" using 5:6 title"6 мкА"    smooth bezier lw  4,\
        "vax_exit.csv" using 9:10:11:12 notitle with xyerrorbars, \
        "vax_exit.csv" using 9:10 title"9 мкА"     smooth bezier lw  4, \
        "vax_exit.csv" using 13:14:15:16 notitle  with xyerrorbars, \
        "vax_exit.csv" using 13:14 title"12 мкА"    smooth bezier lw  4, \
        "vax_exit.csv" using 17:18:19:20 notitle with xyerrorbars, \
        "vax_exit.csv" using 17:18 title"15 мкА"    smooth bezier lw  4, \
        "vax_exit.csv" using 21:22:23:24 notitle with xyerrorbars, \
        "vax_exit.csv" using 21:22 title"18 мкА"    smooth bezier lw  4, \
        "vax_exit.csv" using 25:26:27:28 notitle with xyerrorbars, \
        "vax_exit.csv" using 25:26 title"21 мкА"    smooth bezier lw  4, \
        "vax_exit.csv" using 29:30:31:32 notitle with xyerrorbars, \
        "vax_exit.csv" using 29:30 title"24 мкА"    smooth bezier lw  4, \
        "vax_exit.csv" using 33:34:35:36 notitle with xyerrorbars, \
        "vax_exit.csv" using 33:34 title"27 мкА"    smooth bezier lw  4, \
        "vax_exit.csv" using 37:38:39:40 notitle with xyerrorbars, \
        "vax_exit.csv" using 37:38 title"30 мкА"    smooth bezier lw  4, \
        "vax_exit.csv" using 41:42:43:44 notitle with xyerrorbars, \
        "vax_exit.csv" using 41:42 title"33 мкА"    smooth bezier lw  4, \
        "vax_exit.csv" using 45:46:47:48 notitle with xyerrorbars, \
        "vax_exit.csv" using 45:46 title"36 мкА"    smooth bezier lw  4, \
        "vax_exit.csv" using 49:50:51:52 notitle with xyerrorbars, \
        "vax_exit.csv" using 49:50 title"39 мкА"    smooth bezier lw  4, \
        "vax_exit.csv" using 53:54:55:56 notitle with xyerrorbars, \
        "vax_exit.csv" using 53:54 title"42 мкА"    smooth bezier lw  4, \
        "vax_exit.csv" using 57:58:59:60 notitle with xyerrorbars, \
        "vax_exit.csv" using 57:58 title"45 мкА"    smooth bezier lw  4, \
        "vax_exit.csv" using 61:62:63:64 notitle with xyerrorbars, \
        "vax_exit.csv" using 61:62 title"48 мкА"    smooth bezier lw  4, \
