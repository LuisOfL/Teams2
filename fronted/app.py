import flet as ft
import requests

API_URL = "http://127.0.0.1:8000"

def main(page: ft.Page):
    page.title = "Mini Teams"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    # Estado de la app
    current_channel_id = "general"
    current_user = "Luis"

    # Componentes UI
    channel_list = ft.ListView(expand=True, spacing=5)
    messages_list = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    msg_input = ft.TextField(hint_text="Escribe un mensaje...", expand=True, shift_enter=True)
    channel_title = ft.Text("Selecciona un canal", size=18, weight=ft.FontWeight.BOLD)

    def load_channels():
        try:
            res = requests.get(f"{API_URL}/channels")
            if res.status_code == 200:
                channel_list.controls.clear()
                channels = res.json()
                for ch in channels:
                    channel_list.controls.append(
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.HASHTAG, size=18),
                            title=ft.Text(ch["name"]),
                            data=ch["id"],
                            on_click=lambda e: select_channel(e.control.data, e.control.title.value)
                        )
                    )
                page.update()
        except Exception as ex:
            print(f"Error cargando canales: {ex}")

    def load_messages(channel_id):
        try:
            res = requests.get(f"{API_URL}/channels/{channel_id}/messages")
            if res.status_code == 200:
                messages_list.controls.clear()
                for msg in res.json():
                    messages_list.controls.append(
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(msg["user"], weight=ft.FontWeight.BOLD, size=12, color=ft.Colors.BLUE_200),
                                    ft.Text(msg["content"], size=14)
                                ],
                                spacing=2
                            ),
                            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                            padding=10,
                            border_radius=8
                        )
                    )
                page.update()
        except Exception as ex:
            print(f"Error cargando mensajes: {ex}")

    def select_channel(ch_id, ch_name):
        nonlocal current_channel_id
        current_channel_id = ch_id
        channel_title.value = f"# {ch_name}"
        load_messages(ch_id)

    def send_message(e):
        if not msg_input.value.strip():
            return
        payload = {"user": current_user, "content": msg_input.value.strip()}
        try:
            res = requests.post(f"{API_URL}/channels/{current_channel_id}/messages", json=payload)
            if res.status_code == 200:
                msg_input.value = ""
                load_messages(current_channel_id)
        except Exception as ex:
            print(f"Error enviando mensaje: {ex}")

    # UI Layout
    sidebar = ft.Container(
        width=240,
        bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
        padding=10,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.GROUPS, color=ft.Colors.PRIMARY),
                        ft.Text("Canales", size=20, weight=ft.FontWeight.BOLD)
                    ]
                ),
                ft.Divider(),
                channel_list
            ]
        )
    )

    chat_area = ft.Container(
        expand=True,
        padding=15,
        bgcolor=ft.Colors.SURFACE,
        content=ft.Column(
            controls=[
                channel_title,
                ft.Divider(),
                messages_list,
                ft.Row(
                    controls=[
                        msg_input,
                        ft.IconButton(
                            icon=ft.Icons.SEND,
                            icon_color=ft.Colors.PRIMARY,
                            on_click=send_message
                        )
                    ]
                )
            ]
        )
    )

    page.add(
        ft.Row(
            controls=[sidebar, chat_area],
            expand=True,
            spacing=0
        )
    )

    # Carga inicial
    load_channels()
    select_channel("general", "General")

ft.app(target=main)
    page.add(
        ft.Row(
            controls=[sidebar, chat_area],
            expand=True,
            spacing=0
        )
    )

    # Carga inicial
    load_channels()
    select_channel("general", "General")

ft.app(target=main)