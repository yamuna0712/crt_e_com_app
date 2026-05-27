import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Books,UserModel
from django.shortcuts import render
@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        book_data = Books.objects.create(
            book_id=data.get("book_id"),
            name=data.get("name"),
            price=data.get("price"),
            quantity=data.get("quantity"),
            author=data.get("author"),
            publish_date=data.get("publish_date"),
        )

        return JsonResponse({
            "book_id": book_data.book_id,
            "message": "Book added successfully",
        })

    return JsonResponse({"error": "Only POST method allowed"})

def get_books(request):
    books = Books.objects.all().values()
    response_data=list(books)
    return JsonResponse({
        "books": response_data,
        "message": "Books successfully fetched",
    })

def home_page(request):
    return render(request, "home.html")

def file2(request):
    return render(request,"file2.html",{"range":["sunday","monday"
                                                 ,"tuesday","wednesday","thursday","friday","saturday"]})

def contact_page(request):
    return render(request,"contact.html",{"range":range(1,10),"sum":0})

def profile_page(request):
    return render(request,"profile.html",{"name":"amit","email":"amit@gmail.com",
                                          "role":"admin",
                                          "user_data":[{"name":"amit","email":"amit@gmail.com"},
                                                       {"name": "else", "email": "elsa@gmail.com"},
                                                       {"name": "ammu", "email": "ammu@gmail.com"}]})

'''1.design portfolio page -> name , personal details, professional details, projects,skills
      contact form-name , email  and message input fields
       marks from url and display the grade
       if marks> 80 ->grade A else marks> 60 print B else print False'''

def portfolio_home(request):
    return render(request,"portfolio_home.html")

def portfolio_contact(request):
    return render(request,"portfolio_contact.html")

def grade(request,marks):
    return render(request,"grade.html",{"marks":marks})

@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        date=UserModel.objects.create(
            name=name,
            email=email,
        )
        return HttpResponse("User added successfully")
    return render(request,"user_form.html")


