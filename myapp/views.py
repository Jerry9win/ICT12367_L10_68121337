from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person

def index(request):
    all_person = Person.objects.all() # ดึงข้อมูลจาก Database
    return render(request, "index.html", {'all_person': all_person})

def about(request):
    return render(request,"about.html")

def form(request):
    return render(request,"form.html")

def form(request):
    if request.method == "POST": # 1. เช็คก่อนว่า User กดปุ่มส่งข้อมูลมาใช่ไหม?
        # 2. ดึงข้อมูลจากฟอร์ม (นี่คือที่มาของโค้ดฝั่งซ้ายในรูป!)
        name = request.POST.get('person_name')
        age = request.POST.get('person_age')
        
        # 3. บันทึกลง Model
        person = Person(name=name, age=age)
        person.save()
        
        # 4. บันทึกเสร็จ ให้กลับไปหน้าแรกเพื่อดูรายชื่อที่เพิ่มมา
        return redirect('index')

    # ถ้าแค่เปิดหน้าเว็บปกติ (ไม่ได้กดปุ่ม) ก็โชว์ฟอร์มเปล่าๆ
    return render(request, 'form.html')