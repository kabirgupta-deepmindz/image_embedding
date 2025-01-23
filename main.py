import os
import json
from sentence_transformers import SentenceTransformer


model = SentenceTransformer('all-MiniLM-L6-v2')

metadata_file = "./metadata.json"
embedding_file = "./embedding.json"

isExists = os.path.isfile(metadata_file)

if isExists:
    # print("")
    with open(metadata_file, "r") as f:
        # print(type(f))
        metadata = json.load(f)
    # print(metadata)
else:
    print(f"File with path {isExists}")
    exit()

text_embeddings = []

SKIP_IMAGE_CHECK = True
for item in metadata:
    # print(item)
    file_path = item.get("title", "")
    image_exists = os.path.isfile(file_path)
    if SKIP_IMAGE_CHECK | image_exists:
        print(f"File for Image {image_exists}, exists")
        description = item.get("description", "")
        print("description", description)

        if not description:
            print("Description not found!")
            continue
        else:
            print('Generating Embedding for Image Description!')
            embedding = model.encode(description)
            text_embeddings.append({
                'filename':file_path,
                'description': description,
                'embedding': embedding.tolist(
                )
            })
    else:
        print(f"Image file for path {file_path} does not exists, Skipping Embedding!")
        continue

if(len(text_embeddings) > 0):
     with open(embedding_file ,'w') as f:
            json.dump(text_embeddings, f)

print("Text embeddings generated and saved successfully.")