from time import sleep

import flet as ft

from navigation_state_manager import NavigationStateManager
from page_events import PageEvents
    

state = NavigationStateManager()
e = PageEvents()


def update_module(event: ft.ControlEvent):
    e.clear_page(event)
    state.navbar_index = event.page.navigation_bar.selected_index
    e.change_appbar_title(str(state.current_module.label), event)
    sections = state.current_module.drawer_sections
    event.page.drawer.controls = sections
    e.open_drawer(event)
    event.page.drawer.selected_index = state.drawer_index
    e.add_to_page(sections[state.drawer_index].content, event)
    e.update_page(event)
    sleep(1.5)
    e.close_drawer(event)
    e.update_page(event)


def update_content(event: ft.ControlEvent):
    event.page.clean()
    module_sections = state.current_module._drawer_sections
    section = module_sections[event.page.drawer.selected_index]
    event.page.add(section.content)
    event.page.update()
    event.page.drawer.open = False
    event.page.update()
