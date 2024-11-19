questions_list = [
    {
        "question": "Qual é a solução da equação 3x + 5 = 14?",
        "options": ["x = 1", "x = 2", "x = 3", "x = 4"],
        "answer": "x = 3"
    },
    {
        "question": "Qual é o valor aproximado da raiz quadrada de 225?",
        "options": ["13", "14", "15", "16"],
        "answer": "15"
    },
    {
        "question": "Quanto é 12 x 15?",
        "options": ["120", "150", "180", "200"],
        "answer": "180"
    },
    {
        "question": "Qual é a derivada de f(x) = 3x² + 2x - 5?",
        "options": ["6x + 2", "3x² + 2", "6x - 2", "2x - 3"],
        "answer": "6x + 2"
    },
    {
        "question": "Qual é o resultado da integral de ∫ 2x dx?",
        "options": ["x² + C", "2x + C", "x²", "2x"],
        "answer": "x² + C"
    },

    {
        "question": "Qual é o valor da expressão log₁₀(100)?",
        "options": ["1", "2", "3", "4"],
        "answer": "2"
    },
    {
        "question": "Resolva a equação exponencial: 2^x = 32.",
        "options": ["x = 3", "x = 4", "x = 5", "x = 6"],
        "answer": "x = 5"
    },
    {
        "question": "Qual é a matriz inversa da matriz identidade 2x2?",
        "options": ["[1,0;0,1]", "[0,1;1,0]", "Não existe", "É a própria matriz identidade"],
        "answer": "É a própria matriz identidade"
    },
    {
        "question": "Qual é a solução do sistema linear: 2x + y = 5 e x - y = 1?",
        "options": ["x = 2, y = 1", "x = 3, y = 2", "x = 4, y = 3", "x = 1, y = 2"],
        "answer": "x = 2, y = 1"
    },
    {
        "question": "Qual é o limite de lim (x→∞) (3x² + 5x) / (x² + 2x)?",
        "options": ["3", "2", "1", "0"],
        "answer": "3"
    },
]
habilidades = [
    {"Elimina duas alternativas quando usado"},
    {"Avança o dobro de casas que você tirar, caso acerte a pergunta"},
    {"O jogador pode trocar sua pergunta uma vez "},
    {"Ganha bonus de acordo com a velocidade de resposta" }

]
COLOR_DESCRIPTIONS = {
    "Branco": "Elimina duas alternativas quando usado",
    "Vermelho": "Avança o dobro de casas que você tirar, caso acerte a pergunta",
    "Verde": "O jogador pode trocar sua pergunta",
    "Amarelo": "Ganha bonus de acordo com a velocidade de resposta"
}



