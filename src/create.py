#Se importan las libreiras
import json
import logging
import todoList

#Se define la funcion create
def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation failed")
        raise Exception("Couldn't create the todo item.")
    item = todoList.put_item(data['text'])
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    return response
    #Nos retorna la respuesta