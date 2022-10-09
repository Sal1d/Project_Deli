from main.forms import AuthenticationForm, UserRegistrationForm, CreateBookForm


def get_context_data(request):
    context = {
        'login': AuthenticationForm(),
        'register': UserRegistrationForm(),
        'book_add': CreateBookForm(),
    }
    return context
