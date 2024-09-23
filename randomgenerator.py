
import streamlit as st
st.set_page_config(layout="wide")

# Function to generate random numbers using the mid-square method
def mid_square_method(n, u):
    results = []
    i = n
    while i:
        k = len(str(u))
        u = u**2
        u_str = str(u)
        while len(u_str) < k * 2:
            u_str = '0' + u_str
        if k % 2:
            start = (k - 1) // 2
        else:
            start = k // 2 
        u_str = u_str[start:start + k]
        u = int(u_str)
        results.append(u)
        i -= 1
    return results

# ----Streamlit app----
st.title("Mid-Square Random Number Generator")
n = st.number_input("Enter the sample size (n):", min_value=1)
u = st.number_input("Enter the initial seed (u):", min_value=1)
if st.button("Generate Random Numbers"):
    results = mid_square_method(n, u)
    st.write("Generated Numbers:")
    st.write(results)
