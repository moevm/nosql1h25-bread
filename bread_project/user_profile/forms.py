from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# Получаем модель пользователя:
User = get_user_model()


class CustomUserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ("username", "email", "last_name", "first_name")


class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, required=True)
    # first_name = forms.CharField(max_length=30, required=True, help_text="Optional")
    # last_name = forms.CharField(max_length=150, required=True, help_text="Optional")

    # Наследуем класс Meta от соответствующего класса родительской формы.
    # Так этот класс будет не перезаписан, а расширен.
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "email",
            "last_name",
            "first_name",
        )
