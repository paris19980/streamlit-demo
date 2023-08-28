#################################
##   pages/More tutorials.py   ##
#################################

###############################################################
# import python libraries
###############################################################
import streamlit as st

###############################################################
# page info
###############################################################
st.set_page_config(
    page_title="More tutorials | HKUST Digital Humanities Initiative",
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
st.title("📝 More tutorials")

st.markdown("""
https://digitalhumanities.hkust.edu.hk/tutorials/

Welcome to visit our website, where we have a series of tutorials waiting to unlock your skills in digital humanities. We understand the growing importance of leveraging technology in the field of humanities, and our tutorials are designed to equip you with the knowledge and tools to excel in this domain. 

If you have any questions or feedback, please feel free to [reach out to us](https://forms.office.com/r/FPkLhaE2sr).

Happy learning! 🎉

---

_The [HKUST Digital Humanities Initiative](https://digitalhumanities.hkust.edu.hk/) is a collaborative community aimed at bringing together faculty, library, and students to explore digital humanities skills and develop innovative digital projects. It bridges the gap between science and the humanities through digital methods and practices._

""")



