from django.shortcuts import render, redirect
from .forms import UserForms


def user_form(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page after saving the form
            return redirect('success')
    else:
        form = UserForms()
    return render(request, 'user_form.html', {'form': form})


def success(request):
    return render(request, 'success.html')
