from dotenv import load_dotenv
import os

load_dotenv()

nama_depan = os.getenv("VARIABLE_DEPAN")
nama_belakang = os.getenv("VARIABLE_BELAKANG")

print("VARIABLE_DEPAN: ", nama_depan)
print("VARIABLE_BELAKANG: ", nama_belakang)

