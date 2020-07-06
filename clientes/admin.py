from django.contrib import admin
from .models import Cliente, Documento, Venda, Produto


class ClienteAdmin(admin.ModelAdmin):
    # fields = (('doc', 'first_name', 'last_name'), 'age', 'salary', 'foto')
    # exclude = ('bio',)
    list_display = ('first_name', 'last_name', 'doc', 'age', 'salary', 'tem_bio', 'tem_foto')
    fieldsets = (
        ('Dados pessoais', {'fields': ('first_name', 'last_name', 'doc')}),
        ('Dados complementares', {'fields': ('age', 'salary', 'bio')}),
        ('Imagens', {
            'classes': ('collapse',),
            'fields': ('foto',)
        })
    )
    readonly_fields = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'venda__produtos__nome')

    def tem_foto(self, obj):
        return 'Sim' if obj.foto else 'Não'

    def tem_bio(self, obj):
        return obj.bio[:5] + '...' if obj.bio else 'Sem bio'

    tem_foto.short_description = 'foto'
    tem_bio.short_description = 'bio'


class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'get_total',)
    list_filter = ('cliente__doc', 'produtos__nome',)
    search_fields = ('cliente__first_name', 'cliente__last_name', 'cliente__doc__num_doc')
    readonly_fields = ('get_total', 'cliente', 'get_desconto', 'get_impostos')
    fieldsets = (
        ('Dados da venda', {'fields': ('numero', 'cliente')}),
        ('Detalhes da venda', {'fields': ('produtos', 'get_desconto', 'get_impostos', 'get_total')})
    )


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
