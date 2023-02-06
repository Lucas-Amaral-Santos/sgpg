from django.db import models
from aluno.models import Endereco, Titulacao, Graduacao
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime

class Colegiado(models.Model):
      colegiado_membro = models.BooleanField(default=False)
      colegiado_data_entrada = models.DateField(null=True, blank=True)
      colegiado_data_saida = models.DateField(null=True, blank=True)

      def __str__(self):
            if self.colegiado_membro:
                  return 'Membro'
            else:
                  return 'Não Membro'

class PosDoutorado(models.Model):
      concluido = models.BooleanField(verbose_name='Concluído:')
      ano_inicio = models.IntegerField(null=True, blank=True, verbose_name='Ano de início:')
      ano_fim = models.IntegerField(null=True, blank=True, verbose_name='Ano de término:')
      instituicao_posdoc = models.CharField(max_length=200, null=True, blank=True, verbose_name='Instituição de Pós-doutorado:')
      pais = models.CharField(max_length=200, null=True, blank=True, verbose_name='País:')

      def __str__(self):
            return str(self.id)

class Trabalho(models.Model):
      instituicao_trabalho = models.CharField(max_length=200, verbose_name='Instituição:')
      setor = models.CharField(max_length=200, null=True, blank=True, verbose_name='Setor:')
      admissao = models.DateField(null=True, blank=True, verbose_name='Admissão:')
      cargo = models.CharField(max_length=200, verbose_name='Cargo:')
      telefone  = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefone:')
      categoria = models.CharField(max_length=200, null=True, blank=True, verbose_name='Categoria:') 
      email = models.EmailField(null=True, blank=True, verbose_name='Email:')

      def __str__(self):
            return str(self.instituicao_trabalho)

class Professor(models.Model):

      TIPO_DOCENTE_CHOICES = (
            ("Permanente", "Permanente"),
            ("Colaborador", "Colaborador"),
            ("Coorientador", "Coorientador"),
            ("Visitante", "Visitante"),
            ("Pos Doutor", "Pós Doutor"),
      )

      nome = models.CharField(max_length=200, verbose_name='Nome:')
      sexo = models.CharField(max_length=50, null=True, blank=True, verbose_name='Sexo:')
      dt_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de nascimento:')
      estrangeiro = models.BooleanField(default=False, verbose_name='Estrangeiro:')
      nacionalidade = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nacionalidade:')
      naturalidade = models.CharField(max_length=2, null=True, blank=True, verbose_name='Naturalidade:')
      cpf = models.CharField(max_length=14, null=True, blank=True, verbose_name='CPF:')
      identidade = models.CharField(max_length=12, null=True, blank=True, verbose_name='Identidade:')
      identidade_uf= models.CharField(max_length=2, null=True, blank=True, verbose_name='UF:')
      identidade_orgao = models.CharField(max_length=100, null=True, blank=True, verbose_name='Orgão Expeditor:')
      tipo_docente = models.CharField(max_length=100, choices=TIPO_DOCENTE_CHOICES, null=True, blank=True, verbose_name='Tipo de docente:')
      
      endereco = models.OneToOneField(Endereco, on_delete=models.DO_NOTHING)
      titulacao = models.OneToOneField(Titulacao, on_delete=models.DO_NOTHING)
      graduacao = models.OneToOneField(Graduacao, on_delete=models.DO_NOTHING, null=True)
      trabalho = models.ForeignKey(Trabalho, on_delete=models.DO_NOTHING, related_name="professor_trabalho")
      pos_doutorado = models.ForeignKey(PosDoutorado, on_delete=models.DO_NOTHING, related_name="professor_pos_doutorado")
      membro_colegiado = models.ForeignKey(Colegiado, on_delete=models.DO_NOTHING, related_name="professor_membro_colegiado")

      slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
      updated = models.DateTimeField(auto_now=True)
      cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='professor_cadastrado_por')

      def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Professor, self).save(*args, **kwargs)

      def __str__(self):
            return  self.nome