from django.db import models
   
class Cliente(models.Model):
    queixa_choices = (
        ('D', 'Depressao'),
        ('A', 'Ansiedade'),
    )

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    queixa = models.CharField(max_length=1, choices=queixa_choices)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, blank=True)
        
        
    def __str__(self):
        return self.nome        
     