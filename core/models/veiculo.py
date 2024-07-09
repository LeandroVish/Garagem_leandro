from django.db import models
from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio

class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos", null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos", null=True, blank=True)
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    acessorio = models.ManyToManyField(Acessorio, related_name="veiculos")

    def __str__(self):
        return f"{self.modelo} {self.ano} {self.cor}"
    
    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"