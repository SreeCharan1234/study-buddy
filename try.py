import streamlit as st

# Create two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div style="border: 2px solid #ccc; padding: 20px; background-color: #f0f0f0; border-radius: 10px;">
        <h2>Product A</h2>
        <p>This is a brief description of Product A. Highlight its key features and benefits.</p>
        <p><strong>To purchase,</strong> please visit our online store at [link to store]. You can also contact our sales team at [phone number] or [email address].</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="border: 2px solid #ccc; padding: 20px; background-color: #f0f0f0; border-radius: 10px;">
        <h2>Product B</h2>
        <p>This is a brief description of Product B. Highlight its key features and benefits.</p>
        <p><strong>To purchase,</strong> please fill out the contact form below or call us at [phone number].</p>
        <button>Contact Us</button>
    </div>
    """, unsafe_allow_html=True)
