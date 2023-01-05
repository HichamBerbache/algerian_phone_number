class AlgerianPhoneNumber:
    def __init__(self, number):
        self.number = number 
 
    def is_valid(self):
        return len(self.number) == 12 and self.number[:3] == '+213'
 
    def get_international_indicator(self):
        return '+213' if self.number[0] == '0' else '00213'
