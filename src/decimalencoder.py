# Importacion de librerias

import decimal
import json

# marca un error en la linea 8
# This is a workaround for: http://bugs.python.org/issue16535

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)
