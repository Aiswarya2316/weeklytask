class SkinServices:
    def _init_(self):
        self.services = {
            'Facial': 30,
            'Microdermabrasion': 60,
            'Chemical Peel': 80
        }

    def list_services(self):
        return self.services

    def get_price(self, service_name):
        return self.services.get(service_name, "Service not found")