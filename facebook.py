import time
import dryscrape
from threading import Timer

email    = ''
password = ''

sess = dryscrape.Session(base_url = 'https://www.facebook.com')

sess.set_attribute('auto_load_images', False)

print "Logging in..."
sess.visit('/')

email_field    = sess.at_css('#email')
password_field = sess.at_css('#pass')
email_field.set(email)
password_field.set(password)

email_field.form().submit()

sess.visit('https://www.facebook.com/lists/479727515440839')

#import ipdb; ipdb.set_trace()
# for link in sess.css('div[id^="substream_"]').xpath('//a[@href]'):
# 		print link['href']
def scrapFacebook():
	for status in sess.css('div[id^="substream_"]'):
		for content in status.css('.userContentWrapper'):
			if len(content.css('.userContent')) > 0:
				print content.css('.userContent')[0].text()
				# print content.css('.userContent')[0].text()
				print '-----------'

t = Timer(10.0, scrapFacebook)
t.start()
