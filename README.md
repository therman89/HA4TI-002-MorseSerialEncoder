# Morse Serial Encoder(Auto-keyer)
Often times HAMs need to send the same messages over and over again(e.g. CQ CQ DE HA4TI PSE K). As a lazy engineer, I did not want to do that by hand, so I created a very simple python script to make my life easier. I wanted to create an auto keyer with the least effort. I had a CP2104 USB -- RS-232 bridge lying around and found out that it is possible to control my FT-817 rig with its flow control pins. The morse key is just a simple switch, wich turns on the transmitter and sends a tone if the contacts are closed. To imitate this, the RTS signal of the module can be used. If the signal is logic low, the contacts are closed. This is a **non-isolated connection**, meaning that you might be galvanically connected to your antenna. To isolate your computer from the radio, you can use an *opto coupler*.
This python script encodes text to Morse code and sends it via virtual COM port. It uses the RTS signal through the standard pyserial library. You can add, modify and delete the available messages by editing the 'messages' list variable in the code. The number of commands is limited to 10 to keep things simple.
# Requirements
* Python 2.7 installed 
* An USB -- RS-232 bridge(e.g. CP2104 module)
* 3.5mm jack cable
* 3.5mm jack splitter

# Instructions
1. Connect the 3.5mm jack cable to the USB -- RS-232 bridge as shown below. Solder the audio cable to jumper cables and use electrical tape to prevent them from shorting together.
Inside the FT-817 the morse key has a ~12kOhm pullup resistor to the +5V rail. The CP2104 pins are 5V tolerant, so there sould be no problem connecting them together. The correct connection of the module and the radio is the following:

Sleeve <-----> GND
Tip <-----> RTS
![connection](https://github.com/therman89/HA4TI002-MorseSerialEncoder/raw/master/CP2104_conn.jpg)
2. Use a jack splitter to create a wired OR connection of the key and the auto-keyer
3. Start the python code from the command line
    Available commands in the program:
    * '0-9': Send the pre defined messages
    * 's': Set the speed of morse code
    * '&': Exit program
    * '?': List of commands

# Disclaimer
The program can be copied, modified freely under GPL license. This project is considered a hack. By connecting your computer to your radio with cables without isolation **can be dangerous**, especially in stormy weather. **Do it at your own risk!** and I can not be held responsible for any damage caused to your radio or computer. 

