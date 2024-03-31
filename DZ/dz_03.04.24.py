import re
password_pattern = re.compile(r"^[a-zA-Z0-9-_@]{6,18}$")
password = "my-p@ssword"

if re.match(password_pattern, password):
    print("Пароль соответствует критериям.")
else:
    print("Пароль не соответствует критериям.")
