$(function () {
    $('[data-toggle="tooltip"]').tooltip()
});



$("#div_id_portador_deficiencia_qual").hide();
$("#id_portador_deficiencia").click(function() {
  if($(this).prop('checked')) {
    console.log("Checked");
    $("#div_id_portador_deficiencia_qual").fadeIn(700);
  } else {
    $("#div_id_portador_deficiencia_qual").fadeOut(700);
  }
});



$(".aluno #id_cep").focusout(function(){
  //Início do Comando AJAX
  $.ajax({
    //O campo URL diz o caminho de onde virá os dados
    //É importante concatenar o valor digitado no CEP
    url: 'https://viacep.com.br/ws/'+$(this).val().replace('-','')+'/json/',
    
    //Aqui você deve preencher o tipo de dados que será lido,
    //no caso, estamos lendo JSON.
    dataType: 'json',
    //SUCESS é referente a função que será executada caso
    //ele consiga ler a fonte de dados com sucesso.
    //O parâmetro dentro da função se refere ao nome da variável
    //que você vai dar para ler esse objeto.
    success: function(resposta){
      //Agora basta definir os valores que você deseja preencher
      //automaticamente nos campos acima.
      $(".aluno #id_rua").val(resposta.logradouro);
      $(".aluno #id_complemento").val(resposta.complemento);
      $(".aluno #id_bairro").val(resposta.bairro);
      $(".aluno #id_municipio").val(resposta.localidade);
      $(".aluno #id_uf").val(resposta.uf);
      //Vamos incluir para que o Número seja focado automaticamente
      //melhorando a experiência do usuário
      $(".aluno #id_numero").focus();
    }
  });
});

$(".endereco_trabalho #id_trabalho_cep").focusout(function(){
  //Início do Comando AJAX
  $.ajax({
    //O campo URL diz o caminho de onde virá os dados
    //É importante concatenar o valor digitado no CEP
    url: 'https://viacep.com.br/ws/'+$(this).val().replace('-','')+'/json/',
    
    //Aqui você deve preencher o tipo de dados que será lido,
    //no caso, estamos lendo JSON.
    dataType: 'json',
    //SUCESS é referente a função que será executada caso
    //ele consiga ler a fonte de dados com sucesso.
    //O parâmetro dentro da função se refere ao nome da variável
    //que você vai dar para ler esse objeto.
    success: function(resposta){
      //Agora basta definir os valores que você deseja preencher
      //automaticamente nos campos acima.
      $(".endereco_trabalho #id_trabalho_rua").val(resposta.logradouro);
      $(".endereco_trabalho #id_trabalho_complemento").val(resposta.complemento);
      $(".endereco_trabalho #id_trabalho_bairro").val(resposta.bairro);
      $(".endereco_trabalho #id_trabalho_municipio").val(resposta.localidade);
      $(".endereco_trabalho #id_trabalho_uf").val(resposta.uf);
      //Vamos incluir para que o Número seja focado automaticamente
      //melhorando a experiência do usuário
      $(".endereco_trabalho #id_trabalho_numero").focus();
    }
  });
});

$(".professor #id_cep").focusout(function(){
  //Início do Comando AJAX
  $.ajax({
    //O campo URL diz o caminho de onde virá os dados
    //É importante concatenar o valor digitado no CEP
    url: 'https://viacep.com.br/ws/'+$(this).val().replace('-','')+'/json/',
    
    //Aqui você deve preencher o tipo de dados que será lido,
    //no caso, estamos lendo JSON.
    dataType: 'json',
    //SUCESS é referente a função que será executada caso
    //ele consiga ler a fonte de dados com sucesso.
    //O parâmetro dentro da função se refere ao nome da variável
    //que você vai dar para ler esse objeto.
    success: function(resposta){
      //Agora basta definir os valores que você deseja preencher
      //automaticamente nos campos acima.
      $(".professor #id_rua").val(resposta.logradouro);
      $(".professor #id_complemento").val(resposta.complemento);
      $(".professor #id_bairro").val(resposta.bairro);
      $(".professor #id_municipio").val(resposta.localidade);
      $(".professor #id_uf").val(resposta.uf);
      //Vamos incluir para que o Número seja focado automaticamente
      //melhorando a experiência do usuário
      $(".professor #id_numero").focus();
    }
  });
});


const date = new Date().toJSON().slice(0, 10);

$("#id_membros_passados").change(function () {
  if ($(this).is(":checked")) {
    $('#id_data_saida_inicio').removeAttr("readonly").attr('value', date);
    $('#id_data_saida_fim').removeAttr("readonly").attr('value', date);
  }
  else {
    $('#id_data_saida_inicio').attr('readonly', true).attr('value', '');
    $('#id_data_saida_fim').attr('readonly', true).attr('value', '');
  }
});

$("#id_membros_ativos_view").change(function () {
  if (!$(this).is(":checked")) {
    $('#id_membros_ativos').addAttr("checked");
  }
  else {
    $('#id_membros_ativos').removeAttr("checked");
  }
});



