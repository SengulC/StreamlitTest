import streamlit as st

if 'chapters' not in st.session_state: st.session_state.chapters = [{"story": "Ashskslas sfghjk shjaksakl", "images": ["https://picsum.photos/512"]},{"story": "Qwerwetyui wtyquio tyqwuio", "images": ["https://picsum.photos/512"]}]

for index, chapter in enumerate(st.session_state.chapters):
    story = chapter["story"]
    images = chapter["images"]
    
    st.write(story) 
    cols = st.columns(3)
    st.divider()
    count = 0
    for i, image in enumerate(images):
        with cols[count]:
            count+=1
            if count == 3:
                count = 0
            st.image(images[i])      

def submit():
    st.session_state.chapters.append({"story": "THE STORY IS CHANGED.", "images": ["https://picsum.photos/512"]})

st.text_input('', placeholder="Caption", on_change=submit)

prompt = st.chat_input("Say something", on_submit=submit, disabled=True)
   
