from django.shortcuts import render
from myapp.models import Book

# Create your views here.
from django.shortcuts import render
 
def DisplayMyPage(request):
    return render(request, 'myapp/mypage.html', { 'welcome_text': 'Hello World!' })

def DisplayMyPageWithParameter(request, my_parameter):
	welcometext = my_parameter
	return render(request, 'myapp/mypage.html', {'welcome_text' : welcometext})


def InsertBook(request, isbn, title, memo):
    Book(isbn=isbn, title=title, memo={'content': memo}).save()
    return render(request, 'myapp/mypage.html',
                  { 'welcome_text': 'Insert: ' + title })

def DisplayBook(request, isbn):
	result = Book.objects.filter(isbn=isbn)[0]
	bookinfo = "ISBN: {0}; TITLE: {1}; MEMO: {2}".format(result.isbn, result.title,result.memo['content'])

	return render(request, 'myapp/mypage.html',
                  { 'welcome_text': bookinfo })
