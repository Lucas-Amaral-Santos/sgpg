from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from config.models import UnidadeFederativa, Sexo, EstadoCivil, Etnia, Vinculo, StatusOptions

class EnsinoMedio(models.Model):

    ENSINO_MEDIO_TIPO_CHOICES = (
        ('Pública', 'Pública'),
        ('Particular', 'Particular'),
    )

    ensino_medio_instituicao = models.CharField(max_length=200, null=True, blank=True, verbose_name="Instituição:")
    ensino_medio_ano_inicio = models.IntegerField(null=True, blank=True, verbose_name="Ano de Início:")
    ensino_medio_ano_conclusao = models.IntegerField(null=True, blank=True, verbose_name="Ano de Conclusão:")
    ensino_medio_municipio = models.CharField(max_length=200, null=True, blank=True, verbose_name="Município:")
    ensino_medio_tipo = models.CharField(max_length=200, choices=ENSINO_MEDIO_TIPO_CHOICES, verbose_name='Tipo de instituição:', null=True, blank=True)

    def __str__(self):
        return str(self.ensino_medio_instituicao)

class Titulacao(models.Model):
    titulacao = models.CharField(max_length=200, null=True, blank=True, verbose_name="Titulação:")
    titulacao_area = models.CharField(max_length=200, null=True, blank=True, verbose_name="Área:")
    titulacao_ano = models.IntegerField(null=True, blank=True, verbose_name="Ano:")
    data_qualificacao = models.DateField(null=True, blank=True, verbose_name="Data da Qualificação:")
    uf = models.CharField(max_length=2, null=True, blank=True, verbose_name="UF:")
    instituicao_titulacao = models.CharField(max_length=200, null=True, blank=True, verbose_name="Instituição:")
    obs_geral = models.TextField(null=True, blank=True, verbose_name="Observações Gerais")

    def __str__(self):
        return str(self.titulacao)

class Residencia(models.Model):
    instituicao_residencia = models.CharField(max_length=200, null=True, blank=True, verbose_name="Instituição:")
    residencia_ano_inicio = models.IntegerField(null=True, blank=True, verbose_name="Ano de Início:")
    residencia_ano_fim = models.IntegerField(null=True, blank=True, verbose_name="Ano de Término:")
    especialidade = models.CharField(max_length=200, null=True, blank=True, verbose_name="Especialidade:") 
    uf = models.CharField(max_length=2, null=True, blank=True, verbose_name="UF:")

    def __str__(self):
        return str(self.instituicao_residencia)

class Endereco(models.Model):
    cep = models.CharField(max_length=8, null=True, blank=True, verbose_name="CEP:")
    endereco = models.CharField(max_length=200, null=True, blank=True, verbose_name="Endereço:")
    numero = models.CharField(max_length=200, null=True, blank=True, verbose_name="Número:")
    complemento = models.CharField(max_length=200, null=True, blank=True, verbose_name="Complemento:")
    bairro = models.CharField(max_length=200, null=True, blank=True, verbose_name="Bairro:")
    municipio = models.CharField(max_length=200, null=True, blank=True, verbose_name="Município:")
    uf = models.CharField(max_length=2, null=True, blank=True, verbose_name="UF:")
    pais = models.CharField(max_length=200, null=True, blank=True, verbose_name="País:")
    telefone1 = models.CharField(max_length=15, null=True, blank=True, verbose_name="Telefone:")
    telefone2 = models.CharField(max_length=15, null=True, blank=True, verbose_name="Telefone 2:")

    def __str__(self):
        return str(self.id)

class Trabalho(models.Model):
    VINCULO_CHOICES = (
        ("Estatutário", "Estatutário"),
        ("CLT", "CLT"),
        ("Autônomo", "Autônomo"),
        ("Outros", "Outros"),
    )

    trabalho = models.CharField(max_length=200, null=True, blank=True, verbose_name='Trabalho:')
    tipo_vinculo = models.ForeignKey(Vinculo, on_delete=models.DO_NOTHING, verbose_name='Tipo de Vínculo:', null=True, blank=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.DO_NOTHING, null=True, blank=True) 
    email = models.EmailField(null=True, blank=True, verbose_name="Email de trabalho:")
    data_termino = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.trabalho)

class Graduacao(models.Model):
    graduacao_area = models.CharField(max_length=200, verbose_name="Área:") 
    instituicao = models.CharField(max_length=200, verbose_name="Instituição:")
    local = models.CharField(max_length=200, null=True, blank=True, verbose_name="Local:")
    graduacao_ano_inicio = models.IntegerField(null=True, blank=True, verbose_name="Ano de início:")
    graduacao_ano_fim = models.IntegerField(null=True, blank=True, verbose_name="Ano de término:")
    residencia = models.OneToOneField(Residencia, on_delete=models.DO_NOTHING)
    bolsa_graduacao = models.BooleanField(default=False)
    agencia = models.CharField(max_length=200, null=True, blank=True)
    iniciacao_cientifica = models.BooleanField(default=False)

    def __str__(self):
        return self.instituicao

class Status(models.Model):
    status = models.ForeignKey(StatusOptions, on_delete=models.CASCADE)

    def __str__(self):
        return self.status.status_options

class Aluno(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome:")
    cpf = models.CharField(max_length=14, verbose_name='CPF:', blank=True)
    nome_pai = models.CharField(max_length=200, null=True, blank=True, verbose_name='Nome do pai:')
    nome_mae = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nome da mãe:")
    naturalidade = models.ForeignKey(UnidadeFederativa, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="Naturalidade:")
    nacionalidade = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nacionalidade:")
    dt_nascimento = models.DateField()
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="Estado civil:")
    identidade = models.CharField(max_length=12, verbose_name="Identidade:")
    identidade_uf = models.CharField(max_length=2, verbose_name="UF:")
    identidade_orgao = models.CharField(max_length=100, verbose_name="Orgão expedidor:")
    sexo = models.ForeignKey(Sexo, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="Sexo:", related_name="aluno_sexo")
    email = models.EmailField(null=True, blank=True, verbose_name="Email:")
    etnia = models.ForeignKey(Etnia, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="Etnia:")
    situacao = models.CharField(max_length=50, null=True, blank=True, verbose_name="Situação:")
    foto = models.ImageField(null=True, blank=True, upload_to='img')

    status = models.OneToOneField(Status, on_delete=models.CASCADE, related_name='aluno_status')
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, related_name='aluno_endereco', null=True)
    graduacao = models.OneToOneField(Graduacao, on_delete=models.CASCADE, related_name='aluno_graduacao', null=True)
    ensino_medio = models.OneToOneField(EnsinoMedio, on_delete=models.CASCADE, related_name='aluno_ensino_medio', null=True)
    titulacao = models.OneToOneField(Titulacao, on_delete=models.CASCADE, related_name='aluno_titulacao', null=True)
    trabalho = models.OneToOneField(Trabalho, on_delete=models.CASCADE, related_name='aluno_trabalho', null=True)
    residencia = models.OneToOneField(Residencia, on_delete=models.CASCADE, related_name='aluno_residencia', null=True)

    slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
    updated = models.DateTimeField(auto_now=True)
    dt_cadastro = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='aluno_cadastrado_por')

    def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Aluno, self).save(*args, **kwargs)

    def __str__(self):
            return str(self.nome)

class Afastamento(models.Model):
    afastamento = models.CharField(max_length=200)
    data_ini = models.DateField()
    data_fim = models.DateField()
    aluno = models.ManyToManyField(Aluno, related_name="afastamento_aluno")

    def __str__(self):
        if self is not None:
            return self.afastamento
        else:
            return 'Não informado'