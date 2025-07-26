def get_person_parts(person):
    # given_name
    # family_name
    # title
    return [person[key] for key in ('given_name', 'family_name', 'title')]

def format_data_for_display(people):
    def get_item(p):
        return f'{p["given_name"]} {p["family_name"]}: {p["title"]}'
    return [get_item(person) for person in people]


def format_data_for_excel(people):
    items = ['given,family,title']
    items += [','.join(get_person_parts(person)) for person in people]
    return '\n'.join(items)
