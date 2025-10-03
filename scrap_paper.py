class Apartment:
    """
     Awesome DocString goes here
     """

    num_apt_visited = 0

    def __init__(self, rent, sqft, num_rooms, num_bathrooms, apt_num):
        self.rent = rent
        self.sqft = sqft
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.apt_num = apt_num
        Apartment.num_apt_visited += 1
    def pricePerSqft(self):
        return self.rent / self.sqft
    def betterDeal(self, other):
        if self.pricePerSqft() > other.pricePerSqft():
            return other
        else:
            return self
    def __str__(self):
        return "Apt. num: " + str(self.apt_num) + " Rent: " \
                + str(self.rent) + " Sqft:" + str(self.sqft)

apt1 = Apartment(2000, 870, 2, 1, 1323)
apt2 = Apartment(1980, 790, 1, 1, 1325)
apt3 = Apartment(2100, 770, 2, 1, 1120)
apt4 = Apartment(2000, 870, 2, 1, 1123)
apt5 = Apartment(2150, 970, 2, 2, 923)

print(apt1)
# print(apt2)
# print(apt3)
# print(apt4)
# print(apt5)

print(apt1.betterDeal(apt5))
# print(apt2.pricePerSqft())