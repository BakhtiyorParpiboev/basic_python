'''unittest lesson 1'''
def phone_model(model,brand,price=None):
    if price:
        return f"{brand.capitalize()} {model.lower()} is ${price}"
    else:
        return f"{brand.title()}: {model}"
    
n = phone_model('iphone 15 pro max','apple',1499)
print(n)