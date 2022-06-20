from functools import cache
import subprocess
import pysrt
from ast import Global
from PyQt5 import QtWidgets
from soupsieve import match
from sqlalchemy import false, null, true
from sympy import O
from app_window import Ui_MainWindow
import sys
from deep_translator import GoogleTranslator
from PyQt5.QtWidgets import QFileDialog, QLabel, QListWidgetItem
import random
from threading import Thread
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import re
minWin = True
myThred = Thread()
stopThread = False
paths = []
ui = Ui_MainWindow()
LastDirectory = ""


def thread():
    global myThred
    myThred = Thread(target=Func_trans, args=(paths,))
    myThred.start()


def do3a2_thread():
    Thread(target=do3a2_LCD,).start()


def Func_Open_Directory():
    pathlist = paths[0].split("/")[:-1]
    locationPath = '/'.join(map(str, pathlist))
    # print(locationPath)
    path = os.path.realpath(locationPath)
    os.startfile(path)


def Func_getPath():

    global paths
    global LastDirectory
    orginalpath = os.path.join(os.path.join(
        os.environ['USERPROFILE']), 'Desktop')
    ui.listofpaths.clear()
    if LastDirectory == "":
        LastDirectory = orginalpath
    # else:
    #   La
    #tempPath = r"D:\torrentsDownload\UNITY COURSES\Unity-VFX-Graph-Beginner-To-Intermediate\03 Orb Explosion"
    paths = QFileDialog.getOpenFileNames(
        filter="*.srt *.vtt", directory=LastDirectory)[0]

    f = open(paths[0])
    LastDirectory = os.path.dirname(f.name)
    f.close()

    for item in paths:
        item = item.split("/")[-1]
        QListWidgetItem(item, ui.listofpaths)
    pa = str(paths)[1:]
    pa = pa[:-1]
    ui.firstinfo.setPlaceholderText(pa)


def do3a2_LCD():
    do3a2 = ["اللهم إملأ  قبر أبي بالرضا و النور و الفسحة و السرور ", " اللهم إجعل قبره بنَعيمك إلى يوم يُبعث", "اللهم ارحم أبي واغفر لهُ و اضئ قبرهُ بنور الجنة، واجعل لقبره وملامحه نورًا إلى يوم يبعثون،", "اللهُم  ارحم من أصبحوا في ودائعك و برِّد عليهم قبورهم و أعفُ عنهم و أجعل الجنّه داراً لهم .", "اللهم ارحم أبي فقيد قلبي واغفرله وآنس وحشته ووسع قبره اللهم اجعل عيده في الجنة أجمل", "اللهمّ إنّ ابي كان يشهد أنّك لا إله إلّا أنت، وأنّ محمّدًا عبدك ورسولك، وأنت أعلم به.", "اللهمّ إنّا نتوسّل بك إليك، ونقسم بك عليك أن ترحم ابي ولا تعذّبه، وأن تثبّته عند السّؤال.", "اللهمّ إنّ ابي نَزَل بك وأنت خير منزولٍ به، وأصبح فقيرًا إلى رحمتك، وأنت غنيٌّ عن عذابه.",
             "اللهمّ أبدل ابي دارًا خيرًا من داره، وأهلًا خيرًا من أهله، وأدخله الجنّة، وأعذه من عذاب القبر، ومن عذاب النّار.", "اللهمّ عامله بما أنت أهله، ولا تعامله بما هو أهله.", "اللهمّ اجز ابي عن الإحسان إحسانًا، وعن الإساءة عفوًا وغفرانًا.", "اللهمّ إن كان ابي محسنًا فزد من حسناته، وإن كان مسيئًا فتجاوز عن سيّئاته.", "اللهمّ أدخل ابي الجنّة من غير مناقشة حساب، ولا سابقة عذاب.", "اللهمّ اّنس ابي في وحدته، وفي وحشته، وفي غربته.", "اللهمّ أنزل ابي منزلًا مباركًا، وأنت خير المنزلين.", "اللهمّ انقل ابي من مواطن الدّود، وضيق اللّحود، إلى جنّات الخلود.", "اللهم اجعل عن يمينه نورًا، حتّى تبعثه آمنًا مطمئنًّا في نورٍ من نورك.", "اللهمّ اجعل قبر ابي روضةً من رياض الجنّة، ولا تجعله حفرةً من حفر النّار.", "اللهمّ افسح لأبي في قبره مدّ بصره، وافرش قبره من فراش الجنّة."]
    random.shuffle(do3a2)

    ui.do3a2Text.setText("نسألكم الدعاء لابي رحمة الله عليه")
    time.sleep(5)
    while true:
        for do3a2_item in do3a2:
            time.sleep(4)
            ui.do3a2Text.setText(do3a2_item)
            if stopThread:
                break
        if stopThread:
            break


