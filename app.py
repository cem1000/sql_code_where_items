import streamlit as st

def to_sql_format(items, data_type, items_per_line=5):
    if data_type == "string":
        formatted_items = [f"'{item}'" for item in items]
    else:
        formatted_items = [f"{item}" for item in items]

    # Insert line breaks after every 5 items
    lines = []
    for i in range(0, len(formatted_items), items_per_line):
        line = ", ".join(formatted_items[i:i + items_per_line])
        lines.append(line)

    # Join items with commas and wrap in brackets
    formatted_items = "(\n" + ",\n".join(lines) + "\n)"

    return formatted_items

def app():
    st.title('SQL WHERE Clause Converter')
    st.sidebar.subheader('Instructions')
    st.sidebar.markdown("""
    1. Enter a list of items in the text box, with each item on a new line.
    2. Select the data type of the items.
    3. Click the 'Convert to SQL Format' button.
    4. The converted SQL WHERE clause will be displayed.
    """)
    st.sidebar.subheader('About')
    st.sidebar.markdown("""
    This app allows you to quickly convert a list of items into a SQL WHERE clause format. This can be useful when you want to use the items in a WHERE clause in a SQL query.
    """)
    st.write('Enter your list of items:')
    input_text = st.text_area('', height=200)
    data_type = st.selectbox('Select the data type of your items:', ['string', 'integer'])
    if st.button('Convert to SQL Format'):
        items = input_text.split('\n')
        if len(items) > 1:
            try:
                formatted_items = to_sql_format(items, data_type)
            except ValueError as e:
                st.error(str(e))

            if formatted_items:
                st.write(f"SQL format for {data_type} items:")
                st.code(formatted_items)
        else:
            st.warning("Please enter at least 2 items, each on a new line.")

if __name__ == '__main__':
    app()
