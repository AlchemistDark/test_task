from django import forms

class NewURL (forms.Form):
    url_name = forms.CharField(max_length=1024)    # URL из списка
    flag1 = forms.BooleanField()                   # обработано или ещё нет
    flag2 = forms.BooleanField()                   # успешно или нет
    date_time = forms.DateTimeField()              # дата и время обработки
    site_name = forms.CharField(max_length=1024)   # заголовок страницы
    site_code = forms.CharField(max_length=32)     # кодировка страницы
    h1_name = forms.CharField(max_length=1024)     # заголовок H1
    
    def save (self):
        new_url=urls_base.objects.create(
            url_name = 'заглушка URL',              # URL из списка
            flag1 = false,                              # ещё не обработано
            date_time = 'заглушка дата-время'       # дата и время обработки
    
        )
        return new_url
  