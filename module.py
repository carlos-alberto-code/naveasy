import flet as ft


class Section(ft.NavigationDrawerDestination):

    def __init__(self, label: str, icon: str, content: ft.Control) -> None:
        super().__init__(label, icon)
        self.content = content


class Module(ft.NavigationDestination):

    all = []

    def __init__(self, label: str, icon: str, *sections: Section) -> None:
        super().__init__(label, icon)
        self.sections = sections
        self.all.append(self)

    def __repr__(self):
        return f'Module(label={self.label}, icon={self.icon}, sections={self.sections})'