from typing import List
from module import Module


class NavigationState:
    # Tiene la responsabilidad de mantener el estado de la navegación.
    
    _instance = None

    # Implementar un singleton para que el estado de la navegación sea único.
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self._modules = []
        self._drawer_index = 0
        self._destination_index = 0
    
    @property
    def modules(self) -> List[Module]:
        return self._modules
    
    @modules.setter
    def modules(self, modules: List[Module]) -> None:
        self._modules = modules
    
    @property
    def destination_index(self) -> int:
        return self._destination_index
    
    @destination_index.setter
    def destination_index(self, index: int) -> None:
        self._destination_index = index
    
    @property
    def drawer_index(self) -> int:
        return self._drawer_index
    
    @drawer_index.setter
    def drawer_index(self, index: int) -> None:
        self._drawer_index = index
    
    @property
    def current_module(self) -> Module:
        return self._modules[self._destination_index]
    
    def __repr__(self) -> str:
        return f'State(index={self._destination_index}, current_module={self.current_module.label})'
    