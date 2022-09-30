#!/bin/bash
if [[ -d ~/.local/share/backgrounds/Dynamic_Wallpapers ]]
then 
	rm -r ~/.local/share/backgrounds/Dynamic_Wallpapers
	echo "Cleaning up"
fi

echo "Installing wallpapers..."
mkdir -p ~/.local/share/backgrounds/
mkdir -p ~/.local/share/gnome-background-properties/
cp -r $(pwd)/Dynamic_Wallpapers ~/.local/share/backgrounds/Dynamic_Wallpapers
cp $(pwd)/xml/* ~/.local/share/gnome-background-properties/
python3 $(pwd)/install_variants.py

echo "Wallpapers has been installed. Enjoy setting them as your desktop background!"
