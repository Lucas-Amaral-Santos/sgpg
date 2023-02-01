$(function () {
    $('[data-toggle="tooltip"]').tooltip()
});

$(".aluno #id_cep").focusout(function(){
  //Início do Comando AJAX
  $.ajax({
    //O campo URL diz o caminho de onde virá os dados
    //É importante concatenar o valor digitado no CEP
    url: 'https://viacep.com.br/ws/'+$(this).val()+'/json/',
    
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

$(".endereco_trabalho #id_cep").focusout(function(){
  //Início do Comando AJAX
  $.ajax({
    //O campo URL diz o caminho de onde virá os dados
    //É importante concatenar o valor digitado no CEP
    url: 'https://viacep.com.br/ws/'+$(this).val()+'/json/',
    
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
      $(".endereco_trabalho #id_rua").val(resposta.logradouro);
      $(".endereco_trabalho #id_complemento").val(resposta.complemento);
      $(".endereco_trabalho #id_bairro").val(resposta.bairro);
      $(".endereco_trabalho #id_municipio").val(resposta.localidade);
      $(".endereco_trabalho #id_uf").val(resposta.uf);
      //Vamos incluir para que o Número seja focado automaticamente
      //melhorando a experiência do usuário
      $(".endereco_trabalho #id_numero").focus();
    }
  });
});

$(".professor #id_cep").focusout(function(){
  //Início do Comando AJAX
  $.ajax({
    //O campo URL diz o caminho de onde virá os dados
    //É importante concatenar o valor digitado no CEP
    url: 'https://viacep.com.br/ws/'+$(this).val()+'/json/',
    
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