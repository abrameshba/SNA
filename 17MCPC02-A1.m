#!/usr/bin/gnuplot -persist
reset
set title "Degree distribution" font ",14" textcolor rgbcolor "royalblue"
set ylabel "Number of scientists"
set xlabel "Degree of scientists"
set terminal postscript eps enhanced color 
#set terminal pdfcairo 
set output "17MCPC02-1.eps"
set style histogram rowstacked gap 0
set style fill solid 0.5 border lt -1
plot 'geom.txt' using 1:2 smooth freq with boxes notitle

reset
#set title "Power law" font ",14" textcolor rgbcolor "royalblue"
set ylabel "Number of scientists"
set xlabel "Degree of scientists"
set terminal postscript eps enhanced color 
#set terminal pdfcairo 
set output "17MCPC02-2.eps"
#best fit
c=947.35
d=-0.95
f(x) = a * ( x ** b)
g(x) = c * ( x ** d)
a=2480.4587
b=-1.8
fit f(x) 'geom.txt' via a, b
fit g(x) 'geom.txt' via c, d
plot 'geom.txt' using 1:2 with points pointtype 3 pointsize 1  lc rgb "#EE82EE" title "scientists", f(x)  title "power law"  dashtype 5, g(x)  title "best fit" dashtype 3


 
