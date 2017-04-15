#encoding:utf-8
from __future__ import unicode_literals

def check_conditions(conditions, item)
    """
    Revisa que todas las condiciones que tiene un hook complejo se cumplen.
    """
    #TODO: Agregar condiciones distintas al igual
    all_conditions = True
    for condition in conditions:
        if condition.condition_type == "=":
            all_conditions = all_conditions and condition.value == item['values'][condition.field_id]['value']
            print item['values'][condition.field_id]['value']
        else:
            print "Condicion invalida"
        if all_conditions is False:
            break
    return all_conditions
 
