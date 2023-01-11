#importacion de librerias
import json
import decimalencoder
import todoList

#definicion de funcion get
def get(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
        #se retorna la respuesta 404
    return response
