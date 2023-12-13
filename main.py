import streamlit

def largest_value(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3


def main():
    streamlit.title("Largest Value between three Numbers")

    n1=streamlit.number_input("First Number")
    n2=streamlit.number_input("Second Number")
    n3=streamlit.number_input("Third Number")

    if streamlit.button("Submit"):
        largest_integer=largest_value(n1,n2,n3)
        streamlit.success("Largest value :"+str(largest_integer))

if __name__ == "__main__":
    main()