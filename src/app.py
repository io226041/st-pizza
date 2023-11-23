import os
from dataclasses import dataclass
import streamlit as st

from backend import predict_price, create_model
from ui import app_main_frame, app_sidebar

TOPPINGS = {
    "sauce": ["Tomato Sauce", "Pesto", "Alfredo"],
    "vegetable": ["Pepperoni", "Mushrooms", "Onions", "Tomatoes"],
    "meat": ["Sausage", "Bacon", "Gyros"],
    # "chease": ["Cheddar", "Mozzarella", "Parmesan", "Feta"],
}

IMG_GEN_MODEL = "dall-e-3"
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']


@dataclass
class PizzaConfig:
    toppings: [str]
    size: str
    extra_sauce: bool
    extra_cheese: bool
    distance: int
    location: str
    rating: int


def main():
    model = create_model(csv_file="data/pizza_dataset_relative_price.csv")
    pizza_config = app_sidebar()
    predicted_price = predict_price(pizza_config, model)
    app_main_frame(pizza_config, predicted_price, IMG_GEN_MODEL)


if __name__ == "__main__":
    main()
