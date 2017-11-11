# Raspberry Pi Test Pattern Genreator
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
