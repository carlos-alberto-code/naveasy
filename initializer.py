import inspect
from typing import List

import flet as ft

from module import Module


class Initializer:
    # Tiene la responsabilidad de proporcionar los controles iniciales de la estructura de navegación, junto con los módulos que se van a utilizar.
    # Se creo para que el dev pueda personalizar cómo inicializar la aplicación.

    # Implementar un singleton
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, modules: List[Module], navbar_index: int = 0, drawer_index: int = 0) -> None:
        if not modules:
            raise ValueError('Initializer: modules list is empty.')
        if navbar_index >= len(modules):
            raise ValueError(f'Initializer: navbar_index ({navbar_index}) is out of range for modules list.')
        # Comprobar si el drawer_index está fuera del rango de algún módulo, para lanzar una advertencia.
        for module in modules:
            if drawer_index >= len(module.sections):
                if drawer_index >= len(module.sections):
                    raise IndexError(f'Initializer: drawer_index ({drawer_index}) is out of range for module "{module.label}". Change it to a valid index for all modules.')
        self._modules = modules
        self.navbar_index = navbar_index
        self.drawer_index = drawer_index
    
    @property
    def modules(self) -> List[Module]:
        return self._modules
    
    @modules.setter
    def modules(self, modules: List[Module]) -> None:
        self._modules = modules
    
    @property
    def init_module(self) -> Module:
        return self.modules[self.navbar_index]
    
    @property
    def content(self) -> ft.Control:
        return self.init_module.sections[self.drawer_index].content

    def __repr__(self) -> str:
        return (
            f'Initializer(self.NAVBAR_INDEX={self.navbar_index}, self.DRAWER_INDEX={self.drawer_index}) '
            f'-> Has {len(self.modules)} modules'
            f'\nModule names are: {[module.label for module in self.modules]}'
            f'\nThe selected module is "{self.init_module.label}", and it has {len(self.init_module.sections)} sections.'
            f'\nThe section names are: {[section.label for section in self.init_module.sections]}'
            f'\n\nEnd Initializer...'
        )
