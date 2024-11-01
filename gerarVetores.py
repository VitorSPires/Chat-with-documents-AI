from sentence_transformers import SentenceTransformer
from annoy import AnnoyIndex
import json

# Inicializar o modelo Hugging Face para embeddings
modelo_embeddings = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Textos para indexação
with open("Manual-CAM_ES.txt", "r", encoding="utf-8") as input:
    textos = input.read().split("\n\n") 

# Configuração do índice
dimensao = 384  # Dimensão do modelo de embeddings
annoy_index = AnnoyIndex(dimensao, 'angular')

# Dicionário para mapear IDs de índice com textos originais
mapa_texto_id = {}

# Gerar embeddings e adicionar ao Annoy
for idx, texto in enumerate(textos):
    print(f'Gerando vetores: {idx+1}/{len(textos)}')
    embedding = modelo_embeddings.encode(texto)
    annoy_index.add_item(idx, embedding)
    mapa_texto_id[idx] = texto.replace('\n', '')

# Construir o índice com 10 árvores
annoy_index.build(10)

# Salvar o índice e o mapeamento de IDs
annoy_index.save('indice_vetores.ann')
with open('mapa_texto_id.json', 'w') as f:
    json.dump(mapa_texto_id, f)

print("Índice e mapeamento de textos salvos com sucesso.")
