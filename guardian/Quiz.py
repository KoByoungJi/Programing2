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
                                ft.Row(
                                    [
                                        ft.TextButton(text="수정", on_click=self.fn_taskMdf, data=schedule),
                                        ft.TextButton(text="삭제", on_click=self.fn_taskDelete, data=schedule)
                                    ],
                                    alignment=ft.MainAxisAlignment.END,
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

    def fn_taskAdd(self, e):
        def fn_saveDlg(e):
            taskInfo = {"seniorId":self.seniorId, "taskContent":title.value, "datetime":date.value+time.value+"00", "check":True}
            Api.AddTask(taskInfo)

            self.dlg_modal.open = False
            self.page.update()

        def fn_cancelDlg(e):
            self.dlg_modal.open = False
            self.page.update()

        title = ft.TextField(width=300, height=50, label="제목", text_style=ft.TextStyle(size=15,color="#FFFFFF"), border_radius=10, border_width=3, border_color="#0085FF")
        date = ft.TextField(width=300, height=50, label="날짜", text_style=ft.TextStyle(size=15,color="#FFFFFF"), border_radius=10, border_width=3, border_color="#0085FF")
        time = ft.TextField(width=300, height=50, label="시간", text_style=ft.TextStyle(size=15,color="#FFFFFF"), border_radius=10, border_width=3, border_color="#0085FF")

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(value="스케줄 추가", size=20),
            content=ft.Column(
                width=300,
                height=170,
                controls=[title, date, time]
            ),
            actions=[
                ft.TextButton(text="취소", on_click=fn_cancelDlg),
                ft.TextButton(text="저장", on_click=fn_saveDlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def fn_taskMdf(self, e):
        def fn_saveDlg(e):
            taskInfo = {"seniorId":data["seniorId"], "taskId":data["taskId"], "taskContent":title.value, "datetime":date.value+time.value+"00", "check":True}
            Api.UpdateTask(taskInfo)

            self.dlg_modal.open = False
            self.page.update()

        def fn_cancelDlg(e):
            self.dlg_modal.open = False
            self.page.update()

        data = e.control.data

        title = ft.TextField(width=300, height=50, label="제목", value=data["taskContent"],
            text_style=ft.TextStyle(size=15,color="#FFFFFF"), border_radius=10, border_width=3, border_color="#0085FF",
        )
        date = ft.TextField(width=300, height=50, label="날짜", value=datetime.strptime(data["datetime"], "%Y%m%d%H%M%S").strftime("%Y%m%d"),
            text_style=ft.TextStyle(size=15,color="#FFFFFF"), border_radius=10, border_width=3, border_color="#0085FF",
        )
        time = ft.TextField(width=300, height=50, label="시간", value=datetime.strptime(data["datetime"], "%Y%m%d%H%M%S").strftime("%H%M"),
            text_style=ft.TextStyle(size=15,color="#FFFFFF"), border_radius=10, border_width=3, border_color="#0085FF",
        )

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(value="스케줄 수정", size=20),
            content=ft.Column(
                width=300,
                height=170,
                controls=[title, date, time]
            ),
            actions=[
                ft.TextButton(text="취소", on_click=fn_cancelDlg),
                ft.TextButton(text="저장", on_click=fn_saveDlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            # on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def fn_taskDelete(self, e):
        def fn_saveDlg(e):
            taskInfo = {"seniorId":data["seniorId"], "taskId":data["taskId"]}
            Api.DeleteTask(taskInfo)

            self.dlg_modal.open = False
            self.page.update()

        def fn_cancelDlg(e):
            self.dlg_modal.open = False
            self.page.update()

        data = e.control.data

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(value="확인", size=20),
            content=ft.Text(
                value="제목: '"+data["taskContent"]+"'\n일시: '"+datetime.strptime(data["datetime"], "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")+"'\n\n해당 스케줄을 삭제하시겠습니까?",
                size=15,
            ),
            actions=[
                ft.TextButton(text="취소", on_click=fn_cancelDlg),
                ft.TextButton(text="삭제", on_click=fn_saveDlg),
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
                ft.Stack(
                    [
                        ft.Container(
                            width=390,
                            height=600,
                            content=self.todoList,
                            # bgcolor="#000000"
                        ),
                        ft.FloatingActionButton(
                            top=540,
                            left=310,
                            icon=ft.icons.ADD,
                            on_click=self.fn_taskAdd
                        )
                    ],
                    width=390,
                    height=600,
                ),
            ],
        )
