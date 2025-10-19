import string

password = input('Введите пароль: ')
isValid = True
allowed_sym = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
errors = ""
if len(password) != 8:
    errors = errors + 'Длина пароля не равна 8 \n'
    isValid = False
if isValid == True:
    print("Надежный пароль")
else:
    print("Пароль не надежный \n")
    print(errors)