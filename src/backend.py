import streamlit as st

import pandas as pd
from openai import OpenAI
from sklearn.model_selection import train_test_split
from statsmodels import api as sm

import warnings

warnings.filterwarnings("ignore")

client = None


def is_topic_set(x):
    return not x.startswith("no")


def predict_price(pizza_config, model):

    data = {
        'Intercept': [2],
        'Topping 1': [is_topic_set(pizza_config.toppings[0])],
        'Topping 2': [is_topic_set(pizza_config.toppings[1])],
        'Topping 3': [is_topic_set(pizza_config.toppings[2])],
        'Size': [pizza_config.size],
        'Extras Sauce': [int(pizza_config.extra_sauce)],
        'Extra Cheese': [int(pizza_config.extra_cheese)],
        'Distance to City Center (km)': [pizza_config.distance],
        'Restaurant': [pizza_config.location],
        'Rating': [pizza_config.rating]
    }
    print(data)
    df = pd.DataFrame(data)

    df['Topping 1'] = df['Topping 1'].astype(int)
    df['Topping 2'] = df['Topping 2'].astype(int)
    df['Topping 3'] = df['Topping 3'].astype(int)
    df['Extras Sauce'] = df['Extras Sauce'].astype(int)
    df['Extra Cheese'] = df['Extra Cheese'].astype(int)

    print(df.transpose())
    predicted_price = model.predict(df)
    print(f"Predicted Price for the User's Pizza: {predicted_price.values[0]}")
    return predicted_price.values[0]


@st.cache_resource
def create_model(csv_file):
    df = pd.read_csv(csv_file)
    Y = df['Relative Price']
    X = df.drop(['Relative Price', 'Pizza Name', 'Topping 3_Meat', 'Topping 3_None', 'Topping 4_Fish', 'Topping 4_None',
                 'Overall Weight'], axis=1)  # write your code here
    X = sm.add_constant(X)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=1)
    # create the model
    model = sm.OLS(y_train, X_train).fit()  # write your code here
    print(model.summary())
    return model


def make_dalle_request(prompt, img_gen_model):
    try:
        global client
        if client is None:
            client = OpenAI()
        response = client.images.generate(
            model=img_gen_model,
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        # response.raise_for_status()  # Raise an error for bad responses (e.g., 4xx, 5xx)
        return response.data[0].url
    except Exception as e:
        st.error(f"Error making DALL-E API request: {e}")
        return "https://example.com/default_pizza.jpg"


def generate_pizza_image(toppings, img_gen_model, mock):
    if mock:
        return f"https://picsum.photos/seed/{'-'.join(toppings)}/200"
    # Construct a text prompt for DALL-E
    prompt = f"A round pizza on a black table with toppings: {', '.join(toppings)}"
    return make_dalle_request(prompt, img_gen_model)
