from django.forms.forms import Form
from django.forms.fields import CharField, Textarea


class EditPost(Form):
    txt=CharField(widget=Textarea)
    title=CharField()

    def clean(self):
        print(self.data.get('txt', None))
        self.data.get('txt',None).strip(' ')
        self.data.get('title', None).strip(' ')
        try:
            if [str(i[0]).isalpha() for i in self.data['txt'].split(' ')]:
                if [str(i[0]).isalpha() for i in self.data['title'].split(' ')]:
                    return super().clean()
        except:
            pass
        return False

    class Meta:
        fields=('title','txt')