# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os


def replace(file):
    if file[-3:] == 'xml':
        with open(file, 'r') as f:
            lines = f.readlines()
        with open(file, 'w') as f:
            for i in range(len(lines)):
                lines[i] = lines[i].replace('@directory-key@', f'{os.path.expanduser("~")}/.local/share')
            f.writelines(lines)


def handle_directory(directory):
    files = os.listdir(directory)
    for file in files:
        file = directory+'/'+file
        if os.path.isfile(file):
            replace(file)
        else:
            handle_directory(file)


if __name__ == '__main__':
    handle_directory(f'{os.path.expanduser("~")}/.local/share/backgrounds/Dynamic_Wallpapers')
    handle_directory(f'{os.path.expanduser("~")}/.local/share/gnome-background-properties')

