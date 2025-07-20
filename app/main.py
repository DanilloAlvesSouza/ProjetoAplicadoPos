# main.py
import json
import os
from handler import handler

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    payload_path = os.path.join(current_dir, "mock_payload.json")
    with open(payload_path) as f:
        evento = json.load(f)
        resultado = handler(evento, None)
        print(resultado)
