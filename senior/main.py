import flet as ft
import Login as Login

def main(page: ft.Page):
    page.title = "은빛 돌봄(시니어)"
    page.window_width = 390        # window's width is 390 px
    page.window_height = 844       # window's height is 844 px
    page.window_resizable = False  # window is not resizable5
    page.bgcolor = "#E9E9E9"

    page.fonts = {
        "NanumSquareB": "/Users/gobyeongji/Library/Fonts/NanumSquareB.ttf",
        "NanumSquareL": "/Users/gobyeongji/Library/Fonts/NanumSquareL.ttf",
        "NanumSquareR": "/Users/gobyeongji/Library/Fonts/NanumSquareR.ttf"
    }

    # create application instance
    login = Login.Login(page)

    # add application's root control to the page
    page.add(login)

ft.app(target=main)
