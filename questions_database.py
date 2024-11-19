questions_list_2 = [
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



questions_list= [
    # 1 a 10
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
    {
        "id": "1",
        "question": "Qual é a complexidade do busca binária?",
        "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
        "answer": "O(log n)"
    },
    {
        "id": "2",
        "question": "Pior caso do Bubble Sort?",
        "options": ["O(n)", "O(n²)", "O(log n)", "O(n log n)"],
        "answer": "O(n²)"
    },
    {
        "id": "3",
        "question": "Qual estrutura acessa o centro mais rápido?",
        "options": ["Fila", "Pilha", "Lista Dupla", "Vetores"],
        "answer": "Vetores"
    },
    {
        "id": "4",
        "question": "Qual algoritmo encontra menor caminho com pesos positivos?",
        "options": ["Dijkstra", "Bellman-Ford", "BFS", "DFS"],
        "answer": "Dijkstra"
    },
    {
        "id": "5",
        "question": "Pior caso do QuickSort?",
        "options": ["O(n)", "O(n²)", "O(log n)", "O(n log n)"],
        "answer": "O(n²)"
    },
    {
        "id": "6",
        "question": "BST vs AVL: Qual a diferença?",
        "options": [
            "AVL balanceia altura das subárvores",
            "BST aceita apenas elementos únicos",
            "Folhas da BST estão no mesmo nível",
            "BST tem no máximo 3 filhos"
        ],
        "answer": "AVL balanceia altura das subárvores"
    },
    {
        "id": "7",
        "question": "Dijkstra trabalha com quais pesos?",
        "options": ["Qualquer peso", "Pesos negativos", "Pesos positivos", "Sem peso"],
        "answer": "Pesos positivos"
    },
    {
        "id": "8",
        "question": "Quando usar MergeSort em vez de QuickSort?",
        "options": [
            "Dados quase ordenados",
            "O(n log n) garantido no pior caso",
            "Pouca memória disponível",
            "Dados pequenos"
        ],
        "answer": "O(n log n) garantido no pior caso"
    },
    {
        "id": "9",
        "question": "BFS é melhor que DFS quando?",
        "options": [
            "BFS acha o menor caminho",
            "DFS é mais rápido",
            "BFS usa menos memória",
            "BFS é para grafos direcionados"
        ],
        "answer": "BFS acha o menor caminho"
    },
    {
        "id": "10",
        "question": "Complexidade do HeapSort?",
        "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
        "answer": "O(n log n)"
    },
    {
        "id": "11",
        "question": "O que é um DAG?",
        "options": [
            "Grafo sem ciclos com direção",
            "Grafo onde todos vértices têm grau 0",
            "Grafo onde existe pelo menos um ciclo",
            "Grafo totalmente conectado"
        ],
        "answer": "Grafo sem ciclos com direção"
    },
    {
        "id": "12",
        "question": "Complexidade do DFS com lista de adjacência?",
        "options": ["O(n)", "O(n²)", "O(n + m)", "O(m)"],
        "answer": "O(n + m)"
    },
    {
        "id": "13",
        "question": "O que é 'backtracking'?",
        "options": [
            "Explora todas possibilidades",
            "Resolve problemas usando simulações",
            "Decisões ótimas em etapas",
            "Sempre acha solução ótima"
        ],
        "answer": "Explora todas possibilidades"
    },
    {
        "id": "14",
        "question": "Ordenação estável mantém o quê?",
        "options": [
            "Ordem relativa de iguais",
            "Ordem crescente",
            "Menor tempo de execução",
            "Gasta menos memória"
        ],
        "answer": "Ordem relativa de iguais"
    },
    {
        "id": "15",
        "question": "Vantagem do Bellman-Ford sobre Dijkstra?",
        "options": [
            "Trabalha com pesos negativos",
            "Requer grafo conectado",
            "Menor complexidade",
            "Mais rápido em grafos densos"
        ],
        "answer": "Trabalha com pesos negativos"
    },
    {
        "id": "16",
        "question": "Busca sequencial: Complexidade?",
        "options": ["O(1)", "O(n)", "O(n log n)", "O(log n)"],
        "answer": "O(n)"
    },
    {
        "id": "17",
        "question": "Objetivo do algoritmo de compressão?",
        "options": [
            "Reduzir tamanho dos dados",
            "Minimizar tempo de execução",
            "Evitar duplicações",
            "Armazenar em ordem"
        ],
        "answer": "Reduzir tamanho dos dados"
    },
    {
        "id": "18",
        "question": "Floyd-Warshall vs Dijkstra: diferença?",
        "options": [
            "Resolve para todos os pares",
            "Usa menos memória",
            "Mais eficiente em grafos pequenos",
            "Resolve só caminhos mínimos simples"
        ],
        "answer": "Resolve para todos os pares"
    },
    {
        "id": "19",
        "question": "O que é uma árvore AVL?",
        "options": [
            "Árvore balanceada por altura",
            "Nó com no máximo 2 filhos",
            "Todos filhos têm mesmo valor",
            "Armazenamento em lista"
        ],
        "answer": "Árvore balanceada por altura"
    },
    {
        "id": "20",
        "question": "Insertion Sort no pior caso?",
        "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
        "answer": "O(n²)"
    },
    {
        "id": "21",
        "question": "Propriedade de uma BST?",
        "options": [
            "Subárvore esquerda tem valores menores",
            "Filhos têm no máximo dois nós",
            "Todos os nós têm alturas iguais",
            "Todos os valores são únicos"
        ],
        "answer": "Subárvore esquerda tem valores menores"
    },
    {
        "id": "22",
        "question": "Radix Sort é eficiente porque?",
        "options": [
            "Não usa comparação de elementos",
            "É rápido com listas pequenas",
            "Usa menos memória",
            "Ordena melhor strings"
        ],
        "answer": "Não usa comparação de elementos"
    },
    {
        "id": "23",
        "question": "Busca binária requer o quê?",
        "options": [
            "Dados ordenados",
            "Dados únicos",
            "Dados sem repetição",
            "Dados numéricos"
        ],
        "answer": "Dados ordenados"
    },
    {
        "id": "24",
        "question": "Uso da fila de prioridade?",
        "options": [
            "Dijkstra",
            "Busca em largura",
            "Organizar dados",
            "Evitar duplicações"
        ],
        "answer": "Dijkstra"
    },
    {
        "id": "25",
        "question": "Complexidade média de hash table?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"],
        "answer": "O(1)"
    },
    {
        "id": "26",
        "question": "O que é overfitting?",
        "options": [
            "Treina bem, generaliza mal",
            "Erra dados de treino",
            "Não aprende padrões",
            "Tem baixa precisão sempre"
        ],
        "answer": "Treina bem, generaliza mal"
    },
    {
        "id": "27",
        "question": "O que é programação dinâmica?",
        "options": [
            "Divide problemas em subproblemas",
            "Decisões locais ótimas",
            "Sempre mais rápida que gulosa",
            "É usada só em grafos"
        ],
        "answer": "Divide problemas em subproblemas"
    },
    {
        "id": "28",
        "question": "Heap binário é?",
        "options": [
            "Árvore onde pai ≥ filhos",
            "Lista ordenada",
            "Fila eficiente",
            "Grafo cíclico"
        ],
        "answer": "Árvore onde pai ≥ filhos"
    },
    {
        "id": "29",
        "question": "Complexidade do Selection Sort?",
        "options": ["O(n)", "O(n²)", "O(log n)", "O(n log n)"],
        "answer": "O(n²)"
    },
    {
        "id": "30",
        "question": "O que é um algoritmo guloso?",
        "options":[
            "Melhor decisão local",
            "Melhor solução global",
            "Explora todas opções",
            "Usa programação dinâmica"
        ]
    }
];