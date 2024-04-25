from time import sleep

import flet as ft

from navigation_structures import NavigationStructureFactory
from initializer import Initializer
from module import Module
from modules import(
    inventory,
    purchase,
)


def main(page: ft.Page):

    modules = Module.all
    init    = Initializer(modules=modules, navbar_index=1, drawer_index=1)
    print('En el main: ', init.navbar_index, init.drawer_index)
    struct  = NavigationStructureFactory(initializer=init)

    page.vertical_alignment     = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment   = ft.CrossAxisAlignment.CENTER
    page.window_maximized       = True

    page.add(init.initial_drawer_section_content)

    page.navigation_bar = struct.navbar
    page.drawer         = struct.drawer
    page.appbar         = struct.appbar()
    page.update()

    sleep(1.5)
    page.drawer.open = False
    page.update()

ft.app(target=main)