#!/usr/bin/env python3

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
from shutil import copy


def get_last(dir):
    return dir.split('/')[-1]


def handle_directory(dir):
    files = os.listdir(dir)
    if len(files) != 2:
        return
    print(f'enter name for {dir}')
    name = get_last(dir)
    new_dir = f'{os.path.expanduser("~")}/.local/share/backgrounds/Dynamic_Wallpapers/' + name
    # os.makedirs(new_dir)
    filess = os.listdir(new_dir)
    filess.sort()
    for i in range(len(filess)):
        filess[i] = new_dir + '/' + filess[i]
        # copy(i_d, new_dir + '/' + i)
        # filess.append(new_dir + '/' + i)

    xml = f'<?xml version="1.0" encoding="UTF-8" ?><!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd"><wallpapers><wallpaper deleted="false"><name>{name}</name><filename>{filess[0]}</filename><filename-dark>{filess[1]}</filename-dark><options>zoom</options><shade_type>solid</shade_type><pcolor>#3465a4</pcolor><scolor>#000000</scolor></wallpaper></wallpapers>'
    with open(f'{os.path.expanduser("~")}/.local/share/gnome-background-properties/' + name + '.xml', 'w') as f:
        f.writelines(xml)


def print_hi(name):
    dirs = os.listdir(name)
    for i in dirs:
        i = name + '/' + i
        if not os.path.isfile(i):
            handle_directory(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('./Dynamic_Wallpapers')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
