from typing import Any, List
import flet as ft
from flet_core.control import OptionalNumber
from flet_core.navigation_bar import (
    NavigationBarLabelBehavior,
    NavigationDestination,
)
from flet_core.ref import Ref
from flet_core.types import (
    AnimationValue,
    OffsetValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
)
# from inextracker.ui.widgets.colors import dark_theme, light_theme


class NavBar(ft.NavigationBar):
    def __init__(
        self,
        navigation_destinations: List[ft.NavigationDestination],
        navigation_views: List[ft.Control],
        pg: ft.Page,
        ref: Ref | None = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: bool | int | None = None,
        col: ResponsiveNumber | None = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        on_animation_end=None,
        visible: bool | None = None,
        disabled: bool | None = None,
        data: Any = None,
        destinations: List[NavigationDestination] | None = None,
        selected_index: int | None = None,
        bgcolor: str | None = None,
        label_behavior: NavigationBarLabelBehavior | None = None,
        elevation: OptionalNumber = None,
        on_change=None,
    ):
        super().__init__(
            ref,
            width,
            height,
            left,
            top,
            right,
            bottom,
            expand,
            col,
            opacity,
            rotate,
            scale,
            offset,
            aspect_ratio,
            animate_opacity,
            animate_size,
            animate_position,
            animate_rotation,
            animate_scale,
            animate_offset,
            on_animation_end,
            visible,
            disabled,
            data,
            destinations,
            selected_index,
            bgcolor,
            label_behavior,
            elevation,
            on_change,
        )
        self.navigation_destinations = navigation_destinations
        self.navigation_views = navigation_views
        self.pg = pg
        self.pre_check()

        self.destinations = self.navigation_destinations

        self.destination_index_to_views_mapping = (
            self.create_destination_view_mapping()
        )

        self.selected_index = 0
        self.elevation = 6.6666666666
        self.destinations = self.navigation_destinations
        self.on_change = self.on_changing_navigation_page

    def on_changing_navigation_page(self, e):
        for index, control in self.destination_index_to_views_mapping:
            if index == self.selected_index:
                print(
                    f"onChange: {index=} == {self.selected_index=}\nVisible -> True\n\t============="
                )
                control.visible = True

            else:
                print(
                    f"onChange: {index=} != {self.selected_index=}\nVisible -> False\n\t============="
                )
                control.visible = False
        else:
            print("onChange: Updates")
            self.update()
            self.pg.update()

    def create_destination_view_mapping(self):
        if len(self.navigation_destinations) == len(self.navigation_views):
            print("create_destination_view_mapping: Returning Mapping")
            return tuple(enumerate(self.navigation_views))
        else:
            raise Exception("Unequal Mappings Supplied")

    def pre_check(self):
        for view in self.navigation_views:
            view.visible = False
            print(f"Precheck: Setting Visible -> False")

        else:
            self.navigation_views[0].visible = True
            print("Precheck: Update")
            self.pg.update()


def main(page: ft.Page):
    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        theme_switcher.label = (
            "Light theme"
            if page.theme_mode == ft.ThemeMode.LIGHT
            else "Dark theme"
        )

        # page.theme = (
        #     light_theme
        #     if page.theme_mode == ft.ThemeMode.LIGHT
        #     else dark_theme
        # )

        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT
    theme_switcher = ft.Switch(label="Light theme", on_change=theme_changed)
    page.add(theme_switcher)

    d1 = ft.NavigationDestination(icon=ft.icons.BOOKMARK)
    d2 = ft.NavigationDestination(icon=ft.icons.BOOKMARK)
    d3 = ft.NavigationDestination(icon=ft.icons.BOOKMARK)

    v1 = ft.Text("v1")
    v2 = ft.Text("v2")
    v3 = ft.Text("v3")

    page.add(v1)
    page.add(v2)
    page.add(v3)

    page.navigation_bar = NavBar(
        navigation_destinations=[d1, d2, d3],
        navigation_views=[v1, v2, v3],
        pg=page,
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main)