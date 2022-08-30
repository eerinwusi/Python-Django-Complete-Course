from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

projects_list = [
    {
        'id': '1',
        'title': 'Ecommerce website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio website',
        'description': 'This was a project where I built out my portfolio'
    },
    {
        'id': '3',
        'title': 'Social network',
        'description': 'Awesome open source project I am still working on'
    }
]
def projects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projects_list}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for project in projects_list:
        if project['id'] == pk:
            projectObj = project
    return render(request, 'projects/single-project.html', {'project': projectObj})
