# importacion de librerias
import json
import decimalencoder
import todoList

# definicion de funcion list


def list(event, context):
    # fetch all todos from the database
    result = todoList.get_items()
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result, cls=decimalencoder.DecimalEncoder)
    }
    # retorna respuesta 200
    return response
