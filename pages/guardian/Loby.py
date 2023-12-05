import flet as ft

class Loby(ft.UserControl):
    def __init__(self, page):
        super().__init__()

        self.page = page

        self.page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.CHECKLIST,
                    label="스케줄",
                ),
                ft.NavigationDestination(
                    icon=ft.icons.QUESTION_MARK,
                    label="결과",
                ),
            ],
            bgcolor="#0085FF",
            # on_change=print(self.page.navigation_bar.selected_index),
        )

    def build(self):
        return ft.Column(
            width=390,
            controls=[
                ft.Container(
                    width=390,
                    height=60,
                    bgcolor="#0085FF",
                    content=ft.Text(
                        value="스케줄",
                        size=30,
                        color="#FFFFFF",
                        font_family="NanumSquareB",
                        text_align="LEFT",
                    ),
                    padding=ft.padding.only(top=10, left=15)
                ),
            ],
        )
