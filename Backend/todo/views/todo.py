from django.shortcuts import render

# invoked when user wants to view a specific todo
def todo(request, todo_id):
  if request.method == 'GET':
    template_name = 'orders/todo.html'
    return render(request, template_name)

