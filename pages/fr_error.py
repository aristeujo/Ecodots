from threading import Timer
from constants import Constants
from pages import ParentControllerClass
from pages.common import PageConfigModel


class FrErrorPageController(ParentControllerClass):
    def __init__(self, app):
        super().__init__(app)
        self.name = 'FR_errorPage'
        self.timer = None

    def _RegisterConfigAndEvents(self):
        self.update_config = {}
        self.AppUi.FR_errorHome.clicked.connect(lambda: self._NavigateToHomePage())
        # self.AppUi.FR_errorBack.clicked.connect(lambda: self._NavigateToContactPage())     # later we will change it

    def start(self):
        super().start()

        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

        self.timer = Timer(Constants.ErrorTimer, self._NavigateToHomePage)
        self.timer.start()

    def stop(self):
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

        super().stop()

    def _NavigateToContactPage(self):
        self.stop()
        print(f"--------- {self.name} Back Button Button Clicked ---------")
        self.AppUi.menuNavigation.setCurrentWidget(self.AppUi.contactPage)
        self.MainApp.contact_page.start()

    def _NavigateToHomePage(self):
        print(f"--------- {self.name} Home Button Button Clicked ---------")
        self.stop()
        self.AppUi.screenNavigation.setCurrentWidget(self.AppUi.homePage)
        self.MainApp.home_page.start()