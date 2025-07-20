import pandas as pd
import json

# Загружаем Excel-файл
df = pd.read_excel('materials.XLS')  # Убедись, что файл так называется

# Покажем первые строки, чтобы убедиться в структуре
print("📄 Предварительный просмотр таблицы:")
print(df.head())

# Выбираем нужные столбцы — предположим, что:
# - первый столбец — коды
# - второй — названия
df = df.iloc[:, [0, 1]]
df.columns = ['code', 'name']

# Удаляем пустые строки
df = df.dropna()

# Создаём словарь {код: название}
materials = {str(row['code']).strip(): str(row['name']).strip() for _, row in df.iterrows()}

# Сохраняем в JSON
with open('materials.json', 'w', encoding='utf-8') as f:
    json.dump(materials, f, ensure_ascii=False, indent=2)

print('✅ Успешно! materials.json создан.')