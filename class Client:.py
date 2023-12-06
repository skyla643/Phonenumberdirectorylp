class Client:
    def __init__(self, name, company, phone_number, feedback):
        self.name = name
        self.company = company
        self.phone_number = phone_number
        self.feedback = feedback

class PhoneLookupDatabase:
    def __init__(self):
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)

    def lookup_by_phone_number(self, phone_number):
        for client in self.clients:
            if client.phone_number == phone_number:
                return client
        return None
    def display(self,):
        for client in self.clients:
            print(client)

# Create instances of clients
client1 = Client("Richard Anderson", "Tech Innovators", "(555) 123-4567", "Excellent for vetting clients.")
client2 = Client("Angela Roberts", "Global Solutions", "(555) 234-5678", "Essential tool for business.")
client3 = Client("Jonathan Carter", "Future Enterprises", "(555) 345-6789", "Helpful in identifying contacts.")

# Create a Phone Lookup Database
phone_lookup_db = PhoneLookupDatabase()

# Add clients to the database
phone_lookup_db.add_client(client1)
phone_lookup_db.add_client(client2)
phone_lookup_db.add_client(client3)

# Simulate a phone number lookup
lookup_number = "(555) 123-4567"
found_client = phone_lookup_db.lookup_by_phone_number(lookup_number)

# Display the result
if found_client:
    print(f"Client found: {found_client.name} from {found_client.company}")
    print(f"Feedback: {found_client.feedback}")
else:
    print(f"No client found for phone number: {lookup_number}")
print('diplay')
phone_lookup_db.display()