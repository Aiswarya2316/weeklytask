class Billing:
    def _init_(self):
        self.bills = []

    def generate_bill(self, customer_name, service_name, amount):
        bill = {
            'customer_name': customer_name,
            'service_name': service_name,
            'amount': amount
        }
        self.bills.append(bill)
        return bill

    def list_bills(self):
        return self.bills