menu = [
        {'title': "Сотрудники", 'url_name': 'persons'},
        {'title': "Оборудование", 'url_name': 'equipments'},
        {'title': "Журнал изменений", 'url_name': 'eqlogs'},
        {'title': "О сайте", 'url_name': 'about'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context