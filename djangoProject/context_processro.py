from main.forms import AuthenticationForm, UserRegistrationForm


def get_context_data(request):
    context = {
        'login': AuthenticationForm(),
        'register': UserRegistrationForm()
    }
    return context
