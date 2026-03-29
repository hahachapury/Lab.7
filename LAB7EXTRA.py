import io
import tkinter as tk
from PIL import Image, ImageTk
import requests

def get_cat():
    Cat_URL = 'https://cataas.com/cat'
    params = {
        'json': True
    }
    try:
        response = requests.get(Cat_URL, params=params)
        print("Статус JSON-запроса:", response.status_code)
        if response.status_code != 200:
            print("Ошибка при запросе JSON")
            return None
        data = response.json()
        print("Полный URL картинки:", data['url'])
    except Exception as e:
        print("Ошибка получения URL:", e)
        return None

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        img_resp = requests.get(data['url'], headers=headers, timeout=10)
        print("Статус загрузки картинки:", img_resp.status_code)
        if img_resp.status_code != 200:
            print("Не удалось загрузить картинку")
            return None
        image = Image.open(io.BytesIO(img_resp.content))
        print("Размер изображения (ширина x высота):", image.size)
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)
        return photo
    except Exception as e:
        print("Ошибка при обработке изображения:", e)
        return None

def show_cat():
    photo = get_cat()
    if photo:
        label.config(image=photo)
        label.image = photo
    else:
        label.config(text="Не удалось загрузить кота", image="")

# wndw
root = tk.Tk()
root.title("Cat")
root.geometry("800x600")

# png bg
canvas = tk.Canvas(root, width=500, height=600, bg='light blue')
canvas.pack(fill="both", expand=True)

# generate button
button = tk.Button(root, text="GENERATE CAT",font=("Arial", 16), command=show_cat, bg="blue")
canvas.create_window(350, 100, window=button)

# output
cat_label = tk.Label(root)
canvas.create_window(350, 180, window=cat_label)


label = tk.Label(root)
label.pack(pady=10, expand=True)

root.mainloop()
