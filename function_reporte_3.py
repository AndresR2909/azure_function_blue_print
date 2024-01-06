import azure.functions as func
import logging
from logica.logica_reportes import ReportLogic

report_logic = ReportLogic()
bp3 = func.Blueprint()

@bp3.route(route="reporte_3", auth_level=func.AuthLevel.FUNCTION)
@bp3.blob_input(arg_name="inputblob",
                path="reportes/reporte3.txt",
                connection="SAREPORTS_CONNECTION_STRING")
@bp3.blob_output(arg_name="outputblob",
                path="reportes/reporte3.txt",
                connection="SAREPORTS_CONNECTION_STRING")
def http_trigger_reporte_3(req: func.HttpRequest, inputblob: func.InputStream ,outputblob: func.Out[str]) -> func.HttpResponse:
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
        result = read_data.decode('utf-8')+"\n"+report_logic.logic_3(name)
        text = f"http_trigger_reporte_3, {result}. read data {read_data}.This HTTP triggered function executed successfully."
        outputblob.set(text)
        return func.HttpResponse(text,status_code=200)
    else:
        text = "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response."
        return func.HttpResponse(
             text,
             status_code=200
        )