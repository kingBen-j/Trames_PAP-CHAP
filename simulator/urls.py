from django.urls import path

from .views import home, traffic_logs, security_matrix, nodes

app_name = "simulator"

urlpatterns = [
    path("", home, name="home"),
    path("traffic-logs/", traffic_logs, name="traffic_logs"),
    path("security-matrix/", security_matrix, name="security_matrix"),
    path("nodes/", nodes, name="nodes"),
]
