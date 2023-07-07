from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView
from django.urls import reverse
from .models import Page
from .forms import PageForm


# Create your views here.
def index(request):
    return render(request, "diarys/index.html")


# def page_list(request):
#     object_list = Page.objects.all()
#     paginator = Paginator(object_list, 8)
#     curr_page_num = request.GET.get("page")
#     if curr_page_num is None:
#         curr_page_num = 1
#     page = paginator.page(curr_page_num)
#     return render(request, "diarys/page_list.html", {"page": page})


class PageListView(ListView):
    model = Page
    template_name = "diarys/page_list.html"
    ordering = ["-dt_created"]
    paginate_by = 8
    page_kwarg = "page"


def info(request):
    return render(request, "diarys/info.html")


def page_detail(request, page_id):
    object = get_object_or_404(Page, id=page_id)
    return render(request, "diarys/page_detail.html", {"object": object})


# def page_create(request):
#     if request.method == "POST":
#         form = PageForm(request.POST)
#         if form.is_valid():
#             new_page = form.save()
#             return redirect("page-detail", page_id=new_page.id)
#     else:
#         form = PageForm()
#     return render(request, "diarys/page_form.html", {"form": form})


class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    template_name = "diarys/page_form.html"

    def get_success_url(self):
        return reverse("page-detail", kwargs={"page_id": self.object.id})


def page_update(request, page_id):
    object = get_object_or_404(Page, id=page_id)
    if request.method == "POST":
        form = PageForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect("page-detail", page_id=object.id)
    else:
        form = PageForm(instance=object)
    return render(request, "diarys/page_form.html", {"form": form})


def page_delete(request, page_id):
    object = get_object_or_404(Page, id=page_id)
    if request.method == "POST":
        object.delete()
        return redirect("page-list")
    else:
        return render(request, "diarys/page_confirm_delete.html", {"object": object})
