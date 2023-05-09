import pickle
import os
import pathlib


class Ticket:
    name = ' '
    email = ' '
    event = ' '
    reference = 200000

    def bookticket(self):
        self.name = input('enter your name please:')
        self.email = input('enter your email please:')
        file1 = pathlib.Path('events.data')
        if file1.exists():
            infile = open('events.data','rb')
            eventdetails =pickle.load(infile)

            self.reference = int(input('enter reference code (1-150):'))
            while True:
                if self.reference<=1:
                    print('Error! Please enter valid reference code')
                    self.reference =  int(input('enter reference code (1-150):'))
                else:
                    break
        for event in eventdetails:
            print('Available event code: '+event.eventcode + 'Event name: '+event.eventname)
        infile.close()
        self.event = input('enter event code:')

    def check(self):
        file1 = pathlib.Path('tickets.data')
        if file1.exists():
            infile = open('tickets.data','rb')
            ticketdetails = pickle.load(infile)
            for ticket in ticketdetails:
                if ticket.email ==self.email and ticket.event ==self.event:
                    return True
            infile.close()
    def totalticketcount(self):
        file1 = pathlib.Path('events.data')
        if file1.exists():
            infile = open('events.data','rb')
            eventdetails = pickle.load(infile)
            for event in eventdetails:
                if event.eventcode ==self.event:
                    return int(event.totalavailableseat)
            infile.close()
        else:
            return 0
    def bookedseatscount(self):
        file1 = pathlib.Path('events.data')
        counter = 0
        if file1.exists():
            infile = open('tickets.data','rb')
            ticketdetails = pickle.load(infile)
            for ticket in ticketdetails:
                if ticket.event ==self.event:
                    counter = counter + 1
            return int(counter)
        return 0


class Event:
    eventname = ''
    eventcode = ''
    totalavailableseat = 20
    def createevent(self):
        self.eventname = input('enter name of the event:')
        self.eventcode = input('enter event code:')
        self.totalavailableseat = input('enter number of available seats:')
        print('-------Event created succesefully!!!')



def bookeventticket():
    ticket = Ticket()
    ticket.bookticket()
    if ticket.check():
        print('You have already booked a seat')
    
    elif ticket.bookedseatscount()>=ticket.totalticketcount():
        print('All ticket were sold out')
    else:
        print('ticket booked')
        saveticketdetails(ticket)
        

def saveticketdetails(ticket):
    file1 = pathlib.Path('tickets.data')
    if file1.exists():
        infile = open('tickets.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(ticket)
        infile.close()
        os.remove('tickets.data')
    else:
        oldlist = [ticket]
    outfile = open('tempTicket.data','wb')
    pickle.dump(oldlist,outfile)
    outfile.close()
    os.rename('tempTicket.data','tickets.data')

def getticketdetails():
    file1 = pathlib.Path('tickets.data')
    if file1.exists():
        infile = open('tickets.data','rb')
        ticketdetails = pickle.load(infile)
        print('----------Ticket Details--------')
        print('T-Ref     C-Name   C-Email   E-Code')
        for ticket in ticketdetails:
            print(ticket.reference,'\t',ticket.name,'\t',ticket.email,'\t',ticket.event)
        infile.close()
        print('-------------')
        input('press enter to main menu')
    else:
        print('no ticket record is found')

def createevent():
    event = Event()
    event.createevent()
    saveEventdetails(event)

def saveEventdetails(event):
    file1 = pathlib.Path('events.data')
    if file1.exists():
        infile = open('events.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(event)
        infile.close()
        os.remove('events.data')
    else:
        oldlist = [event]
    outfile = open('tempevents.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('tempevents.data', 'events.data')

def getEventDetails():
    file1 = pathlib.Path('events.data')
    if file1.exists():
        infile = open('events.data','rb')
        eventdetails = pickle.load(infile)
        print('---------Event Details-------')
        print('E-Name  E-Code   E-Total Seats')
        for event in eventdetails:
            print(event.eventname,'\t',event.eventcode,'\t',event.totalavailableseat)
        infile.close()
        print('-----------------------------')
        input('press enter to main menu')
    else:
        print('no events record is found')

def geteventSummary():
    filetickets = pathlib.Path('tickets.data')
    if filetickets.exists():
        infiletickets = open('tickets.data','rb')
        ticketdetails = pickle.load(infiletickets)
    
    fileEvents = pathlib.Path('events.data')
    if fileEvents.exists():
        infileEvents = open('events.data','rb')
        eventdetails = pickle.load(infileEvents)

        print('---------REPORTS---------')
        for event in eventdetails:
            print('\n\n Event name: '+ event.eventname + '|Total seats: '+ event.totalavailableseat)
            for ticket in ticketdetails:
                if event.eventcode ==ticket.event:
                    print(ticket.reference,'\t',ticket.name,'\t',ticket.email)

        infileEvents.close()
        infiletickets.close()

        print('--------------------')
        input('press enter to main menu')
    else:
        print('no events records found')


ch = ''
num = 0
while True:
    print('\t\t\t\t*************')
    print('\t\t\t\tEVENT MANAGEMENT SYSTEM')
    print('\t\t\t\t*************')
    print('\tMAIN MENU')
    print('\t1. BOOK TICKET')
    print('\t2.VIEW TICKET')
    print('\t3. CREATE EVENT')
    print('\t4. VIEW EVENTS')
    print('\tSelect your option please(1-5)')
    ch = input()


    if ch == '1':
        bookeventticket()
    elif ch =='2':
        getticketdetails()
    elif ch =='3':
        createevent()
    elif ch=='4':
        getEventDetails()
    elif ch =='5':
        geteventSummary()











