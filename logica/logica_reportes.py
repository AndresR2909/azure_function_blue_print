class ReportLogic:
    def __init__(self):
        self._base_text = "Logica"

    def logic_1(self,parameter:str)->str:
        output = f" {self._base_text} 1: " + parameter
        return output

    def logic_2(self,parameter:str)->str:
        output = f"{self._base_text} 2: " + parameter
        return output
    
    def logic_3(self,parameter:str)->str:
        output = f"{self._base_text} 3: " + parameter
        return output