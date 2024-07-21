class HairServices:
    def _init_(self):
        self.services = {
            'Haircut': 20,
            'Hair Coloring': 50,
            'Hair Treatment': 70
        }

    def list_services(self):
        return self.services

    def get_price(self, service_name):
        return self.services.get(service_name, "Service not found")