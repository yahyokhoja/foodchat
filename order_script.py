# order_script.py

import json

order_data = {
    "phone_number": "+992929281129",
    "items": [
        {"dish": "Pizza", "quantity": 1},
        {"dish": "Shashlik", "quantity": 2}
    ],
    "total_price": 20.0,
    "status": "pending"
}

# Преобразование данных в JSON
order_json = json.dumps(order_data, ensure_ascii=False, indent=4)
print(order_json)
