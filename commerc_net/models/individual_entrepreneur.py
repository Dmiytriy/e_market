from django.db import models

from commerc_net.models.base import BaseModel


class IndividualEntrepreneur(BaseModel):
    provider = models.ForeignKey('Factory', on_delete=models.SET_NULL, verbose_name='Производитель', null=True)

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'