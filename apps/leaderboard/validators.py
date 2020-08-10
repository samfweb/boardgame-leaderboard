from django.core.exceptions import ValidationError


def validate_unique_genre(string):
    from .models import Genre
    validate_unique_name(Genre, string)


def validate_unique_boardgame(string):
    from .models import Boardgame
    validate_unique_name(Boardgame, string)


def validate_unique_name(model, string):
    instances = model.objects.all()

    for instance in instances:
        if instance.name.lower() == string.lower():
            raise ValidationError(
                ('Duplicate name exists for %(model)s: %(value)s'),
                params={'value': string, 'model':str(model)},
            )
