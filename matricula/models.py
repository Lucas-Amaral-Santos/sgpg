from django.db import models
from aluno.models import Aluno
from professor.models import Professor
from disciplina.models import DisciplinaOfertada
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from config.models import LinhaPesquisa, Grau, Linguas

class Curso(models.Model):

    CURSO_CHOICES = (
        ("Mestrado", "Mestrado"),
        ("Doutorado", "Doutorado"),
    )
    curso = models.CharField(max_length=200, choices=CURSO_CHOICES, verbose_name='Curso:')
    orientador = models.CharField(max_length=200, verbose_name='Orientador:')
    coorientador = models.CharField(max_length=200, verbose_name='Coorientador:')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Curso, self).save(*args, **kwargs)

class Nota(models.Model):
    nota = models.FloatField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    dt_nota = models.DateField(auto_now=True)

    def __str__(self):
        if self.nota:
            return 'Sim'
        else:
            return 'Não'

class Probatorio(models.Model):
    data_inscricao = models.DateField(verbose_name='Data da inscrição:')
    nota = models.OneToOneField(Nota, on_delete=models.DO_NOTHING, related_name='probatorio_nota', null=True, verbose_name='Nota:')
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, related_name='probatorio_aluno', verbose_name='Aluno:')
    grau = models.ForeignKey(Grau, on_delete=models.CASCADE, related_name='probatorio_grau', verbose_name='Grau de Aplicação:')

    probatorio = models.BooleanField(default=True)
    linha_pesquisa = models.ForeignKey(LinhaPesquisa, on_delete=models.DO_NOTHING, null=True, blank=True)

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    updated = models.DateTimeField(auto_now=True)
    dt_cadastro = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='probatorio_cadastrado_por')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Probatorio, self).save(*args, **kwargs)

    def __str__(self):
        return self.aluno.nome

class Matricula(models.Model):

    STATUS_CHOICES = (
        ('Ativo', 'Ativo'),
        ('Titulado', 'Titulado'),
        ('Jubilado', 'Jubilado'),
        ('Abandono', 'Abandono')
    )

    numero = models.CharField(max_length=10, verbose_name='Número:')
    probatorio = models.ForeignKey(Probatorio, on_delete=models.CASCADE, related_name='matricula_probatorio', verbose_name='Probatório:')
    dt_matricula = models.DateField(verbose_name="Data de Matrícula:")
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, related_name="matricula_curso", null=True, blank=True, verbose_name='Curso:')
    requisita_bolsa = models.BooleanField(verbose_name='Requisita bolsa:')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name='Status:')
    linha_pesquisa = models.ForeignKey(LinhaPesquisa, on_delete=models.DO_NOTHING, null=True, blank=True)
    grau = models.ForeignKey(Grau, on_delete=models.CASCADE, related_name='matricula_grau', verbose_name='Grau de Aplicação:')

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    updated = models.DateTimeField(auto_now=True)
    dt_cadastro = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='matricula_cadastrado_por')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Matricula, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.probatorio.aluno)
    
    class Meta:
        verbose_name = "matricula"

class Bolsa(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Bolsa:')
    agencia = models.CharField(max_length=200, verbose_name='Agência:')
    dt_inicio = models.DateField(verbose_name='Data de início:')
    iniciacao_cientifica = models.BooleanField(verbose_name='Iniciação científica:')
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='bolsa_matricula', verbose_name='Matrícula:')
    dt_cadastro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Afastamento(models.Model):
    motivo = models.CharField(max_length=200, verbose_name='Motivo:')
    saida = models.DateField(verbose_name='Saída:')
    retorno = models.DateField(verbose_name='Retorno:')
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='afastamento_matricula', verbose_name='Matrícula:')

    dt_cadastro = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.motivo

class InscricaoProbatorio(models.Model):
    SITUACAO_CHOICES = (
        ("Cursando","Cursando"),
        ("Aprovado","Aprovado"),
        ("Reprovado", "Reprovado"),
        ("Trancado", "Trancado")
    )

    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.CASCADE, related_name='inscricao_probatorio_disciplina_ofertada')
    probatorio = models.ForeignKey(Probatorio, on_delete=models.CASCADE, related_name="inscricao_probatorio_probatorio")
    situacao = models.CharField(max_length=200, choices=SITUACAO_CHOICES, default=SITUACAO_CHOICES[0])
    nota = models.FloatField(validators=[MaxValueValidator(100),MinValueValidator(0)], null=True, blank=True)

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    updated = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='inscricao_probatorio_cadastrado_por')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(InscricaoProbatorio, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.disciplina_ofertada)

class Inscricao(models.Model):
    SITUACAO_CHOICES = (
        ("Cursando","Cursando"),
        ("Aprovado","Aprovado"),
        ("Reprovado", "Reprovado"),
        ("Trancado", "Trancado")
    )

    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.CASCADE, related_name='inscricao_disciplina_ofertada')
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name="inscricao_matricula")
    nota = models.FloatField(validators=[MaxValueValidator(100),MinValueValidator(0)], null=True, blank=True)
    situacao = models.CharField(max_length=200, choices=SITUACAO_CHOICES, default=SITUACAO_CHOICES[0])

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    updated = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='inscricao_cadastrado_por')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Inscricao, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.disciplina_ofertada)

    class Meta:
        verbose_name_plural = "Inscrições"


class VersaoFinal(models.Model):
    versao_final = models.BooleanField()
    dt_versao = models.DateField(auto_now=True)

    def __str__(self):
        if self.versao_final:
            return 'Sim'
        else:
            return 'Não'
    
    class Meta:
        verbose_name_plural = "Versões Finais"


class TrabalhoFinal(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    diploma = models.BooleanField(null=True, blank=True)
    dt_diploma = models.DateField(null=True, blank=True)

    matricula = models.OneToOneField(Matricula, on_delete=models.CASCADE, null=True, related_name="matricula_trabalho_final")
    probatorio = models.OneToOneField(Probatorio, on_delete=models.CASCADE, null=True, related_name="probatorio_trabalho_final")
    versao_final = models.OneToOneField(VersaoFinal, on_delete=models.DO_NOTHING, null=True, related_name="versao_final_trabalho_final")
    nota = models.OneToOneField(Nota, on_delete=models.CASCADE, null=True, related_name="nota_trabalho_final")

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    dt_cadastro = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='trabalho_final_cadastrado_por')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(TrabalhoFinal, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.titulo)

    class Meta:
        verbose_name_plural = "Trabalhos Finais"

class ExameLinguas(models.Model):
    lingua = models.ForeignKey(Linguas, on_delete=models.DO_NOTHING, related_name="exame_linguas")
    nota = models.FloatField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    dt_nota = models.DateField(auto_now=True)
    probatorio = models.ManyToManyField(Probatorio, related_name="probatorio_exame_linguas")

    def __str__(self):
        return str(self.lingua)

    class Meta:
        verbose_name = "Exame de Lingua"
        verbose_name_plural = "Exames de Linguas"

class Orientacao(models.Model):

    TIPO_ORIENTACAO_CHOICES = (
        ("Orientador", "Orientador"),
        ("Coorientador", "Coorientador"),
    )

    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING, related_name="orientacao_professor")
    tipo = models.CharField(max_length=200, choices=TIPO_ORIENTACAO_CHOICES)
    professor_externo = models.BooleanField()
    trabalho_final = models.ForeignKey(TrabalhoFinal, on_delete=models.DO_NOTHING, related_name="orientacao_trabalho_final")

    def __str__(self):
        return str(self.professor)

    class Meta:
        verbose_name_plural = "Orientações"