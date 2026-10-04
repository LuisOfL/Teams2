import flet as ft

def create_left_nav(on_chat_click, on_call_click):
    return ft.Container(
        content=ft.Column([
            ft.IconButton(icon=ft.Icons.CHAT, icon_color=ft.Colors.INDIGO_300, tooltip="Chat", on_click=on_chat_click),
            ft.IconButton(icon=ft.Icons.PEOPLE, icon_color=ft.Colors.WHITE70, tooltip="Equipos"),
            ft.IconButton(icon=ft.Icons.CALENDAR_MONTH, icon_color=ft.Colors.WHITE70, tooltip="Calendario"),
            ft.IconButton(icon=ft.Icons.PHONE, icon_color=ft.Colors.WHITE70, tooltip="Llamadas", on_click=on_call_click),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
        width=65,
        bgcolor="#181818"
    )