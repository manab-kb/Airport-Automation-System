from dataclasses import dataclass

"""
Decorator object, defined to specify the types of each of the parameters that will be stored in the database, whilst
creating, editing and saving entries of the details of each data object. 
"""

@dataclass
class Ticket:
    idTicket: str
    passengerName: str
    createdAt: str
    idFlight: str
