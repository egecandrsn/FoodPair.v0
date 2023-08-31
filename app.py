import gensim
from gensim.models import Word2Vec
import gradio as gr

# Load your trained Word2Vec model
model = Word2Vec.load("word2vecsg2.model")

def recommend_ingredients(*ingredients):
    # Filter out any None values from the ingredients
    ingredients = [i for i in ingredients if i]

    # Get most similar ingredients
    similar_ingredients = model.wv.most_similar(positive=ingredients, topn=8)
    
    # Format the output
    output = "\n".join([f"{ingredient}:  %{round(similarity*100, 2)}" for ingredient, similarity in similar_ingredients])
    
    return output

# Get the vocabulary of the model and sort it alphabetically
vocab = sorted(model.wv.index_to_key)

# Allow user to select multiple ingredients
ingredient_selections = [gr.inputs.Dropdown(choices=vocab, label=f"Ingredients {i+1}") for i in range(6)]

# Create the interface
iface = gr.Interface(
    fn=recommend_ingredients, 
    inputs=ingredient_selections, 
    outputs="text", 
    title="Ingredient Recommender",
    description="Select up to 6 ingredients to get recommendations for similar ingredients.",
    layout="vertical"
)

iface.launch()
