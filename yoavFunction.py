import logging
import azure.functions as func
import json

app = func.FunctionApp()

@app.route(route="echo", auth_level=func.AuthLevel.FUNCTION)
def echo_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    # Get the request body
    try:
        req_body = req.get_json()
        body = req_body
    except ValueError:
        body = req.get_body().decode('utf-8')
    
    # Get URL parameters if any
    params = dict(req.params)
    
    # Construct the response
    response = {
        "message": "Echo Function",
        "body": body,
        "params": params,
        "method": req.method
    }
    
    return func.HttpResponse(
        body=json.dumps(response),
        status_code=200,
        mimetype="application/json"
    )