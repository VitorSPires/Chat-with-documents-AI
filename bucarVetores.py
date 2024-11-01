from sentence_transformers import SentenceTransformer
from annoy import AnnoyIndex
import json

# Carregar o modelo de embeddings e o índice
modelo_embeddings = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
dimensao = 384  # Dimensão do modelo de embeddings
annoy_index = AnnoyIndex(dimensao, 'angular')
annoy_index.load('indice_vetores.ann')

# Carregar o mapeamento de IDs para textos
with open('mapa_texto_id.json', 'r') as f:
    mapa_texto_id = json.load(f)

# Função de busca por similaridade
def buscar_texto_similar(texto_consulta, top_k=5):
    # Gerar embedding da consulta
    embedding_consulta = modelo_embeddings.encode(texto_consulta)
    
    # Buscar os top_k itens mais similares
    ids_similares, distancias = annoy_index.get_nns_by_vector(embedding_consulta, top_k, include_distances=True)
    
    # Recuperar textos e similaridades
    #resultados = [(mapa_texto_id[str(idx)], 1 - distancia) for idx, distancia in zip(ids_similares, distancias)]
    resultados = [(mapa_texto_id[str(idx)]) for idx, distancia in zip(ids_similares, distancias)]
    
    return resultados

# Exemplo de busca
#texto_consulta = "biological risk"
#resultados_similares = buscar_texto_similar(texto_consulta)

# Exibir os resultados
#for texto, similaridade in resultados_similares:
#    print(f"Texto: {texto}\n Similaridade: {similaridade:.2f}\n\n---------\n\n")
