import pandas as pd
import streamlit as st
import numpy as np

option = st.sidebar.radio("Pages",["**Home**", "**Timeline**", "**Characters and Objects**", "**Whole Lore**", "**TREASURE**", "**ZERO : FEVER**", "**THE WORLD**", "**Golden Hour**", "**Circle Theory**", "**Motifs**"])

if option == "**Home**":
    st.title("welcome loretinys!")

elif option == "**Timeline**":
    st.write("this page is currently under construction")

elif option == "**Characters and Objects**":
    characters_and_objects = {
        "ateez": """
            coming soon
        """,
        "cromer": """
            <div style="display: flex; justify-content: center; gap: 20px;">
                <div style="flex: 1; text-align: center;">
                     <p style="font-size: 2.0em;"><strong>CROMER</strong></p>

            :orange-background[**Confirmed Lore**]     
              
            The Cromer is an object that allows whoever is using it to travel either between the two universes, through time, or into others' dreams.
            The power it holds at any given time is dependent on the phase of the moon.   
              
            The Cromer was originally given to ATEEZ by their counterparts in Inception (ZERO : FEVER pt.1) in order to bring ATEEZ to Strictland.
            This Cromer was then broken during the events of Deja Vu.  
            In their original unvierse, ATEEZ stole their universe's Cromer to return to Strictland.   
            
              
            :orange-background[**Widely Accepted Theory**]  
              
            - Full Moon: Unknown powers but suspected spacial teleportation
            - Crescent Moon: Travel to other people's dreams (such as in Illusion or Inception)
            - Solar Eclipse: Travel through time
            - Lunar Eclipse: Unknown powers displayed in Crazy Form and Deja Vu.  

            :orange-background[**My Theory**]  
            There are two types of cromers; one giving to the main ATEEZ group by HALATEEZ in their dreams (INCEPTION) and one that ATEEZ stole from the museum in Universe A.

            <div style="display: flex; justify-content: center; gap: 20px;">
                <div style="flex: 1; text-align: center;">
                    <img src="https://pbs.twimg.com/media/E_QTQtXXMAI45rL.jpg:large" width="100%">
                     <p style="font-size: 0.9em;">Universe Z Cromer</p>
                </div>
                <div style="flex: 1; text-align: center;">
                    <img src="https://cdn.discordapp.com/attachments/1020918229440401478/1376907535042220104/Screenshot_2025-05-27_at_8.58.54_AM.png?ex=68370892&is=6835b712&hm=bec72c4a5bd1dd6cf259d1597459de9e0a322c5c28a2409f11d64be30448b33c&" width="37.5%">
                     <p style="font-size: 0.9em;">Universe Z Cromer</p>
                </div>
            </div>
              
            There is some evidence that after the Z Cromer broke in Deja Vu, HALATEEZ spent time rebuilding it. This is shown in the TREASURE Ep.2 album were we can see studies of sand, and then the Z Cromer reappearing with HALATEEZ in the Answer concept photos.

            <div style="display: flex; justify-content: center; gap: 20px;">
                <div style="flex: 1; text-align: center;">
                    <img src="https://kpopping.com/documents/27/3/800/SCANS-ATEEZ-TREASURE-EP-2-Zero-To-One-documents-10.jpeg?v=7baea" style=""width: 100%; height: auto; display: block;">
                     <p style="font-size: 0.9em;">Scan from TREASURE EP.2 ZERO TO ONE in which notes can be seen of ATEEZ studying types of sand, perhaps to fix or remake the Cromer</p>
                </div>
                <div style="flex: 1; text-align: center">
                    <img src="https://0.soompi.io/wp-content/uploads/2019/12/30191745/ateez-wooyoung-2.jpeg" width="89.5%">
                    <p style="font-size: 0.9em;">The Universe Z Cromer reappearing in the concept photos of TREASURE EPILOGUE.</p>
                </div>
            </div>
        """,
        "the grimes siblings": """
        """,
        "halateez": """
            coming soon
        """,
        "henry jo": """
            henry jo
        """,
        "left eye": """
            coming soon
        """,
        "sopro": """
        """,
    }

    alias_map = {
    "chromer": "cromer",
    "grimes siblings": "the grimes siblings",
    "z": "henry jo",
}


    inquiry = st.text_input("Please type the item or character you would like to know about. If you would like the information on everyone, please type 'all'.")
    case_inquiry = inquiry.strip().lower()
    if case_inquiry in characters_and_objects:
        st.markdown(characters_and_objects[case_inquiry], unsafe_allow_html=True)
    elif case_inquiry in alias_map:
        st.markdown(characters_and_objects[alias_map[case_inquiry]], unsafe_allow_html=True)
    elif case_inquiry == "all":
        for item in characters_and_objects.values():
            st.markdown(item, unsafe_allow_html=True)

