from django.shortcuts import render

from blog.forms import WhoAreYouForm


def index(request):
    msg = None
    if request.method == "GET":
        form = WhoAreYouForm()
    else:
        form = WhoAreYouForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data
            msg = dict(age=form_data.get("your_age"), name=form_data.get("your_name"))
    return render(request, "index.html", {"form": form, "msg": msg})