from .interfaces.IObserver import IObserver


class CLIView(IObserver):
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller

    def update(self):
        pass