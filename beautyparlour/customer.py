class customers:
    def _init_(self):
        self.customers = {}

    def add_customer(self, name, contact):
        self.customers[name] = contact

    def get_customer(self, name):
        return self.customers.get(name, "Customer not found")