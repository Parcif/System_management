import os
import subprocess
import pyautogui as pag
import time
import sys


commands = ("off", "reboot", "update" )
print("\nВведите команду или help для просмотра доступных команд: ")
ans = input()

if (ans == "help"):
    print("\nДоступные команды:")
    for i in range (len(commands)):
        print(commands[i])

elif (ans == "off"):
    os.system('shutdown /p /f')  # sudo shutdown -h now на линуксе

elif (ans == "reboot"):
    os.system('shutdown -r -t 0')

elif (ans == "0"):
    #way = input("\nВведите путь локального репозитория: ")
    #x = subprocess.Popen(['start', 'cmd'], shell=True)
    #x.wait()

    #p2 = subprocess.run(["F:/GIIIIIIIT", "-c", "print('ocean')"])
    #os.system("cd F:")
    #os.system('cd "F:\Git123"')
    #res = subprocess.run('ls')

    #p1.wait()

    cmd2 = "git clone https://github.com/Parcif/Line_deleter"
    cmd= "git pull"
    #p2 = subprocess.run("cd C:\\Users\\Artem1\\Desktop\\testim", shell=True)

    os.chdir("C:\\Users\\Artem1\\Desktop\\Line_deleter")
    p3 = subprocess.run(cmd, shell=True)

    if p3.returncode==0:
        print("command success")
    #time.sleep(1)
    '''pag.typewrite("cd " + way)
    pag.press('enter')
    pag.typewrite("git push origin master")
    pag.press('enter')'''

else:
    print("\nНеизвеcтная команда!")





