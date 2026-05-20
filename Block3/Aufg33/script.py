import os

if os.path.exists('data.txt'):
    with open('data.txt', 'r') as f:
        print(f"Gelesen aus Datei: {f.read()}")
else:
    print("Datei nicht gefunden!")