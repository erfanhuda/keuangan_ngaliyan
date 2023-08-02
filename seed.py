from auth import DB_SESSION as session, Auth
from pathlib import Path
from model.model import Person, User, Role
import random
import datetime
from cryptography.fernet import Fernet

# with open(Path(BASE_DIR.parent, "data", "test.csv"), 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     final_reader = {col: [] for col in ["name", "phone"]}

#     for x in reader:
#         p = Person(name=x['name'])
#         session.add(p)
#         session.commit()

def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    id = ''

    for _ in range(0, length, 3):
        id += random.choice(number)
        id += random.choice(alpha)
        id += random.choice(Alpha)

    return id.encode()

def generate_app_token():
    key = Fernet.generate_key()

    return key

def encrypt_password(key, string):
    f = Fernet(key)
    
    return f.encrypt(string)

def decrypt_password(key, string):
    f = Fernet(key)

    return f.decrypt(string)

def expiry_date():
    current_date = datetime.datetime.now()
    timedelta = datetime.timedelta(days=180)

    return current_date + timedelta

def register_admin(username: str) -> None:
    auth_key = random_id(35)
    user = Auth(name=username, auth_key=auth_key, auth_key_expired=expiry_date(), datetime=datetime.datetime.utcnow())

    session.add(User(user=user.name, passw=user.auth_key))
    session.commit()

# superadmin = Auth(name="mandauhitam", auth_key=random_id(20), auth_key_expired=expiry_date(), datetime=datetime.datetime.utcnow())
# session.add(User(user=superadmin.name, passw=superadmin.auth_key))
# session.add(Role(name="keuangan", slug="superadmin"))
# session.add(Person(name="Erfan Huda", user_id=1))
# session.commit()

# print(generate_app_token())
keys = generate_app_token()
encoded = random_id(43)

print(keys.decode())