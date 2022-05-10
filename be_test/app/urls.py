from rest_framework import routers

from django.urls import include, re_path

from django.urls import include


from be_test.app.views.users_views import UsersViewsSet
from be_test.app.views.jobs_views import JobsViewsSet

router = routers.DefaultRouter()

router.register(r'user', UsersViewsSet)
router.register(r'jobs', JobsViewsSet)

urlpatterns = [
    re_path('', include(router.urls))
]
