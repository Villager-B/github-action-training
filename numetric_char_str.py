import html
import sys


def main():
    try:
        f_name = sys.argv[1]
    except BaseException:
        print('Please Write your file name')
        print('''Useage :
         python numetric_char_str.py [file name]
        ''')
        sys.exit(0)

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


if __name__ == '__main__':
    main()
