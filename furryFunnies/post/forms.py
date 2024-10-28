from django import forms
from furryFunnies.mixins import ReadOnlyFields
from furryFunnies.post.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'updated_at')


class PostCreateForm(PostBaseForm):
    class Meta:
        model = Post
        exclude = ('author', 'updated_at')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "Put an attractive and unique title..."}),
            'content': forms.Textarea(
                attrs={'placeholder': "Share some interesting facts about your adorable pets..."}),

        }


class PostEditForm(PostBaseForm):

    def __init__(self, *args, **kwargs):
        super(PostBaseForm, self).__init__(*args, **kwargs)
        self.fields['image_url'].help_text = None


class PostDeleteForm(ReadOnlyFields, PostBaseForm):

    def __init__(self, *args, **kwargs):
        super(PostBaseForm, self).__init__(*args, **kwargs)
        self.fields['image_url'].help_text = None
