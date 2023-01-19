#importa las librerias, aqui solo todolist.py
import todoList

#se define la funcion delete
def delete(event, context):
    todoList.delete_item(event['pathParameters']['id'])

    # create a response
    response = {
        "statusCode": 200
    }
#se retorna la respesta 200 que es "todo correcto"
    return response
