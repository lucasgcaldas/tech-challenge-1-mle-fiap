# Tech Challenge - Fase 1 - Machine Learning Engineering

## Grupo

- Bruna Guimarães Silva - RM358115
- Lucas Gomes Caldas - RM358850
- Vitor Augusto Toledo Azevedo Pinto - RM354025

## Configuração do Projeto

### Instalação do SQLite

O banco de dados escolhido para o projeto foi o SQLite devido sua flexibildiade de funcionamento e facilidade de instalação. O artigo a seguir mostra como baixar o SQLite nos principais sistemas opercionais (Windows, Linux e Mac) -> [SQLite: da instalação até sua primeira tabela](https://www.alura.com.br/artigos/sqlite-da-instalacao-ate-primeira-tabela?utm_term=&utm_campaign=%5BSearch%5D+%5BPerformance%5D+-+Dynamic+Search+Ads+-+Artigos+e+Conte%C3%BAdos&utm_source=adwords&utm_medium=ppc&hsa_acc=7964138385&hsa_cam=11384329873&hsa_grp=164240702375&hsa_ad=703829337057&hsa_src=g&hsa_tgt=aud-2200131122553:dsa-2276348409543&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiA_qG5BhDTARIsAA0UHSIUB23PS0VQLrHD_0VJfdPYY-16M5EIIJSwgDHwJhnnlNPRxxySEHMaAs77EALw_wcB)

### Inicialização do Projeto

- ```$ python -m venv venv```
- ```$ pip install -r requirements.txt```
- ```$ uvicorn main:app --reload```
- Para acessar a aplicação -> [http://localhost:8000/docs/](http://localhost:8000/docs/)

### Funcionamento

O funcionamento do sistema segue de acordo com o fluxo a seguir:

```Cadastro de Usuário -> Autenticação de Usuário -> Consulta nas rotas GET```

Observação: Não é possível consultar a API sem antes estar logado!
