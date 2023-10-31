import subprocess


if __name__ == '__main__':
    print(subprocess.run(['wc','-l','../clown.txt']))
    print(subprocess.run(['gnome-terminal']))

