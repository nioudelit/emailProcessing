# -*- coding: utf-8 -*-
#!/usr/bin/env python

import poplib
import os
import time
#import serial

while True:
    fichier = open("nbr.txt", "r")
    test = open("verif.txt", "w")
    contenu = fichier.read()

    #ser = serial.Serial('/dev/tty.usbserial', 9600)

    M = poplib.POP3('pop.sfr.fr') #REMPLACER VARIABLE, EX: pop.free.fr, pop.3.bbox.fr… ou IMAP

    login= "adressemail@sfr.fr" #REMPLACER VARIABLE ICI
    code="motdepasse" #REMPLACER VARIABLE ICI
    mServer = poplib.POP3('pop.sfr.fr') # ICI AUSSI REMPLACER VARIABLE

    #Login to mail server
    mServer.user(login)
    mServer.pass_(code)

    #Get the number of mail messages
    numMessages = len(mServer.list()[1])

    print "You have %d messages." % (numMessages)
    if(str(numMessages) != contenu):
        print("Nouveaux MESSAGES !!!")
        fichier = open("nbr.txt", "w")
        fichier.write(str(numMessages))
        test.write("1")
        #ser.write('13')
    else:
        print("Pas de nouveaux messages mon gars")
        test.write("0")

    fichier.close()
    test.close()

    print "Liste des Messages reçus:"

    for mList in range(numMessages) :
        for msg in mServer.retr(mList+1)[1]:
            if msg.startswith('Subject'):
                print '\t' + msg
                break
    time.sleep(60)

mServer.quit() #facultatif
