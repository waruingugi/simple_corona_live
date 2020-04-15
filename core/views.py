from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import redirect
from core.forms import ReportForm, CasesForm, UsernameForm
from core.models import Users, Choices
from datetime import date
import math

# Initiate logging
import logging
import corona.corona_logger # noqa
# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)

# CHOICES
MUTAHI_KAGWE = 'MUTAHI_KAGWE'
MERCY_MWANGANGI = 'MERCY_MWANGANGI'


# Create your views here.
def home(request):
    """ Handles the home page"""
    assert isinstance(request, HttpRequest)
    logger.info('Rendering home page.')

    return render(
        request,
        'core/home.html',
        {
            'title': 'Results'
        }
    )


def get_report(request):
    """ Handles the symptoms page"""
    assert isinstance(request, HttpRequest)
    logger.info('Rendering get tomorrow report page.')

    report_form = ReportForm(request.POST or None)
    if report_form.is_valid():
        logger.info('Report form is valid')
        choice = report_form.data['customRadio']
        read_report = []

        if choice == MUTAHI_KAGWE:
            read_report.append(MUTAHI_KAGWE)

        if choice == MERCY_MWANGANGI:
            read_report.append(MERCY_MWANGANGI)

        request.session['read_report'] = choice

        return redirect(get_numbers)

    logger.info('Tomorrow report saved successfully')

    return render(
        request,
        'core/report.html',
        {
            'title': 'Predict',
            'form': report_form
        }
    )


def get_numbers(request):
    """Renders the get_numbers page."""
    assert isinstance(request, HttpRequest)
    logger.info('Rendering get_numbers page')

    cases_form = CasesForm(request.POST or None)

    if cases_form.is_valid():
        logger.info('Cases form is valid')

        active_cases = cases_form.cleaned_data.get('active_cases')
        new_cases = cases_form.cleaned_data.get('new_cases')
        total_cases = cases_form.cleaned_data.get('total_cases')

        request.session['active_cases'] = active_cases
        request.session['new_cases'] = new_cases
        request.session['total_cases'] = total_cases

        return redirect(get_username)

    return render(
        request,
        'core/numbers.html',
        {
            'title': 'Cases',
            'form': cases_form
        }
    )


def get_username(request):
    """Renders the get_username page."""
    assert isinstance(request, HttpRequest)
    logger.info('Rendering get_username page')

    username_form = UsernameForm(request.POST or None)

    if username_form.is_valid():
        logger.info('Username form is valid')
        username = username_form.cleaned_data.get('username')
        username_qs = Users.objects.filter(username=username)
        if not username_qs.exists():
            created_user = Users.objects.create(
                username=username
            )
            Choices.objects.create(
                user=created_user
            )

            logger.info('{} successfull registration'.format(username))

        user = Users.objects.get(username=username)
        user_choices = Choices.objects.get(user=user)

        user_choices.answers = [ request.session['read_report'] ]
        user_choices.active_cases = request.session['active_cases']

        user_choices.new_cases = request.session['new_cases']
        user_choices.total_cases = request.session['total_cases']
        user_choices.save()

        return redirect(predictions_set)

    return render(
        request,
        'core/username.html',
        {
            'title': 'Username',
            'form': username_form
        }
    )


def predictions_set(request):
    """Renders the predictions_set page."""
    assert isinstance(request, HttpRequest)
    logger.info('Rendering predictions_set page')

    return render(
        request,
        'core/set.html',
        {
            'title': 'Done'
        }
    )


def winners(request):
    """Renders the winners page."""
    assert isinstance(request, HttpRequest)
    logger.info('Rendering winners page')

    return render(
        request,
        'core/winners.html',
        {
            'title': 'Winners'
        }
    )
