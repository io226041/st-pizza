import streamlit as st

# Placeholder function for generating pizza images using DALL-E API
def generate_pizza_image(toppings):
    # Replace this with actual DALL-E API calls to generate pizza images
    # Simulating the image URL based on the toppings for illustration
    toppings_to_images = {
        "Pepperoni": "https://example.com/pepperoni_pizza.jpg",
        "Mushrooms": "https://example.com/mushroom_pizza.jpg",
        "Onions": "https://example.com/onion_pizza.jpg",
        "Sausage": "https://example.com/sausage_pizza.jpg",
        "Bacon": "https://example.com/bacon_pizza.jpg",
        "Olives": "https://example.com/olive_pizza.jpg",
        "Cheese": "https://example.com/cheese_pizza.jpg",
    }

    # Concatenate images for selected toppings into a single image
    combined_image_url = "https://example.com/default_pizza.jpg"  # Default image URL
    for topping in toppings:
        combined_image_url += "_" + toppings_to_images.get(topping, "default")

    return combined_image_url

def main():
    st.title("Pizza Toppings Selector")

    # Create a sidebar for input fields
    st.sidebar.header("Select Toppings")
    topping1 = st.sidebar.selectbox("Topping 1", ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Olives", "Cheese"])
    topping2 = st.sidebar.selectbox("Topping 2", ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Olives", "Cheese"])
    topping3 = st.sidebar.selectbox("Topping 3", ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Olives", "Cheese"])

    selected_toppings = [topping1, topping2, topping3]

    # Display a single pizza image with all three selected toppings in the center
    # st.image(generate_pizza_image(selected_toppings), caption="Combined Toppings", width=400, use_container_width=True)
    st.write(generate_pizza_image(selected_toppings), caption="Combined Toppings", width=400, use_container_width=True)

    st.write(f"You have selected toppings: {topping1}, {topping2}, {topping3}")

if __name__ == "__main__":
    main()
