from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')


def yashoda(request):

    s = '<h2>Navigation<h2><br><br><a href="https://www.youtube.com/">YouTube</a><br><br><a href="https://translate.google.com/">translate</a>'

    djtext = request.POST.get('text','default')
    djcheck = request.POST.get('checkbox_1','off')
    uppercheck = request.POST.get('checkbox_2','off')
    newline = request.POST.get('checkbox_3','off')
    space = request.POST.get('checkbox_4','off')
    charcount = request.POST.get('checkbox_5','off') 

    perpose=""
    spacial_char = ';@&'
    string=""
    strupper=""
    str_newline=""
    str_space=""
    str_charcount=""
    str_charspace=""
    # duo=""
    main_str=""

    if djcheck == "on":
        for char in djtext:
            if char not in spacial_char:
                string = string + char
        perpose="remove spcial char"
        main_str = string

    if(uppercheck=="on"):
        strupper =  djtext.upper()
        perpose="Uppercase String"
        main_str = strupper

    if(newline=="on"):
        for char in djtext:
            if char !="\n" and char!='\r':
                str_newline = str_newline + char
        perpose="remove new line"
        main_str = str_newline


    if(space=="on"):
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:str_space = str_space + char
        perpose="remove space"
        main_str = str_space
    
    if(charcount=="on"):
        count=0
        sp=0
        for char in djtext:
            if char!=" ":
                count = count+1
            else:
                sp= sp + 1
        perpose="Count Character"
        str_charcount = count
        main_str = str_charcount
        # str_charspace = sp
        
    if(djcheck != "on" and uppercheck!="on" and newline!="on" and space!="on" and charcount!="on"):
        return HttpResponse("Error : \nSelect any one button !"+s)

    dict = {'allcheckbuttonwork':main_str,'perpose':perpose}
    return render(request,'remove.html',dict)
    