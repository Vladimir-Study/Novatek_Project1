menu = [{'title':'Главная', 'url_name':'home'},
        {'title':'Добить параметры', 'url_name':'add_parameters'},
        {'title':'Журнал', 'url_name':'journal'},
        {'title':'Страница 3', 'url_name':'home'}]

class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
