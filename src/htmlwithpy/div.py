from htmlwithpy.element import Element
class Div(Element):
    def __init__(self,className = None,id = None,styleSheet = False):
        super().__init__(className ,id,styleSheet)
        self.name = "div"
        
       



