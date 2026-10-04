import flet as ft

def create_sidebar(user_name_field, on_connect_click, on_chat_click, on_call_click):
    return ft.Container(
        content=ft.Column([
            ft.Text("Microsoft Teams", weight=ft.FontWeight.BOLD, size=15, color=ft.Colors.WHITE),
            ft.Divider(color=ft.Colors.GREY_800),
            user_name_field,
            ft.ElevatedButton("Conectar al Servidor", on_click=on_connect_click, bgcolor=ft.Colors.INDIGO, color=ft.Colors.WHITE, width=140),
            ft.Divider(color=ft.Colors.GREY_800),
            ft.Text("CANALES", size=11, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_400),
            ft.ListTile(leading=ft.Icon(ft.Icons.TAG, size=18), title=ft.Text("General", size=13), on_click=on_chat_click),
            ft.ListTile(leading=ft.Icon(ft.Icons.TAG, size=18), title=ft.Text("Desarrollo", size=13)),
            ft.ListTile(leading=ft.Icon(ft.Icons.TAG, size=18), title=ft.Text("Proyectos", size=13)),
            ft.Container(expand=True),
            ft.Container(
                content=ft.ElevatedButton(
                    "🎥 Unirse a Llamada", 
                    icon=ft.Icons.VIDEO_CALL, 
                    on_click=on_call_click, 
                    bgcolor=ft.Colors.PURPLE_700, 
                    color=ft.Colors.WHITE
                ),
                padding=5
            )
        ], spacing=10),
        width=230,
        padding=12,
        bgcolor="#202020"
    )