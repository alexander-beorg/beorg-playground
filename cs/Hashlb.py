import hashlib


database_rows = [
    {'name': 'Наталья', 'email': 'nata123@mail.ru', 'ip': '127.0.0.1'},
    {'name': 'Наталья', 'email': 'nata@mail.ru', 'ip': '122.0.0.1'},
    {'name': 'Михаил', 'email': 'mikha@yandex.ru', 'ip': '127.0.0.1'},
]

database_sha = [
    {'name': 'Наталья', 'email': 'nata123@mail.ru', 'ip': '127.0.0.1'},
    {'name': 'Наталья', 'email': 'nata@mail.ru', 'ip': '122.0.0.1'},
    {'name': 'Михаил', 'email': 'mikha@yandex.ru', 'ip': '127.0.0.1'},
]


if __name__ == "__main__":

    for b in database_sha:
        b['name'] = hashlib.sha256("{}".format(b['name']).encode()).hexdigest()
        b['email'] = hashlib.sha256("{}".format(b['email']).encode()).hexdigest()
        b['ip'] = hashlib.sha256("{}".format(b['ip']).encode()).hexdigest()

    print(database_rows)
    print(database_sha)

    print("\n")

    print("#####"*17)
    print(database_sha[0]["name"], database_rows[0]["name"], database_sha[0]["name"] == hashlib.sha256("{}".format(database_rows[0]["name"]).encode()).hexdigest())
    print(database_sha[0]["email"], database_rows[0]["email"], database_sha[0]["email"] == hashlib.sha256("{}".format(database_rows[0]["email"]).encode()).hexdigest())
    print(database_sha[0]["ip"], database_rows[0]["ip"], database_sha[0]["ip"] == hashlib.sha256("{}".format(database_rows[0]["ip"]).encode()).hexdigest())
    print("*****"*17)
    print(database_sha[1]["name"], database_rows[1]["name"], database_sha[1]["name"] == hashlib.sha256("{}".format(database_rows[1]["name"]).encode()).hexdigest())
    print(database_sha[1]["email"], database_rows[1]["email"], database_sha[1]["email"] == hashlib.sha256("{}".format(database_rows[1]["email"]).encode()).hexdigest())
    print(database_sha[1]["ip"], database_rows[1]["ip"], database_sha[1]["ip"] == hashlib.sha256("{}".format(database_rows[1]["ip"]).encode()).hexdigest())
    print("*****"*17)
    print(database_sha[2]["name"], database_rows[2]["name"], database_sha[2]["name"] == hashlib.sha256("{}".format(database_rows[2]["name"]).encode()).hexdigest())
    print(database_sha[2]["email"], database_rows[2]["email"], database_sha[2]["email"] == hashlib.sha256("{}".format(database_rows[2]["email"]).encode()).hexdigest())
    print(database_sha[2]["ip"], database_rows[2]["ip"], database_sha[2]["ip"] == hashlib.sha256("{}".format(database_rows[2]["ip"]).encode()).hexdigest())
    print("#####"*17)

    # print(database_sha[1]["name"], database_rows[1]["name"], database_sha[1]["name"] == hashlib.sha256("{}".format(database_rows[1]["name"]).encode()).hexdigest())
    # print(database_sha[0]["name"], database_rows[0]["name"], database_sha[0]["name"] == hashlib.sha256("{}".format(str(input())).encode()).hexdigest())

    # b = 1
    # while b == 1:
    #     t = database_sha[0]["name"]
    #     print(f'{t}')
    #     d = hashlib.sha256("{}".format(str(input())).encode()).hexdigest()
    #     if t == d:
    #         print('True')
    #         b = 0
    #     else:
    #         print('False')

    # nn = "password"
    # h = hashlib.md5("{}".format(nn).encode())
    # p = h.hexdigest()
    # print(p)    # Пароль, сохраненный в базе #'5f4dcc3b5aa765d61d8327deb882cf99'
    # h2 = hashlib.md5(b"password")   # Пароль, введенный пользователем
    # if p == h2.hexdigest(): print("Пароль правильный")

