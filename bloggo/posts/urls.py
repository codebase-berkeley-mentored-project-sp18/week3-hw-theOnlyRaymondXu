from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #################################################################
    # Question 1
    # REPLACE THE BELOW LINE with the correct view and URL for the about page
    url(r'^not_the_right_url/$', None, name='about'),
    #################################################################
    # Question 2
    # REPLACE THE BELOW LINE with the correct view and URL for the post details page
    url(r'^also_not_right/(?P<pk>\d+)$', None, name='post_details'),
]