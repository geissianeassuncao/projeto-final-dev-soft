from django.shortcuts import render

from rest_framework import viewsets
from appelderlink import models
from .serializers import MedicoSerializer, PacienteSerializer, ReceitaSerializer, AgendamentoSerializer, \
    PeriodoSerializer, MedicamentoSerializer, EspecialidadeSerializer, AgendaSerializer, CidadeSerializer, \
    EstadoSerializer, MedicoEspecialidadeSerializer, HorarioSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = models.Medico.objects.all()
    serializer_class = MedicoSerializer

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = models.Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

class MedicoEspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = models.MedicoEspecialidade.objects.all()
    serializer_class = MedicoEspecialidadeSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = models.Paciente.objects.all()
    serializer_class = PacienteSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = models.Agenda.objects.all()
    serializer_class = AgendaSerializer

class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = models.Periodo.objects.all()
    serializer_class = PeriodoSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = models.Horario.objects.all()
    serializer_class = HorarioSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = models.Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = models.Receita.objects.all()
    serializer_class = ReceitaSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = models.Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = models.Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = models.Cidade.objects.all()
    serializer_class = CidadeSerializer


