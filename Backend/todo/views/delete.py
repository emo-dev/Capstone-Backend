from django.shortcuts import render

# invoked when a user wants to delete a todo
def delete(request):
  if request.method == 'GET':
    template_name = 'delete.html'
    return render(request, template_name)

