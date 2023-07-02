"# Orientacao-a-objetos-2" 

---------------------------
---Log aula 04 "Herença"---
---------------------------

-Alteração da class "playlist", tirando a "list"
-Criação da função "listagem"
-Criação da função "tamanho" da listagem

-------------------------------
---Log aula 05 "Duck Typing"---
-------------------------------

-Criação da função "__getitem__" para definir o iteravel
-Utilizando o duck typing para fazer a alteração da funçao "tamanho" pra "__len__" 

--------------------------------------------------------------Python Data model--------------------------------------------------------------

Inicialização - "__init__"(inicialiação do objeto)
Representação "__str__"(converter o objeto em string), "__repr__"(mostrar como o objeto foi criado, principalmente ao compilador)
Container, sequencia "__contains__"(Faz a função do "in" porem existem outras aplicações), "__iter__"(definir o iteravel), "__len__"(retorna o tamanho da lista), "__getitem__"(percorer a lista, pegar o item)
Numericos "__add__", "__sub__", "__mul__", "__mod__"

---------------------------------------------------------------------------------------------------------------------------------------------

-Classes Abstratas, importação do abc e dele importar a colletion "MutableSequence" e importação do complex de numbers