from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools import Logger
from Ports import data, mapper
import json

logger = Logger()
app = APIGatewayRestResolver()


@app.post("/cadastro_usuario")
def cadastro_usuario():
    body = app.current_event.json_body
    usuario = mapper.mapear_usuario(body)
    data.cadastrar_usuario(usuario)

    return json.dumps({
        "statusCode": 201
    })


@logger.inject_lambda_context(log_event=True)
def lambda_handler(event, context: LambdaContext):
    return app.resolve(event, context)