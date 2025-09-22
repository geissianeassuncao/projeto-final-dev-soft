from django.contrib import admin
from appelderlink import models

class MedicoAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    search_fields = ["nome"]
    list_filter = ["nome"]

admin.site.register(models.Medico, MedicoAdmin)

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    search_fields = ["nome"]
    list_filter = ["nome"]

admin.site.register(models.Especialidade, EspecialidadeAdmin)

class MedicoEspecialidadeAdmin(admin.ModelAdmin):
    list_display = ["id"]
    search_fields = ["id"]
    list_filter = ["id"]

admin.site.register(models.MedicoEspecialidade, MedicoEspecialidadeAdmin)

class PacienteAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    search_fields = ["nome"]
    list_filter = ["nome"]

admin.site.register(models.Paciente, PacienteAdmin)

class AgendaAdmin(admin.ModelAdmin):
    list_display = ["id", "medico", "data_inicial"]
    search_fields = ["medico__nome"]
    list_filter = ["medico", "data_inicial"]

admin.site.register(models.Agenda, AgendaAdmin)

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ["id", "agenda"]
    search_fields = ["agenda__medico__nome"]
    list_filter = ["agenda"]

admin.site.register(models.Periodo, PeriodoAdmin)

class HorarioAdmin(admin.ModelAdmin):
    list_display = ["id", "disponivel"]
    search_fields = ["periodo__agenda__medico__nome"]
    list_filter = ["disponivel"]

admin.site.register(models.Horario, HorarioAdmin)

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ["id", "paciente", "horario"]
    search_fields = ["paciente__nome", "horario__periodo__agenda__medico__nome"]
    list_filter = ["paciente", "horario__periodo__agenda__medico"]

admin.site.register(models.Agendamento, AgendamentoAdmin)

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ["id", "data"]
    search_fields = ["data"]
    list_filter = ["data"]

admin.site.register(models.Receita, ReceitaAdmin)

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "dosagem"]
    search_fields = ["nome"]
    list_filter = ["nome"]

admin.site.register(models.Medicamento, MedicamentoAdmin)

class EstadoAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    search_fields = ["nome"]
    list_filter = ["nome"]

admin.site.register(models.Estado, EstadoAdmin)

class CidadeAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    search_fields = ["nome"]
    list_filter = ["nome"]

admin.site.register(models.Cidade, CidadeAdmin)


