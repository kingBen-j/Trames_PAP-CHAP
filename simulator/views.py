from django.shortcuts import render


def home(request):
    return render(request, "simulator/vortex_net_sim.html", {"active_page": "simulator"})


def traffic_logs(request):
    return render(request, "simulator/traffic_logs.html", {"active_page": "traffic_logs"})


def security_matrix(request):
    return render(request, "simulator/security_matrix.html", {"active_page": "security_matrix"})


def nodes(request):
    return render(request, "simulator/nodes.html", {"active_page": "nodes"})
