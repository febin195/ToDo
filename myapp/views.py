from django.shortcuts import render,redirect

from django.views.generic import View

from django.contrib.auth import authenticate,login,logout

from myapp.forms import Userform,Loginform,Taskform

from myapp.models import User,TaskModel

from django.utils.decorators import method_decorator

# Create your views here.


def is_user(fn):

    def wrapper(request,**kwargs):

        id=kwargs.get('pk')

        obj= TaskModel.objects.get(id=id)

        if obj.user_id == request.user:

            return fn(request,**kwargs)
        
        else:

            return redirect('login')
        
    return wrapper    




class Registration_view(View):

    def get(self,request):

        form=Userform

        return render(request,"Register.html",{'form':form})
    
    def post(self,request):

        form=Userform(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            User.objects.create_user(**form.cleaned_data)

        return redirect("login")  
    
class Login(View):

    def get(self,request):

        form= Loginform

        return render(request,"login.html",{'form':form})

    def post(self,request):

        form=Loginform(request.POST)

        if form.is_valid():

            username=form.cleaned_data.get("username")

            password=form.cleaned_data.get("password")

            user = authenticate(request,username=username,password=password) #usernae and password

            

            if user:

                login(request,user)

                # print(request.user)


                return redirect("home")
            
            else:

                return render(request,"login.html")
class Taskhome(View):

    def get(self,request):

        

        data=TaskModel.objects.filter(user_id=request.user)

        return render(request,"home.html",{'data':data})              

class TaskAdd(View):

    def get(self,request):

        form=Taskform

        data=TaskModel.objects.filter(user_id=request.user)

        return render(request,"addtask.html",{'form':form,'data':data})   

    def post(self,request):

        form=Taskform(request.POST)

        if form.is_valid():

            TaskModel.objects.create(**form.cleaned_data,user_id=request.user)

            data=TaskModel.objects.filter(user_id=request.user).order_by('is_completed','created_date')

            return render(request,"home.html",{'form':form,'data':data})


class TaskAll(View):

    def get(self,request):

        data=TaskModel.objects.filter(user_id=request.user)

        return render(request,"taskview.html",{'data':data})  

@method_decorator(decorator=is_user,name='dispatch') 
class TaskDelete(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        data=TaskModel.objects.get(id=id)

        if data.user_id == request.user:

            data.delete()
            
            return redirect('home')
        
        else:

            return redirect('login')
    
@method_decorator(decorator=is_user,name='dispatch')     
class TaskUpdate(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        data=TaskModel.objects.get(id=id)

        form=Taskform(instance=data)

        return render(request,"taskupdate.html",{'form':form})
    
    def post(self,request,**kwargs):
        
        id=kwargs.get("pk")

        data=TaskModel.objects.get(id=id)

        form=Taskform(request.POST,instance=data)

        if form.is_valid():

            form.save()

        data=TaskModel.objects.filter(user_id=request.user)    

        return redirect('home')
    
@method_decorator(decorator=is_user,name='dispatch')    
class TaskDetail(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        data=TaskModel.objects.get(id=id)

        return render(request,"detail.html",{'data':data})    
    
@method_decorator(decorator=is_user,name='dispatch') 
class Task_Status(View):

    def get(self,request,**kwargs):

        id=kwargs.get('pk')

        data=TaskModel.objects.get(id=id)

        if data.is_completed == False:

            data.is_completed=True

            data.save()

        return redirect('home')    


class Signout(View):

    def get(self,request):

        logout(request)

        return redirect('login')
    

class Completed_view(View):

    def get(self,request):

        data=TaskModel.objects.filter(is_completed=True,user_id=request.user)

        return render(request,'completed.html',{'data':data})  


class Userdetailview(View):

    def get(self,request):

        total=TaskModel.objects.filter(user_id=request.user).count()

        incompleted=TaskModel.objects.filter(user_id=request.user,is_completed=False).count()

        completed=total-incompleted

        

        return render(request,'userdetail.html',{'total':total,'incompleted':incompleted,'completed':completed})      















           
    