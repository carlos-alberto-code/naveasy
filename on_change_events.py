import flet as ft
from time import sleep

from navigation_state import NavigationStateManager
from page_events import PageEvents
    

navigation_state = NavigationStateManager()
print(navigation_state.drawer_index)
print(navigation_state.destination_index)
e = PageEvents()


def update_module(event: ft.ControlEvent):
    e.clear_page(event)
    e.open_drawer(event)
    # Actualizar el estado de la navegación
    navigation_state._destination_index = event.page.navigation_bar.selected_index # Índice del módulo seleccionado

    module_name = navigation_state.current_module.label
    e.change_appbar_title(str(module_name), event)
    sections = navigation_state.current_module._drawer_sections
    event.page.drawer.controls = sections
    drawer_index = navigation_state._drawer_index
    event.page.drawer.selected_index = drawer_index
    event.page.add(sections[navigation_state._drawer_index]._content)
    event.page.update()
    sleep(1.5)
    event.page.drawer.open = False
    event.page.update()


def update_content(event: ft.ControlEvent):
    event.page.clean()
    module_sections = navigation_state.current_module._drawer_sections
    section = module_sections[event.page.drawer.selected_index]
    event.page.add(section.content)
    event.page.update()
    event.page.drawer.open = False
    event.page.update()


