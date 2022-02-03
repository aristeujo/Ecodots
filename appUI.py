from assets import ui_assets
from PyQt5 import QtCore, QtGui, QtWidgets


class UiComponents(object):
    def build_ui(self, ecodots):

        self.userData = []

        ecodots.setObjectName("ecodots")
        ecodots.resize(800, 1280)
        ecodots.setMinimumSize(QtCore.QSize(0, 80))
        self.centralwidget = QtWidgets.QWidget(ecodots)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        # screenNavigation widget have to screens in it, one the homePage and the menuPage, and then the menuPage have futher Pages like the finalPage,FrPage, wasteDoorPage, rewardPage, contactPage
        self.screenNavigation = QtWidgets.QStackedWidget(self.centralwidget)
        self.screenNavigation.setObjectName("screenNavigation")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setStyleSheet("background-image: url(:/newPrefix/BG.png);")
        self.homePage.setObjectName("homePage")
        self.homePageMainFrame = QtWidgets.QFrame(self.homePage)
        self.homePageMainFrame.setGeometry(QtCore.QRect(0, 0, 800, 1280))
        self.homePageMainFrame.setStyleSheet("background:none;\n"
                                             "background-image: url(:/newPrefix/5.png);")
        self.homePageMainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.homePageMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.homePageMainFrame.setObjectName("homePageMainFrame")
        self.homePage_FRButton = QtWidgets.QLabel(self.homePageMainFrame)
        self.homePage_FRButton.setGeometry(QtCore.QRect(70, 980, 661, 211))
        self.homePage_FRButton.setStyleSheet("")
        self.homePage_FRButton.setText("")
        self.homePage_FRButton.setObjectName("homePage_FRButton")
        self.homePage_counterMainFrame = QtWidgets.QFrame(self.homePageMainFrame)
        self.homePage_counterMainFrame.setGeometry(QtCore.QRect(0, 455, 791, 421))
        self.homePage_counterMainFrame.setStyleSheet("border: none; background-image: url(:/newPrefix/coungbg.png);")
        # self.homePage_counterMainFrame.setStyleSheet("background-image: url(:/newPrefix/coungbg.png);")
        self.homePage_counterMainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.homePage_counterMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.homePage_counterMainFrame.setObjectName("homePage_counterMainFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.homePage_counterMainFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.homePage_counterBottomText = QtWidgets.QLabel(self.homePage_counterMainFrame)
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(14)
        self.homePage_counterBottomText.setFont(font)
        self.homePage_counterBottomText.setStyleSheet("background: none;\n"
                                                      "color: black;")
        self.homePage_counterBottomText.setAlignment(QtCore.Qt.AlignCenter)
        self.homePage_counterBottomText.setObjectName("homePage_counterBottomText")
        self.gridLayout_4.addWidget(self.homePage_counterBottomText, 7, 0, 1, 3)
        self.homePage_counterMilharesLabel = QtWidgets.QLabel(self.homePage_counterMainFrame)
        self.homePage_counterMilharesLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(12)
        self.homePage_counterMilharesLabel.setFont(font)
        self.homePage_counterMilharesLabel.setStyleSheet("background: none;\n"
                                                         "color:rgb(84,84,84);")
        self.homePage_counterMilharesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.homePage_counterMilharesLabel.setObjectName("homePage_counterMilharesLabel")
        self.gridLayout_4.addWidget(self.homePage_counterMilharesLabel, 6, 1, 1, 1)
        self.homePage_counterMilhoesLabel = QtWidgets.QLabel(self.homePage_counterMainFrame)
        self.homePage_counterMilhoesLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(12)
        self.homePage_counterMilhoesLabel.setFont(font)
        self.homePage_counterMilhoesLabel.setStyleSheet("background: none;\n"
                                                        "color:rgb(84,84,84);")
        self.homePage_counterMilhoesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.homePage_counterMilhoesLabel.setObjectName("homePage_counterMilhoesLabel")
        self.gridLayout_4.addWidget(self.homePage_counterMilhoesLabel, 6, 0, 1, 1)
        self.homePage_counterCentenasLabel = QtWidgets.QLabel(self.homePage_counterMainFrame)
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(12)
        self.homePage_counterCentenasLabel.setFont(font)
        self.homePage_counterCentenasLabel.setStyleSheet("background: none;\n"
                                                         "color:rgb(84,84,84);")
        self.homePage_counterCentenasLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.homePage_counterCentenasLabel.setObjectName("homePage_counterCentenasLabel")
        self.gridLayout_4.addWidget(self.homePage_counterCentenasLabel, 6, 2, 1, 1)
        self.homePage_CounterTitle = QtWidgets.QLabel(self.homePage_counterMainFrame)
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans Black")
        font.setPointSize(24)
        self.homePage_CounterTitle.setFont(font)
        self.homePage_CounterTitle.setStyleSheet("background: none;")
        self.homePage_CounterTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.homePage_CounterTitle.setObjectName("homePage_CounterTitle")
        self.gridLayout_4.addWidget(self.homePage_CounterTitle, 0, 0, 1, 3)
        self.homePage_counterHeading = QtWidgets.QLabel(self.homePage_counterMainFrame)
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(16)
        self.homePage_counterHeading.setFont(font)
        self.homePage_counterHeading.setStyleSheet("background: none;")
        self.homePage_counterHeading.setAlignment(QtCore.Qt.AlignCenter)
        self.homePage_counterHeading.setObjectName("homePage_counterHeading")
        self.gridLayout_4.addWidget(self.homePage_counterHeading, 1, 0, 1, 3)
        self.homePage_counterFrame = QtWidgets.QFrame(self.homePage_counterMainFrame)
        self.homePage_counterFrame.setEnabled(True)
        self.homePage_counterFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.homePage_counterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.homePage_counterFrame.setObjectName("homePage_counterFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.homePage_counterFrame)
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.homePage_counterMilhoes = QtWidgets.QLabel(self.homePage_counterFrame)
        self.homePage_counterMilhoes.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(80)
        self.homePage_counterMilhoes.setFont(font)
        self.homePage_counterMilhoes.setStyleSheet("color:white;\n"
                                                   "background: none;\n"
                                                   "background-color:rgb(84,84,84);\n"
                                                   "border-radius: 20px;\n"
                                                   "margin-left: 10px;")
        self.homePage_counterMilhoes.setAlignment(QtCore.Qt.AlignCenter)
        self.homePage_counterMilhoes.setObjectName("homePage_counterMilhoes")
        self.horizontalLayout.addWidget(self.homePage_counterMilhoes)
        self.homePage_counterMihares = QtWidgets.QLabel(self.homePage_counterFrame)
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(80)
        self.homePage_counterMihares.setFont(font)
        self.homePage_counterMihares.setStyleSheet("color:white;\n"
                                                   "background: none;\n"
                                                   "background-color:rgb(84,84,84);\n"
                                                   "border-radius: 20px;\n"
                                                   "")
        self.homePage_counterMihares.setAlignment(QtCore.Qt.AlignCenter)
        self.homePage_counterMihares.setObjectName("homePage_counterMihares")
        self.horizontalLayout.addWidget(self.homePage_counterMihares)
        self.homePage_counterCentenas = QtWidgets.QLabel(self.homePage_counterFrame)
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(80)
        self.homePage_counterCentenas.setFont(font)
        self.homePage_counterCentenas.setStyleSheet("color:white;\n"
                                                    "background: none;\n"
                                                    "background-color:rgb(84,84,84);\n"
                                                    "border-radius: 20px;\n"
                                                    "")
        self.homePage_counterCentenas.setAlignment(QtCore.Qt.AlignCenter)
        self.homePage_counterCentenas.setObjectName("homePage_counterCentenas")
        self.horizontalLayout.addWidget(self.homePage_counterCentenas)
        self.gridLayout_4.addWidget(self.homePage_counterFrame, 4, 0, 1, 3)
        self.homePage_counterBottomRightText = QtWidgets.QLabel(self.homePage_counterMainFrame)
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(8)
        self.homePage_counterBottomRightText.setFont(font)
        self.homePage_counterBottomRightText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.homePage_counterBottomRightText.setStyleSheet("background: none;\n"
                                                           "color:rgb(84,84,84);")
        self.homePage_counterBottomRightText.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.homePage_counterBottomRightText.setObjectName("homePage_counterBottomRightText")
        self.gridLayout_4.addWidget(self.homePage_counterBottomRightText, 8, 2, 1, 1)
        self.homePage_cityNameFrame = QtWidgets.QFrame(self.homePageMainFrame)
        self.homePage_cityNameFrame.setGeometry(QtCore.QRect(80, 40, 361, 91))
        self.homePage_cityNameFrame.setStyleSheet("border:none; background:none;")
        self.homePage_cityNameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.homePage_cityNameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.homePage_cityNameFrame.setObjectName("homePage_cityNameFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.homePage_cityNameFrame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.homePage_cityName = QtWidgets.QLabel(self.homePage_cityNameFrame)
        self.homePage_cityName.setMaximumSize(QtCore.QSize(16777214, 30))
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.homePage_cityName.setFont(font)
        self.homePage_cityName.setStyleSheet("color:white;\n"
                                             "margin-left:10px;")
        self.homePage_cityName.setObjectName("homePage_cityName")
        self.gridLayout_3.addWidget(self.homePage_cityName, 0, 0, 1, 3)
        self.homePage_whetherIcon = QtWidgets.QLabel(self.homePage_cityNameFrame)
        self.homePage_whetherIcon.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.homePage_whetherIcon.setFont(font)
        self.homePage_whetherIcon.setStyleSheet("background-image: url(:/newPrefix/weather.png);")
        self.homePage_whetherIcon.setText("")
        self.homePage_whetherIcon.setObjectName("homePage_whetherIcon")
        self.gridLayout_3.addWidget(self.homePage_whetherIcon, 1, 0, 2, 1)
        # self.homePage_temperatureUnit = QtWidgets.QLabel(self.homePage_cityNameFrame)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        # self.homePage_temperatureUnit.setFont(font)
        # self.homePage_temperatureUnit.setStyleSheet("color:white;")
        # self.homePage_temperatureUnit.setObjectName("homePage_temperatureUnit")
        # self.gridLayout_3.addWidget(self.homePage_temperatureUnit, 2, 2, 1, 1)
        self.homePage_temperature = QtWidgets.QLabel(self.homePage_cityNameFrame)
        self.homePage_temperature.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.homePage_temperature.setFont(font)
        self.homePage_temperature.setStyleSheet("color:white;")
        self.homePage_temperature.setObjectName("homePage_temperature")
        self.gridLayout_3.addWidget(self.homePage_temperature, 1, 1, 2, 1)
        self.homePage_dateTimeFrame = QtWidgets.QFrame(self.homePageMainFrame)
        self.homePage_dateTimeFrame.setGeometry(QtCore.QRect(150, 200, 460, 191))
        self.homePage_dateTimeFrame.setStyleSheet("border: none; background:none;")
        self.homePage_dateTimeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.homePage_dateTimeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.homePage_dateTimeFrame.setObjectName("homePage_dateTimeFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.homePage_dateTimeFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.homePage_time = QtWidgets.QLabel(self.homePage_dateTimeFrame)
        self.homePage_time.setMinimumSize(QtCore.QSize(350, 0))
        self.homePage_time.setMaximumSize(QtCore.QSize(457, 120))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(80)
        self.homePage_time.setFont(font)
        self.homePage_time.setStyleSheet("color:white;")
        self.homePage_time.setAlignment(QtCore.Qt.AlignCenter)
        self.homePage_time.setObjectName("homePage_time")
        self.verticalLayout.addWidget(self.homePage_time)
        self.homePage_date = QtWidgets.QLabel(self.homePage_dateTimeFrame)
        self.homePage_date.setMinimumSize(QtCore.QSize(440, 0))
        self.homePage_date.setMaximumSize(QtCore.QSize(458, 40))
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.homePage_date.setFont(font)
        self.homePage_date.setStyleSheet("color:white;")
        self.homePage_date.setAlignment(QtCore.Qt.AlignCenter)
        self.homePage_date.setObjectName("homePage_date")
        self.verticalLayout.addWidget(self.homePage_date)
        self.screenNavigation.addWidget(self.homePage)
        self.menuPage = QtWidgets.QWidget()
        self.menuPage.setStyleSheet("background-image: url(:/newPrefix/BG.png);\n"
                                    "background-repeat: none;")
        self.menuPage.setObjectName("menuPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.menuPage)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.menuFrame = QtWidgets.QFrame(self.menuPage)
        self.menuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuFrame.setObjectName("menuFrame")
        self.menuNavigation = QtWidgets.QStackedWidget(self.menuFrame)
        self.menuNavigation.setGeometry(QtCore.QRect(0, 120, 801, 1161))
        self.menuNavigation.setStyleSheet("background:none;\n"
                                          "background-image: url(:/newPrefix/shortRadius.png);")
        self.menuNavigation.setObjectName("menuNavigation")
        self.FRPage = QtWidgets.QWidget()
        self.FRPage.setStyleSheet("background-image: url(:/newPrefix/longRadius.png);\n"
                                  "background-repeat:none;")
        self.FRPage.setObjectName("FRPage")
        self.FRPage_FRFrame = QtWidgets.QFrame(self.FRPage)
        self.FRPage_FRFrame.setGeometry(QtCore.QRect(95, 200, 601, 421))
        self.FRPage_FRFrame.setStyleSheet("border:none; background:none;\n"
                                          "background-image: url(:/newPrefix/Webp.net-resizeimage (3).png);")
        self.FRPage_FRFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FRPage_FRFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRPage_FRFrame.setObjectName("FRPage_FRFrame")
        self.FR_imageContainer = QtWidgets.QFrame(self.FRPage_FRFrame)
        self.FR_imageContainer.setGeometry(QtCore.QRect(27, 21, 560, 381))
        self.FR_imageContainer.setStyleSheet("background:none;\n"
                                             "border-radius: 15px;\n"
                                             "border-image: url(assets/invest.png);")
        self.FR_imageContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FR_imageContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FR_imageContainer.setObjectName("FR_imageContainer")
        self.FRpage_Message = QtWidgets.QLabel(self.FRPage)
        self.FRpage_Message.setGeometry(QtCore.QRect(120, 660, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.FRpage_Message.setFont(font)
        self.FRpage_Message.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.FRpage_Message.setObjectName("FRpage_Message")
        self.FR_username = QtWidgets.QLabel(self.FRPage)
        self.FR_username.setGeometry(QtCore.QRect(120, 760, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.FR_username.setFont(font)
        self.FR_username.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.FR_username.setObjectName("FR_username")
        self.FRPageTitle = QtWidgets.QLabel(self.FRPage)
        self.FRPageTitle.setGeometry(QtCore.QRect(250, 60, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.FRPageTitle.setFont(font)
        self.FRPageTitle.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.FRPageTitle.setObjectName("FRPageTitle")
        self.FRPage_FRicon = QtWidgets.QLabel(self.FRPage)
        self.FRPage_FRicon.setGeometry(QtCore.QRect(90, 20, 161, 151))
        self.FRPage_FRicon.setStyleSheet("background-image: url(:/newPrefix/FR_icon.png);")
        self.FRPage_FRicon.setText("")
        self.FRPage_FRicon.setObjectName("FRPage_FRicon")
        self.menu_yesBtn = QtWidgets.QPushButton(self.FRPage)
        self.menu_yesBtn.setGeometry(QtCore.QRect(420, 860, 261, 121))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.menu_yesBtn.setFont(font)
        self.menu_yesBtn.setStyleSheet("QPushButton{\n"
                                  "background:none;\n"
                                  "color:white;\n"
                                  "    background-color: rgba(132,218,95, 1);\n"
                                  "    border: none;\n"
                                  "    border-radius: 20px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  " background-color: rgba(132,218,95, 0.8);\n"
                                  "}")
        self.menu_yesBtn.setObjectName("menu_yesBtn")
        self.menu_noBtn = QtWidgets.QPushButton(self.FRPage)
        self.menu_noBtn.setGeometry(QtCore.QRect(110, 860, 261, 121))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.menu_noBtn.setFont(font)
        self.menu_noBtn.setStyleSheet("QPushButton{\n"
                                 "background:none;\n"
                                 "color:white;\n"
                                 "    background-color: rgba(254,46,45, 1);\n"
                                 "    border: none;\n"
                                 "    border-radius: 20px;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 " background-color: rgba(254,46,45, 0.8);\n"
                                 "}")
        self.menu_noBtn.setObjectName("menu_noBtn")
        self.menu_yesBtn.raise_()
        self.FRPage_FRFrame.raise_()
        self.FRpage_Message.raise_()
        self.FR_username.raise_()
        self.FRPageTitle.raise_()
        self.FRPage_FRicon.raise_()
        self.menu_noBtn.raise_()
        self.menuNavigation.addWidget(self.FRPage)
        self.wasteDoorPage = QtWidgets.QWidget()
        self.wasteDoorPage.setStyleSheet("background-image: url(:/newPrefix/Webp.net-resizeimage (5).png);")
        self.wasteDoorPage.setObjectName("wasteDoorPage")
        self.wasteDoorPage_frame = QtWidgets.QFrame(self.wasteDoorPage)
        self.wasteDoorPage_frame.setGeometry(QtCore.QRect(90, 410, 601, 421))
        self.wasteDoorPage_frame.setStyleSheet("background:none;\n"
                                   "border:none;background-image: url(:/newPrefix/Webp.net-resizeimage (3).png);")
        self.wasteDoorPage_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wasteDoorPage_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wasteDoorPage_frame.setObjectName("frame_6")
        self.wasteDoorPage_gifContainer = QtWidgets.QFrame(self.wasteDoorPage_frame)
        self.wasteDoorPage_gifContainer.setGeometry(QtCore.QRect(27, 21, 560, 381))
        self.wasteDoorPage_gifContainer.setStyleSheet("background:none;\n"
                                                      "border-radius: 15px;\n"
                                                      "border-image: url(assets/invest.png);")
        self.wasteDoorPage_gifContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wasteDoorPage_gifContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wasteDoorPage_gifContainer.setObjectName("wasteDoorPage_gifContainer")
        self.wasteDoorPage_Username = QtWidgets.QLabel(self.wasteDoorPage)
        self.wasteDoorPage_Username.setGeometry(QtCore.QRect(120, 190, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.wasteDoorPage_Username.setFont(font)
        self.wasteDoorPage_Username.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.wasteDoorPage_Username.setObjectName("wasteDoorPage_Username")
        self.wateDoorPagemessage = QtWidgets.QLabel(self.wasteDoorPage)
        self.wateDoorPagemessage.setGeometry(QtCore.QRect(120, 240, 591, 101))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.wateDoorPagemessage.setFont(font)
        self.wateDoorPagemessage.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.wateDoorPagemessage.setObjectName("wateDoorPagemessage")

        # self.wasteDoorPageHomeBtn = QtWidgets.QPushButton(self.wasteDoorPage)
        # self.wasteDoorPageHomeBtn.setGeometry(QtCore.QRect(640, 1020, 101, 111))
        # self.wasteDoorPageHomeBtn.setStyleSheet("QPushButton{\n"
        #                                         "    background-image: url(:/newPrefix/house copy.png);\n"
        #                                         "background-repeat: none;\n"
        #                                         "color:white;\n"
        #                                         "    border: none;\n"
        #                                         "}")
        # self.wasteDoorPageHomeBtn.setText("")
        # self.wasteDoorPageHomeBtn.setObjectName("wasteDoorPageHomeBtn")
        # self.wasteDoorPageBackBtn = QtWidgets.QPushButton(self.wasteDoorPage)
        # self.wasteDoorPageBackBtn.setGeometry(QtCore.QRect(50, 1020, 101, 101))
        # self.wasteDoorPageBackBtn.setStyleSheet("QPushButton{\n"
        #                                         "    background-image: url(:/newPrefix/back.png);\n"
        #                                         "color:white;\n"
        #                                         "    border: none;\n"
        #                                         "    border-radius: 50px;\n"
        #                                         "}\n"
        #                                         "QPushButton:hover{\n"
        #                                         " background-color: rgba(255,255,255,0.5);\n"
        #                                         "}")
        # self.wasteDoorPageBackBtn.setText("")
        # self.wasteDoorPageBackBtn.setObjectName("wasteDoorPageBackBtn")

        self.menuNavigation.addWidget(self.wasteDoorPage)
        self.wastePage = QtWidgets.QWidget()
        self.wastePage.setStyleSheet("background-image: url(:/newPrefix/asdf.png);")
        self.wastePage.setObjectName("wastePage")
        self.wastePage_icon = QtWidgets.QLabel(self.wastePage)
        self.wastePage_icon.setGeometry(QtCore.QRect(130, 60, 101, 121))
        self.wastePage_icon.setStyleSheet("background-image: url(:/newPrefix/Webp.net-resizeimage (6).png);")
        self.wastePage_icon.setText("")
        self.wastePage_icon.setObjectName("wastePage_icon")
        self.wastePage_horizontalLine = QtWidgets.QLabel(self.wastePage)
        self.wastePage_horizontalLine.setGeometry(QtCore.QRect(90, 490, 611, 71))
        self.wastePage_horizontalLine.setStyleSheet("background-image: url(:/newPrefix/line.png);")
        self.wastePage_horizontalLine.setText("")
        self.wastePage_horizontalLine.setObjectName("wastePage_horizontalLine")
        self.weighing_username = QtWidgets.QLabel(self.wastePage)
        self.weighing_username.setGeometry(QtCore.QRect(110, 200, 591, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.weighing_username.setFont(font)
        self.weighing_username.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.weighing_username.setObjectName("weighing_username")
        self.wastePage_voceLabel = QtWidgets.QLabel(self.wastePage)
        self.wastePage_voceLabel.setGeometry(QtCore.QRect(110, 250, 591, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.wastePage_voceLabel.setFont(font)
        self.wastePage_voceLabel.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.wastePage_voceLabel.setObjectName("wastePage_voceLabel")
        self.wastePage_WasteValue = QtWidgets.QLabel(self.wastePage)
        self.wastePage_WasteValue.setGeometry(QtCore.QRect(260, 320, 301, 121))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(70)
        font.setBold(False)
        font.setWeight(50)
        self.wastePage_WasteValue.setFont(font)
        self.wastePage_WasteValue.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.wastePage_WasteValue.setObjectName("wastePage_WasteValue")
        self.wastePage_wasteUnit = QtWidgets.QLabel(self.wastePage)
        self.wastePage_wasteUnit.setGeometry(QtCore.QRect(190, 450, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.wastePage_wasteUnit.setFont(font)
        self.wastePage_wasteUnit.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.wastePage_wasteUnit.setObjectName("wastePage_wasteUnit")
        self.wastePage_metaAnnualLabel = QtWidgets.QLabel(self.wastePage)
        self.wastePage_metaAnnualLabel.setGeometry(QtCore.QRect(270, 570, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.wastePage_metaAnnualLabel.setFont(font)
        self.wastePage_metaAnnualLabel.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.wastePage_metaAnnualLabel.setObjectName("wastePage_metaAnnualLabel")
        self.wastePage_wasteTargetValue = QtWidgets.QLabel(self.wastePage)
        self.wastePage_wasteTargetValue.setGeometry(QtCore.QRect(220, 640, 171, 111))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(60)
        font.setBold(False)
        font.setWeight(50)
        self.wastePage_wasteTargetValue.setFont(font)
        self.wastePage_wasteTargetValue.setStyleSheet("background-image: url(:/newPrefix/trans.png);\n"
                                                      "")
        self.wastePage_wasteTargetValue.setObjectName("wastePage_wasteTargetValue")
        self.wastePage_totalTargetValue = QtWidgets.QLabel(self.wastePage)
        self.wastePage_totalTargetValue.setGeometry(QtCore.QRect(390, 680, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.wastePage_totalTargetValue.setFont(font)
        self.wastePage_totalTargetValue.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.wastePage_totalTargetValue.setObjectName("wastePage_totalTargetValue")
        self.wastePage_progressBar = QtWidgets.QProgressBar(self.wastePage)
        self.wastePage_progressBar.setGeometry(QtCore.QRect(120, 780, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wastePage_progressBar.setFont(font)
        self.wastePage_progressBar.setStyleSheet("QProgressBar{\n"
                                                 "Background: none;\n"
                                                 "Background-color: rgb(255, 222, 89);\n"
                                                 "color: rgb(0, 0, 0);\n"
                                                 "border-style: solid;\n"
                                                 "border: none;\n"
                                                 "border-radius:15px;\n"
                                                 "text-align: center;\n"
                                                 "}\n"
                                                 "QProgressBar::chunk{\n"
                                                 "border-radius:15px;\n"
                                                 "background-color: rgb(29, 179, 164);\n"
                                                 "}\n"
                                                 "")
        self.wastePage_progressBar.setProperty("value", 24)
        self.wastePage_progressBar.setObjectName("wastePage_progressBar")
        self.wastePageTitle = QtWidgets.QLabel(self.wastePage)
        self.wastePageTitle.setGeometry(QtCore.QRect(250, 60, 341, 111))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.wastePageTitle.setFont(font)
        self.wastePageTitle.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.wastePageTitle.setObjectName("wastePageTitle")

        # self.wastePage_BackBtn = QtWidgets.QPushButton(self.wastePage)
        # self.wastePage_BackBtn.setGeometry(QtCore.QRect(50, 1020, 101, 101))
        # self.wastePage_BackBtn.setStyleSheet("QPushButton{\n"
        #                                    "    background-image: url(:/newPrefix/back.png);\n"
        #                                    "color:white;\n"
        #                                    "    border: none;\n"
        #                                    "    border-radius: 50px;\n"
        #                                    "}\n"
        #                                    "QPushButton:hover{\n"
        #                                    " background-color: rgba(255,255,255,0.5);\n"
        #                                    "}")
        # self.wastePage_BackBtn.setText("")
        # self.wastePage_BackBtn.setObjectName("watePageBackBtn")
        # self.wastePage_HomeBtn = QtWidgets.QPushButton(self.wastePage)
        # self.wastePage_HomeBtn.setGeometry(QtCore.QRect(640, 1020, 101, 111))
        # self.wastePage_HomeBtn.setStyleSheet("QPushButton{\n"
        #                                    "    background-image: url(:/newPrefix/house copy.png);\n"
        #                                    "background-repeat: none;\n"
        #                                    "color:white;\n"
        #                                    "    border: none;\n"
        #                                    "}")
        # self.wastePage_HomeBtn.setText("")
        # self.wastePage_HomeBtn.setObjectName("watePageHomeBtn")

        self.menuNavigation.addWidget(self.wastePage)
        self.rewardPage = QtWidgets.QWidget()
        self.rewardPage.setObjectName("rewardPage")
        self.rewardPage_horizontalLine = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_horizontalLine.setGeometry(QtCore.QRect(90, 510, 611, 71))
        self.rewardPage_horizontalLine.setStyleSheet("background-image: url(:/newPrefix/line.png);")
        self.rewardPage_horizontalLine.setText("")
        self.rewardPage_horizontalLine.setObjectName("rewardPage_horizontalLine")
        self.rewardPage_username = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_username.setGeometry(QtCore.QRect(120, 200, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.rewardPage_username.setFont(font)
        self.rewardPage_username.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.rewardPage_username.setObjectName("rewardPage_username")
        self.rewardPage_voceLabel = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_voceLabel.setGeometry(QtCore.QRect(120, 240, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.rewardPage_voceLabel.setFont(font)
        self.rewardPage_voceLabel.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.rewardPage_voceLabel.setObjectName("rewardPage_voceLabel")
        self.rewardPage_Icon = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_Icon.setGeometry(QtCore.QRect(100, 40, 131, 141))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rewardPage_Icon.setFont(font)
        self.rewardPage_Icon.setStyleSheet("background-image: url(:/newPrefix/Webp.net-resizeimage (8).png);\n"
                                           "background-repeat:none;")
        self.rewardPage_Icon.setText("")
        self.rewardPage_Icon.setObjectName("rewardPage_Icon")
        self.rewardPageTitle = QtWidgets.QLabel(self.rewardPage)
        self.rewardPageTitle.setGeometry(QtCore.QRect(250, 50, 341, 111))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.rewardPageTitle.setFont(font)
        self.rewardPageTitle.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.rewardPageTitle.setLineWidth(1)
        self.rewardPageTitle.setObjectName("rewardPageTitle")
        self.rewardPage_EDLabel = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_EDLabel.setGeometry(QtCore.QRect(120, 330, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans SemiBold")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.rewardPage_EDLabel.setFont(font)
        self.rewardPage_EDLabel.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.rewardPage_EDLabel.setObjectName("rewardPage_EDLabel")
        self.rewardPage_rewardEDAmount = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_rewardEDAmount.setGeometry(QtCore.QRect(220, 310, 491, 141))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(70)
        font.setBold(False)
        font.setWeight(50)
        self.rewardPage_rewardEDAmount.setFont(font)
        self.rewardPage_rewardEDAmount.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.rewardPage_rewardEDAmount.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.rewardPage_rewardEDAmount.setObjectName("rewardPage_rewardEDAmount")
        self.rewardPage_emLabel = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_emLabel.setGeometry(QtCore.QRect(260, 470, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.rewardPage_emLabel.setFont(font)
        self.rewardPage_emLabel.setStyleSheet("")
        self.rewardPage_emLabel.setObjectName("rewardPage_emLabel")
        self.rewardPage_recomLable = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_recomLable.setGeometry(QtCore.QRect(315, 470, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.rewardPage_recomLable.setFont(font)
        self.rewardPage_recomLable.setStyleSheet("")
        self.rewardPage_recomLable.setObjectName("rewardPage_recomLable")
        self.rewardPage_resgateLabel = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_resgateLabel.setGeometry(QtCore.QRect(120, 610, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.rewardPage_resgateLabel.setFont(font)
        self.rewardPage_resgateLabel.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.rewardPage_resgateLabel.setObjectName("rewardPage_resgateLabel")
        self.rewardPage_RLabel = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_RLabel.setGeometry(QtCore.QRect(120, 690, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans SemiBold")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.rewardPage_RLabel.setFont(font)
        self.rewardPage_RLabel.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.rewardPage_RLabel.setObjectName("rewardPage_RLabel")
        self.rewardPage_redemptionValue = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_redemptionValue.setGeometry(QtCore.QRect(230, 680, 471, 141))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(70)
        font.setBold(False)
        font.setWeight(50)
        self.rewardPage_redemptionValue.setFont(font)
        self.rewardPage_redemptionValue.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.rewardPage_redemptionValue.setObjectName("rewardPage_redemptionValue")
        self.rewardPage_footerText = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_footerText.setGeometry(QtCore.QRect(100, 840, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.rewardPage_footerText.setFont(font)
        self.rewardPage_footerText.setStyleSheet("")
        self.rewardPage_footerText.setObjectName("rewardPage_footerText")
        self.rewardPage_footerEcodots = QtWidgets.QLabel(self.rewardPage)
        self.rewardPage_footerEcodots.setGeometry(QtCore.QRect(360, 840, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sauce Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.rewardPage_footerEcodots.setFont(font)
        self.rewardPage_footerEcodots.setStyleSheet("")
        self.rewardPage_footerEcodots.setObjectName("rewardPage_footerEcodots")

        # self.FR_errorBackBtn = QtWidgets.QPushButton(self.rewardPage)
        # self.FR_errorBackBtn.setGeometry(QtCore.QRect(50, 1020, 101, 101))
        # self.FR_errorBackBtn.setStyleSheet("QPushButton{\n"
        #                                    "    background-image: url(:/newPrefix/back.png);\n"
        #                                    "color:white;\n"
        #                                    "    border: none;\n"
        #                                    "    border-radius: 50px;\n"
        #                                    "}\n"
        #                                    "QPushButton:hover{\n"
        #                                    " background-color: rgba(255,255,255,0.5);\n"
        #                                    "}")
        # self.FR_errorBackBtn.setText("")
        # self.FR_errorBackBtn.setObjectName("FR_errorBackBtn")
        # self.FR_errorHomeBtn = QtWidgets.QPushButton(self.rewardPage)
        # self.FR_errorHomeBtn.setGeometry(QtCore.QRect(640, 1020, 101, 111))
        # self.FR_errorHomeBtn.setStyleSheet("QPushButton{\n"
        #                                    "    background-image: url(:/newPrefix/house copy.png);\n"
        #                                    "background-repeat: none;\n"
        #                                    "color:white;\n"
        #                                    "    border: none;\n"
        #                                    "}")
        # self.FR_errorHomeBtn.setText("")
        # self.FR_errorHomeBtn.setObjectName("FR_errorHomeBtn")

        self.menuNavigation.addWidget(self.rewardPage)
        self.finalPage = QtWidgets.QWidget()
        self.finalPage.setObjectName("finalPage")
        self.finalPage_icon = QtWidgets.QLabel(self.finalPage)
        self.finalPage_icon.setGeometry(QtCore.QRect(110, 50, 131, 101))
        self.finalPage_icon.setStyleSheet("background-image: url(:/newPrefix/tick.png);\n"
                                          "background-repeat:none;")
        self.finalPage_icon.setText("")
        self.finalPage_icon.setObjectName("finalPage_icon")
        self.finalPageTitle = QtWidgets.QLabel(self.finalPage)
        self.finalPageTitle.setGeometry(QtCore.QRect(260, 50, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.finalPageTitle.setFont(font)
        self.finalPageTitle.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.finalPageTitle.setObjectName("finalPageTitle")
        self.finalPage_username = QtWidgets.QLabel(self.finalPage)
        self.finalPage_username.setGeometry(QtCore.QRect(110, 210, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.finalPage_username.setFont(font)
        self.finalPage_username.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.finalPage_username.setObjectName("finalPage_username")
        self.finalPage_message = QtWidgets.QLabel(self.finalPage)
        self.finalPage_message.setGeometry(QtCore.QRect(110, 260, 331, 111))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.finalPage_message.setFont(font)
        self.finalPage_message.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.finalPage_message.setObjectName("finalPage_message")
        self.finalPage_ecodotsLogo = QtWidgets.QLabel(self.finalPage)
        self.finalPage_ecodotsLogo.setGeometry(QtCore.QRect(220, 470, 351, 271))
        self.finalPage_ecodotsLogo.setStyleSheet("background-image: url(:/newPrefix/logo1.png);")
        self.finalPage_ecodotsLogo.setText("")
        self.finalPage_ecodotsLogo.setObjectName("finalPage_ecodotsLogo")

        # self.finalPage_homeBtn = QtWidgets.QPushButton(self.finalPage)
        # self.finalPage_homeBtn.setGeometry(QtCore.QRect(640, 1020, 101, 111))
        # self.finalPage_homeBtn.setStyleSheet("QPushButton{\n"
        #                                      "    background-image: url(:/newPrefix/house copy.png);\n"
        #                                      "background-repeat: none;\n"
        #                                      "color:white;\n"
        #                                      "    border: none;\n"
        #                                      "}")
        # self.finalPage_homeBtn.setText("")
        # self.finalPage_homeBtn.setObjectName("finalPage_homeBtn")
        # self.finalPageBackBtn = QtWidgets.QPushButton(self.finalPage)
        # self.finalPageBackBtn.setGeometry(QtCore.QRect(50, 1020, 101, 101))
        # self.finalPageBackBtn.setStyleSheet("QPushButton{\n"
        #                                     "    background-image: url(:/newPrefix/back.png);\n"
        #                                     "color:white;\n"
        #                                     "    border: none;\n"
        #                                     "    border-radius: 50px;\n"
        #                                     "}\n"
        #                                     "QPushButton:hover{\n"
        #                                     " background-color: rgba(255,255,255,0.5);\n"
        #                                     "}")
        # self.finalPageBackBtn.setText("")
        # self.finalPageBackBtn.setObjectName("finalPageBackBtn")

        self.menuNavigation.addWidget(self.finalPage)
        self.FR_errorPage = QtWidgets.QWidget()
        self.FR_errorPage.setObjectName("FR_errorPage")
        self.FRerrorPage_errorImagecontainer = QtWidgets.QFrame(self.FR_errorPage)
        self.FRerrorPage_errorImagecontainer.setGeometry(QtCore.QRect(90, 220, 601, 421))
        self.FRerrorPage_errorImagecontainer.setStyleSheet("background:none;\n"
                                                           "background-image: url(:/newPrefix/Webp.net-resizeimage (3).png);")
        self.FRerrorPage_errorImagecontainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FRerrorPage_errorImagecontainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRerrorPage_errorImagecontainer.setObjectName("FRerrorPage_errorImagecontainer")
        self.FRerrorPage_errorImage = QtWidgets.QFrame(self.FRerrorPage_errorImagecontainer)
        self.FRerrorPage_errorImage.setGeometry(QtCore.QRect(160, 80, 261, 261))
        self.FRerrorPage_errorImage.setStyleSheet("\n"
                                                  "background-image: url(:/newPrefix/alert.png);")
        self.FRerrorPage_errorImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FRerrorPage_errorImage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRerrorPage_errorImage.setObjectName("FRerrorPage_errorImage")
        self.FRerrorPage_Icon = QtWidgets.QLabel(self.FR_errorPage)
        self.FRerrorPage_Icon.setGeometry(QtCore.QRect(100, 30, 161, 151))
        self.FRerrorPage_Icon.setStyleSheet("background-image: url(:/newPrefix/FR_icon.png);")
        self.FRerrorPage_Icon.setText("")
        self.FRerrorPage_Icon.setObjectName("FRerrorPage_Icon")
        self.FRerrorPage_errorMessage = QtWidgets.QLabel(self.FR_errorPage)
        self.FRerrorPage_errorMessage.setGeometry(QtCore.QRect(120, 680, 271, 181))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.FRerrorPage_errorMessage.setFont(font)
        self.FRerrorPage_errorMessage.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.FRerrorPage_errorMessage.setObjectName("FRerrorPage_errorMessage")
        self.FRerrorPage_Title = QtWidgets.QLabel(self.FR_errorPage)
        self.FRerrorPage_Title.setGeometry(QtCore.QRect(260, 60, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.FRerrorPage_Title.setFont(font)
        self.FRerrorPage_Title.setStyleSheet("background-image: url(:/newPrefix/trans.png);")
        self.FRerrorPage_Title.setObjectName("FRerrorPage_Title")
        self.FR_errorBack = QtWidgets.QPushButton(self.FR_errorPage)
        self.FR_errorBack.setGeometry(QtCore.QRect(50, 1020, 101, 101))
        self.FR_errorBack.setStyleSheet("QPushButton{\n"
                                        "    background-image: url(:/newPrefix/back.png);\n"
                                        "color:white;\n"
                                        "    border: none;\n"
                                        "    border-radius: 50px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        " background-color: rgba(255,255,255,0.5);\n"
                                        "}")
        self.FR_errorBack.setText("")
        self.FR_errorBack.setObjectName("FR_errorBack")
        self.FR_errorHome = QtWidgets.QPushButton(self.FR_errorPage)
        self.FR_errorHome.setGeometry(QtCore.QRect(640, 1020, 101, 111))
        self.FR_errorHome.setStyleSheet("QPushButton{\n"
                                        "    background-image: url(:/newPrefix/house copy.png);\n"
                                        "background-repeat: none;\n"
                                        "color:white;\n"
                                        "    border: none;\n"
                                        "}")
        self.FR_errorHome.setText("")
        self.FR_errorHome.setObjectName("FR_errorHome")
        self.menuNavigation.addWidget(self.FR_errorPage)
        self.contactPage = QtWidgets.QWidget()
        self.contactPage.setObjectName("contactPage")
        self.contactPage_Title = QtWidgets.QLabel(self.contactPage)
        self.contactPage_Title.setGeometry(QtCore.QRect(280, 60, 351, 101))
        self.contactPage_Title.setStyleSheet("background-image: url(:/newPrefix/ezgif-6-41bfaeb68d77.png);")
        self.contactPage_Title.setText("")
        self.contactPage_Title.setObjectName("contactPage_Title")
        self.contactPage_icon = QtWidgets.QLabel(self.contactPage)
        self.contactPage_icon.setGeometry(QtCore.QRect(120, 60, 131, 111))
        self.contactPage_icon.setStyleSheet("background-image: url(:/newPrefix/ezgif-6-9d38daa47a89.png);")
        self.contactPage_icon.setText("")
        self.contactPage_icon.setObjectName("contactPage_icon")
        self.number_lineEdit = QtWidgets.QLineEdit(self.contactPage)
        self.number_lineEdit.setValidator(QtGui.QIntValidator())
        self.number_lineEdit.setGeometry(QtCore.QRect(130, 210, 541, 95))
        self.number_lineEdit.setMinimumSize(QtCore.QSize(0, 95))
        self.number_lineEdit.setMaximumSize(QtCore.QSize(16777215, 95))
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.number_lineEdit.setFont(font)
        self.number_lineEdit.setStyleSheet("border:2px solid;\n"
                                           "border-radius:10px;")
        self.number_lineEdit.setText("")
        self.number_lineEdit.setMaxLength(15)
        self.number_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.number_lineEdit.setObjectName("number_lineEdit")

        # self.contactPageBackBtn = QtWidgets.QPushButton(self.contactPage)
        # self.contactPageBackBtn.setGeometry(QtCore.QRect(50, 1020, 101, 101))
        # self.contactPageBackBtn.setStyleSheet("QPushButton{\n"
        #                                       "    background-image: url(:/newPrefix/back.png);\n"
        #                                       "color:white;\n"
        #                                       "    border: none;\n"
        #                                       "    border-radius: 50px;\n"
        #                                       "}\n"
        #                                       "QPushButton:hover{\n"
        #                                       " background-color: rgba(255,255,255,0.5);\n"
        #                                       "}")
        # self.contactPageBackBtn.setText("")
        # self.contactPageBackBtn.setObjectName("contactPageBackBtn")

        # self.contactPageHomeBtn = QtWidgets.QPushButton(self.contactPage)
        # self.contactPageHomeBtn.setGeometry(QtCore.QRect(640, 1020, 101, 111))
        # self.contactPageHomeBtn.setStyleSheet("QPushButton{\n"
        #                                       "    background-image: url(:/newPrefix/house copy.png);\n"
        #                                       "background-repeat: none;\n"
        #                                       "color:white;\n"
        #                                       "    border: none;\n"
        #                                       "}")
        # self.contactPageHomeBtn.setText("")
        # self.contactPageHomeBtn.setObjectName("contactPageHomeBtn")
        self.contactPage_dialPadFrame = QtWidgets.QFrame(self.contactPage)
        self.contactPage_dialPadFrame.setGeometry(QtCore.QRect(145, 330, 511, 491))
        self.contactPage_dialPadFrame.setStyleSheet("background:none;")
        self.contactPage_dialPadFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contactPage_dialPadFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contactPage_dialPadFrame.setObjectName("contactPage_dialPadFrame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.contactPage_dialPadFrame)
        self.gridLayout_6.setSpacing(20)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.dial_7 = QtWidgets.QPushButton(self.contactPage_dialPadFrame)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.dial_7.setFont(font)
        self.dial_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_7.setStyleSheet("QPushButton{\n"
                                  "background:none;\n"
                                  "     background-color: rgba(255,255,255, 1);\n"
                                  "background-repeat:none;\n"
                                  " border: 1px solid;\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  " background-color: rgba(0,0,0, 0.1);\n"
                                  "}")
        self.dial_7.setIconSize(QtCore.QSize(65, 65))
        self.dial_7.setObjectName("dial_7")
        self.gridLayout_6.addWidget(self.dial_7, 2, 0, 1, 1)
        self.dial_4 = QtWidgets.QPushButton(self.contactPage_dialPadFrame)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.dial_4.setFont(font)
        self.dial_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_4.setStyleSheet("QPushButton{\n"
                                  "background:none;\n"
                                  "     background-color: rgba(255,255,255, 1);\n"
                                  "background-repeat:none;\n"
                                  " border: 1px solid;\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  " background-color: rgba(0,0,0, 0.1);\n"
                                  "}")
        self.dial_4.setIconSize(QtCore.QSize(65, 65))
        self.dial_4.setObjectName("dial_4")
        self.gridLayout_6.addWidget(self.dial_4, 1, 0, 1, 1)
        self.dial_1 = QtWidgets.QPushButton(self.contactPage_dialPadFrame)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.dial_1.setFont(font)
        self.dial_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_1.setStyleSheet("QPushButton{\n"
                                  "background:none;\n"
                                  "     background-color: rgba(255,255,255, 1);\n"
                                  "background-repeat:none;\n"
                                  " border: 1px solid;\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  " background-color: rgba(0,0,0, 0.1);\n"
                                  "}")
        self.dial_1.setIconSize(QtCore.QSize(65, 65))
        self.dial_1.setObjectName("dial_1")
        self.gridLayout_6.addWidget(self.dial_1, 0, 0, 1, 1)
        self.dial_6 = QtWidgets.QPushButton(self.contactPage_dialPadFrame)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.dial_6.setFont(font)
        self.dial_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_6.setStyleSheet("QPushButton{\n"
                                  "background:none;\n"
                                  "     background-color: rgba(255,255,255, 1);\n"
                                  "background-repeat:none;\n"
                                  " border: 1px solid;\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  " background-color: rgba(0,0,0, 0.1);\n"
                                  "}")
        self.dial_6.setIconSize(QtCore.QSize(65, 65))
        self.dial_6.setObjectName("dial_6")
        self.gridLayout_6.addWidget(self.dial_6, 1, 2, 1, 1)
        self.dial_9 = QtWidgets.QPushButton(self.contactPage_dialPadFrame)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.dial_9.setFont(font)
        self.dial_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_9.setStyleSheet("QPushButton{\n"
                                  "background:none;\n"
                                  "     background-color: rgba(255,255,255, 1);\n"
                                  "background-repeat:none;\n"
                                  " border: 1px solid;\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  " background-color: rgba(0,0,0, 0.1);\n"
                                  "}")
        self.dial_9.setIconSize(QtCore.QSize(65, 65))
        self.dial_9.setObjectName("dial_9")
        self.gridLayout_6.addWidget(self.dial_9, 2, 2, 1, 1)
        self.dial_0 = QtWidgets.QPushButton(self.contactPage_dialPadFrame)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.dial_0.setFont(font)
        self.dial_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_0.setStyleSheet("QPushButton{\n"
                                  "background:none;\n"
                                  "     background-color: rgba(255,255,255, 1);\n"
                                  "background-repeat:none;\n"
                                  " border: 1px solid;\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  " background-color: rgba(0,0,0, 0.1);\n"
                                  "}")
        self.dial_0.setIconSize(QtCore.QSize(65, 65))
        self.dial_0.setObjectName("dial_0")
        self.gridLayout_6.addWidget(self.dial_0, 3, 1, 1, 1)
        self.dial_2 = QtWidgets.QPushButton(self.contactPage_dialPadFrame)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.dial_2.setFont(font)
        self.dial_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_2.setStyleSheet("QPushButton{\n"
                                  "background:none;\n"
                                  "     background-color: rgba(255,255,255, 1);\n"
                                  "background-repeat:none;\n"
                                  " border: 1px solid;\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  " background-color: rgba(0,0,0, 0.1);\n"
                                  "}")
        self.dial_2.setIconSize(QtCore.QSize(65, 65))
        self.dial_2.setObjectName("dial_2")
        self.gridLayout_6.addWidget(self.dial_2, 0, 1, 1, 1)
        self.dial_ok = QtWidgets.QPushButton(self.contactPage_dialPadFrame)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.dial_ok.setFont(font)
        self.dial_ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_ok.setStyleSheet("QPushButton{\n"
                                   "color:white;\n"
                                   "background:none;\n"
                                   "     background-color: rgba(132,218,95, 1);\n"
                                   "background-repeat:none;\n"
                                   " border: 1px solid;\n"
                                   "    border-radius: 5px;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   " background-color: rgba(0,0,0, 0.1);\n"
                                   "}")
        self.dial_ok.setIconSize(QtCore.QSize(65, 65))
        self.dial_ok.setObjectName("dial_ok")
        self.gridLayout_6.addWidget(self.dial_ok, 3, 0, 1, 1)
        self.dial_5 = QtWidgets.QPushButton(self.contactPage_dialPadFrame)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.dial_5.setFont(font)
        self.dial_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_5.setStyleSheet("QPushButton{\n"
                                  "background:none;\n"
                                  "     background-color: rgba(255,255,255, 1);\n"
                                  "background-repeat:none;\n"
                                  " border: 1px solid;\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  " background-color: rgba(0,0,0, 0.1);\n"
                                  "}")
        self.dial_5.setIconSize(QtCore.QSize(65, 65))
        self.dial_5.setObjectName("dial_5")
        self.gridLayout_6.addWidget(self.dial_5, 1, 1, 1, 1)
        self.dial_8 = QtWidgets.QPushButton(self.contactPage_dialPadFrame)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.dial_8.setFont(font)
        self.dial_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_8.setStyleSheet("QPushButton{\n"
                                  "background:none;\n"
                                  "     background-color: rgba(255,255,255, 1);\n"
                                  "background-repeat:none;\n"
                                  " border: 1px solid;\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  " background-color: rgba(0,0,0, 0.1);\n"
                                  "}")
        self.dial_8.setIconSize(QtCore.QSize(65, 65))
        self.dial_8.setObjectName("dial_8")
        self.gridLayout_6.addWidget(self.dial_8, 2, 1, 1, 1)
        self.dial_3 = QtWidgets.QPushButton(self.contactPage_dialPadFrame)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.dial_3.setFont(font)
        self.dial_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_3.setStyleSheet("QPushButton{\n"
                                  "background:none;\n"
                                  "     background-color: rgba(255,255,255, 1);\n"
                                  "background-repeat:none;\n"
                                  " border: 1px solid;\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  " background-color: rgba(0,0,0, 0.1);\n"
                                  "}")
        self.dial_3.setIconSize(QtCore.QSize(65, 65))
        self.dial_3.setObjectName("dial_3")
        self.gridLayout_6.addWidget(self.dial_3, 0, 2, 1, 1)
        self.dial_backspace = QtWidgets.QPushButton(self.contactPage_dialPadFrame)
        self.dial_backspace.setEnabled(True)
        self.dial_backspace.setMinimumSize(QtCore.QSize(0, 75))
        self.dial_backspace.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.dial_backspace.setFont(font)
        self.dial_backspace.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dial_backspace.setStyleSheet("QPushButton{\n"
                                          "background:none;\n"
                                          "     background-color: rgba(255,255,255, 1);\n"
                                          "background-repeat:none;\n"
                                          " border: 1px solid;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          " background-color: rgba(0,0,0, 0.1);\n"
                                          "}")
        self.dial_backspace.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/backspace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dial_backspace.setIcon(icon)
        self.dial_backspace.setIconSize(QtCore.QSize(65, 65))
        self.dial_backspace.setObjectName("dial_backspace")
        self.gridLayout_6.addWidget(self.dial_backspace, 3, 2, 1, 1)
        self.menuNavigation.addWidget(self.contactPage)
        self.frame = QtWidgets.QFrame(self.menuFrame)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 121))
        self.frame.setStyleSheet("border:none;background:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.homePage_cityNameFrame_2 = QtWidgets.QFrame(self.frame)
        self.homePage_cityNameFrame_2.setMaximumSize(QtCore.QSize(250, 90))
        self.homePage_cityNameFrame_2.setStyleSheet("background:none;")
        self.homePage_cityNameFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.homePage_cityNameFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.homePage_cityNameFrame_2.setObjectName("homePage_cityNameFrame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.homePage_cityNameFrame_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.menu_cityName = QtWidgets.QLabel(self.homePage_cityNameFrame_2)
        self.menu_cityName.setMaximumSize(QtCore.QSize(16777214, 30))
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.menu_cityName.setFont(font)
        self.menu_cityName.setStyleSheet("color:white;\n"
                                         "border:none;margin-left:10px;")
        self.menu_cityName.setObjectName("menu_cityName")
        self.gridLayout_5.addWidget(self.menu_cityName, 0, 0, 1, 3)
        self.menu_whetherIcon = QtWidgets.QLabel(self.homePage_cityNameFrame_2)
        self.menu_whetherIcon.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.menu_whetherIcon.setFont(font)
        self.menu_whetherIcon.setStyleSheet("background-image: url(:/newPrefix/weather.png);")
        self.menu_whetherIcon.setText("")
        self.menu_whetherIcon.setObjectName("menu_whetherIcon")
        self.gridLayout_5.addWidget(self.menu_whetherIcon, 1, 0, 2, 1)
        self.menu_temperature = QtWidgets.QLabel(self.homePage_cityNameFrame_2)
        self.menu_temperature.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.menu_temperature.setFont(font)
        self.menu_temperature.setStyleSheet("color:white;")
        self.menu_temperature.setObjectName("menu_temperature")
        self.gridLayout_5.addWidget(self.menu_temperature, 1, 1, 2, 1)
        # self.menu_temperatureUnit = QtWidgets.QLabel(self.homePage_cityNameFrame_2)
        font = QtGui.QFont()
        font.setFamily("Mont Heavy DEMO")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        # self.menu_temperatureUnit.setFont(font)
        # self.menu_temperatureUnit.setStyleSheet("color:white;")
        # self.menu_temperatureUnit.setObjectName("menu_temperatureUnit")
        # self.gridLayout_5.addWidget(self.menu_temperatureUnit, 2, 2, 1, 1)
        self.horizontalLayout_2.addWidget(self.homePage_cityNameFrame_2)
        self.menu_time = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(45)
        self.menu_time.setFont(font)
        self.menu_time.setStyleSheet("color:white;\n"
                                     "background: none;\n"
                                     "margin-left: 20px;")
        self.menu_time.setObjectName("menu_time")
        self.horizontalLayout_2.addWidget(self.menu_time)
        # self.menu_supportBtn = QtWidgets.QPushButton(self.frame)
        # self.menu_supportBtn.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        # self.menu_supportBtn.setFont(font)
        # self.menu_supportBtn.setStyleSheet("QPushButton{\n"
        #                               "background:none;\n"
        #                               "color:white;\n"
        #                               "    background-color: none;\n"
        #                               "    border: 4px solid;\n"
        #                               "    border-radius: 10px;\n"
        #                               "border-color:white;\n"
        #                               "}\n"
        #                               "QPushButton:hover{\n"
        #                               " background-color: rgba(0,0,0, 0.1);\n"
        #                               "}")
        # self.menu_supportBtn.setObjectName("menu_supportBtn")
        # self.horizontalLayout_2.addWidget(self.menu_supportBtn)
        self.gridLayout_2.addWidget(self.menuFrame, 0, 0, 1, 1)
        self.screenNavigation.addWidget(self.menuPage)
        self.gridLayout.addWidget(self.screenNavigation, 0, 0, 1, 1)
        ecodots.setCentralWidget(self.centralwidget)

        self.retranslate_ui(ecodots)
        self.screenNavigation.setCurrentIndex(0)
        self.menuNavigation.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ecodots)

    def retranslate_ui(self, ecodots):
        _translate = QtCore.QCoreApplication.translate
        ecodots.setWindowTitle(_translate("ecodots", "MainWindow"))
        self.homePage_counterBottomText.setText(
            _translate("ecodots", "de toneladas produzidas entre 01/jan à 9/set de 2021."))
        self.homePage_counterMilharesLabel.setText(_translate("ecodots", "milhares"))
        self.homePage_counterMilhoesLabel.setText(_translate("ecodots", "      milhões "))
        self.homePage_counterCentenasLabel.setText(_translate("ecodots", "centenas"))
        self.homePage_CounterTitle.setText(_translate("ecodots", "Residuômetro: Brasil"))
        self.homePage_counterHeading.setText(
            _translate("ecodots", "Produção de Resíduos Sólidos em Centros Urbanos"))
        self.homePage_counterMilhoes.setText(_translate("ecodots", "00"))
        self.homePage_counterMihares.setText(_translate("ecodots", "000"))
        self.homePage_counterCentenas.setText(_translate("ecodots", "000"))
        self.homePage_counterBottomRightText.setText(_translate("ecodots", "Fonte: IBGE, e-REVERSE e Abrelpe."))
        self.homePage_cityName.setText(_translate("ecodots", "Manaus"))
        # self.homePage_temperatureUnit.setText(_translate("ecodots", "°C"))
        self.homePage_temperature.setText(_translate("ecodots", "99"))
        self.homePage_time.setText(_translate("ecodots", "99:99"))
        self.homePage_date.setText(_translate("ecodots", "Quinta-feira, 9 de setembro"))
        self.FRpage_Message.setText(_translate("ecodots", "Olá,\n"
                                                             "Você é:"))
        self.FR_username.setText(_translate("ecodots", "Usuário_teste?"))
        self.FRPageTitle.setText(_translate("ecodots", "Reconhecimento\n"
                                                          "Facial"))
        self.menu_yesBtn.setText(_translate("ecodots", "SIM"))
        self.menu_noBtn.setText(_translate("ecodots", "NÃO"))
        self.wasteDoorPage_Username.setText(_translate("ecodots", "Usuario_test,"))
        self.wateDoorPagemessage.setText(_translate("ecodots", "Deposite seus\n"
                                                                  "resíduos recicláveis"))
        self.weighing_username.setText(_translate("ecodots", "Usuario_teste, "))
        self.wastePage_voceLabel.setText(_translate("ecodots", "Você depositou:"))
        self.wastePage_WasteValue.setText(_translate("ecodots", "1,35"))
        self.wastePage_wasteUnit.setText(_translate("ecodots", "kg de resíduos recicláveis"))
        self.wastePage_metaAnnualLabel.setText(_translate("ecodots", "Meta Anual:"))
        self.wastePage_wasteTargetValue.setText(_translate("ecodots", "35"))
        self.wastePage_totalTargetValue.setText(_translate("ecodots", "/350"))
        self.wastePageTitle.setText(_translate("ecodots", "Pesagem &\n"
                                                             "Recompensa"))
        self.rewardPage_username.setText(_translate("ecodots", "usernameTest"))
        self.rewardPage_voceLabel.setText(_translate("ecodots", "Você receberá:"))
        self.rewardPageTitle.setText(_translate("ecodots", "Recompensa & \n"
                                                              "Resgate"))
        self.rewardPage_EDLabel.setText(_translate("ecodots", "ED$"))
        self.rewardPage_rewardEDAmount.setText(_translate("ecodots", "168,75"))
        self.rewardPage_emLabel.setText(_translate("ecodots", "em"))
        self.rewardPage_recomLable.setText(_translate("ecodots", "recompensas."))
        self.rewardPage_resgateLabel.setText(_translate("ecodots", "Resgate até:"))
        self.rewardPage_RLabel.setText(_translate("ecodots", "R$"))
        self.rewardPage_redemptionValue.setText(_translate("ecodots", "0,65"))
        self.rewardPage_footerText.setText(_translate("ecodots", "em descontos no"))
        self.rewardPage_footerEcodots.setText(_translate("ecodots", "Marketplace Ecodots®"))
        self.finalPageTitle.setText(_translate("ecodots", "Operação\n"
                                                             "Finalizada!"))
        self.finalPage_username.setText(_translate("ecodots", "Usuário,"))
        self.finalPage_message.setText(_translate("ecodots", "Parabéns e\n"
                                                                "Muito Obrigada!"))
        self.FRerrorPage_errorMessage.setText(_translate("ecodots", "Erro!,\n"
                                                                       "Usuário não\n"
                                                                       "identificado!"))
        self.FRerrorPage_Title.setText(_translate("ecodots", "Operação\n"
                                                                "Finalizada!\n"
                                                                ""))
        self.dial_7.setText(_translate("ecodots", "7"))
        self.dial_4.setText(_translate("ecodots", "4"))
        self.dial_1.setText(_translate("ecodots", "1"))
        self.dial_6.setText(_translate("ecodots", "6"))
        self.dial_9.setText(_translate("ecodots", "9"))
        self.dial_0.setText(_translate("ecodots", "0"))
        self.dial_2.setText(_translate("ecodots", "2"))
        self.dial_ok.setText(_translate("ecodots", "OK"))
        self.dial_5.setText(_translate("ecodots", "5"))
        self.dial_8.setText(_translate("ecodots", "8"))
        self.dial_3.setText(_translate("ecodots", "3"))

        self.menu_cityName.setText(_translate("ecodots", "Noppe"))
        self.menu_temperature.setText(_translate("ecodots", "99"))
        # self.menu_temperatureUnit.setText(_translate("ecodots", "°C"))
        self.menu_time.setText(_translate("ecodots", "12:00"))
        # self.menu_supportBtn.setText(_translate("ecodots", "Support"))
