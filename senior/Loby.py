import flet as ft
import threading
import time

import Schedule as Schedule
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

        checkTask = threading.Thread(target=self.fn_checkTask)
        checkTask.start()

    def fn_checkTask(self):
        while(True):
            print(1)
            time.sleep(10)

    def fn_drawInit(self):
        self.page.appbar = ft.AppBar(
            title=ft.Text(
                value=(lambda idx: "오늘 할일" if idx == 0 else "퀴즈")(self.selected_index),
                weight=ft.FontWeight.BOLD,
                color="#FFFFFF"
            ),
            bgcolor="#0085FF",
            center_title=True,
            actions=[
                ft.IconButton(
                    icon=ft.icons.REFRESH, 
                    tooltip="새로고침",
                    icon_color="#FFFFFF",
                    on_click=self.fn_refresh,
                    visible=(lambda idx: True if idx == 0 else False)(self.selected_index),
                )
            ],
            color=ft.colors.WHITE,
        )

        self.page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.CHECKLIST,
                    label="오늘 할일",
                ),
                ft.NavigationDestination(
                    icon=ft.icons.QUESTION_MARK,
                    label="퀴즈",
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
            self.schedule = Quiz.Quiz(self.page, self.userInfo)
            self.page.add(self.schedule)

        self.page.update()

    def fn_refresh(self, e):
        self.page.clean()
        self.fn_drawInit()
        self.schedule = Schedule.Schedule(self.page, self.userInfo)
        self.page.add(self.schedule)
        self.page.update()
