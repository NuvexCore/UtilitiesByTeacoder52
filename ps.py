#reading files in declarated path and folders inside and searching part of text
import os
import json

TARGET_NAME = "§l§5Jujutsu Awakening §7| §bTriple §dTrouble §mUpdate §e1.85 §7| §rAddon BP"

SEARCH_PATH = r"C:\Users\Ignat\AppData"

VALID_EXTENSIONS = [
    ".json",
    ".ldb",
    ".txt"
]

found = False

for root, dirs, files in os.walk(SEARCH_PATH):
    for file in files:
        file_path = os.path.join(root, file)

        # Проверяем только нужные расширения
        if not any(file.lower().endswith(ext) for ext in VALID_EXTENSIONS):
            continue

        try:
            # Читаем файл как текст
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Быстрая проверка
            if TARGET_NAME not in content:
                continue

            # Пытаемся найти manifest.json структуру
            if '"header"' in content and '"name"' in content:
                print("=" * 80)
                print(f"[FOUND] {file_path}")
                print("=" * 80)

                # Выводим кусок текста вокруг найденного имени
                index = content.find(TARGET_NAME)

                start = max(0, index - 500)
                end = min(len(content), index + 500)

                print(content[start:end])
                print("\n")

                found = True

        except Exception as e:
            # Некоторые файлы могут быть заняты Minecraft'ом
            print(f"[SKIP] {file_path} -> {e}")

if not found:
    print("Ничего не найдено.")
