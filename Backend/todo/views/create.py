from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from todo.forms import ToDoForm

# invoked when a user wants to create a todo
@login_required
def create(request):
    if request.method == 'POST':
        todo_form = ToDoForm(data=request.POST)    

        if todo_form.is_valid():
            # Save the user's form data to the database.
            todo = todo_form.save(commit=False)           
            todo.user = request.user
            todo.save()            

        return HttpResponseRedirect("home")

    elif request.method == 'GET':
        todo_form = ToDoForm()        
        template_name = 'create.html'
        return render(request, template_name, {
            'todo_form': todo_form})

