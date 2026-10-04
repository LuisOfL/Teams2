import flet as ft
import json
import websockets

from components.left_nav import create_left_nav
from components.sidebar import create_sidebar
from views.chat_view import get_chat_view
from views.call_view import get_call_view

WS_URL = "ws://localhost:8000/ws/"

async def main(page: ft.Page):
    page.title = "Microsoft Teams - Flet & FastAPI"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    # Actualizado para Flet 0.28+
    page.window.width = 1150
    page.window.height = 720

    user_name = ft.TextField(label="Tu Nombre", value="Usuario1", width=140, text_size=12)
    chat_messages = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    
    async def on_submit_chat(e):
        await send_chat(e)

    new_message = ft.TextField(
        hint_text="Escribe un mensaje en General...", 
        expand=True, 
        border_color=ft.Colors.GREY_700,
        focused_border_color=ft.Colors.INDIGO_300,
        on_submit=on_submit_chat
    )
    
    websocket = None
    content_area = ft.Column(expand=True, spacing=0)

    # --- WEBSOCKET LISTENER ---
    async def connect_ws(e):
        nonlocal websocket
        if not user_name.value:
            return
        try:
            uri = f"{WS_URL}{user_name.value}"
            websocket = await websockets.connect(uri)
            show_chat_view()
            
            async for message in websocket:
                data = json.loads(message)
                m_type = data.get("type", "chat")
                sender = data.get("sender", "Anónimo")
                
                if m_type == "chat":
                    chat_messages.controls.append(
                        ft.Container(
                            content=ft.Row([
                                ft.CircleAvatar(content=ft.Text(sender[:2].upper()), bgcolor=ft.Colors.INDIGO_700, radius=18),
                                ft.Column([
                                    ft.Row([
                                        ft.Text(sender, weight=ft.FontWeight.BOLD, size=12, color=ft.Colors.INDIGO_200),
                                        ft.Text("Justo ahora", size=10, color=ft.Colors.GREY_500)
                                    ], spacing=10),
                                    ft.Text(data.get("text", ""), size=14, color=ft.Colors.WHITE70)
                                ], spacing=2, expand=True)
                            ], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.START),
                            padding=5
                        )
                    )
                    page.update()
                elif m_type == "notification":
                    chat_messages.controls.append(
                        ft.Text(f"⚙️ {data.get('text')}", size=11, italic=True, color=ft.Colors.AMBER_300)
                    )
                    page.update()
        except Exception as ex:
            print(f"Error en la conexión WebSocket: {ex}")

    async def send_chat(e):
        if new_message.value.strip() and websocket:
            msg = {"type": "chat", "text": new_message.value}
            await websocket.send(json.dumps(msg))
            new_message.value = ""
            new_message.update()

    # --- CAMBIO DE VISTAS ---
    def show_chat_view(e=None):
        content_area.controls.clear()
        content_area.controls.append(
            get_chat_view(chat_messages, new_message, send_chat)
        )
        page.update()

    def show_call_view(e=None):
        content_area.controls.clear()
        content_area.controls.append(
            get_call_view(user_name.value or "Usuario", show_chat_view)
        )
        page.update()

    # Ensamblaje de Componentes de Layout
    left_nav = create_left_nav(show_chat_view, show_call_view)
    side_panel = create_sidebar(user_name, connect_ws, show_chat_view, show_call_view)

    main_layout = ft.Row([
        left_nav,
        side_panel,
        content_area
    ], expand=True, spacing=0)

    page.add(main_layout)

ft.app(target=main)