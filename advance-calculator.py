import streamlit as st
import math

# Title of the app
st.title("Scientific Calculator")

# Input from user
expression = st.text_input("Enter the mathematical expression:")

# Display buttons
if st.button('Evaluate'):
    try:
        # Safe evaluation of mathematical expressions using eval
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Operations Reference
st.sidebar.header("Operations Reference")

st.sidebar.write("""
### Basic Operations:
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`

### Scientific Functions:
- Sine: `sin()`
- Cosine: `cos()`
- Tangent: `tan()`
- Square Root: `sqrt()`
- Power: `pow(base, exp)`
- Exponential: `exp()`
- Logarithm: `log()`

### Constants:
- Pi: `pi`
- Euler's number: `e`
""")
