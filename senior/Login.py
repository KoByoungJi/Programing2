import flet as ft

import Loby as GuardianLoby
import CallApi as Api

class Login(ft.UserControl):
    def __init__(self, page):
        super().__init__()

        self.page = page

    def fn_close_dlg(self, e):
        self.dlg_modal.open = False
        self.page.update()

    def fn_login(self, e):
        id = self.seniorId.value

        result, data = Api.SeniorLogin(id)
        if result:
            data["seniorId"] = id
            self.page.clean()
            GuardianLoby.Loby(self.page, data)
        else:
            self.dlg_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text(
                    value="로그인 오류",
                    size=20
                ),
                content=ft.Text(
                    value=data,
                    text_align="CENTER",
                    size=15,
                ),
                actions=[
                    ft.TextButton("확인", on_click=self.fn_close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )

            self.page.dialog = self.dlg_modal
            self.dlg_modal.open = True
            self.page.update()

    def build(self):
        self.seniorId = ft.TextField(
            width=300,
            height=50,
            hint_text="숫자 8자리",
            hint_style=ft.TextStyle(size=12,color="#AAAAAA"),
            text_style=ft.TextStyle(size=12,color="#2F2F2F"),
            border_radius=20,
            border_width=3,
            border_color="#0085FF",
        )

        self.tab_type = ft.Tabs(
            label_color="#2F2F2F",
            unselected_label_color="#2F2F2F",
            overlay_color = {
                ft.MaterialState.FOCUSED:"#0085FF",
                ft.MaterialState.PRESSED:"#0085FF",
            },
            indicator_color="#0085FF",
            divider_color = "#0085FF",
            indicator_tab_size = False,
            scrollable=False,
            selected_index=0,
            # on_change=self.tabs_changed,
            tabs=[
                ft.Tab(
                    text="시니어",
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Text(value="시니어 코드", color="#AAAAAA"),
                                padding=ft.padding.only(top=30, left=30)
                            ),
                            ft.Container(
                                content=self.seniorId,
                                padding=ft.padding.only(left=30)
                            ),
                            ft.Container(
                                content=ft.ElevatedButton(
                                    width=100,
                                    height=40,
                                    text="로그인",
                                    style=ft.ButtonStyle(
                                        color="#FFFFFF",
                                        bgcolor="#0085FF"
                                    ),
                                    on_click=self.fn_login,
                                ),
                                alignment=ft.alignment.center_right,
                                padding=ft.padding.only(top=20, right=30)
                            )
                        ]
                    )
                ),
                ft.Tab(
                    text="보호자",
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Text(value="아이디", color="#AAAAAA"),
                                padding=ft.padding.only(top=30, left=30)
                            ),
                            ft.Container(
                                content=ft.TextField(
                                    width=300,
                                    height=50,
                                    text_style=ft.TextStyle(size=12,color="#2F2F2F"),
                                    border_radius=20,
                                    border_width=3,
                                    border_color="#0085FF",
                                ),
                                padding=ft.padding.only(left=30)
                            ),
                            ft.Container(
                                content=ft.Text(value="비밀번호", color="#AAAAAA"),
                                padding=ft.padding.only(top=5, left=30)
                            ),
                            ft.Container(
                                content=ft.TextField(
                                    width=300,
                                    height=50,
                                    text_style=ft.TextStyle(size=12,color="#2F2F2F"),
                                    border_radius=20,
                                    border_width=3,
                                    border_color="#0085FF",
                                    password=True
                                ),
                                padding=ft.padding.only(left=30)
                            ),
                            ft.Container(
                                content=ft.ElevatedButton(
                                    width=100,
                                    height=40,
                                    text="로그인",
                                    style=ft.ButtonStyle(
                                        color="#FFFFFF",
                                        bgcolor="#0085FF"
                                    ),
                                    # on_click=self.fn_login,
                                ),
                                alignment=ft.alignment.center_right,
                                padding=ft.padding.only(top=20, right=30)
                            )
                        ]
                    )
                ),
            ],
        )

        return ft.Column(
            width=390,
            controls=[
                ft.Row(
                    height=250,
                    controls=[
                        ft.Text(
                            value="은빛 돌봄",
                            size=32,
                            color="#000000",
                            font_family="NanumSquareB",
                            text_align="CENTER"
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Column(
                    height=300,
                    controls=[
                        self.tab_type,
                    ],
                ),
            ],
        )
