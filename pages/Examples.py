###########################
##   pages/Examples.py   ##
###########################

###############################################################
# import python libraries
###############################################################
import streamlit as st

###############################################################
# page info
###############################################################
st.set_page_config(
    page_title="Examples of streamlit commands | HKUST Digital Humanities Initiative",
    page_icon="👋",
)

###############################################################
# sidebar
###############################################################
with st.sidebar:
    st.markdown("""
                [HKUST Digital Humanities Initiative](https://digitalhumanities.hkust.edu.hk/)
                """)
    st.markdown("""
                This website serves as a demo to showcase the capabilities and functionalities of Streamlit in creating web applications. If you are interested in learning the step-by-step process of how this website was created, please refers to [our article](https://digitalhumanities.hkust.edu.hk/tutorials/learn-python-from-zero-for-absolute-beginner-3-create-website/) for detailed instructions and explanations.
                """)

###############################################################
# page content
###############################################################
st.caption("Demo by HKUST Digital Humanities Initiative")
st.title("Examples of Streamlit Commands")

st.markdown(
    """
    Streamlit offers numerous possibilities from creating interactive visualizations to building data-driven web applications. We highly recommend you to explore its full potential by reading its documentation. Discover the vast possibilities that Streamlit offers!

    👉 https://docs.streamlit.io/library/api-reference

    """)

st.image('./images/streamlit-doc.gif')


