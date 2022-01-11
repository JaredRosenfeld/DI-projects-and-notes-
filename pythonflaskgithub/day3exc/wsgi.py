import random
from app import app
import string

alphabet = string.ascii_letters
secret1 = ''
for i in range(256):
    secret1 += random.choice(alphabet)
app.config['SECRET_KEY'] = secret1

if __name__ == "__main__":         # Protect this code to be ran if he is imported
    app.run(port=5000, debug=True)