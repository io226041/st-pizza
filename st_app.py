import streamlit as st

def main():
    st.title("Pizza Toppings Selector")

    # Option field for "topping1" with 7 values
    topping1 = st.selectbox("Select Topping 1", ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Olives", "Cheese"])

    # Option field for "topping2" with 7 values
    topping2 = st.selectbox("Select Topping 2", ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Olives", "Cheese"])

    # Option field for "topping3" with 7 values
    topping3 = st.selectbox("Select Topping 3", ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Olives", "Cheese"])

    st.write(f"You have selected toppings: {topping1}, {topping2}, {topping3}")

if __name__ == "__main__":
    main()
