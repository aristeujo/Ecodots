import utils

from pages import ParentControllerClass


class ContactPageController(ParentControllerClass):
    def __init__(self, app):
        super().__init__(app)
        self.name = 'contactPage'

    def _RegisterConfigAndEvents(self):
        self.update_config = {}
        utils.clickable(self.AppUi.dial_1).connect(lambda: self.AppUi.number_lineEdit.insert(str(1)))
        utils.clickable(self.AppUi.dial_2).connect(lambda: self.AppUi.number_lineEdit.insert(str(2)))
        utils.clickable(self.AppUi.dial_3).connect(lambda: self.AppUi.number_lineEdit.insert(str(3)))
        utils.clickable(self.AppUi.dial_4).connect(lambda: self.AppUi.number_lineEdit.insert(str(4)))
        utils.clickable(self.AppUi.dial_5).connect(lambda: self.AppUi.number_lineEdit.insert(str(5)))
        utils.clickable(self.AppUi.dial_6).connect(lambda: self.AppUi.number_lineEdit.insert(str(6)))
        utils.clickable(self.AppUi.dial_7).connect(lambda: self.AppUi.number_lineEdit.insert(str(7)))
        utils.clickable(self.AppUi.dial_8).connect(lambda: self.AppUi.number_lineEdit.insert(str(8)))
        utils.clickable(self.AppUi.dial_9).connect(lambda: self.AppUi.number_lineEdit.insert(str(9)))
        utils.clickable(self.AppUi.dial_0).connect(lambda: self.AppUi.number_lineEdit.insert(str(0)))
        utils.clickable(self.AppUi.dial_backspace).connect(lambda: self.AppUi.number_lineEdit.backspace())
        utils.clickable(self.AppUi.dial_ok).connect(self._NavigateToWasteDoorPage)

        # self.AppUi.contactPageHomeBtn.clicked.connect(lambda: self._NavigateToHomePage())
        # self.AppUi.contactPageBackBtn.clicked.connect(lambda: self._NavigateToFRPage())

    def _NavigateToWasteDoorPage(self):
        phone_no = self.AppUi.number_lineEdit.text()
        print(f"--------- {self.name} DialPad OK Button Button Clicked: {phone_no} ---------")

        user_name, error = utils.get_user_name_from_phone_no_api(phone_no)
        if error:
            self._NavigateToErrorPage()
        else:
            self.stop()
            self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.wasteDoorPage)
            self.MainApp.waste_door_page.start()

    def _NavigateToFRPage(self):
        self.stop()
        print(f"--------- {self.name} Back Button Button Clicked ---------")
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.FRPage)
        self.MainApp.fr_page.start()

    def _NavigateToErrorPage(self):
        # Navigating To Error Page
        self.stop()
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.FR_errorPage)
        self.MainApp.fr_error_page.start()

    def _NavigateToHomePage(self):
        print(f"--------- {self.name} Home Button Button Clicked ---------")
        self.stop()
        self.AppUi.screenNavigation.setCurrentWidget(self.AppUi.homePage)
        self.MainApp.home_page.start()
