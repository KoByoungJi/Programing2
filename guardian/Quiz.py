import flet as ft
from datetime import datetime

import CallApi as Api

class Quiz(ft.UserControl):
    def __init__(self, page, userInfo):
        super().__init__()

        self.page = page
        # self.guardianId = userInfo["guardianId"]
        self.guardianName = userInfo["guardianName"]
        self.seniorId = userInfo["seniorId"]
        self.seniorName = userInfo["seniorName"]

        self.fn_setList()

    def fn_setList(self):
        self.quizList = ft.ListView(expand=1, spacing=10, padding=0, auto_scroll=True)

        # now = datetime.now().strftime("%Y%m%d%H%M%S")

        self.quizInfo = Api.GetQuiz(self.seniorId)

        for idx, quiz in enumerate(self.quizInfo):
            self.quizList.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    # leading=ft.Icon((lambda check: ft.icons.CIRCLE_OUTLINED if check else ft.icons.CHECK_CIRCLE_OUTLINE)(quiz["check"])),
                                    leading=ft.Icon(name=ft.icons.CHECK_CIRCLE_OUTLINE),
                                    title=ft.Text(value=quiz["question"], size=15),
                                    # subtitle=ft.Text(value=datetime.strptime(schedule["datetime"], "%Y%m%d%H%M%S").strftime("%H:%M"), size=10),
                                    # content_padding=10
                                ),
                                ft.Row(
                                    [
                                        ft.TextButton(text="결과보기", on_click=self.fn_taskMdf, data=quiz),
                                    ],
                                    alignment=ft.MainAxisAlignment.END,
                                ),
                            ]
                        ),
                        width=400,
                        padding=10,
                    ),
                    # color=(lambda now,datetime: "" if now>datetime else "#0085FF")(now,schedule["datetime"]),
                )
            )

        self.page.update()

    def fn_taskMdf(self, e):
        def fn_cancelDlg(e):
            self.dlg_modal.open = False
            self.page.update()

        data = e.control.data

        radioGroup = ft.RadioGroup(
            content=ft.Column(
                [
                    ft.Radio(value=data["choices"][0], label=data["choices"][0]),
                    ft.Radio(value=data["choices"][1], label=data["choices"][1]),
                    ft.Radio(value=data["choices"][2], label=data["choices"][2]),
                    ft.Radio(value=data["choices"][3], label=data["choices"][3])
                ]
            ),
            value=data["answer"]
        )

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(value=data["question"], size=20),
            content=ft.Column(
                width=300,
                height=170,
                controls=[radioGroup]
            ),
            actions=[
                ft.TextButton(text="닫기", on_click=fn_cancelDlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            # on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def build(self):
        return ft.Column(
            width=390,
            controls=[
                ft.Container(
                    width=390,
                    height=600,
                    content=self.quizList,
                    # bgcolor="#000000"
                ),
            ],
        )
