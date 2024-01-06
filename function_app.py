import azure.functions as func 
from function_reporte_1 import bp1
from function_reporte_2 import bp2
from function_reporte_3 import bp3

app = func.FunctionApp() 

app.register_functions(bp1) 
app.register_functions(bp2) 
app.register_functions(bp3) 