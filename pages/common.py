import time


class PageConfigModel:
    def __init__(self, name, interval, last_updated, callback):
        self.Name = name
        self.Interval = interval
        self.LastUpdated = last_updated
        self.CallBack = callback

    def Run(self):
        self.CallBack()

    def Print(self):
        print("Name: ", self.Name)
        print("Interval: ", self.Interval)
        print("LastUpdated: ", self.LastUpdated)


class ParentControllerClass:
    def __init__(self, app):
        from appUI import UiComponents
        self.name = 'ParentControllerClass'
        self.MainApp = app
        self.AppUi: UiComponents = app.appUi
        self.IsStarted = False
        self.CurrentTime = 0

    def _RegisterConfigAndEvents(self):
        self.update_config = {}
        print("Parent Class ---- You haven't Registered any Events or Config for this Class: ", self.name)

    def start(self):
        self.IsStarted = True
        self._RegisterConfigAndEvents()

    def stop(self):
        self.IsStarted = False

    def update_data(self):
        current_screen_name = self.AppUi.screenNavigation.currentWidget().objectName()
        current_menu_name = self.AppUi.menuNavigation.currentWidget().objectName()
        # if current_screen_name != self.name and self.IsStarted:
        if not self.IsStarted:
            return

        # print(current_screen_name, self.name)

        self.CurrentTime = time.time()
        for key in self.update_config:
            conf: PageConfigModel = self.update_config.get(key)
            if conf is None:
                continue

            diff = self.CurrentTime - conf.LastUpdated
            if diff >= conf.Interval:
                conf.Run()
                conf.LastUpdated = self.CurrentTime