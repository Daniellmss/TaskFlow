from django.db import models

# Create your models here.

class Tarefa(models.Model):
    class Prioridade(models.IntegerChoices):
        BAIXA = 1, "Baixa"
        MEDIA = 2, "Média"
        ALTA = 3, "Alta"
    nome = models.CharField(max_length=32)
    descricao = models.CharField(max_length=256, blank=True)
    concluida = models.BooleanField(default=False)
    prioridade = models.IntegerField(
        choices = Prioridade.choices,
        default= Prioridade.BAIXA
    )
