# This is a sample Python script.

class User:
    def __init__(self, ism, familya, t_yili, email_adres):
        self.ism = ism
        self.familya = familya
        self.t_yili = t_yili
        self.email_adres = email_adres
    def get_info(self):
        return f"{self.ism} {self.familya} {self.t_yili} {self.email_adres}"

    def e_mail(self):
        return f" {self.email_adres}"
user1 = User("Diyorbek", "Ashiraliyev", 2017, "diyorbek@gmail.com")
print(user1.get_info())
print(user1.e_mail())
