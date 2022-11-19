from PyQt5.QtWidgets import QWidget
from base.IFigure import IFigure


class IPlayWindow(QWidget): 
    def GameStateUpdate(self) -> None:
        raise NotImplementedError

    def UpdateCell(self) -> None:
        raise NotImplementedError
    
    def UpdateFigure(self, shape: IFigure) -> None:
        raise NotImplementedError
    
    def PauseGame(self) -> None:
        raise NotImplementedError
    
    def CloseWindow(self) -> None:
        raise NotImplementedError
    
    def closeEvent(self, event) -> None:
        raise NotImplementedError