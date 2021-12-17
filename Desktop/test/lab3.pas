program lab1;
//uses crt;
uses crt, Math;
  //const pi = 3.14;
  var   i,u,i1,u1,r:real;

  begin
    clrscr;
    write('I: ');
    read(i);
    write('+- I: ');
    read(i1);

    write('U: ');
    read(u);
    write('+- U: ');
    read(u1);


    r:=sqrt((power((u1/i),2)) + ( power(((u*i1)/(i*i)),2) ));




    writeln(' ' );
    writeln('ПОХИБКА',r);
    writeln(' ' );
end.
