 psi-avaliacao1-christiankallil
Atividade avaliativa da disciplina de PSI.

 Refatoração Quitanda da Esquina - MVC com Blueprints

1. Problemas arquiteturais identificados no código inicial
1. Rotas concentradas no lugar errado: O arquivo `app.py` continha todas as rotas da aplicação, acumulando responsabilidades de Controller.
2. Classe Produto no Controller: A classe `Produto` estava definida dentro de `app.py`, violando o padrão MVC, pois deveria residir na camada Model (`models.py`).
3. Blueprint não registrado: O arquivo `blueprints/produtos/__init__.py` criava o `produtos_bp`, mas ele nunca era registrado no `app.py`, então a aplicação o ignorava.
4. Responsabilidades de apresentação misturadas com o Controller: A rota `ver_produto` retornava um HTML em formato de f-string diretamente no Controller, em vez de usar `render_template`.
5. Código repetido: A lógica de filtragem de produtos por nome e categoria estava duplicada dentro das rotas.
6. Endpoint incorreto: A rota `index` e `ver_produto` usavam `url_for` genéricos que não condiziam com a futura arquitetura de Blueprints.

 2. Onde ficou o Model e o Controller?
- Model: Ficou no arquivo `models.py`. É onde reside a classe `Produto` (com seus atributos `id`, `nome`, `categoria`, `preco`, `unidade`) e as listas em memória (`produtos`, `usuarios`). Exemplo de trecho: `class Produto: def __init__(self, id, nome, categoria, preco, unidade): ...`
- Controller: Ficou nos arquivos `routes.py` dentro de cada Blueprint (`blueprints/produtos/routes.py` e `blueprints/auth/routes.py`). Eles são responsáveis por receber a requisição, chamar o Model e devolver a View. Exemplo de trecho: `@produtos_bp.route("/") def index(): ... return render_template("produtos/index.html", ...)`

 3. Por que o `url_for` e os endpoints precisaram ser ajustados?
Eles precisaram ser ajustados porque, ao mover as rotas para Blueprints, o Flask exige que o nome do endpoint seja prefixado com o nome do Blueprint para evitar conflitos de nomes. 
Exemplo de mudança: A rota `index` que antes era acessada via `url_for('index')` no `base.html`, agora precisa ser acessada via `url_for('produtos.index')`, pois a função `index` agora pertence ao Blueprint `produtos`. O mesmo ocorreu com o login, que passou de `url_for('login')` para `url_for('auth.login')`.