questions_list_1_12= [
    # 1 a 10
    {
        "id": 1,
        "question": "Qual é a complexidade de tempo de um algoritmo de busca binária em uma lista ordenada?",
        "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
        "answer": "O(log n)"
    },
    {
        "id": 1,
        "question": "Qual é o pior caso de complexidade de tempo de um algoritmo de ordenação Bubble Sort?",
        "options": ["O(n)", "O(n²)", "O(log n)", "O(n log n)"],
        "answer": "O(n²)"
    },
    {
        "id": 1,
        "question": "Em qual estrutura de dados o acesso ao elemento central é mais eficiente?",
        "options": ["Fila", "Pilha", "Lista Duplamente Encadeada", "Vetores"],
        "answer": "Vetores"
    },
    {
        "id": 1,
        "question": "Qual é o algoritmo mais eficiente para encontrar o menor caminho em um grafo ponderado com pesos positivos?",
        "options": ["Algoritmo de Dijkstra", "Algoritmo de Bellman-Ford", "Busca em Largura", "Busca em Profundidade"],
        "answer": "Algoritmo de Dijkstra"
    },
    {
        "id": 1,
        "question": "Qual é o pior caso de complexidade do algoritmo QuickSort?",
        "options": ["O(n)", "O(n²)", "O(log n)", "O(n log n)"],
        "answer": "O(n²)"
    },
    {
        "id": 1,
        "question": "Qual é a principal diferença entre uma árvore binária de busca (BST) e uma árvore AVL?",
        "options": ["Em uma AVL, a altura das subárvores é balanceada", "Uma BST permite apenas a inserção de elementos únicos", "Em uma BST, as folhas estão sempre no mesmo nível", "Árvore binária balanceada tem no máximo 3 filhos por nó"],
        "answer": "Em uma AVL, a altura das subárvores é balanceada"
    },
    {
        "id": 1,
        "question": "Qual é a principal característica do algoritmo de Dijkstra?",
        "options": ["Ele encontra o caminho mais curto entre todos os pares de vértices", "Ele encontra o caminho mais curto entre dois vértices com pesos negativos", "Ele encontra o caminho mais curto entre dois vértices com pesos positivos", "Ele encontra o maior caminho em um grafo não ponderado"],
        "answer": "Ele encontra o caminho mais curto entre dois vértices com pesos positivos"
    },
    {
        "id": 1,
        "question": "Em que situação o algoritmo de MergeSort é preferível em relação ao algoritmo QuickSort?",
        "options": ["Quando os dados são quase ordenados", "Quando é necessário um algoritmo com complexidade média O(n log n)", "Quando é necessário garantir uma complexidade O(n log n) no pior caso", "Quando se lida com dados pequenos"],
        "answer": "Quando é necessário garantir uma complexidade O(n log n) no pior caso"
    },
    {
        "id": 1,
        "question": "Qual é a principal vantagem do algoritmo de busca em largura (BFS) em relação ao algoritmo de busca em profundidade (DFS)?",
        "options": ["BFS é mais eficiente em grafos direcionados", "BFS sempre encontra o caminho mais curto entre dois nós", "DFS é mais fácil de implementar", "BFS é mais eficiente em termos de memória"],
        "answer": "BFS sempre encontra o caminho mais curto entre dois nós"
    },
    {
        "id": 1,
        "question": "Qual é a complexidade de tempo do algoritmo de ordenação HeapSort?",
        "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
        "answer": "O(n log n)"
    },
    
    # 11 a 20
    {
        "id": 1,
        "question": "O que é um grafo acíclico dirigido (DAG)?",
        "options": ["Um grafo em que todos os vértices têm grau 0", "Um grafo onde existe pelo menos um ciclo", "Um grafo onde não há ciclos e as arestas têm direção", "Um grafo onde todos os vértices são isolados"],
        "answer": "Um grafo onde não há ciclos e as arestas têm direção"
    },
    {
        "id": 1,
        "question": "Qual é a complexidade de tempo do algoritmo de busca em profundidade (DFS) em um grafo representado por uma lista de adjacência?",
        "options": ["O(n)", "O(n²)", "O(n + m)", "O(m)"],
        "answer": "O(n + m)"
    },
    {
        "id": 1,
        "question": "Qual é a principal característica da técnica de 'backtracking'?",
        "options": ["Exploração completa e exaustiva de todas as possibilidades", "Usa uma abordagem gulosa para resolver problemas", "Resolve problemas através de simulações", "Sempre encontra a solução ótima de um problema"],
        "answer": "Exploração completa e exaustiva de todas as possibilidades"
    },
    {
        "id": 1,
        "question": "Em um algoritmo de ordenação, qual é a diferença entre 'estável' e 'instável'?",
        "options": ["Um algoritmo estável preserva a ordem relativa de elementos iguais", "Um algoritmo estável usa menos memória", "Um algoritmo instável é mais eficiente", "Um algoritmo instável não pode ser implementado de forma recursiva"],
        "answer": "Um algoritmo estável preserva a ordem relativa de elementos iguais"
    },
    {
        "id": 1,
        "question": "Qual é a principal vantagem do algoritmo de Bellman-Ford em relação ao algoritmo de Dijkstra?",
        "options": ["Bellman-Ford não pode lidar com grafos direcionados", "Bellman-Ford não encontra o caminho mais curto entre todos os pares de vértices", "Bellman-Ford pode lidar com pesos negativos, mas tem maior complexidade", "Bellman-Ford requer que o grafo esteja totalmente conectado"],
        "answer": "Bellman-Ford pode lidar com pesos negativos, mas tem maior complexidade"
    },
    {
        "id": 1,
        "question": "Qual é a complexidade do algoritmo de busca sequencial (linear search)?",
        "options": ["O(1)", "O(n)", "O(n log n)", "O(log n)"],
        "answer": "O(n)"
    },
    {
        "id": 1,
        "question": "Qual é o objetivo principal de um algoritmo de compressão de dados?",
        "options": ["Reduzir a complexidade de tempo de um problema", "Minimizar o uso de memória", "Reduzir o tamanho dos dados para facilitar o armazenamento ou a transmissão", "Otimizar a ordem de execução dos comandos"],
        "answer": "Reduzir o tamanho dos dados para facilitar o armazenamento ou a transmissão"
    },
    {
        "id": 1,
        "question": "Qual é a vantagem principal do algoritmo de Floyd-Warshall sobre o algoritmo de Dijkstra?",
        "options": ["Floyd-Warshall encontra o caminho mais curto entre dois vértices", "Floyd-Warshall pode lidar com pesos negativos e encontra o caminho mais curto entre todos os pares de vértices", "Floyd-Warshall é mais eficiente em grafos grandes", "Floyd-Warshall usa menos memória que Dijkstra"],
        "answer": "Floyd-Warshall pode lidar com pesos negativos e encontra o caminho mais curto entre todos os pares de vértices"
    },
    {
        "id": 1,
        "question": "O que é uma árvore AVL?",
        "options": ["Uma árvore binária de busca balanceada onde a diferença de altura entre as subárvores de qualquer nó é no máximo 1", "Uma árvore binária onde cada nó tem no máximo 2 filhos", "Uma árvore com nós balanceados de acordo com o valor da chave", "Uma árvore em que os filhos esquerdos sempre são maiores que os filhos direitos"],
        "answer": "Uma árvore binária de busca balanceada onde a diferença de altura entre as subárvores de qualquer nó é no máximo 1"
    },
    {
        "id": 1,
        "question": "Qual é a complexidade do algoritmo de ordenação Insertion Sort no pior caso?",
        "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
        "answer": "O(n²)"
    },
    {
        "id": 1,
        "question": "Em uma árvore binária de busca (BST), qual é a propriedade fundamental?",
        "options": ["Os valores na subárvore esquerda são maiores que o nó raiz", "Os valores na subárvore direita são menores que o nó raiz", "Todos os nós possuem no máximo dois filhos", "Todos os nós possuem um único filho"],
        "answer": "Os valores na subárvore esquerda são menores que o nó raiz"
    },
    {
        "id": 1,
        "question": "Qual é o algoritmo mais utilizado para encontrar o caminho mais curto entre dois nós em um grafo ponderado?",
        "options": ["Algoritmo de Dijkstra", "Algoritmo de Floyd-Warshall", "Busca em Largura", "Busca em Profundidade"],
        "answer": "Algoritmo de Dijkstra"
    },
    {
        "id": 1,
        "question": "O que é um ciclo em um grafo?",
        "options": ["Uma sequência de arestas que formam uma linha reta", "Uma sequência de vértices em que o último é igual ao primeiro", "Uma sequência de vértices sem repetições", "Uma sequência de arestas conectando dois vértices adjacentes"],
        "answer": "Uma sequência de vértices em que o último é igual ao primeiro"
    },
    {
        "id": 1,
        "question": "Qual é a principal diferença entre 'busca de força bruta' e 'algoritmos de busca eficientes'?",
        "options": ["Busca de força bruta explora todas as possibilidades", "Busca de força bruta usa mais memória", "Busca de força bruta é sempre mais eficiente", "Busca de força bruta requer dados ordenados"],
        "answer": "Busca de força bruta explora todas as possibilidades"
    },
    {
        "id": 1,
        "question": "Qual é a complexidade do algoritmo de ordenação Selection Sort?",
        "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
        "answer": "O(n²)"
    },
    {
        "id": 1,
        "question": "Em um algoritmo de busca binária, qual é a condição para que ele funcione corretamente?",
        "options": ["Os dados devem estar ordenados", "Os dados não podem conter repetições", "Os dados devem ser não ordenados", "Os dados devem ser numéricos"],
        "answer": "Os dados devem estar ordenados"
    },
    {
        "id": 1,
        "question": "Qual é a principal vantagem do algoritmo de Radix Sort?",
        "options": ["Ele é eficiente para números grandes", "Ele é mais rápido que o MergeSort", "Ele não requer comparação de elementos", "Ele é eficiente para listas pequenas"],
        "answer": "Ele não requer comparação de elementos"
    },
    {
        "id": 1,
        "question": "Qual é a complexidade de tempo do algoritmo de busca em largura (BFS) em um grafo representado por uma matriz de adjacência?",
        "options": ["O(n)", "O(n²)", "O(n + m)", "O(log n)"],
        "answer": "O(n²)"
    },
    {
        "id": 1,
        "question": "Qual é a diferença entre programação dinâmica e técnica gulosa?",
        "options": ["Programação dinâmica resolve problemas otimizando subproblemas menores, enquanto técnica gulosa toma decisões locais", "Técnica gulosa é mais eficiente em todos os casos", "Programação dinâmica é usada apenas para problemas de grafos", "Programação dinâmica toma decisões locais sem considerar o problema completo"],
        "answer": "Programação dinâmica resolve problemas otimizando subproblemas menores, enquanto técnica gulosa toma decisões locais"
    },
    {
        "id": 1,
        "question": "O que é um heap binário?",
        "options": ["Uma estrutura de dados baseada em filas", "Uma árvore binária onde cada nó é maior ou igual a seus filhos", "Uma lista ordenada em ordem crescente", "Uma estrutura baseada em grafos"],
        "answer": "Uma árvore binária onde cada nó é maior ou igual a seus filhos"
    },
    {
        "id": 1,
        "question": "Qual é a principal aplicação da estrutura de dados 'fila de prioridade'?",
        "options": ["Implementação de busca em largura (BFS)", "Implementação de algoritmos de caminho mínimo como Dijkstra", "Organização de dados em ordem crescente", "Armazenamento eficiente de dados duplicados"],
        "answer": "Implementação de algoritmos de caminho mínimo como Dijkstra"
    },
    {
        "id": 1,
        "question": "O que significa dizer que um algoritmo tem complexidade 'polinomial'?",
        "options": ["Que o tempo de execução cresce de forma linear", "Que o tempo de execução cresce mais rápido que exponencialmente", "Que o tempo de execução pode ser expresso como um polinômio de grau n", "Que o algoritmo tem complexidade constante"],
        "answer": "Que o tempo de execução pode ser expresso como um polinômio de grau n"
    },
    {
        "id": 1,
        "question": "Qual é a principal diferença entre listas simplesmente encadeadas e listas duplamente encadeadas?",
        "options": ["Listas duplamente encadeadas permitem navegação bidirecional", "Listas simplesmente encadeadas armazenam os elementos em ordem inversa", "Listas duplamente encadeadas são mais rápidas para inserções", "Listas simplesmente encadeadas permitem acesso direto por índice"],
        "answer": "Listas duplamente encadeadas permitem navegação bidirecional"
    },
    {
        "id": 1,
        "question": "Qual é a função principal de uma tabela hash?",
        "options": ["Ordenar elementos de forma eficiente", "Armazenar e recuperar dados rapidamente usando uma chave", "Evitar duplicação de dados", "Armazenar dados em ordem crescente"],
        "answer": "Armazenar e recuperar dados rapidamente usando uma chave"
    },
    {
        "id": 1,
        "question": "Qual é a complexidade média de busca em uma tabela hash bem projetada?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "answer": "O(1)"
    },
    {
        "id": 1,
        "question": "O que é um algoritmo de força bruta?",
        "options": ["Um algoritmo que tenta todas as soluções possíveis", "Um algoritmo que usa menos memória para resolver problemas", "Um algoritmo que sempre encontra a solução ótima", "Um algoritmo que usa programação dinâmica"],
        "answer": "Um algoritmo que tenta todas as soluções possíveis"
    },
    {
        "id": 1,
        "question": "O que significa 'overfitting' em aprendizado de máquina?",
        "options": ["Quando o modelo aprende bem os dados de treinamento, mas generaliza mal para novos dados", "Quando o modelo tem precisão perfeita em todos os dados", "Quando o modelo não consegue aprender os dados de treinamento", "Quando o modelo tem precisão baixa em todos os cenários"],
        "answer": "Quando o modelo aprende bem os dados de treinamento, mas generaliza mal para novos dados"
    },
    {
        "id": 1,
        "question": "Qual é a diferença entre complexidade de tempo e complexidade de espaço?",
        "options": ["Complexidade de tempo mede o uso de memória, enquanto a de espaço mede o tempo de execução", "Complexidade de tempo mede o tempo de execução e a de espaço mede o uso de memória", "Ambas são idênticas para todos os algoritmos", "A complexidade de espaço é irrelevante em grandes programas"],
        "answer": "Complexidade de tempo mede o tempo de execução e a de espaço mede o uso de memória"
    },
    {
        "id": 1,
        "question": "O que é um algoritmo guloso?",
        "options": ["Um algoritmo que sempre toma a melhor decisão local, sem considerar o problema global", "Um algoritmo que encontra a solução ótima em todos os casos", "Um algoritmo que usa recursão para resolver problemas", "Um algoritmo que tenta todas as soluções possíveis"],
        "answer": "Um algoritmo que sempre toma a melhor decisão local, sem considerar o problema global"
    },
    {
        "id": 1,
        "question": "Qual é a principal característica de um algoritmo NP-completo?",
        "options": ["É um algoritmo que sempre encontra a solução ótima", "É um problema que pode ser verificado em tempo polinomial, mas cuja solução pode não ser encontrada em tempo polinomial", "É um problema que sempre requer força bruta para ser resolvido", "É um problema que não possui solução"],
        "answer": "É um problema que pode ser verificado em tempo polinomial, mas cuja solução pode não ser encontrada em tempo polinomial"
    }
]
# Questoes de equação 
