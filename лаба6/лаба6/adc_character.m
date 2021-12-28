x=xlsread('DAC_ADC', 'Sheet1', 'H13:H20'); 
y=xlsread('DAC_ADC', 'Sheet1', 'I13:I20');



grid on;
xlabel('U_{âõ}, Â');
ylabel('N');

hold on;

plot(x,y, 'k*');


coeff=polyfit(x,y,2);
x_grid = linspace(min(x), max(x), 500);
y_grid = polyval(coeff, x_grid);


plot(x_grid, y_grid, 'r');