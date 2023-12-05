import flet as ft
import pages.senior.Loby as SeniorLoby
import pages.guardian.Loby as GuardianLoby

class Login(ft.UserControl):
    def __init__(self, page):
        super().__init__()

        self.page = page

    def fn_login(self, e):
        print(self.tab_type.selected_index)
        self.page.clean()
        if (self.tab_type.selected_index == 0):
            self.page.add(SeniorLoby.Loby(self.page))
        else:
            self.page.add(GuardianLoby.Loby(self.page))

    def build(self):
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
                                # content=ft.TextField(hint_text="What needs to be done?", on_submit=self.add_clicked, expand=True)
                                content=ft.TextField(
                                    width=300,
                                    height=50,
                                    hint_text="숫자 8자리",
                                    hint_style=ft.TextStyle(size=12,color="#AAAAAA"),
                                    text_style=ft.TextStyle(size=12,color="#2F2F2F"),
                                    border_radius=20,
                                    border_width=3,
                                    border_color="#0085FF",
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
                                    on_click=self.fn_login,
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
