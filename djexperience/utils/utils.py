def get_field_display(query, field, choicelist):
    ''' Retorna o get_FOO_display manualmente quando se usa .objects.values()
    no queryset '''
    res = []
    choices = dict(choicelist)
    for obj in query:
        new_obj = obj
        new_obj[field] = choices.get(obj[field], None)
        res.append(new_obj)
    return res
