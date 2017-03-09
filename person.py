def build_person(firs_name,last_name):
    """Return a  dictionary of information about a person"""
    person = {'first': firs_name , "last":last_name}
    return person

cricketer = build_person("Arslana Sabir", "Sabir HUssain")

print (cricketer)