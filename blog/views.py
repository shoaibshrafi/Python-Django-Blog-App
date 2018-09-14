from django.shortcuts import render

def home(request):
    posts = [
        {
            'author' : 'Shoaib',
            'date_posted' : 'September 14, 2018',            
            'title' : 'Blog Title 1',
            'content' : 'First blog post'
        },
        {
            'author' : 'Najib',
            'date_posted' : 'September 13, 2018',            
            'title' : 'Blog Title 2',
            'content' : 'Second blog post'
        },
        {
            'author' : 'Raheema',
            'date_posted' : 'September 13, 2018',            
            'title' : 'Blog Title 3',
            'content' : 'Third blog post'
        }

    ] 
        
    return render(request, 'blog/home.html', {'posts' : posts})

def about(request):
    return render(request, 'blog/about.html')
