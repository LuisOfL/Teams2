import flet as ft

def get_call_view(user_name: str, on_hang_up):
    video_grid = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.CircleAvatar(content=ft.Icon(ft.Icons.PERSON, size=40), radius=35, bgcolor=ft.Colors.INDIGO),
                ft.Text(f"{user_name} (Tú)", color=ft.Colors.WHITE, weight=ft.FontWeight.W_500)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor=ft.Colors.GREY_900,
            expand=True,
            border_radius=12,
            alignment=ft.alignment.center,
            border=ft.border.all(1, ft.Colors.GREY_800)
        ),
        ft.Container(
            content=ft.Column([
                ft.CircleAvatar(content=ft.Icon(ft.Icons.PERSON, size=40), radius=35, bgcolor=ft.Colors.TEAL),
                ft.Text("Participante Externo", color=ft.Colors.WHITE, weight=ft.FontWeight.W_500)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor=ft.Colors.GREY_900,
            expand=True,
            border_radius=12,
            alignment=ft.alignment.center,
            border=ft.border.all(1, ft.Colors.GREY_800)
        )
    ], expand=True, spacing=15)

    call_controls = ft.Row([
        ft.IconButton(icon=ft.Icons.MIC, icon_color=ft.Colors.WHITE, bgcolor=ft.Colors.GREY_800, tooltip="Silenciar micro"),
        ft.IconButton(icon=ft.Icons.VIDEOCAM, icon_color=ft.Colors.WHITE, bgcolor=ft.Colors.GREY_800, tooltip="Apagar cámara"),
        ft.IconButton(icon=ft.Icons.SCREEN_SHARE, icon_color=ft.Colors.WHITE, bgcolor=ft.Colors.GREY_800, tooltip="Compartir pantalla"),
        ft.VerticalDivider(width=10, color=ft.Colors.GREY_700),
        ft.IconButton(
            icon=ft.Icons.CALL_END, 
            icon_color=ft.Colors.WHITE, 
            bgcolor=ft.Colors.RED_700, 
            tooltip="Abandonar llamada", 
            on_click=on_hang_up
        )
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=15)

    return ft.Column([
        ft.Container(
            content=ft.Row([
                ft.Icon(ft.Icons.VIDEO_CALL, color=ft.Colors.GREEN_400),
                ft.Text("Reunión en curso: Sala General", weight=ft.FontWeight.BOLD, size=15)
            ]),
            padding=15,
            bgcolor=ft.Colors.GREY_900
        ),
        ft.Container(content=video_grid, padding=20, expand=True, bgcolor=ft.Colors.BLACK),
        ft.Container(content=call_controls, padding=15, bgcolor=ft.Colors.GREY_900)
    ], expand=True)