import flet as ft


class Section(ft.NavigationDrawerDestination):

    def __init__(self, label: str, icon: str, content: ft.Control) -> None:
        super().__init__(label, icon)
        self._content = content
    
    @property
    def content(self):
        return self._content


class Module(ft.NavigationDestination):

    all = []

    def __init__(self, label: str, icon: str, *sections: Section) -> None:
        super().__init__(label, icon)
        self._drawer_sections = sections
        self.all.append(self)
    
    @property
    def drawer_sections(self):
        return self._drawer_sections

    def __repr__(self):
        return f'Module(label={self.label}, icon={self.icon}, sections={self._drawer_sections})'