from time import sleep

import flet as ft

from navigation_state_manager import NavigationStateManager
from page_events import PageEvents
    

state = NavigationStateManager()
e = PageEvents()


def update_module(event: ft.ControlEvent):
    # Limpiar los controles de la página.
    e.clear_page(event)
    # Establecer el índice del módulo(destination) seleccionado.
    state.navbar_index = event.page.navigation_bar.selected_index
    # Cambiar el título del appbar.
    e.change_appbar_title(str(state.current_module.label), event)
    # Obtener los controles(secciones) del drawer en función del módulo (destination) seleccionado
    sections = state.current_module.drawer_sections
    # Inyectar los controles(secciones) al drawer.
    event.page.drawer.controls = sections
    # Abrir el drawer.
    e.open_drawer(event)
    # Establecer el índice de la seccion(drawer_control) definida en el Initializer.
    event.page.drawer.selected_index = state.drawer_index
    # Agregar el contenido de la sección seleccionada a la página.
    e.add_to_page(sections[state.drawer_index].content, event)
    e.update_page(event)
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
