import streamlit as st
import requests

# DALL-E API endpoint (replace with the actual endpoint if available)
dalle_api_endpoint = "https://example.com/dalle/api"

def make_dalle_request(prompt):
    try:
        response = requests.post(dalle_api_endpoint, json={"prompt": prompt})
        response.raise_for_status()  # Raise an error for bad responses (e.g., 4xx, 5xx)
        return response.json().get("image_url", "https://example.com/default_pizza.jpg")
    except requests.exceptions.RequestException as e:
        st.error(f"Error making DALL-E API request: {e}")
        return "https://example.com/default_pizza.jpg"

def generate_pizza_image(toppings):
    # Construct a text prompt for DALL-E
    prompt = f"A round pizza with toppings: {', '.join(toppings)}"
    return make_dalle_request(prompt)

def main():
    st.title("Pizza Toppings Selector")

    # Create a sidebar for input fields
    st.sidebar.header("Select Toppings")
    topping1 = st.sidebar.selectbox("Topping 1", ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Olives", "Cheese"])
    topping2 = st.sidebar.selectbox("Topping 2", ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Olives", "Cheese"])
    topping3 = st.sidebar.selectbox("Topping 3", ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Olives", "Cheese"])

    selected_toppings = [topping1, topping2, topping3]

    # Display a single pizza image with all three selected toppings in the center
    st.image(generate_pizza_image(selected_toppings), caption="Combined Toppings", width=400, use_container_width=True)

    st.write(f"You have selected toppings: {topping1}, {topping2}, {topping3}")

if __name__ == "__main__":
    main()
