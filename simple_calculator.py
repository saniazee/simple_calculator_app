import streamlit as st

def calculate_bmi(number1, number2,operation):

    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        return number1 / number2
        if number2 != 0:
            return number1 / number2
        st.write('Division by zero error')
        return 'Division by zero error'    
    
 
 
def main():
    st.title('Simple Calculator')

    number1 = st.number_input('Enter the first number',format='%f')
    number2 = st.number_input('Enter the second number',format='%f')
    operation = st.selectbox('Select operation', ['+', '-', '*', '/'])
    if st.button('Calculate'):
        result = calculate_bmi(number1, number2, operation)
        st.write(f"Result: {result}")
if __name__ == '__main__':



 main() 