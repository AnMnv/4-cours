unit lab3;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    x1: TEdit;
    OK: TButton;
    Edit1: TEdit;
    Label1: TLabel;
    r1: TLabel;
    t: TEdit;
    t1: TLabel;
    procedure Edit1Change(Sender: TObject);
    procedure OKClick(Sender: TObject);
    procedure xChange(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}



  { TForm1 }

  procedure TForm1.OKClick(Sender: TObject);
  var ai, f, z, s, a_curr, eps,y,k,x: real;
  begin

      Try
   eps:= StrToFloat(t.Text);
   except
     On E : EConvertError do
     begin
       ShowMessage('Точность введена не корректоно!');
      // exit;
     end;
   end;

   Try
   x:= StrToFloat(x1.Text);
   except
     On E : EConvertError do
     begin
       ShowMessage('Х введён не корректоно!');
       //exit;
     end;
   end;

   //finally



    ai:=x;
    f:=1;
    s:= ai;
    y:=1;
    k:=1 ;
    while true  do
        begin;
              y:= y*(-1);
              f*=k;
              z:= x*x;
              a_curr:= (y*z)/(f*(2*k+1));
              ai:= a_curr;
              s:=  a_curr;



           if (abs(a_curr)-abs(ai))< eps
            then
            break;
            //exit;
            k:=k+1;
        end;
     Edit1.Text:=FloatToSTR(s);

        //t.Clear;
  end;

procedure TForm1.xChange(Sender: TObject);
begin

end;

procedure TForm1.Edit1Change(Sender: TObject);
begin

end;

  begin


end.

