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
                    label="퀴즈",
                ),
            ],
            bgcolor="#0085FF",
            # on_change=print(self.page.navigation_bar.selected_index),
        )

        self.setList()

    def setList(self):
        self.todoList = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        # for i in range(0, 60):
        #     self.todoList.controls.append(ft.Text(f"Line {i}"))

        # self.todoList.controls.append(
        #     ft.Card(
        #         content=ft.Container(
        #             content=ft.Column(
        #                 [
        #                     ft.ListTile(
        #                         leading=ft.Icon(ft.icons.MEDICATION),
        #                         title=ft.Text("약 복용"),
        #                         subtitle=ft.Text("12:30"),
        #                     ),
        #                     ft.Row(
        #                         [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
        #                         alignment=ft.MainAxisAlignment.END,
        #                     ),
        #                 ]
        #             ),
        #             width=400,
        #             padding=10,
        #         )
        #     )
        # )

        self.todoList.controls.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.MEDICATION),
                                title=ft.Text("약 복용"),
                                subtitle=ft.Text("12:30"),
                            ),
                            # ft.Row(
                            #     [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                            #     alignment=ft.MainAxisAlignment.END,
                            # ),
                        ]
                    ),
                    width=400,
                    padding=10,
                )
            )
        )

        self.todoList.controls.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.LOCAL_HOSPITAL),
                                title=ft.Text("병원 방문"),
                                subtitle=ft.Text(
                                    "14:00"
                                ),
                            ),
                            # ft.Row(
                            #     [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                            #     alignment=ft.MainAxisAlignment.END,
                            # ),
                        ]
                    ),
                    width=400,
                    padding=10,
                ),
                color="#0085FF",
            )
        )

        self.todoList.controls.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.QUIZ),
                                title=ft.Text("퀴즈 풀기"),
                                subtitle=ft.Text(
                                    "17:00"
                                ),
                            ),
                            # ft.Row(
                            #     [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                            #     alignment=ft.MainAxisAlignment.END,
                            # ),
                        ]
                    ),
                    width=400,
                    padding=10,
                ),
            ),
        )

        self.page.update()

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
                ft.Container(
                    width=390,
                    content=self.todoList,
                ),
            ],
        )
