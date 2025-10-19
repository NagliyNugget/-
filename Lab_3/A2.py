import string

password = input('Введите пароль: ')
isValid = True
allowed_sym = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
errors = ""
if len(password) != 8:
    errors = errors + 'Длина пароля не равна 8 \n'
    isValid = False
if password.lower() == password:
    errors = errors + 'В пароле отсутствуют заглавные буквы \n'
    isValid = False
if password.upper() == password:
    errors = errors + 'В пароле отсутствуют строчные буквы \n'
    isValid = False
if not any(symbol.isdigit() for symbol in password):
    errors = errors + 'В пароле отсутствуют цифры \n'
    isValid = False
if ('*' not in password) and ('-' not in password) and ('#' not in password):
    errors = errors + 'В пароле отсутствуют специальные символы \n'
    isValid = False
if (set(password) - set(allowed_sym)) != set():
    errors = errors + 'В пароле используются непредусмотренные символы \n'
    isValid = False
if isValid == True:
    print("Надежный пароль")
else:
    print("Пароль не надежный \n")
    print(errors)