elif option == "**Whole Lore**":
    st.write("this page is currently under construction")

elif option == "**TREASURE**":
    st.caption("officially confirmed or widely accepted lore theories are in italics, all other theories are in regular text and typically include supporting evidence, but could prove to be partially or entirely incorrect.")
    st.markdown("""
        
            <div style="display: flex; justify-content: center; gap: 20px;">
                <div style="flex: 1; text-align: center;">
                    <p style="font-size: 2.0em;"><strong>TREASURE EP.1 : ALL TO ZERO</strong></p>
         
            Originally, Say My Name was going to be the ATEEZ debut. For that reason, Say My Name will be treated as chronologically first.   
                  
            According to the diary entries, the Treasure series takes place before the Fever series. It's recommended you review the ZERO : FEVER series prior to reading the lore on Treasure.
                
            :orange-background[**Say My Name**]  
                  
            *After stealing the Universe A Cromer back, ATEEZ return to Strictland and fight to free HALATEEZ and Yeosang. They're successful in freeing Yeosang, but it's unclear what happens to the men in the black fedoras after the events of the Say My Name MV.*
                  
            ATEEZ does not free HALATEEZ from jail. However, HALATEEZ has somehow rebuilt a second cromer and is able to escape prison on their own.  
            Evidence of this theory is that there are studies of the universe and sand in The Treasure Ep.2 album scans. Further evidence is that from this point on it does not seem as though both groups are working together, and it seems HALATEEZ is more in the shadow
            
            :orange-background[**Intro: Long Journey**]  
            :orange-background[**Treasure**]      
            :orange-background[**Pirate King**]  
            :orange-background[**Twilight**]  
            :orange-background[**Stay**]  
            :orange-background[**My Way**]  
                
            <div style="display: flex; justify-content: center; gap: 20px;">
                <div style="flex: 1; text-align: center;">
                    <p style="font-size: 2.0em;"><strong>TREASURE EP.2 : ZERO TO ONE</strong></p>
                
            :orange-background[**HALA HALA**]    
            :orange-background[**Desire**]  
            :orange-background[**Light**]  
            :orange-background[**Promise**]  
                
            <div style="display: flex; justify-content: center; gap: 20px;">
                <div style="flex: 1; text-align: center;">
                    <p style="font-size: 2.0em;"><strong>TREASURE EP.3 : ONE TO ALL</strong></p>
                
            :orange-background[**Utopia**]  
            :orange-background[**Illusion**]  
            :orange-background[**Crescent**]  
            :orange-background[**Wave**]  
            :orange-background[**Aurora**]   
            :orange-background[**Dancing Like Butterfly Wings**]  
                
            <div style="display: flex; justify-content: center; gap: 20px;">
                <div style="flex: 1; text-align: center;">
                    <p style="font-size: 2.0em;"><strong>TREASURE EP.FIN : ALL TO ACTION</strong></p>
                
            :orange-background[**End of the Beginning**]  
            :orange-background[**Wonderland**]  
            :orange-background[**Dazzling Light**]  
            :orange-background[**Mist**]   
            :orange-background[**Precious Overture**]   
            :orange-background[**Win**]  
            :orange-background[**If Without You**]  
            :orange-background[**Thank U**]  
            :orange-background[**Sunrise**]
                
            <div style="display: flex; justify-content: center; gap: 20px;">
                <div style="flex: 1; text-align: center;">
                    <p style="font-size: 2.0em;"><strong>TREASURE EPILOGUE : ACTION TO ANSWER</strong></p>
                

        """, unsafe_allow_html=True)

elif option == "**ZERO : FEVER**":
    st.write("this page is currently under construction")

elif option == "**THE WORLD**":
    st.write("this page is currently under construction")

elif option == "**Golden Hour**":
    st.write("this page is currently under construction")

elif option == "**Circle Theory**":
    st.write("this page is currently under construction")

elif option == "**Motifs**":
    st.write("this page is currently under construction")

else:
    st.write("this page is currently under construction")

