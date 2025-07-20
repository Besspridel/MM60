import json

# Загружаем текущий файл
with open("materials.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# Создаем новый словарь с нужной структурой
code_to_name = raw_data
name_to_code = {v: k for k, v in raw_data.items()}

structured_data = {
    "code_to_name": code_to_name,
    "name_to_code": name_to_code
}

# Сохраняем обратно
with open("materials.json", "w", encoding="utf-8") as f:
    json.dump(structured_data, f, ensure_ascii=False, indent=2)

print("✅ JSON файл успешно преобразован.")