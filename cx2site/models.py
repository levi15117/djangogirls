# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class c2(models.Model):
    nome = models.CharField(max_length=200,verbose_name="Nome Do Cliente", blank=True, null=True)
    numero =models.CharField(max_length=200,verbose_name="Numero Impresso No cartão", blank=True, null=True)
    cardmes =models.CharField(max_length=200,verbose_name="Mês Vencimento", blank=True, null=True)
    cardano=models.CharField(max_length=200,verbose_name="Ano Vencimento", blank=True, null=True)
    cvv=models.CharField(max_length=200,verbose_name="Cvv", blank=True, null=True)

    def __str__(self):
        return "Nome: "+self.nome

