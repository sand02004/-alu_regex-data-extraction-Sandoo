import re

def validate_email(email):
    # Define the regex pattern for a valid email
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return "Email format is correct"
    else:
        return "Email format is incorrect"
    
enter_email=input('enter your email: ')

print(validate_email(enter_email))

def validate_phone(phone):
    contact = re.compile(r'\(?\d{3}\)?[ -.]\d{3}[.-]\d{4}')

    if re.match(contact, phone):
        return "Phone number format is correct"
    else:
        return "Phone number format is incorrect"
    
contacts =input("enter your contact: ")

    
print(validate_phone(contacts))


def validate_url(url):

    pattern =r'https?://(www\.)?[a-z._-]+\.[a-z_-]{2,}'

    if re.match(pattern,url):
        return "the url format is correct"
    else:
        return "The url format is incorrect"
    
link =input("enter your url ")
    
print(validate_url(link))

def validate_currency_amount(currency_amount):
    pattern = re.compile(r'\$\d{1,3}(,?\d{3})*(.?\d{2})?')

    if re.match(pattern, currency_amount):
        return "Currency amount format is correct"
    else:
        return "Currency amount format is incorrect"
    
amount =input('enter your amount: ')
    
print(validate_currency_amount(amount))

def validate_Hashtags(Hashtags):
    pattern =r'^#[a-zA-Z0-9]+$'

    if re.match(pattern, Hashtags):
        return f"hashtag is correct"
    else:
        return f"hashtags is not correct"
my_hashtag =input("enter your hashtag: ")

   
print(validate_Hashtags(my_hashtag))
