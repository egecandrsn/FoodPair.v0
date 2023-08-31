# FoodPair.v0 Ingredient Recommender using Word2Vec

This repository contains a simple application that uses the Word2Vec model to recommend similar ingredients based on the user's selection. The application provides a user-friendly interface where you can select up to 6 ingredients, and it will display a list of recommended ingredients that are similar to the selected ones.

## How It Works

The application utilizes the Gensim library to load a pre-trained Word2Vec model that has learned to represent words (in this case, ingredients) in a high-dimensional vector space. The model captures semantic relationships between words, allowing it to find ingredients that are similar in meaning or context.

### Prerequisites

To run this application, you need to have Python and the required libraries installed. You can install the necessary dependencies using the following command:

```bash
pip install gensim gradio
```

### Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/egecandrsn/ingredient-recommender.git
```

2. Navigate to the project directory:

```bash
cd ingredient-recommender
```

3. Run the application:

```bash
python app.py
```

4. A web interface will open in your default web browser. You can select ingredients from the dropdown menus. Choose up to 6 ingredients, and the application will display a list of recommended ingredients based on your selection.

5. Experiment with different ingredient combinations to explore various recommendations.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify and expand upon this README as needed to provide more information about your project, its purpose, and how users can use or contribute to it.
