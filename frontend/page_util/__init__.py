
def has_fields(form, fields):
    for field in fields:
        if field not in form or len(form[field]) == 0:
            return False
    return True
