import flet as ft

import CallApi as Api
import Schedule
import Quiz

class Loby(ft.UserControl):
    def __init__(self, page, userInfo):
        super().__init__()

        self.page = page
        self.userInfo = userInfo

        self.selected_index = 0
        self.fn_drawInit()
        self.schedule = Schedule.Schedule(self.page, self.userInfo)
        self.page.add(self.schedule)

        self.page.update()

    def fn_drawInit(self):
        self.page.appbar = ft.AppBar(
            title=ft.Text(
                value=(lambda idx: "스케줄 관리" if idx == 0 else "퀴즈 결과")(self.selected_index),
                weight=ft.FontWeight.BOLD,
                color="#FFFFFF"
            ),
            bgcolor="#0085FF",
            center_title=True,
            actions=[
                ft.IconButton(
                    icon=ft.icons.ARROW_OUTWARD, 
                    tooltip="즉시알림",
                    icon_color="#FFFFFF",
                    on_click=self.fn_directMsg,
                    visible=(lambda idx: True if idx == 0 else False)(self.selected_index),
                ),
                ft.IconButton(
                    icon=ft.icons.REFRESH, 
                    tooltip="새로고침",
                    icon_color="#FFFFFF",
                    on_click=self.fn_refresh,
                )
            ],
            color=ft.colors.WHITE,
        )

        self.page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.CHECKLIST,
                    label="스케줄 관리",
                ),
                ft.NavigationDestination(
                    icon=ft.icons.QUESTION_MARK,
                    label="퀴즈 결과",
                ),
            ],
            bgcolor="#0085FF",
            on_change=self.fn_navigateChange,
        )
        self.page.navigation_bar.selected_index = self.selected_index

    def fn_navigateChange(self, e):
        self.selected_index = e.control.selected_index

        self.page.clean()
        self.fn_drawInit()

        if self.selected_index == 0:
            self.schedule = Schedule.Schedule(self.page, self.userInfo)
            self.page.add(self.schedule)
        elif self.selected_index == 1:
            self.quiz = Quiz.Quiz(self.page, self.userInfo)
            self.page.add(self.quiz)

        self.page.update()

    def fn_directMsg(self, e):
        def fn_saveDlg(e):
            # taskInfo = {"seniorId":data["seniorId"], "taskId":data["taskId"], "taskContent":title.value, "datetime":date.value+time.value+"00", "check":True}
            # Api.UpdateTask(taskInfo)

            self.dlg_modal.open = False
            self.page.update()

        def fn_cancelDlg(e):
            self.dlg_modal.open = False
            self.page.update()

        msg = ft.TextField(width=300, height=50, label="내용 입력",
            text_style=ft.TextStyle(size=15,color="#FFFFFF"), border_radius=10, border_width=3, border_color="#0085FF",
        )

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(value="즉시 알림", size=20),
            content=ft.Column(
                width=300,
                height=50,
                controls=[msg]
            ),
            actions=[
                ft.TextButton(text="취소", on_click=fn_cancelDlg),
                ft.TextButton(text="전송", on_click=fn_saveDlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def fn_refresh(self, e):
        self.page.clean()
        self.fn_drawInit()
        if self.selected_index == 0:
            self.schedule = Schedule.Schedule(self.page, self.userInfo)
            self.page.add(self.schedule)
        else:
            self.quiz = Quiz.Quiz(self.page, self.userInfo)
            self.page.add(self.quiz)

        self.page.update()
