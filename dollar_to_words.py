from num2words import num2words
##Ganesh created from desktop on 08/03/2025..

def dollar_to_words(amount):
    try:
        amount = int(amount)
        words = num2words(amount, to='cardinal', lang='en')
        words = words.replace('-', ' ')
        words = words.replace(' and', ' and')
        words = words.capitalize()
        return words
    except ValueError:
        return "Invalid input. Please enter a valid dollar amount."

if __name__ == "__main__":
    dollar_input = input("Enter dollar amount (e.g., 1234): $")
    print(dollar_to_words(dollar_input))
