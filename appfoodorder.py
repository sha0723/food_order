import streamlit as st

st.title("Food Ordering System")

customer_name = st.text_input("Enter Customer Name")
food = st.selectbox("Select Food", ["Nasi Lemak", "Chicken Chop", "Burger"])
quantity = st.number_input("Quantity", min_value=0, step=1)  # Allows 0 for validation

prices = {"Nasi Lemak": 5, "Chicken Chop": 12, "Burger": 8}

if st.button("Order"):
    try:
        if not customer_name or not customer_name.strip():
            st.error("Customer name cannot be empty!")
        elif quantity <= 0:
            st.error("Quantity must be greater than 0!")
        else:
            total = quantity * prices[food]
            st.success("Order placed successfully!")
            st.markdown("----- Booking Summary -----")
            st.write(f"**Customer Name:** {customer_name}")
            st.write(f"**Food:** {food}")
            st.write(f"**Quantity:** {quantity}")
            st.write(f"**Total Price: RM {total:.2f}")
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
