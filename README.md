# 📩: Controlnet-Downloader-Models v0.0.1


Este diretório contém o Controlnet-Downloader-Models v0.0.1, um script Python desenvolvido para automatizar o download de modelos do ControlNet para uso no Stable Diffusion WebUI (A1111).

## 🏁 Pré-requisitos

Antes de começar, assegure-se de ter o Python instalado em seu sistema. Este script foi testado com o Python versão 3.8 ou superior.

## Instalação das Dependências

O Controlnet-Downloader-Models necessita das bibliotecas `requests`, `beautifulsoup4` e `tqdm`. Instale-as utilizando o seguinte comando:

```bash
pip install requests beautifulsoup4 tqdm
```

## Clonando o Repositório

Para obter o Controlnet-Downloader-Models, clone o repositório do projeto do GitHub:

```bash
git clone https://github.com/carlosrocha-dev/controlnet-downloader-models.git
cd controlnet-downloader-models
```
copie o arquivo `controlnet-downloader-models.py` para a pasta: `\stable-diffusion-webui\extensions\sd-webui-controlnet\models`

## Executando o Controlnet-Downloader

Para baixar os modelos do ControlNet, siga as instruções abaixo:

Navegue até o diretório do Controlnet-Downloader:

```bash
cd \stable-diffusion-webui\extensions\sd-webui-controlnet\models
```

Execute o script download_controlnet_models.py:
```bash
python controlnet-downloader-models.py
```
Uma barra de progresso será mostrada no terminal para cada arquivo sendo baixado, indicando o progresso.

![Upload Screenshot](https://github.com/carlosrocha-dev/Controlnet-Downloader-Model/assets/3737837/247ad06f-8e7b-4ba6-b4c0-4737647888d3)

## Verificação dos Arquivos Baixados ✔️

Após a execução do script, verifique se todos os arquivos .pth necessários foram baixados corretamente e estão localizados no diretório
```\stable-diffusion-webui\extensions\sd-webui-controlnet\models.```

### Importante ⚠️:

*Não feche o terminhal enqundo o script estiver sendo executado!*

## Suporte

Caso encontre problemas ou tenha dúvidas, verifique se todas as dependências foram instaladas corretamente e se a sua versão do Python é compatível.

Se os problemas persistirem, consulte a documentação do projeto Stable Diffusion WebUI ou abra um issue no repositório do projeto.
