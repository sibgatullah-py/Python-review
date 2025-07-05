from django.shortcuts import render


def Home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        print(name,age)
        
    return render(request, 'index.html',locals())# the datas here can be sent with making the name and age as a dictionary but it's done with locals()
