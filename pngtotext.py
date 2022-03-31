import glob
import subprocess
#from multiprocessing import Pool

png_files = glob.glob('./*.png')
names = [f[2:][:-4] for f in png_files]

def pngtotext(png_files, names):
    for (file, name) in zip(png_files, names):
        print("converting ", name)
        subprocess.run(['tesseract', file, name])

def concat_files(txt_files):
    txt_files.sort()

    data = ''
    for file in txt_files:
        with open(file, 'r+') as f:
            data += f.read()

    print(data)


'''
def conv(pair):
    (file, name) = pair
    print("converting ", name)
    subprocess.run(['tesseract', file, name]),

with Pool(8) as p:
    p.map(conv, zip(png_files, names))

'''

#pngtotext(png_files, names)

txt_files = glob.glob('./*.txt')
concat_files(txt_files)
