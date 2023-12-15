



# Google Slides
  
Este módulo permite criar, escrever e atualizar Apresentações Google. Você pode adicionar ou remover slides e texto neles; baixe a apresentação em vários formatos; e mais.  

  
![banner](imgs/BannerGoogleSlides.jpg)


## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  

## Como usar este módulo

Antes de usar este módulo, você deve registrar seu aplicativo no Google Cloud Portal.

1. Faça login com uma conta do Google e entre no seguinte link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Preencha o formulário para criar um novo projeto e pressione "Criar".
3. No Menu de Navegação (Esquerda), entre em API e Serviços.
4. Vá para a seção superior e pressione "+ ATIVAR API E SERVIÇOS".
5. Pesquise por "Google Slides API", selecione-o e pressione "ATIVAR". O mesmo acontece com a "API do Google Drive".
6. Volte para o Menu de Navegação, vá para API e Serviços e depois entre em Credenciais.
7. Pressione Criar credenciais e selecione ID do cliente OAuth. Em seguida, selecione Tipo de aplicativo: Aplicativo de desktop, dê um nome a ele e pressione Criar.
8. Faça download do arquivo JSON de credenciais.
9. Por fim, volte ao Menu de Navegação, vá até a Tela de Consentimento e adicione seu usuário na seção "Testar Usuários" (mesmo que seja o mesmo que está criando o 
app).

Nota: Quando a primeira conexão for feita, um arquivo .pickle será criado na pasta raiz do Rocketbot, para se conectar ao mesmo serviço com outra conta, você deve dar um nome a cada sessão. Se as credenciais expirarem, você deverá excluir o arquivo .pickle e criar e baixar um arquivo de credenciais novo (JSON).

## Descrição do comando

### Configurar credenciais G-Suite
  
Obtém permissão para trabalhar no Google Slides com o Rocketbot
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho||C:/caminho/credenciais.json|
|Session||session|
|Variável onde o resultado será salvo||Variável|

### Nova Apresentação
  
Crie uma nova apresentação do Google Slides com Rocketbot
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Título da apresentação||Titulo|
|Variável onde o ID será salvo||Variável|
|Session||session|

### Adicionar slide em branco
  
Adicione um novo slide à sua apresentação do Apresentações Google
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da apresentação||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Variável onde o resultado será salvo||Variável|

### Adicionar slide de layout
  
Adicione um novo slide com título e corpo à sua apresentação do Apresentações Google
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da apresentação||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Variável onde o resultado será salvo||Variável|

### Excluir Apresentação
  
Excluir uma Apresentação Google selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Apresentação||14olZxHX8sQUzUg33h72b-uK32jxC1u3uwsKlw0gEgM0|
|Session||session|
|Variável onde o resultado será salvo||Variável|

### Excluir Slide
  
Excluir uma slide de uma Apresentação Google selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Apresentação||14olZxHX8sQUzUg33h72b-uK32jxC1u3uwsKlw0gEgM0|
|Slide ID||SLIDES_API1476047835_0|
|Session||session|
|Variável onde o resultado será salvo||Variável|

### Adicionar Texto
  
Insira um novo texto na Apresentação Google com Rocketbot. Este comando é usado para slides em branco.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Apresentação||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|ID do slide||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Texto||Texto para inserir|
|Tamanho da fonte|Tamanho da fonte que o texto escrito terá.|12|
|Alinhamento|Alinhamento que o texto escrito terá.|Left|
|Cor do texto|Cor que o texto escrito terá|Black|
|Negrito|Selecione se o texto ficará em negrito.|True|
|Itálico|Selecione se o texto ficará em itálico.|True|
|Sublinhar|Selecione se o texto será sublinhado.|False|
|Variável onde o ID será salvo||Variável|
|Identificador de texto||MeuTexto1|
|Session||session|

### Inserir Texto
  
Insira texto em um elemento já criado em um slide específico do Apresentações Google.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Apresentação||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|ID do slide||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Texto||Texto para inserir|
|Tamanho da fonte|Tamanho da fonte que o texto escrito terá.|12|
|Alinhamento|Alinhamento que o texto escrito terá.|Left|
|Cor do texto|Cor que o texto escrito terá|Black|
|Negrito|Selecione se o texto ficará em negrito.|True|
|Itálico|Selecione se o texto ficará em itálico.|True|
|Sublinhar|Selecione se o texto será sublinhado.|False|
|Variável onde o ID será salvo||Variável|
|ID do Elemento ao qual o Texto será inserido||MinhaCaixadeTexto|
|Session||session|

### Excluir texto
  
Remova o texto de um elemento em uma apresentação do Apresentações Google com Rocketbot
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Apresentação||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|ID do slide||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|ID do Elemento que contém o texto||MeuTexto1|
|Variável onde o ID será salvo||Variável|
|Session||session|

### Baixar Apresentação
  
Baixe uma apresentação do Apresentações Google em formato PP ou PDF com Rocketbot
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Apresentação||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Formato de arquivo (Slides)||---- Select format ----|
|Caminho onde salvar o arquivo||C:\users\usuario\Downloads|
|Variável onde o resultado será salvo||Variável|
|Session||session|

### Obter Info
  
Obtém o nome da apresentação e os elementos do slide indicado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Apresentação||14olZxHX8sQUzUg33h72b-uK32jxC1u3uwsKlw0gEgM0|
|Índice do slide para obter||0|
|Session||session|
|Variável onde o resultado será salvo||Variável|