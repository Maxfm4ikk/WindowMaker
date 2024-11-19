# WindowMaker 5.0 Most Modern and Stable Version, Open-Source. Description in Russian.

import tkinter as tk
from tkinter import filedialog, messagebox
import ctypes
import subprocess
import time
import threading
import os
import winreg

# Локализация
translations = {
    "ru": {
        "title": "Создание системных окон",
        "num_windows_label": "Количество окон:",
        "title_label": "Заголовки окон (через запятую):",
        "text_label": "Тексты сообщений (через запятую):",
        "icon_label": "Типы иконок (info, warning, error, через запятую):",
        "delay_label": "Задержки перед запуском программы (в секундах, через запятую):",
        "button_type_label": "Тип кнопок (ok, okcancel, yesno):",
        "program_name_label": "Введите имя программы (или выберите файл):",
        "choose_program_button": "Выбрать программу",
        "create_button": "Создать системные окна",
        "open_scenarios_button": "Открыть меню сценариев",
        "switch_to_english": "Переключиться на английский",
        "scenario_window_title": "Меню сценариев",
        "scenario_title_label": "Заголовок:",
        "scenario_text_label": "Текст сообщения:",
        "scenario_icon_label": "Тип иконки (info, warning, error):",
        "scenario_button_type_label": "Тип кнопок (ok, okcancel, yesno):",
        "add_scenario_button": "Добавить сценарий",
        "run_scenarios_button": "Запустить сценарии"
    },
    "en": {
        "title": "Create System Windows",
        "num_windows_label": "Number of windows:",
        "title_label": "Window titles (comma-separated):",
        "text_label": "Message texts (comma-separated):",
        "icon_label": "Icon types (info, warning, error, comma-separated):",
        "delay_label": "Delays before launching programs (in seconds, comma-separated):",
        "button_type_label": "Button type (ok, okcancel, yesno):",
        "program_name_label": "Enter program name (or choose file):",
        "choose_program_button": "Choose program",
        "create_button": "Create system windows",
        "open_scenarios_button": "Open scenario menu",
        "switch_to_english": "Switch to English",
        "scenario_window_title": "Scenario Menu",
        "scenario_title_label": "Title:",
        "scenario_text_label": "Message text:",
        "scenario_icon_label": "Icon type (info, warning, error):",
        "scenario_button_type_label": "Button type (ok, okcancel, yesno):",
        "add_scenario_button": "Add scenario",
        "run_scenarios_button": "Run scenarios"
    }
}

# Устанавливаем язык по умолчанию
current_lang = "ru"

# Сохранение текущей локализации
def save_language_setting():
    with open('settings.txt', 'w') as f:
        f.write(current_lang)

# Загрузка языка из файла
def load_language_setting():
    global current_lang
    if os.path.exists('settings.txt'):
        with open('settings.txt', 'r') as f:
            lang = f.read().strip()
            if lang in translations:
                current_lang = lang

# Определение темы Windows
def get_windows_theme():
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        return "light" if value == 1 else "dark"
    except Exception:
        return "light"

# Установка темы
def apply_theme():
    current_theme = get_windows_theme()
    bg_color = "black" if current_theme == "dark" else "white"
    fg_color = "white" if current_theme == "dark" else "black"
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Label, tk.Button)):
            widget.config(bg=bg_color, fg=fg_color)

# Переключение языка
def switch_language():
    global current_lang
    current_lang = "en" if current_lang == "ru" else "ru"
    update_texts()
    save_language_setting()

# Обновление текстов
def update_texts():
    root.title(translations[current_lang]["title"])
    num_windows_label.config(text=translations[current_lang]["num_windows_label"])
    title_label.config(text=translations[current_lang]["title_label"])
    text_label.config(text=translations[current_lang]["text_label"])
    icon_label.config(text=translations[current_lang]["icon_label"])
    delay_label.config(text=translations[current_lang]["delay_label"])
    button_type_label.config(text=translations[current_lang]["button_type_label"])
    program_name_label.config(text=translations[current_lang]["program_name_label"])
    choose_program_button.config(text=translations[current_lang]["choose_program_button"])
    create_button.config(text=translations[current_lang]["create_button"])
    open_scenarios_button.config(text=translations[current_lang]["open_scenarios_button"])
    switch_language_button.config(text=translations[current_lang]["switch_to_english"])
    apply_theme()

# Основные функции программы: генерация окон, сценарии, запуск программ и другие
# ...

# Основное окно
root = tk.Tk()
load_language_setting()  # Загрузка языка
apply_theme()  # Установка темы
root.title(translations[current_lang]["title"])

# Интерфейс
num_windows_label = tk.Label(root, text=translations[current_lang]["num_windows_label"])
num_windows_label.pack()

num_windows_entry = tk.Entry(root)
num_windows_entry.pack()

title_label = tk.Label(root, text=translations[current_lang]["title_label"])
title_label.pack()

title_entry = tk.Entry(root)
title_entry.pack()

text_label = tk.Label(root, text=translations[current_lang]["text_label"])
text_label.pack()

text_entry = tk.Entry(root)
text_entry.pack()

icon_label = tk.Label(root, text=translations[current_lang]["icon_label"])
icon_label.pack()

icon_entry = tk.Entry(root)
icon_entry.pack()

delay_label = tk.Label(root, text=translations[current_lang]["delay_label"])
delay_label.pack()

delay_entry = tk.Entry(root)
delay_entry.pack()

button_type_label = tk.Label(root, text=translations[current_lang]["button_type_label"])
button_type_label.pack()

button_type_entry = tk.Entry(root)
button_type_entry.pack()

program_name_label = tk.Label(root, text=translations[current_lang]["program_name_label"])
program_name_label.pack()

program_name_entry = tk.Entry(root)
program_name_entry.pack()

choose_program_button = tk.Button(root, text=translations[current_lang]["choose_program_button"], command=lambda: ...)
choose_program_button.pack()

create_button = tk.Button(root, text=translations[current_lang]["create_button"], command=lambda: ...)
create_button.pack()

open_scenarios_button = tk.Button(root, text=translations[current_lang]["open_scenarios_button"], command=lambda: ...)
open_scenarios_button.pack()

switch_language_button = tk.Button(root, text=translations[current_lang]["switch_to_english"], command=switch_language)
switch_language_button.pack()

# Финализация интерфейса
update_texts()
root.mainloop()