def ClearAndAddPath():
    ui.listViewFile.clear()


def Func_maximize():
    global minWin
    if minWin:
        MainWindow.showFullScreen()
        minWin = False
    else:
        MainWindow.showNormal()
        minWin = True


def CloseApp():
    global stopThread
    stopThread = True
    MainWindow.close()


def MinApp():
    MainWindow.showMinimized()


def About():
    ui.stackedWidget.setCurrentWidget(ui.about)  # SET PAGE
    # RESET ANOTHERS BUTTONS SELECTED


def Home():
    ui.stackedWidget.setCurrentWidget(ui.widgets)  # SET PAGE
    # RESET ANOTHERS BUTTONS SELECTED


def Func_trans(paths):
    ui.listViewFile.clear()
    fileIsSRT = False
    if paths:
        for path in paths:

            file_name = path.split("/")[-1]
            if file_name[-3:] == "srt":
                fileIsSRT = True
                QListWidgetItem("Translating  : " +
                                file_name, ui.listViewFile)
            else:
                QListWidgetItem("Translating  : " +
                                file_name[:-6], ui.listViewFile)
            QListWidgetItem("Wait Please ...", ui.listViewFile)
            listOfLineWillBeTranslate = []
            translated = []
            listOfLineWillBeTranslate = list()
            _translated = []
            finished = False
            listOfitemSize5000Translated = list()

            with open(path, encoding="utf-8") as f:
                for line in f:
                    line = line.rstrip()
                    if line != '':
                        line = line.replace('\n', '')
                        line = line.strip()
                        line = line.lower()
                        if not re.match(r'[0-1-2-3-4-5-6-7-8-9]{2}[:]{1}[0-1-2-3-4-5-6-7-8-9]{2}[:]{1}', line) and not re.match(r'\d+', line) and "-->" not in line or re.match(r'\d+\D{10}', line):
                            listOfLineWillBeTranslate.append(line)
            for x in listOfLineWillBeTranslate:
                if x == "WEBVTT":
                    listOfLineWillBeTranslate.remove(x)
            newlist = list()
            newitem = ' '
            for item in listOfLineWillBeTranslate:
                if len(newitem) == 0:
                    newitem = item
                else:
                    newitem = newitem + "   |   " + item
                if len(newitem) > 4500:
                    newlist.append(newitem)
                    newitem = ' '

            if len(newitem) > 0:  # grab any left over stuff that was <10 digits at the end
                newlist.append(newitem)
            targetLang = ''
            index_lang = ui.comboBox.currentIndex()
            if index_lang == 0:
                targetLang = 'ar'
            elif index_lang == 1:
                targetLang = 'fr'
            else:
                targetLang = 'en'
            for itemOfLineWillBeTranslate in newlist:
                lineTranslate = GoogleTranslator(
                    source='auto', target=targetLang).translate(itemOfLineWillBeTranslate)
                listOfitemSize5000Translated.append(lineTranslate)

            listOfLineshasBeenTranslate = list()
            _listOfLineshasBeenTranslate = list()
            listToStr = ''.join(str(e) for e in listOfitemSize5000Translated)

            _listOfLineshasBeenTranslate = listToStr.split("|")

            while("" in _listOfLineshasBeenTranslate):
                _listOfLineshasBeenTranslate.remove("")
            while(" " in _listOfLineshasBeenTranslate):
                _listOfLineshasBeenTranslate.remove(" ")
            for lineTrans in _listOfLineshasBeenTranslate:
                listOfLineshasBeenTranslate.append(lineTrans.strip())
            #n = 0
            # if n < len(listOfLineshasBeenTranslate)-1:
                #n = n+1
                # f.write(str(number)+"\n")
                #number = number+1
            List0fOtherLines = []
            if fileIsSRT:
                count = 0
                List0fOtherLines.append(count)
                with open(path, encoding="utf-8") as f:
                    for line in f:
                        line = line.replace('\n', '')
                        line = line.strip()
                        line = line.lower()

                        if re.match(r'[0-1-2-3-4-5-6-7-8-9]{2}[:]{1}[0-1-2-3-4-5-6-7-8-9]{2}[:]{1}', line) and "-->" in line:
                            count = count+1
                            List0fOtherLines.append(line)
                            List0fOtherLines.append(count)
            else:

                List0fOtherLines.append("WEBVTT")
                with open(path, encoding="utf-8") as f:
                    for line in f:
                        line = line.replace('\n', '')
                        line = line.strip()
                        line = line.lower()
                        if re.match(r'[0-1-2-3-4-5-6-7-8-9]{2}[:]{1}[0-1-2-3-4-5-6-7-8-9]{2}[:]{1}', line) and "-->" in line:
                            List0fOtherLines.append(line)
            while('' in List0fOtherLines):
                List0fOtherLines.remove('')
            index_other_Line = 0
            for LinehasBeenTranslate in listOfLineshasBeenTranslate:

                try:
                    translated.append(List0fOtherLines[index_other_Line])
                    index_other_Line = index_other_Line + 1
                    translated.append('\n')
                    translated.append('\n')
                    translated.append(List0fOtherLines[index_other_Line])
                except:
                    print("h")
                index_other_Line = index_other_Line + 1
                translated.append(LinehasBeenTranslate)
                translated.append('\n')
                translated.append('\n')
                finished = True
            for line in _translated:

                translated.append(line)

            if finished:
                if fileIsSRT:
                    #new_trans = addlineBetweenItem(translated, "\n")
                    # write srt file path[:-4]+"."+targetLang+".srt"

                    s = pysrt.SubRipFile(items=translated, encoding="utf-8")
                    if ".en" in path[-7:]:
                        s.save(path=path[:-6]+targetLang +
                               ".srt", encoding="utf-8")
                    else:
                        s.save(path=path[:-3]+targetLang +
                               ".srt", encoding="utf-8")
                    QListWidgetItem(
                        "Finished :  "+file_name[:-6]+targetLang+".srt", ui.listViewFile)
                    if path != paths[-1]:
                        QListWidgetItem(
                            "---------------------", ui.listViewFile)
                else:
                    # write srt file path[:-4]+"."+targetLang+".vtt"
                    s = pysrt.SubRipFile(items=translated, encoding="utf-8")
                    if ".en" in path[-7:]:
                        s.save(path=path[:-6]+targetLang +
                               ".vtt", encoding="utf-8")
                    else:
                        s.save(path=path[:-3]+targetLang +
                               ".vtt", encoding="utf-8")
                    QListWidgetItem(
                        "Translation Completed :  "+file_name[:-6]+targetLang+".vtt", ui.listViewFile)
                    if path != paths[-1]:
                        QListWidgetItem(
                            "---------------------", ui.listViewFile)
        QListWidgetItem(
            "------------------------------------------", ui.listViewFile)
        time.sleep(0.5)
        QListWidgetItem(
            "------------------------------------------", ui.listViewFile)
        time.sleep(0.5)
        QListWidgetItem(
            "All Tasks Have Been Done", ui.listViewFile)
        QListWidgetItem(
            "------------------------------------------", ui.listViewFile)
        time.sleep(0.5)
        QListWidgetItem(
            "------------------------------------------", ui.listViewFile)
        time.sleep(0.5)
        QListWidgetItem(
            "أسألكم الدعاء لأبي رحمة الله عليه", ui.listViewFile)
        time.sleep(0.5)
        QListWidgetItem(
            "------------------------------------------", ui.listViewFile)
        time.sleep(0.5)
        QListWidgetItem(
            "------------------------------------------", ui.listViewFile)
        Func_Open_Directory()
    else:
        QListWidgetItem(
            "------------------------------------------\n---------Please! Select Your Files First---------\n------------------------------------------\n", ui.listViewFile)
        time.sleep(1.5)
        ui.listViewFile.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    global ui
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    global paths
    ui.importbtn.clicked.connect(Func_getPath)
    ui.startbtn.clicked.connect(thread)
    ui.comboBox.activated.connect(ClearAndAddPath)
    ui.closeAppBtn.clicked.connect(CloseApp)
    ui.maximizeRestoreAppBtn.clicked.connect(Func_maximize)
    ui.minimizeAppBtn.clicked.connect(MinApp)
    ui.toggleLeftBox.clicked.connect(About)
    ui.toggleButton.clicked.connect(Home)
    MainWindow.show()
    do3a2_thread()
    sys.exit(app.exec_())


main()
