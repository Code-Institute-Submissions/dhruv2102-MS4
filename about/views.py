from django.shortcuts import render

# Create your views here.


def about(request):
    """
    Returns about page
    """
    return render(request, "about/about.html")
