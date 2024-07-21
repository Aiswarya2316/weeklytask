class Appointments:
    def _init_(self):
        self.appointments = []

    def book_appointment(self, customer_name, service, time):
        self.appointments.append({
            'customer_name': customer_name,
            'service': service,
            'time': time
        })

    def list_appointments(self):
        return self.appointments