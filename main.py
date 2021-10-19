import os
from shutil import copyfile
from pydub import AudioSegment, effects

src = input('Please type the root directory of the music folder: ')
dst = input('Please type the destination directory: ')

src = os.path.abspath(src)
src_prefix = len(src) + len(os.path.sep)
os.makedirs(dst)
print(src)
for root, dirs, files in os.walk(src):
    print('files:' , files)
    for dirname in dirs:
        dirpath = os.path.join(dst, root[src_prefix:], dirname)
        dirpathroot = os.path.join(src, root[src_prefix:], dirname)
        os.mkdir(dirpath)
    for songs in files:
        songformat = songs.partition('.')[-1]
        while songformat.count('.') > 0:
            songformat = songformat.partition('.')[-1]
            if songformat.count('.') == 0:
                break
        songname = songs.partition(songformat)[0]
        rawsound = AudioSegment.from_file(dirpathroot+'\\'+songs, songformat)  
        normalizedsound = effects.normalize(rawsound)  
        normalizedsound.export(dirpath+'\\'+songs, format=songformat)


