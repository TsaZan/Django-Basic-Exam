from furryFunnies.author.models import Author


def get_author():
    return Author.objects.first()