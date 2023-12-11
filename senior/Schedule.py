import flet as ft
from datetime import datetime

import CallApi as Api

class Schedule(ft.UserControl):
    def __init__(self, page, userInfo):
        super().__init__()

        self.page = page
        self.seniorId = userInfo["seniorId"]
        self.seniorName = userInfo["seniorName"]

        self.fn_setList()

    def fn_setList(self):
        self.todoList = ft.ListView(expand=1, spacing=10, padding=0, auto_scroll=True)

        now = datetime.now().strftime("%Y%m%d%H%M%S")

        self.scheduleInfo = Api.GetTask(self.seniorId)

        for idx, schedule in enumerate(self.scheduleInfo):
            self.todoList.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    leading=ft.Icon((lambda check: ft.icons.CIRCLE_OUTLINED if check else ft.icons.CHECK_CIRCLE_OUTLINE)(schedule["check"])),
                                    title=ft.Text(value=schedule["taskContent"], size=15),
                                    subtitle=ft.Text(value=datetime.strptime(schedule["datetime"], "%Y%m%d%H%M%S").strftime("%H:%M"), size=10),
                                    # content_padding=10
                                ),
                            ]
                        ),
                        width=400,
                        padding=10,
                    ),
                    color=(lambda now,datetime: "" if now>datetime else "#0085FF")(now,schedule["datetime"]),
                )
            )

        self.page.update()

    def build(self):
        return ft.Column(
            width=390,
            controls=[
                ft.Stack(
                    [
                        ft.Container(
                            width=390,
                            height=600,
                            content=self.todoList,
                            # bgcolor="#000000"
                        ),
                    ],
                    width=390,
                    height=600,
                ),
            ],
        )
