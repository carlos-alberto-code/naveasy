import flet as ft
from time import sleep

from navigation_state_manager import NavigationStateManager
from page_events import PageEvents
    

state = NavigationStateManager()
e = PageEvents()


def update_module(event: ft.ControlEvent):
    e.clear_page(event)
    e.open_drawer(event)
    # state.destination_index = event.page.navigation_bar.selected_index
    # state.drawer_index = 0
    print(state)
    module_name = state.current_module.label
    e.change_appbar_title(str(module_name), event)
    sections = state.current_module._drawer_sections
    event.page.drawer.controls = sections
    drawer_index = state._drawer_index
    event.page.drawer.selected_index = drawer_index
    event.page.add(sections[state._drawer_index]._content)
    event.page.update()
    sleep(1.5)
    event.page.drawer.open = False
    event.page.update()


def update_content(event: ft.ControlEvent):
    event.page.clean()
    module_sections = state.current_module._drawer_sections
    section = module_sections[event.page.drawer.selected_index]
    event.page.add(section.content)
    event.page.update()
    event.page.drawer.open = False
    event.page.update()


