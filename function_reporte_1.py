import azure.functions as func
import logging
from logica.logica_reportes import ReportLogic

report_logic = ReportLogic()
#app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

bp1 = func.Blueprint() 

@bp1.route(route="reporte_1",auth_level=func.AuthLevel.FUNCTION)
@bp1.blob_input(arg_name="inputblob",
                path="reportes/reporteleer.txt",
                connection="SAREPORTS_CONNECTION_STRING")
@bp1.blob_output(arg_name="outputblob",
                path="reportes/reporte1.txt",
                connection="SAREPORTS_CONNECTION_STRING")
def http_trigger_reporte_1(req: func.HttpRequest, inputblob: func.InputStream ,outputblob: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    if inputblob:
        read_data = inputblob.read()
        logging.info(read_data)

    if name:
        result = report_logic.logic_1(name)
        text = f"http_trigger_reporte_1, {result}. read data {read_data}.This HTTP triggered function executed successfully."
        outputblob.set(text.encode('utf-8'))
        return func.HttpResponse(text,status_code=200)
    else:
        text = "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response."
        return func.HttpResponse(
             text,
             status_code=200
        )
