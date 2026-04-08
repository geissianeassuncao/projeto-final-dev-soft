from rest_framework import serializers
from appelderlink import models

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medico
        fields = '__all__'

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Especialidade
        fields = '__all__'

class MedicoEspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicoEspecialidade
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agenda
        fields = '__all__'

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Periodo
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Horario
        fields = '__all__'

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agendamento
        fields = '__all__'

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Receita
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicamento
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estado
        fields = '__all__'


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cidade
        fields = '__all__'



