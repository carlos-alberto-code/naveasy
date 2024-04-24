from typing import List
import flet as ft

from initializer import Initializer
from navigation_state import NavigationState
from on_change_events import update_module, update_content

class NavigationStructureFactory:
    # Se encarga de crear la estructura de navegación.
    # Usa el Initializer para construir el punto de entrada y tomar los demás módulos.

    # Implementar un singleton
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, initializer: Initializer) -> None:
        self.initializer    = initializer
        self.state          = NavigationState(drawer_index=initializer.drawer_index)
        self.state.modules  = self.initializer.modules
        self.init_module    = self.initializer.init_module
    
    
    def appbar(self, appbar_actions: List[ft.Control] = []):
        return ft.AppBar(
            center_title=True,
            title=ft.Text(f'{self.init_module.label}'),
            actions=appbar_actions
        )
    
    @property
    def navbar(self):
        return ft.NavigationBar(
            selected_index=self.initializer.navbar_index,
            destinations=[module for module in self.initializer.modules],
            on_change=update_module
        )
    
    @property
    def drawer(self):
        return ft.NavigationDrawer(
            open=True,
            selected_index=self.initializer.drawer_index,
            controls=[section for section in self.init_module.sections],
            on_change=update_content
        )