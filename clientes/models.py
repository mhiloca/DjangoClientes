from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Cliente(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    foto = models.ImageField(upload_to='photos', blank=True, null=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    desconto = models.DecimalField(max_digits=3, decimal_places=2)
    impostos = models.DecimalField(max_digits=5, decimal_places=2)
    cliente = models.ForeignKey(
        Cliente,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        db_constraint=False
    )
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return f'This is {self.cliente.first_name}\'s sell.'

    @property
    def total(self):
        tot = 0
        for produto in self.produtos.all():
            tot += produto.preco
        return tot

    def get_desconto(self):
        return round(self.total * self.desconto, 2)

    def get_impostos(self):
        return round(self.total * self.impostos, 2)

    def get_total(self):
        total = (self.total - self.get_desconto()) + self.get_impostos()
        return round(total, 2)


class Dogs(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()


@receiver(m2m_changed, sender=Venda.produtos.through)
def update_vendas_total(sender, instance, **kwargs):
    instance.get_total()
    instance.save()

