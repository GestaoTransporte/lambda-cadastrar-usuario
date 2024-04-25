import boto3
from aws_lambda_powertools import Logger

logger = Logger()

client = boto3.client('ssm')

def get_parameter(name):
    logger.info(f"Obtendo parametro {name}")
    response = client.get_parameter(
        Name=name,
    )
    logger.info("Parametro obtido")
    return response["Parameter"]["Value"]