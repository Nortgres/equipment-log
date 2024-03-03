menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Оборудование", 'url_name': 'equipments'},
        {'title': "Сотрудники", 'url_name': 'persons'},
        #{'title': "Журнал", 'url_name': 'eqlog'},
        #{'title': ""}
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context