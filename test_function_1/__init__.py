import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="test_function_1")
def test_function_1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function 1 processed a request...')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function 1 executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function 1 executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )