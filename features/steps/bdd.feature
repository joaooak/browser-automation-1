# language: pt

Funcionalidade: Automação de browser

Cenário: Logar e pesquisar 
    Dado que acessei o site OrangeHRM
    Dado que loguei no site
    | usuario | senha |
    | opensourcecms | opensourcecms |
    Quando eu procuro um funcionário inexistente
    Então gero uma evidência
