Author Hunter Stiles 2021

Files
phone.py
This is the main application,  
I decided to make a softphone  and  found that twilio was a library that
could create a client and place calls from a python application.  So I
started building my app.  I found that twilio is built for people that
want voice enabled applications to interact with people.  After placing a
call, it seams that it is the application that is meant to interact with
who ever answers the phone. There appears to be no simple way to have the
call get an audio stream from the microphone or send audio to the computer
speakers. Twilio does allow another call to be placed  which ties another
person into the original phone call.  So this softphone will connect you to
the number you dialed by first  calling you on your phone and then ringing
the number dialed.  Your phone number can be configured by setting the
environmental variable MYPHONE.  The default is my cell phone.  Of course,
you could change the code to have the default be your phone number for testing.
The softphone also lets you to send an SMS text message or if you need to get
the message to a number that isn't a cell phone,, you can send the message
via voice. The softphone will call the number and read it after the phone is
answered using text to speech.

directory.py
I wanted the softphone, to have a contact database, so this is a simple
script to create that database. The database is originally populated with
a few numbers. These are real numbers, so if you call want to call or sent
me a message feel free to.  If this script is run a second time, it will
reset the directory to it's original configuration. 

directory.db
The SQLite database that contains contact information.  The application
allows you to send voice/text messages to people in the database, as well
as dialing the number on the phone GUI
Libraries
the application requires the following libraries
twilio, tkinter, logging, sqlite3 and pandas.


Environmental Variables

to configure the application you can set the following 

TWILIO_ACCOUNT_SID -- your Twilio Account SID --trial accounts can be created
for free, but come with significant restrictions. see
https://support.twilio.com/hc/en-us/articles/223136107-How-does-Twilio-s-Free-Trial-work-
for details

TWILIO_ACCOUNT_TOKEN  -- your Twilio Account token

