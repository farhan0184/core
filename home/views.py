from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name':"farhan",'age': 24},
        {'name':"farhan",'age': 17},
        {'name':"farhan",'age': 19},
        {'name':"farhan",'age': 20},
        {'name':"farhan",'age': 13},
    ]
    text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque tenetur dolores corrupti voluptatum excepturi odit, modi beatae, distinctio nulla nisi unde necessitatibus odio animi nihil? Deserunt maiores nobis ea perspiciatis excepturi quisquam eaque magni quae, necessitatibus iure! Delectus quod nobis dolorum nesciunt inventore animi dolores eligendi quas dicta ad rerum explicabo necessitatibus sequi ducimus obcaecati cumque harum eum incidunt fugiat enim, nulla doloremque. Magnam vel veniam labore rem cumque id!"""
    return render(request, 'home/index.html', context={'page': 'Django Page','peoples': peoples, 'text': text})

def about(request):
    return render(request, 'home/about.html', context={"page": 'About'})

def contact(request):
    return render(request, 'home/contact.html', context={"page": 'Contact'})

def success_page(request):
    return HttpResponse(
        """
        <h1>This is success page.</h1>
        <p>success page details.</p>
    """
    )

