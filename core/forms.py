from django import forms
from core.models import Users

# Initiate logging
import logging
import corona.corona_logger # noqa
# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


class ReportForm(forms.Form):
    mutahi = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(attrs={'value': 'mutahi'})
    )
    mercy = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(attrs={'value': 'mercy'})
    )


class CasesForm(forms.Form):
    active_cases = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={'name': 'active_cases'}
        )
    )
    total_cases = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={'name': 'total_cases'}
        )
    )
    new_cases = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={'name': 'new_cases'}
        )
    )


class UsernameForm(forms.Form):
    username = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'name': 'username'}
        )
    )


class UsernameForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'name': 'username'}
        )
    )

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')

        if not username:
            self.add_error('username',
                'Please enter a username'
            )
