import azure.functions as func
import logging
from logica.logica_reportes import ReportLogic

report_logic = ReportLogic()
bp2 = func.Blueprint() 

@bp2.route(route="reporte_2", auth_level=func.AuthLevel.FUNCTION)
@bp2.blob_input(arg_name="inputblob",
                path="reportes/reporteleer.txt",
                connection="SAREPORTS_CONNECTION_STRING")
@bp2.blob_output(arg_name="outputblob",
                path="reportes/reporte2.txt",
                connection="SAREPORTS_CONNECTION_STRING")
def http_trigger_reporte_2(req: func.HttpRequest, inputblob: func.InputStream ,outputblob: func.Out[str]) -> func.HttpResponse:
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
        result = report_logic.logic_2(name)
        text = f"http_trigger_reporte_2, {result}. read data {read_data}.This HTTP triggered function executed successfully."
        outputblob.set(text)
        return func.HttpResponse(text,status_code=200)
    else:
        text = "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response."
        return func.HttpResponse(
             text,
             status_code=200
        )
    