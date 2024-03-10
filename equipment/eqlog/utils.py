menu = [
        {'title': "Сотрудники", 'url_name': 'persons'},
        #{'title': "Добавить сотрудника", 'url_name': 'addperson'},
        {'title': "Оборудование", 'url_name': 'equipments'},
        # {'title': "Журнал", 'url_name': 'eqlog'},
        {'title': "О сайте", 'url_name': 'about'},
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context