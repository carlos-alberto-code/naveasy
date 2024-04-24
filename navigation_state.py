from typing import List
from module import Module


class NavigationState:
    # Tiene la responsabilidad de mantener el estado de la navegación.
    
    index = 0
    _instance = None

    # Implementar un singleton para que el estado de la navegación sea único.
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, drawer_index: int = 0) -> None:
        self._modules = []
        self.drawer_index = drawer_index
    
    @property
    def modules(self) -> List[Module]:
        if not self._modules:
            raise ValueError('No se han asignado módulos a la instancia de NavigationState.')
        if self.drawer_index >= len(self._modules[self.index].sections):
            raise ValueError('El índice del cajón es mayor o igual al número de secciones del módulo actual.')
        return self._modules
    
    @modules.setter
    def modules(self, modules: List[Module]) -> None:
        self._modules = modules
    
    @property
    def current_module(self) -> Module:
        return self._modules[self.index]
    
    def __repr__(self) -> str:
        return f'State(index={self.index}, current_module={self.current_module.label})'
    