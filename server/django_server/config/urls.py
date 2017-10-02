from django.conf.urls import url
import config.views


urlpatterns = [
    url(r'^$', config.views.home, name='home'),
    url(r'^list-config$', config.views.list_config, name='list-config'),
    url(r'^edit-config/([0-9]+)$', config.views.edit_config, name='edit-config'),
    url(r'^get-config/([0-9]+)$', config.views.get_config, name='get-config'),
    url(r'^save-config/([0-9]+)/(apply)?$', config.views.save_config, name='save-config'),

]
