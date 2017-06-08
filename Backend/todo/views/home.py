from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from todo.models import ToDo

# invoked when a user logs in, main view
@login_required
def home(request):
    if request.method == 'POST':
        todo = ToDo.objects.get(pk=request.POST.get('todo'))
        todo.delete()

        return HttpResponseRedirect('home')

    template_name = 'index.html'

    user_todos = ToDo.objects.filter(user=request.user)

    return render(request, template_name, {
                'user_todos': user_todos})

