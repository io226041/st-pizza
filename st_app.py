# Import necessary libraries
import streamlit as st


# Define the main function for your app
def main():
    # Give your app a title
    st.title("Simple Square Calculator")

    # Add a sidebar with some information
    st.sidebar.header("About")
    st.sidebar.text("This is a simple app to calculate the square of a number.")

    # Get user input for a number
    user_input = st.number_input("Enter a number:", min_value=0)

    # Calculate the square of the input number
    square_result = user_input ** 2

    # Display the result
    st.write(f"The square of {user_input} is: {square_result}")


# Run the app
if __name__ == "__main__":
    main()
