import os
import shutil

if __name__ == '__main__':
    packs = os.listdir('Dynamic_Wallpapers')
    for pack in packs:
        packname = pack
        pack = 'Dynamic_Wallpapers/' + pack
        if os.path.isfile(pack):
            continue
        if len(os.listdir(pack)) != 2:
            continue
        wallpapers = os.listdir(pack)
        try:
            os.makedirs(os.path.expanduser('~')+'/.local/share/wallpapers/'+packname+'/contents/images_dark')
            os.makedirs(os.path.expanduser('~')+'/.local/share/wallpapers/'+packname+'/contents/images')
            shutil.copy(pack+'/'+wallpapers[0], os.path.expanduser('~')+'/.local/share/wallpapers/'+packname+'/contents/images/5120x2880.png')
            shutil.copy(pack + '/' + wallpapers[1], os.path.expanduser('~') + '/.local/share/wallpapers/' + packname + '/contents/images_dark/5120x2880.png')
            with open(os.path.expanduser('~')+'/.local/share/wallpapers/'+packname+'/metadata.desktop', 'w') as metafile:
                metafile.write(f'[Desktop Entry]\nName={packname}\n')
        except:
            pass
