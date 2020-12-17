import html
import sys
import os
import glob
import shutil

def main():
    
    files = glob.glob('dirs/*.gml')
    f_name = files[0]
    print('f_name ',f_name)

    with open(f_name) as f:
        print('file read ...')
        before_text = f.read()
        print('DONE')
        print()
        print('Unescape start ...')
        fix_text = html.unescape(before_text)
        print('DONE')

        f_names = f_name.split('.')
        file_name = f_names[0]
        extension = f_names[1]

        with open(file_name + "-unescape." + extension, "w") as wf:
            wf.write(fix_text)

    shutil.move(f_name, "dirs/original")
    shutil.move(file_name + "-unescape." + extension, "dirs/escape")


if __name__ == '__main__':
    main()
