class NailServices:
    def _init_(self):
        self.services = {
            'Manicure': 25,
            'Pedicure': 35,
            'Nail Art': 45
        }

    def list_services(self):
        return self.services

    def get_price(self, service_name):
        return self.services.get(service_name, "Service not found")