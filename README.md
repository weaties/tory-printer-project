# Introduction

This is project inspired by https://nicshackle.wordpress.com/2014/04/09/hashtag-activated-instagram-printer/  and driven by Tory with the idea of creating a Raspberry pi driven instagram printer.

it's pretty crude, but hey - I got it to work with a wifi printer, as well as one connected the the USB port on the Raspberry.

The code and instructions on the original were pretty crude, and the changes I have made are not much better.

# Packages to install

I installed the following packages (I think this is a complete list) on the raspberry Pi.  I think I am using the raspbarrian Distro, but I spun that up a while ago, so I don't really remember.

* install pip on the raspberry
* pip install python-instagram
* pip install cups
* pip install python-cups

## Dead chickens here
I kept getting error with the xhtml2pdf stuff, so these are some of the dead chickens I waved.  I eventually got it to work, but wasn't taking the best notes...

* following instructions here for the xmhtml2pdf  https://pypi.python.org/pypi/xhtml2pdf/
* sudo install pisa - didn't help
* pip install xhtml2pdf

# Instagram Keys

I followed these instructions to get a key http://help.dimsemenov.com/kb/wordpress-royalslider-faq/wp-how-to-get-instagram-client-id-and-client-secret-key  (The key that is in the code has been disabled, I recommend running a branch - but Tory, and she doesn't know what that means ;)  )

# Printers

adding a printer with cups http://www.howtogeek.com/169679/how-to-add-a-printer-to-your-raspberry-pi-or-other-linux-computer/

* This also allowed us to connect to the cups interface over the local network on port 631
