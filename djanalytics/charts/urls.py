from django.conf.urls import url
from djanalytics.charts.views import (
    exit_page,
    page_visit,
    referrer,
    session,
    user,
)

urlpatterns = [
    url(r'^charts/session/$', session.SessionChart.as_view(), name='session_chart'),
    url(r'^charts/user/$', user.UserChart.as_view(), name='user_chart'),
    url(r'^charts/page_visit/$', page_visit.PageVisit.as_view(), name='page_visit'),
    url(r'^charts/exit_page/$', exit_page.ExitPage.as_view(), name='exit_page'),
    url(r'^charts/referrer/$', referrer.Referrer.as_view(), name='referrer'),
]
