from django.shortcuts import render


# Create your views here.
def front(request):
	if request.method=="POST":
		pass
	return render(request,"front.html")

def file(request):
	if request.method=="POST":
		pass
	return render(request,"file.html")	

def music(request):
	if request.method=="POST":
		pass
	return render(request,"music.html")	


def art(request):
	if request.method=="POST":
		pass
	return render(request,"art.html")	

def dance(request):
	if request.method=="POST":
		pass
	return render(request,"dance.html")	

def coding(request):
	if request.method=="POST":
		pass
	return render(request,"coding.html")	

def lit(request):
	if request.method=="POST":
		pass
	return render(request,"lit.html")	

def film(request):
	if request.method=="POST":
		pass
	return render(request,"film.html")			



