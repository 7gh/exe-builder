import os

ok = input('Enter the file name > ')
try:
    os.system(f'pyinstaller --onefile {ok}')
except:
    os.system(f'py -m pip install pyinstaller')
    os.system(f'pyinstaller --onefile {ok}')
os.system('cls')
print('Done!')
input('')
