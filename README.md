# Raspberry Pi Test Pattern Generator
Files for making a PAL test pattern generator with a Raspberry Pi.
I Intended to upload an entire Image file which you could run on the R.Pi. without having to do any software configuration, but it was much to large to put on Github.

You firstly need to install raspbian on your R.Pi. I won't go into details here because there are thousands of brilliant tutorials online which do a much better job of it. 
The buttons for changing the testcard and toggling teletext on/off need to be wired up. I followed this tutorial:

https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/

You also need to install Vbit-Pi for teletext and fbi for the testcards.
For Vbit-Pi, follow these instructions:

http://teastop.co.uk/teletext/vbit/

For FBI, run:
sudo apt-get install fbi

You may also want to update your Raspberry Pi.

Next, you need to connect your buttons circuit to pins 18, 29 and 31.
Import all the code and images in this project to the Pi's home folder, i.e. /home/pi/.
My computer is too old to run Git, so I would download the files as a zip, extract them, and then use WinSCP to copy the files from the computer to the R. Pi. It's really easy, no extra configuration required to move files from one computer to another.

Run 'run.py' by typing:

sudo python run.py

My own system was configured so that the screen does'nt go blank, and it has a 'splashscreen' which comes up at startup. I'm leaving all this up to you, as it took me many hours of googleing to make it work as I wanted and I can't remember what worked and what didn't. I've include my splashscreen in case you want to use it.

You are, of course, welcome to edit the code for your own features and ideas. I compiled it from various sources online while knowing next to nothing about Python, so I'm sure you can do the same.

Here's a youtube video of my own sytem, in both the prototyping and finished stage:

https://youtu.be/wIiouzbJC_g

https://youtu.be/NR3X-FwhJMM

Since PAL and other analogue systems are now considered 'out-of-date', I might start another branch for a high definition version. This would be just for you, as I don't have any use for a HD test pattern generator. The only real changes I can think of that would have to be made would be the testcards. These won't be hard to save in a high definition format. I used a program called 'Test Card Maker' to make my testcards. It seems to be quite old, but can be downloaded from here:

https://archive.org/details/tcmaker
