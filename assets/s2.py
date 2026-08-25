import flet as ft

CONFIGURACOES = {
    "IF1000": {},
    "IF2000": {},
    "IF3000": {},
}

def main(page: ft.Page):
    dd_inversor = ft.Dropdown(
        label="IF",
        width=400,
        dense=True,
        padding=ft.padding.symmetric(vertical=1, horizontal=8),
        text_style=ft.TextStyle(size=15),
        label_style=ft.TextStyle(size=17),
        options=[ft.dropdown.Option(nome) for nome in sorted(CONFIGURACOES.keys())],
    )

    page.add(
        ft.Row(
            [
                ft.Icon(ft.Icons.SETTINGS),
                dd_inversor,
            ]
        )
    )

ft.app(target=main)