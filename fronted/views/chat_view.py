import flet as ft

def get_chat_view(chat_messages, new_message_field, on_send_click):
    return ft.Column([
        ft.Container(
            content=ft.Row([
                ft.Icon(ft.Icons.TAG, color=ft.Colors.PURPLE_300),
                ft.Text("General - Colaboración del Equipo", weight=ft.FontWeight.BOLD, size=15)
            ]),
            padding=15,
            bgcolor=ft.Colors.GREY_900,
            # BorderSide actualizado para la versión 0.28
            border=ft.border.only(bottom=ft.BorderSide(1, ft.Colors.GREY_800))
        ),
        ft.Container(content=chat_messages, padding=15, expand=True),
        ft.Container(
            content=ft.Row([
                new_message_field, 
                ft.IconButton(
                    icon=ft.Icons.SEND_ROUNDED, 
                    icon_color=ft.Colors.INDIGO_300, 
                    on_click=on_send_click,
                    tooltip="Enviar mensaje"
                )
            ]),
            padding=10,
            bgcolor=ft.Colors.GREY_900
        )
    ], expand=True)