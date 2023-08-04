from abc import ABC, abstractmethod
class ToolBox(ABC):
    @abstractmethod
    def viewData(self):
        pass
    def showGraph (self):
        print("Showing graph ")
class Father(ToolBox):
    def viewData(self):
        pass
    @abstractmethod
    def showGraph(self):
        print("Showing graph ")
class Boy(ToolBox):
    def viewData(self):
        print("Showing graph ")
        return "Mukund"
    def showGraph1(self):
        print("Showing graph 1")
c=Boy()
c.viewData()
c.showGraph()
print(c.viewData())
