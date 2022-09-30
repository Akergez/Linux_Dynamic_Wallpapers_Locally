#!/bin/bash
cd ~
echo "Downloading needed files started"
git clone https://github.com/saint-13/Linux_Dynamic_Wallpapers.git  
cd Linux_Dynamic_Wallpapers
echo "Files downloaded"

if [[ -d ~/.local/share/backgrounds/Dynamic_Wallpapers ]]
then 
	rm -r ~/.local/share/backgrounds/Dynamic_Wallpapers
	echo "Setting up"
fi

echo "Installing wallpapers..."
cp -r ./Dynamic_Wallpapers/ ~/.local/share/backgrounds/
cp ./xml/* ~/.local/share/gnome-background-properties/
echo "Dynamic Wallpapers has been installed!"
echo "Deleting files used only for the installation process"
python3 $(pwd)/install_variants.py
cd ~
rm -r Linux_Dynamic_Wallpapers
echo "    |"
echo "    '---> Deleted unneeded files!"
echo "Now, don't forget to set your preferred dynamic wallpaper from Settings!"
