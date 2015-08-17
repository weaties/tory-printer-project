from instagram.client import InstagramAPI
import time
import pygame
import urllib
import cStringIO
import RPi.GPIO as gpio
import cups #for printing
from xhtml2pdf import pisa #for generating PDFs from xhtml
from subprocess import call #for sending command line items from python

#filename for temp pdf
filename = "/home/pi/tmp/tory-print.pdf"

INSTAGRAM_CLIENT_ID='64cb6ac955094f7da4c0eda3cffdbfba'
INSTAGRAM_CLIENT_SECRET='9842e540f06240cbbc2326f6687e9aad'

#Start up the API
api = InstagramAPI(client_id=INSTAGRAM_CLIENT_ID,client_secret=INSTAGRAM_CLIENT_SECRET)

#Start GUI
width = 640
height = 640
#pygame.init()
#window = pygame.display.set_mode((width,height))

#Start GPIO
#try:
#	gpio.setmode(gpio.BCM)
#	gpio.setup(25, gpio.OUT)
#	gpio.output(25, gpio.HIGH)
#	time.sleep(0.5)
#	gpio.output(25, gpio.LOW)

#except Exception, e:
#               print e

def showImage(url):
	p = cStringIO.StringIO(urllib.urlopen(url).read()) #load image url to string, then make it act as a file
	background = pygame.image.load(p,"test.jpg") #load image. test.jpg is just a namehint
	window.blit(background,(0,0)) #put image onto background
	pygame.display.update()

def printout(url):
	#generate content
 	xhtml = '<h1 style="text-align:center">Your image:</h1>\n'
	xhtml += '<p style="text-align:center"><img src="'+url+'" align="middle"></p>'
	pdf = pisa.CreatePDF(xhtml, file(filename, "w"))
 	if not pdf.err:
   		pdf.dest.close()
   		print("pdf created. Sending print...")
   		conn = cups.Connection()
   		printers = conn.getPrinters()
   		for printer in printers:
    			print printer, printers[printer]["device-uri"]
     		printer_name = printers.keys()[0] #use first printer in list
   		conn.printFile(printer_name, filename, "Python_Status_print", {})
   		print("Print request sent")
 	else:
   		print("error creating pdf or printing")
   		xhtml = '' #clear xthml string

maxID=0
new_url=''
old_url=''

while True: #tries again after exception is thrown
	print "in the while loop"
	try:
		while True:
			#Load media filtered by tag query
			recent_tag_media = api.tag_recent_media(1,maxID,'like4like')
			print "found a tag" 
			print recent_tag_media	
			#get URL and tell it to ignore posts older than it
			for media in recent_tag_media[0]:
				new_url = media.images['standard_resolution'].url
				print "the URL is "
				print new_url
				maxID = media.id
				
				if (new_url!=old_url) and (len(media.tags)<7): #ignore overtagged spam
					print "---new post---"
 					print str(media.user)
 					print str(media.caption)
 					print "URL: " + str(new_url)
 					#print len(media.tags)
 					print ''
 					# showImage(str(new_url))
 					printout(str(new_url))
					old_url = new_url
		 	#respect rate limit and cpu
 			time.sleep(15)

		#Close window on exit
		if pygame.QUIT in [e.type for e in pygame.event.get()]:
			break
	except Exception, e:
		print e
		time.sleep(20) #if failed, wait and try again
