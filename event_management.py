import mysql.connector

class Event:
    def __init__(self, ID, event_name, seats, location):
        self.ID = ID
        self.event_name = event_name
        self.seats = seats
        self.location = location

class EventDatabase:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="namiq2003123.",
            database="event",
            port=3307
        )
        self.cursor = self.conn.cursor()

    def search_event_by_id(self, ID):
        query = "SELECT * FROM events WHERE ID = %s"
        values = (ID,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            event = Event(result[0], result[1], result[2], result[3])
            return event
        else:
            return None

    def add_event(self, event):
        query = "INSERT INTO events (ID, event_name, seats, location) VALUES (%s, %s, %s, %s)"
        values = (event.ID, event.event_name, event.seats, event.location)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_event(self, ID):
        query = "DELETE FROM events WHERE ID = %s"
        values = (ID,)
        self.cursor.execute(query, values)
        self.conn.commit()

class UserInterface:
    def __init__(self):
        self.event_manager = EventDatabase()

    def search_event(self):
        ID = input("Enter the ID of the event: ")
        event = self.event_manager.search_event_by_id(ID)
        if event:
            print("ID:", event.ID)
            print("Event Name:", event.event_name)
            print("Seats:", event.seats)
            print("Location:", event.location)
        else:
            print("Event not found.")

    def add_event(self):
        ID = input("Enter the ID of the event: ")
        event_name = input("Enter the event name: ")
        seats = input("Enter the number of seats: ")
        location = input("Enter the location: ")
        event = Event(ID, event_name, seats, location)
        self.event_manager.add_event(event)
        print("Event added successfully.")

    def delete_event(self):
        ID = input("Enter the ID of the event to delete: ")
        self.event_manager.delete_event(ID)
        print("Event deleted successfully.")
