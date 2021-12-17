
import serial

serial_port = '/dev/ttyACM0';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
write_to_file_path = "output1.txt";

output_file = open(write_to_file_path, "w+");
ser = serial.Serial('COM3', 9600)
t = 0
while True:
    line = ser.readline();
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    #print(line);
    output_file.write(line + str(t) + '\t')
    t += 2
    if(t >= 50):
        output_file.close();
