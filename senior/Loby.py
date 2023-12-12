import flet as ft
import threading
import time
import datetime

import Schedule as Schedule
import Quiz
import CallApi as Api

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

        self.checkTask = threading.Thread(target=self.fn_checkTask)
        self.checkTask.start()

    def fn_checkTask(self):
        while(True):
            try:
                fromTime = (datetime.datetime.now() - datetime.timedelta(seconds=20)).strftime("%Y%m%d%H%M%S")
                toTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

                for idx, schedule in enumerate(self.schedule.scheduleInfo):
                    if fromTime <= schedule["datetime"] and schedule["datetime"] <= toTime:
                        self.fn_taskCall(schedule)
                time.sleep(20)
            except Exception as error:
                pass

    def fn_taskCall(self, scheduleInfo):
        def fn_saveDlg(e):
            data = {
                "seniorId": scheduleInfo["seniorId"],
                "taskId": scheduleInfo["taskId"],
                "taskContent": scheduleInfo["taskContent"],
                "datetime": scheduleInfo["datetime"],
                "check": False
            }
            Api.UpdateTask(data)

            self.dlg_modal.open = False
            self.page.update()
            self.audio.release()
            del self.page.overlay[0]

        def fn_closeDlg():
            self.dlg_modal.open = False
            self.page.update()
            self.audio.release()
            del self.page.overlay[0]

        def fn_taskTimeout():
            time.sleep(10)
            fn_closeDlg()

        self.audio = ft.Audio(
            src="/Users/gobyeongji/Desktop/Programing2/iPhone-Alarm-Original.mp3",
            autoplay=True,
            volume=1,
            balance=0,
            on_loaded=lambda _: print("Loaded"),
            on_duration_changed=lambda e: print("Duration changed:", e.data),
            on_position_changed=lambda e: print("Position changed:", e.data),
            on_state_changed=lambda e: print("State changed:", e.data),
            on_seek_complete=lambda _: print("Seek complete"),
        )
        self.page.overlay.append(self.audio)

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Icon(name=ft.icons.ACCESS_ALARM, size=200, color="#0085FF"),
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Text(value=scheduleInfo["taskContent"], size=50),
                        alignment=ft.alignment.center
                    ),
                ],
                height=280,
            ),
            actions=[
                ft.Container(
                    content=ft.ElevatedButton(text="확인", on_click=fn_saveDlg),
                    alignment=ft.alignment.center
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()
        self.audio.play()

        taskTimeout = threading.Thread(target=fn_taskTimeout)
        taskTimeout.start()

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
