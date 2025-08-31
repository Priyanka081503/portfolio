from django.shortcuts import render
from  django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def projects(request):
    projects_show=[
        {"title":"Currency Converter",
         "path":"images/currency_converter.png",
         },
         {"title":"Rock-Paper-Scissors game",
         "path":"images/rock_paper_scissors.png",
         },
          {"title":"Tic-Tac-Toe game",
         "path":"images/tic-tac-toe.png",
         },
        {"title":"Food Website landing page",
         "path":"images/burger.png",
         },
        {"title":"Portfolio",
         "path":"images/portfolio_pic.png",
         },
    ]
    return render(request,"projects.html",{"projects_show":projects_show})


def contact(request):
    return render(request,"contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found",status=404)









