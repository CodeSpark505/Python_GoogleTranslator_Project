import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from datetime import datetime

# Dictionary mapping language codes to full names
language_names = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "zh-cn": "Chinese (Simplified)",
    "ru": "Russian",
    "ur":"Urdu"
    # Add more languages as needed
}

translation_history = []

def translate_text():
    text_to_translate = source_text.get("1.0", tk.END).strip()
    source_language = source_language_combobox.get()
    target_language = target_language_combobox.get()

    translator = Translator()
    translated_text = translator.translate(text_to_translate, src=source_language, dest=target_language).text

    translated_text_display.delete("1.0", tk.END)
    translated_text_display.insert(tk.END, translated_text)

    translation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    translation_history.append((translation_time, text_to_translate, language_names.get(source_language, source_language), language_names.get(target_language, target_language), translated_text))
    

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Translation History")

    # Create a table to display the history
    table = ttk.Treeview(history_window, columns=("Time", "Text", "Source Language", "Target Language", "Translated Text"), show="headings")
    table.heading("Time", text="Time")
    table.heading("Text", text="Text")
    table.heading("Source Language", text="Source Language")
    table.heading("Target Language", text="Target Language")
    table.heading("Translated Text", text="Translated Text")

    # Add data to the table
    for translation in translation_history:
        table.insert("", "end", values=translation)

    table.pack(expand=True, fill="both")

# Create the main window
root = tk.Tk()
root.title("Google Translate")

# Source text input
source_text_label = ttk.Label(root, text="Enter Text to Translate:")
source_text_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
source_text = tk.Text(root, height=5, width=50)
source_text.grid(row=1, column=0, padx=5, pady=5)

# Source language selection
source_language_label = ttk.Label(root, text="Source Language:")
source_language_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
source_language_combobox = ttk.Combobox(root, values=list(language_names.values()))
source_language_combobox.grid(row=3, column=0, padx=5, pady=5)

# Target language selection
target_language_label = ttk.Label(root, text="Target Language:")
target_language_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
target_language_combobox = ttk.Combobox(root, values=list(language_names.values()))
target_language_combobox.grid(row=5, column=0, padx=5, pady=5)

# Translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=6, column=0, padx=5, pady=5)

# History button
history_button = ttk.Button(root, text="History", command=show_history)
history_button.grid(row=0, column=1, padx=5, pady=5)

# Translated text display
translated_text_label = ttk.Label(root, text="Translated Text:")
translated_text_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
translated_text_display = tk.Text(root, height=5, width=50)
translated_text_display.grid(row=8, column=0, padx=5, pady=5)

root.mainloop()
