firstName = "Teja"
lastName = "Dandu"
fullName = f"{firstName} {lastName}"  # The f-strings where f is for format
print(fullName)
print(f"Hello, {fullName.title()}!")


message = f"Hello, {fullName.title()}!"  # Assigning the message to variable
print(message)

fullName = "{} {}".format(firstName, lastName)  # To use format()
print(fullName)


print("Python")
print("\tPython")  # To add a tab use \t
print("\nPython")  # To add a newline string \n
print("Languages:\nPython\nJavascipt\nC")  # Combinations of a newline

# Striping Whitespace

favoriteLanguage = "Python "
print(favoriteLanguage)
favoriteLanguage = (
    favoriteLanguage.rstrip()
)  # To ensure that no whitespace exists at the right end of the string. use rstrip() method
print(favoriteLanguage)


favoriteLanguage = "  Python  "
favoriteLanguage = favoriteLanguage.rstrip()
print(favoriteLanguage)
favoriteLanguage = (
    favoriteLanguage.lstrip()
)  # To lstrip() method ensures that no whitespace exists at the left end of the string
print(favoriteLanguage)
favoriteLanguage = (
    favoriteLanguage.strip()
)  # strip() method removes the both leftend and right end of the string
print(favoriteLanguage)
