from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='foto') # "upload_to='foto'" armazenada na pasta foto 

    def __str__(self):
        return self.nome
    
class Diario(models.Model):
    titulo = models.CharField(max_length=100)
    tags = models.TextField()
    texto = models.TextField()
    pessoas = models.ManyToManyField(Pessoa, null=True, blank=True) #relação de muito pra muitos
    create_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True pega o momento do salvamento no banco de dados

    def __str__(self):
        return self.titulo
    
    def get_tags(self):
        return self.tags.split(',') if self.tags else []

    def set_tags(self, list_tags, reset=False):
        if not reset:
            existing_tags = set(self.get_tags())
            list_tags = existing_tags.union(set(list_tags)) #juntando os dois e sem duplicar nomes por conta do .union
        self.tags = ','.join(list_tags)