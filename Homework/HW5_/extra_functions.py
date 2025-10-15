
def midpoint(point):
    """
    Computes the midpoint between point and 0

    Args:
        point (int): point to which we wish to compute the half distance with 0
    
    Return:
        float: the midpoint between point and 0
    """
    return point / 2

def europe_us(sqm_to_sqft, euro_buy, euro_rent):
    """
    Converts square meters to square feet and euros to dollars.
    
    Args:
		sqm_to_sqft (float): square meters that need to be converted to square feet
        euroToDollars (float): amount in Euros that will be converted to US Dollars
    Return:
		tuple (float, float): tuple containing converted square feet and US dollars
    """

    euroDollarConversion = 1.08 #conversion rate eur to usd

    space_in_sqft = sqm_to_sqft * 10.7639
    buy_price_in_dollar = euroDollarConversion * euro_buy
    rent_price_in_dollar = euroDollarConversion * euro_rent

    return space_in_sqft, buy_price_in_dollar, rent_price_in_dollar
     
           


#This code will only run if extra_functions.py is executed as the main Python script
if __name__ == "__main__":
    # print(midpoint(10))
    # print(midpoint(15))
    # print(midpoint(-10))
    # print(midpoint(-15))

    print(europe_us(10, 25, 20))