#!/usr/bin/env python
import asyncore 
from datetime import datetime 
from smtpd import SMTPServer 
import os 
class EmlServer(SMTPServer): 
   no = 0 
   mail_directory = "_mail" 
   def process_message(self, peer, mailfrom, rcpttos, data): 
       #try: 
           #if not os.path.isdir(self.mail_directory): 
               #os.makedirs(self.mail_directory) 
               #print 'created directory %s' % self.mail_directory 
       #except: 
           #print 'Couldnt create mail directory, heres the mail:' 
           #print data 
           #return 
       #filename = '%s/%s-%d.eml' % (self.mail_directory, 
#datetime.now().strftime('%Y%m%d%H%M%S'), self.no) 
       #f = open(filename, 'w') 
       #f.write(data) 
       #f.close 
       #print '%s saved.' % filename 
       #self.no += 1 
       print data 
if __name__ == '__main__': 
   foo = EmlServer(('localhost', 1025), None) 
   try: 
       asyncore.loop() 
   except KeyboardInterrupt: 
       pass 
