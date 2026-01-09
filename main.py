import flet as ft
from datetime import datetime
def main(page: ft.Page):
    page.title = "Мое первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value='Hello Dolka')


    def text_name(_):
        name = name_input.value.strip()

        if name:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            text_hello.color = None
            text_hello.value = f"{current_time}-Привет, {name}!"
            name_input.value = None
        else:
            text_hello.value = "Введите имя!"
            text_hello.color = ft.Colors.RED
        page.update()
        
        

    elevated_button = ft.ElevatedButton ('send', on_click=text_name, icon=ft.Icons.SEND, color=ft.Colors.RED, icon_color=ft.Colors.BLACK)
    
    name_input = ft.TextField(label='Введите что-то', on_submit=text_name)

    def thememode(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK

    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)
    

    page.add(text_hello, name_input, elevated_button, thememode_button)

ft.app(target=main) 