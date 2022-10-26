from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Flight, Registration_user, Review, Ticket


def get_main_title(request):
    return render(request, "templates/index.html")


class Reg_user(CreateView):
    model = Registration_user
    fields = [
        "email",
        "first_name",
        "last_name",
        "username",
        "passport_number",
        "password",
    ]
    template_name = "reg_users.html"
    success_url = "/"


class Login(LoginView):
    form_class = AuthenticationForm
    fields = [
        "email",
        "password",
    ]
    template_name = "login.html"
    success_url = "/"


class Book(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = [
        "place_in_plane",
        "number_flight",
    ]

    def form_valid(self, form):
        form.instance.passport_number_id = self.request.user.passport_number
        return super().form_valid(form)

    template_name = "book.html"
    success_url = "/trip/"


class Trip(ListView):
    model = Flight
    template_name = "trip.html"


def get_current_book(request, passport_user):
    current_book = Ticket.objects.filter(passport_number=passport_user)
    current_book = {"object_list": current_book}
    return render(request, "templates/current_book.html", current_book)


def my_book(request):
    if "id_passport" in request.POST:
        passport = int(request.POST["id_passport"])
        if request.POST["id_passport"] == request.user.passport_number:
            return redirect(f"/current_book/{passport}/")
        else:
            return redirect("/choose_passport_for_book/")
    else:
        return render(request, "templates/choose_passport_for_book.html")


class Update_ticket(UpdateView):
    model = Ticket
    fields = [
        "place_in_plane",
    ]
    template_name = "up_ticket.html"
    success_url = "/choose_passport_for_book/"


def all_passengers(request, flight_num):
    needed_passports = Ticket.objects.filter(number_flight=flight_num).values_list(
        "passport_number"
    )
    passengers = Registration_user.objects.filter(passport_number__in=needed_passports)

    context = {
        "object_list": passengers,
        "object_list_flight": flight_num,
    }
    return render(request, "all_passengers.html", context)


class Delete_ticket(DeleteView):
    model = Ticket
    fields = [
        "place_in_plane",
        "passport_number",
        "number_flight",
    ]
    template_name = "del_ticket.html"
    success_url = "/choose_passport_for_book/"


class Create_review(CreateView):
    model = Review
    fields = [
        "number_flight",
        "comment",
        "rate",
        "sing_author",
    ]


    template_name = "create_review.html"
    success_url = "/review/"


class All_reviews(ListView):
    model = Review
    template_name = "all_reviews.html"
