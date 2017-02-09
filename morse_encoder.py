from __future__ import print_function
import sys
import time
import serial

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

"""
The following code snippet was taken from
https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/morse_code/
"""
CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-',
        '+': '.-.-.'}

messages = [
    'cq cq de ha4ti ha4ti +k',
    'cq cq de ha4ti/qrp ha4ti/qrp pse k'
]

def dot(port):    
    port.setRTS(1)
    time.sleep(pause)
    port.setRTS(0)
    time.sleep(pause)


def dash(port):    
    port.setRTS(1)
    time.sleep(3*pause)
    port.setRTS(0)
    time.sleep(pause)


def code_text_to_morse(input):
    try:
        s = serial.Serial(port='COM6')
        for letter in input:
            print(letter, end='')
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash(s)
                elif symbol == '.':
                    dot(s)
                else:
                    time.sleep(2*pause)
            time.sleep(3*pause)
    except KeyboardInterrupt:
        print("\nSending interrupted")

tempo = 15
pause = 1.0/tempo


def main():
    go = 1
    global tempo
    global pause
    while go == 1:
        # go = 0
        try:
            print('\n\nWhat message would you like to send?')
            msg = getch()
            if '&' in msg:
                sys.exit(0)
            elif '?' in msg:
                for cnt in range(0, len(messages)):
                    print(str(cnt) + ": " + str(messages[cnt]))
                print ("Current tempo is " + str(tempo))
                print ("Press & to exit program")
                print ("\n")
            elif 's' in msg:
                try:
                    new_tempo = raw_input("Enter tempo: ")
                    if 0 < int(new_tempo) < 30:
                        tempo = int(new_tempo)
                        pause = 1.0/tempo
                        print("Tempo set to: " + str(tempo))
                except Exception as e:
                    print(e.message)

            elif int(msg) in range(0, len(messages), 1):
                code_text_to_morse(messages[int(msg)])

            else:
                pass
        except Exception as e:
            print("Invalid key pressed")
            # print(e.message)




if __name__ == '__main__':
    main()
