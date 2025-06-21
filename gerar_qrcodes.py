import qrcode
import pandas as pd
import os

# Lê o arquivo Excel
df = pd.read_excel("usuarios.xlsx")

# Cria a pasta se não existir
os.makedirs("qrcodes", exist_ok=True)

# Gera QRCodes
for _, row in df.iterrows():
    user_id = row["id"]
    url = f"http://localhost:5000/usuario/{user_id}"
    qr = qrcode.make(url)
    qr.save(f"qrcodes/usuario_{user_id}.png")

print("QRCodes gerados com base no Excel!")
