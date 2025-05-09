# Api de download de planilha de Relações com Investidores do Magazine Luiza
Este script automatiza o processo de navegação no site de Relações com Investidores do Magazine Luiza para realizar o download de uma planilha específica. Ele utiliza a biblioteca Selenium para controlar o navegador e interagir com os elementos da página.

Funcionalidades do Script
Configuração do Navegador:

Configura o navegador Google Chrome para ignorar erros SSL e manter a janela aberta após a execução.
Acesso ao Site:

Abre o site de Relações com Investidores do Magazine Luiza (https://ri.magazineluiza.com.br/#).
Interação com a Página:

Clica em elementos específicos da página para navegar até a seção de downloads.
Aguarda até que o botão de download esteja disponível e clica nele para iniciar o download da planilha.
Espera Dinâmica:

Utiliza WebDriverWait para aguardar que os elementos estejam visíveis e clicáveis antes de interagir com eles.
Manutenção do Navegador Aberto:

Aguarda o usuário pressionar Enter no terminal antes de fechar o navegador, permitindo verificar o estado final da página.
Requisitos
Bibliotecas Python:
selenium: Para automação do navegador.
Google Chrome e ChromeDriver:
O ChromeDriver deve ser compatível com a versão do navegador instalado.
