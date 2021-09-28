import sys

from django.shortcuts import render

# Create your views here.
def index(request):

    if request.method == "POST":
        codeareadata = request.POST['code']

        try:
            #standart standart chiqish ma'lumotnomasini saqlash

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') #standart chiqishni biz yaratgan faylga o'zgartirish

            #kodni ishlatish
            exec(codeareadata)  #Masalan =>   print("Behzod Asliddinov")

            sys.stdout.close()

            sys.stdout = original_stdout  #standart chiqishni asl qiymatiga qaytarish

            # nihoyat fayldan chiqishni o'qing va chiqish o'zgaruvchisida saqlash

            output = open('file.txt', 'r').read()
            return render(request , 'index.html',{'code':codeareadata,'output':output})
        except Exception as e:
            # koddagi xatoni qaytarish uchun
            sys.stdout = original_stdout
            output = e
            return render(request , 'index.html',{'code':codeareadata,'output':output})
   
         
    return render(request , 'index.html')