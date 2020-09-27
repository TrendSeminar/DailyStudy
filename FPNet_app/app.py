import numpy as np
import streamlit as st
import os, urllib, cv2


def main():
    st.title("FPNet Demo: The Analysis of Complicated Drawings")
    
    """
    This *FPNet demo* is able to reconstruct walls \
        in areas with overlapping graphics or nonuniform patterns, \
            thus allowing the room structures to be recovered even from complicated drawings.
    
    <img src="https://raw.githubusercontent.com/syoi92/demo-fpnet/master/src/imgs/fig1.samples.TIF" width="900px"/>
    """
    # st.markdown("![img](https://raw.githubusercontent.com/syoi92/demo-fpnet/master/src/imgs/fig1.samples.TIF \"FPNet demo sample\")")
    fig1 = cv2.imread("src/imgs/fig1.samples.tif", cv2.IMREAD_COLOR)
    st.image(fig1, caption='Fig. \
                 (a) input floor plan images and our results of (b) the style-transferred plans\
                      and (c) the vectorized floor plans',
                       use_column_width=True, channels='BGR')

    readme_text = st.markdown(get_file_content_as_string("src/instruction.md"))


    st.sidebar.title("Contents")
    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Instructions", "Run the app (EAIS-fp)", "Run the app (SNU-fp)"])
    if app_mode == "Instruction":
        st.sidebar.success('To continue select "Run the app".')
    elif app_mode == "Run the app (EAIS-fp)":
        run_the_app()
    elif app_mode == "un the app (SNU-fp)":
        readme_text.empty()



    test_num = st.slider("test dataset", 0, 10, 2, 1)

    image = cv2.imread("src/imgs/Fig. 12.tif", cv2.IMREAD_COLOR)
    image = image[:, :, [2, 1, 0]] # BGR -> RGB

    st.markdown("**results**")
    st.image(image, use_column_width=True)
    



def run_the_app():
    # features[feature] = st.sidebar.slider(feature, 0, 100, 50, 5)

    return


@st.cache(show_spinner=False)
def get_file_content_as_string(path):
    url = 'https://raw.githubusercontent.com/syoi92/demo-fpnet/master/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")

# path = 'src/imgs/fig1.samples.TIF'
@st.cache(show_spinner=False)
def get_file_content_as_img(path):
    url = 'https://raw.githubusercontent.com/syoi92/demo-fpnet/master/' + path
    response = urllib.request.urlopen(url)

    img = cv.imdecode(response.read(), cv.IMREAD_COLOR)
    return response.read().decode("utf-8")


def load_image(num):

#    with urllib.request.urlopen(url) as response:
#        image = np.asarray(bytearray(response.read()), dtype="uint8")
#    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#    image = image[:, :, [2, 1, 0]] # BGR -> RGB
    return num


if __name__ == "__main__":
    main()