import flet as ft
from time import sleep

from navigation_state import NavigationState


class PageEvents:

    def clear_page(self, event: ft.ControlEvent):
        event.page.clean()
    
    def update_page(self, event: ft.ControlEvent):
        event.page.update()
    
    def open_drawer(self, event: ft.ControlEvent):
        event.page.drawer.open = True
        event.page.update()
    
    def close_drawer(self, event: ft.ControlEvent):
        event.page.drawer.open = False
        event.page.update()
    
    def change_appbar_title(self, title: str, event: ft.ControlEvent):
        event.page.appbar.title = ft.Text(value=title)
    

state = NavigationState()
e = PageEvents()


def update_module(event: ft.ControlEvent):
    e.clear_page(event)
    e.open_drawer(event)
    state.index = event.control.selected_index
    module_name = state.current_module.label
    e.change_appbar_title(str(module_name), event)
    sections = state.current_module.sections
    event.page.drawer.controls = sections
    drawer_index = state.drawer_index
    event.page.drawer.selected_index = drawer_index
    event.page.add(sections[state.drawer_index].content)
    event.page.update()
    sleep(1.5)
    event.page.drawer.open = False
    event.page.update()


def update_content(event: ft.ControlEvent):
    event.page.clean()
    module_sections = state.current_module.sections
    section = module_sections[event.page.drawer.selected_index]
    event.page.add(section.content)
    event.page.update()
    event.page.drawer.open = False
    event.page.update()


