import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
import os
from google.oauth2.service_account import Credentials
import gspread

st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
   
    .stSidebar {
        background-color: #000000;
    }
    .stAppHeader {
        background-color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)


option = st.sidebar.radio("Pages",["**Home**", "**Lore Forum**", "**Crash Course**", "**Characters and Objects**", "**Diary Entries**", "**Suggestions**" ])
#"**TREASURE**", "**ZERO : FEVER**", "**THE WORLD**", "**Golden Hour**", "**Motifs**"
if option == "**Home**":
    st.markdown("""
                
        <div style="display: flex; justify-content: center; gap: 20px;">
                <div style="flex: 1; text-align: center;">
                    <p style="font-size: 2.0em;"><strong>ATEEZ Lore Den</strong></p>
              
        """, unsafe_allow_html=True)
    st.image("https://pbs.twimg.com/media/F_i4WCgWsAAeYfJ.jpg:large")
    st.caption("All rights to KQ Entertainment")

elif option == "**Lore Forum**":
    # Scopes required for Google Sheets
    SCOPES = [
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/spreadsheets"
    ]
    credentials = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=SCOPES
    )
    gc = gspread.authorize(credentials)

    SHEET_ID = "1Ivr29klYqpa-jfqScOhcaIJLMKpOHkmSnNcoFfJqOys"
    sh = gc.open_by_key(SHEET_ID)
    worksheet = sh.sheet1  # Use the first sheet

    st.subheader("Welcome to the Den <3")
    st.write("Please share your lore theories or questions below!")

    # Initialize flag
    if "rerun_needed" not in st.session_state:
        st.session_state.rerun_needed = False

    with st.form("forum_form"):
        name = st.text_input("Your name (optional):")
        message = st.text_area("Message:")
        submitted = st.form_submit_button("Post")

        if submitted and message.strip():
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            worksheet.append_row([timestamp, name or "Anonymous", message.strip()])
            st.success("Message posted!")
            # Set flag to trigger rerun outside form
            st.session_state.rerun_needed = True

    # Call rerun outside the form block
    if st.session_state.rerun_needed:
        st.session_state.rerun_needed = False
        st.experimental_rerun()

    # Display all messages
    records = worksheet.get_all_records()
    if records:
        st.markdown("---")
        st.subheader("All Messages")
        for record in records:
            st.write(f"[{record['Timestamp']}] **{record['Name']}**: {record['Message']}")
    else:
        st.info("No messages yet.")
        
elif option == "**Crash Course**":
    st.caption("Officially confirmed lore is in italics, all other theories are in regular text. No evidence of these theories is on this page as it's just a story, but they can be found on other pages. For full details on the diary entries, read the entire diaries.")
    st.markdown("""

                <div style="display: flex; justify-content: center; gap: 20px;">
                <div style="flex: 1; text-align: center;">
                    <p style="font-size: 2.0em;"><strong>ZERO : FEVER</strong></p>
              
            *ATEEZ were all outcasts.*  
            *Hongjoong was abandoned by his family. He longed to be famous so he would finally notice him.*  
            *Seonghwa felt like he couldnt express himself, and wore the 'Be Free' bracelet he saw a girl who would always dance alone and not care who was watching drop.*  
            *Yunho's brother had passed away. His brother's dream was to be a famous rock star, and Yunho decided to follow that dream in his place.*  
            *Yeosang's family put pressure on him to be the best, he always had to be the best at school. It made him feel like a caged bird, sometimes.*  
            *San's family was always moving around, he never had any time to make real friends.*  
            *Mingi was the school bully, and would never admit it was because he thought he'd be bullied himself for being poor.*  
            *Wooyoung just wanted to dance, but his stage fright kept him from doing so.*  
            *Jongho was set to go to college for basketball, but a carreer ending injury left him with no future.*  
                  
            *After finding each other, they started to hang out in an abandoned warehouse Yeosang's father owned. They would play music and dance and briefly feel relief from the struggles of every day life.*  
            But it didnt feel right to Wooyoung. Something was off. He couldn't quite put his finger on what was wrong, but he knew that one day the line would be drawn and his friends wouldn't be on the right side of it.
            *And then, Yeosang's dad found out. When he found out Yeosang was focusing on hobbies and not school, he closed the warehouse permanently. Everyone delt with this in their own way, but Mingi was almost embarrassed he felt a brief moment of hope.*  
            *"It was a stupid dream anyway"*  
            *That earned him a swift punch in the face from Jongho, causing an end to the safe haven of friendship they had built.*  
              
            *But once they split up, they started having strange dreams. They felt the pull back to the warehouse.*  
            *One day, Hongjoong snuck back in and fell asleep on the couch and had the strangest dream of all.*  
                  
            *A man in a black fedora and mask was standing in front of him, holding an hourglass. He didn't have much time time to explain, and could only say the hourglass was the key for crossing countless dimensions, but then Hongjoong woke up.*  
            *As he stretched and rubbed his eyes, he noticed the hourglass sitting on the table. And he was definitly awake.*  
              
            *Hongjoong slowly flipped over the cromer and, almost as if it was fated, the rest of ATEEZ walked into the warehouse. Suddenly more objects started to float off the table, and before they could wrap their heads around it, a bright white light filled the room.*  
                  
            *Before they knew it, a large white man broke down the door of the warehouse and demanded the hourglass. Hongjoong still didn't know what it was, but he knew it was important, and it was given to him. ATEEZ escaped the warehouse and headed for the woods.*
              
            *They shouldve known these woods well, but there was something different about them at the same time, and one brief fight with the white-clad giants left Wooyoung with a sprained ankle, and they lost the hourglass. Offering help was a little boy and a little girl, siblings. The Grimes Siblings.*  
                
            *The Grimes boy explained to ATEEZ that they were no longer in the world they knew, but in a different world they called Strictland. Music was outlawed. Art was outlawed. Emotions were outlawed. Over the megaphones in the town ATEEZ could hear the propaganda ringing through the city;*  
            *"There is a disease in the heart of man. The disease is human emotion"*  
            *As the girl tended to Wooyoung, the boy explained that she could no longer talk. Using energy-transfer technology, the Strictland government had taken her voice for singing* along with the Black Pirates.
              
            *The Black Pirates. The hope of Strictland.*  
              
            *All throughout the city, men in black fedoras and masks would go around singing and performing, helping the citizens override their emotion regulation chips with the joy of music. It was a small rebellion, but a thorn in the side of the government.*
            *"So that's who I saw in my dream.." Hongjoong thought.*
            *The Grimes boy explained to ATEEZ that the hourglass they were given is called the Cromer. He didn't know much about it, but he knew the Black Pirates used it to teleport and evade the police. That was until they were recently captured.*
              
            *Feeling a strange sense of loyalty to the Black Pirates already, ATEEZ decided they would break them from jail, and asked the boy for the directions to the jail.*  
              
            *Along the way to the jail, ATEEZ and the Grimes Siblings made their way to a dump. Hidden within the fog of the burning trash and memories lay the girl's voice, a small marble. They promised they'd find it for her, and she would sing once again.*
            *At the dump they met Left Eye, who warned ATEEZ to be careful in the hallucinogenic smoke. Eventually, Lefteye decided to join ATEEZ. Afterall, his daughter died because of her emotions. As small as she was, she stopped in the middle of the road to look at the one flower sprouting between the cracks, and it was the last thing she saw.*
              
            *Once they made it to the jail, ATEEZ quickly realized that it was an old art museum.*
            *They figured the Cromer would also be here, but decided to go find the Black Pirates first.*  
              
            *Confusion took over the boys as they walked closer to the clear boxes keeping the Black Pirates prisoner. They had the same faces. With a menacing smile, the members of the Black Pirates held their hands up to the glass, and ATEEZ went to touch them**
            Just then, they saw their future for a split second. They wore the black pirates outfits, and they were leading the revolution. They were only interrupted when they were met with a shocking realization.  
                  
            *Where's Yeosang?*  
              
            *Figuring they didn't have much time, Yeosang had broken off to find the Cromer. But seconds after handing the Cromer off to Hongjoong, the Strictland Guardians caught him.*  
            *ATEEZ orchestrated a trade. The Cromer, for Yeosang.*
            *As Yeosang stood in the center and the Cromer flew over his head towards the guardians, it struck him just how important that must be. Why did the guardians need it so bad? To him, it didn't matter why. It just mattered that they didnt have it.*  
            *He reached his hand up and grabbed the Cromer, throwing it on the ground and smashing it.*
            
            *The objects started to float and ATEEZ recognized what was happening immediately, they ran to Yeosang to get him before it was too late. But when the flash of light washed away, only seven boys stood in their warehouse.*  
              
            Unsure of what to do  for the night, ATEEZ decided to go home. They didn't know if Yeosang was dead or alive, or even what they could do about it without the Cromer.  
            Yunho walked through his front door and was met with his brother calling to him from the couch.  
            But wait, that can't be right, can it?  
            His brother died in a car accident, didn't he?  
            *Slowly, the rest of ATEEZ came to the conclusion Yunho did in that moment. Yes, they were home. But they were in the past.*
                  
            *Eventually ATEEZ realized that if the Cromer they had been using was from Strictland, what they called Universe Z, there must be another in their universe, which came to be known as Universe A.*  
            *They read about a religious cult called Sciensalvar. Led by Henry Jo, they believed an ancient Mayan hourglass held the secrets to unlocking the universes.*  
            *That had to be it.*  
                  
            *ATEEZ devised a plan to steal this Cromer, but not everyone was on board. Yunho couldn't leave his brother, not knowing what may happen to him. He would take every last minute he had, even if his brother had noticed something was wrong with Yunho.*  
              
            *ATEEZ, minus Yunho, went to steal the Cromer. But they weren't alone, and were quickly outnumbered and held hostage by the Sciensalvar members, who took the Cromer for themselves.*  
            *Yunho saw the standoff on TV and, after telling his brother not to move, ran to their rescue.*  
            *Eventually, Sciensalvar was gone, and ATEEZ had the Cromer. But in the chaos of the battle, cars were going everywhere, and Yunho quickly found his brother, who had followed him to try and help. I guess you can never change fate.*  
                  
            *Flipping the Cromer, ATEEZ returned to Strictland.*
                
            <div style="display: flex; justify-content: center; gap: 20px;">
            <div style="flex: 1; text-align: center;">
                <p style="font-size: 2.0em;"><strong>TREASURE</strong></p>
            
            ATEEZ rushed back to the Strictland jail, where they once again met HALATEEZ. After speaking to them, they realized that they needed to be in Strictland. They needed to help the Black Pirates.  
              
            Strictland called them terrorists, but everyone knew their name. It was all ATEEZ ever wanted.  
            Using the Cromer, they started doing small performances here and there, always just barely evading the guardians. 
            They're doing this for the greater good, right?  
              
            But as time went on, things started getting hazy.  
            How long have we been here?  
            Where do we come from?  
            And who really are these Black Pirates?
              
            Their dreams were plagued with violence and greed. Their time awake felt like sleep walking.    
              
            They saw the Black Pirates less and less and they went on with their seperate plans, and ATEEZ felt like they were leading their own rebellion. But every once in a while in the corner of their eyes they saw a mask, a hat, someone they didn't recognize.  
                  
            There was one particular dream that kept showing up. They all remembered it, and it was so vivid it was almost like it was real. Almost like a prophecy.  
            Eight men in Wonderland. A gate. Music. A plan. Fire.   
            So much fire. 
              
            They didn't like that dream. Maybe it was more of a nightmare.  
                  
            Throughout all of this, Wooyoung felt seperate. The dreams bothered him more. He would always try to convince ATEEZ that that wasn't them.
            He was always the most disturbed when the *other members suggested radical ideas to overthrow Strictland, such as hacking the emotion regulation chips so ATEEZ themselves could control them.*  
            He was different in their dreams too. He was never part of them. Never part of the group. The Wonderland dream they had kept telling them they needed to lock Wooyoung up, leave him behind. And maybe they should.  
                  
            One day, there was to be a party.  
            The Black Pirates had finally figured out how to overthrow Strictland, and ATEEZ would carry out the plan.  
            Celebrating the end of the war before it happened, ATEEZ and their counterparts clinked glasses and cheered, they had finally found the answer. But it wouldn't be the Black Pirates. No, it would be ATEEZ.  
              
            The faces of the eight men dropped as the Black Pirates started explaining what would happen. That day, there would be a solar eclipse, and it would give the Cromer a special power. The power to go back in time. And the Black Pirates were going to use it.  
              
            Terrified, ATEEZ begged the Black Pirates not to leave them behind. What would they do? This plan seemed familiar but.. what if it went wrong?  
            The Black Pirates just calmly described to ATEEZ that this would be the end. But they didn't want it to end. The Black Pirates wanted to fight forever. They were obsessed with this feeling of the chase, of fighting Strictland. They couldn't just give it up.
            So ATEEZ would end the war, and they would go back to the beginning and fight it again.  
              
            ATEEZ had only been in Strictland for a bit, and they weren't sure what was causing them to lose their memories, but they still had some wits about them. But the Black Pirates? They were insane. Corrupt. Different.
            They wanted to drink something that would cause them to forget entirely. It would make them fully reset when they went back in time, so they could enjoy the war as if it was their first.  
            As they lifted the glasses to their lips, the Black Pirate's Wooyoung shielded the others view of his glass, which was already empty. He would not forget.  
            Instead, across the table, ATEEZ San tried to keep his head up as a dizziness overtook him.  
                  
            They fought. No one can say ATEEZ didn't try. The hope of Strictland, abandoning them when they needed it the most. The chandlier fell and the room filled with flames.  
            When the flames cleared, only half the men were still in the room, and the Black Pirates were gone.  
            
            <div style="display: flex; justify-content: center; gap: 20px;">
            <div style="flex: 1; text-align: center;">
                <p style="font-size: 2.0em;"><strong>THE WORLD</strong></p>
            
            In Strictland, ATEEZ were hurt. They were lost. They were angry. But at least they had a plan.
              
            *The day before they decided to follow through with their plan, a boy found them in their hideout. 
            He said he had a brother who used breakers dropped by ATEEZ to fry his emotion regulation chip, but soon he would be tested in school and killed for having his emotions back.*
            *Luckily, that school was a part of ATEEZ's plan.*
                  
            *As they ran through the halls dropping breakers and playing music*, something seemed familiar. Maybe it was the the gate. Maybe it was the music. Maybe it was the fire. Maybe it was the screams.  
            But they were sure, they'd seen this before.  
              
            *With both brothers safely with ATEEZ, they took them back to the hideout, where they finally started to talk about what to do with the Black Pirates.*  
            ATEEZ started to realize they couldn't do all of this by themselves. They needed to come up with the plans now, and the workload was already getting too much for them. But who could they get to help?  
              
            The Black Pirates?  
              
            I mean, it's what they wanted anyway, right?  
              
            They started sneaking into the Black Pirate's dreams. The Black Pirates felt it, a strange hum in their subconscious, or a strange voice they almost recognized telling them to "Wake Up".  
            But they were happy. They weren't friends, but they all had good lives.  
              
            Or at least, they thought they did.  
              
            Soon their memories started changing.  
            Hongjoongs parents were on vacation, but were they? Or had they abandoned them?  
            Did Yunho ever really have a brother? He kept seeing this car in his dream, what is that?  
            When did San get here? He didn't remember anyone.  
            Only Wooyoung was left with this nagging feeling, is any of this really true?  
              
            In Strictland, ATEEZ slept in their beds, the sand of the Cromer falling next to them under the crescent moon as they fed all their trauma to the men who left them behind.  
              
            This story is doomed to repeat again and again, as each ATEEZ falls back in and out of good and evil. Golden Hour is no different, as ATEEZ once again struggle with the question, "Now that we've gotten everything we wanted, what do we do now?"
        """, unsafe_allow_html=True)


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
            The Grimes siblings are a brother and sister that ATEEZ met in Strictland.  
            The sister has no voice when ATEEZ meet her, as it was taken away by energy-extraction technology because she was singing. Throughout the story, ATEEZ help her find her voice, which is a marble-like object.  
            The boy helps explain to ATEEZ the dynamic of Strictland and the current Black Pirates revolution.  
              
            Both siblings are captured by the Strictland Guardians during Deja Vu (FEVER Pt.3) and are killed using the same energy-extraction technology, which drains there entire lifeforce.
        """,
        "halateez": """
            HALATEEZ is a fan assigned name to what the official lore calls "The Men in the Black Fedoras", or the leaders of the Black Pirates revolution.  
            In Strictland, they use the Cromer to evade police and play music to try and break citizens up from emotion regulation technology.
        """,
        "henry jo": """
            In Universe A, Henry Jo is the leader of a scientific cult called Sciensalvar, which believes that a mayan hourglass is the key to unlocking the multiverse. They also believe that emotions are the leading cause of all humanity's problems.  
            In Universe Z, Henry Jo has become Z, the leader of a totalitarian government with the same beliefs. They have invented emotion regulation technology to keep citizen's emotions under a certain threshold.  
            Z and Henry Jo once met in 1999 when Z travelled back in time before the events of FEVER Pt.3. It's unclear what he said to him, or if this meeting led to the creation of Sciensalvar in Universe A.  
        """,
        "left eye": """
            At the beginning of the story, Left Eye is the caretaker of the dump in Strictland.  
            His daughter was previously killed by being hit by a car, she was trying to pick a flower that had grown in the crack of the road. This emotional event awoke Left Eye from his emotion regulation, and he was therefore sent to the dump.  
            The gasses of the burning trash are hallucinogenic, and he lives in a daze where he believes his daughter is still alive before he is shaken free by Yunho.  
              
            Grateful for them, Left Eye joins ATEEZ in freeing the Men in the Black Fedoras, who had been arrested for terrorism.  
              
            Left Eye continues to help ATEEZ lead the Black Pirates' revolution, often acting as a moral compass for the boys. 
        """,
        "sopro": """
            Sopro was a stone created by one of the four priests of HALAZIA. It was made by gathering the breath of all the priests, and allows the user to sync the breath and emotions of those around them to themselves.  
              
            ATEEZ has had possession of this stone since at least The World Series, but claim to have never used it as Left Eye explained it would be wrong to manipulate people like that.
            The first confirmed use is by Wooyoung in Golden Hour pt.2.  
              
            Many fans theorize that Sopro was used many times before when red lights flash in ATEEZ music videos or performances. 
        """,
    }

    alias_map = {
    "chromer": "cromer",
    "grimes siblings": "the grimes siblings",
    "z": "henry jo",
    "strictland leader": "z",
    "red stone": "sopro",
    "the men in the black fedoras": "halateez",
    "black pirates": "halateez",
    "the black pirates": "halateez",
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
    elif case_inquiry not in alias_map:

        def resolve_alias(name, alias_map):
            visited = set()
            while name in alias_map and name not in visited:
                visited.add(name)
                name = alias_map[name]
            return name

        if case_inquiry:
            resolved = resolve_alias(case_inquiry.lower(), alias_map)

            if resolved == case_inquiry.lower():
                st.warning(f"'{case_inquiry}' was not found. it's either not mapped correctly, or not currently in my system. please submit this as an inquiry and I will add it into the site as soon as possible!  -- Rooni.")
                
                # Request box
                with st.form("request_form"):
                    submitted = st.form_submit_button("Submit Inquiry")
                    request_note = st.text_area("Please add any note, feel free to add contact information so I can let you know when this is updated.")
                    
                    if submitted and request_note.strip():
                        with open("alias_requests.txt", "a") as f:
                            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            f.write(f"[{timestamp}] Request: '{case_inquiry}' → '{request_note.strip()}'\n")
                        st.success("Request submitted!")


elif option == "**Diary Entries**":
    st.markdown("""
                
         <div style="display: block; margin: 0 auto; max-width: 900px; padding: 1rem;">
                    <p style="font-size: 2.0em; text-align: center;"><strong>ZERO : FEVER Pt.1</strong></p>
                
        A. INTRO



        The time passing by, our dreams.


        Out of the procession of busy people, along a deserted side road and after passing a maze of cement walls, I can see the entrance to the factory with the 'No-Entry' warning sign. I cut through the wild grass growing at the entrance to the factory. A path appears with several footprints made through the grass, and as usual a familiar beat can be heard in the distance. The deserted warehouse, rusty iron gates ringing with the beat.


        Opening the iron gate, welcomed by our own space. I see my friends dancing to the familiar beat. When the guys came into my sight one by one, a broad smile lightened up my face. These are faces I never got tired of seeing every day.


        This is our own space. Laughing, crying, arguing, dancing, and singing. A space where our dreams came together, our hideout, our own world, separating us from the adult world. 


        Right now, it is a moment void of compromises and tameness, it is the moment before we opened that door. 


        01 - HONGJOONG



        I don't want to be forgotten as if I never existed.


        I am sure that we live under the same sky and under the same world. But, I feel like I'm a bit different from those people on TV dancing under those bright lights. Once I become a bright star that can be seen from everywhere, like those people on TV, will my family notice me? Even if it were by coincidence, I wish I could meet them at least once. If my family could get back together like before...I miss the warmth of our living room.


        My family scattered around and here I am with my new family I made while living alone...I've met my fellow members by doing music together in our little hideout. Just thinking about them warms my heart! I really hope we can achieve our dreams together! My family, the music I love, and our dreams...We must keep them.


        02 - SEONGHWA



        She, who was dancing to the beat.


        Everything around me froze for a moment. The only thing I could hear was the sound of music coming from her earphones. She was moving as if nothing mattered anymore. Common sense, rules, and this tough world didn't have power over her moves. Right this moment, my world broke along this snowy road. Something changed in me, but I stayed still and couldn't say anything. 


        She dropped a bracelet that had "Be Free" engraved on it. Ever since that day, I went to the same place at the same time.


        But, she never came back. I didn't know her name or her address. Just like the "Be Free" bracelet she wore, she freed herself away. Since the, music never sounded the same again. I can no longer distinguish the structure, code, or the genre of the song. Only the lingering feeling of that day remains.  


        03 - YUNHO



        Weather is clear.


        Hey brother, you look like you are in such a good mood today! The weather is so good as well. Even though I was running to see you, I didn't even feel the heat. On days like this, we would have gone to the Han River for some street performance, right? Ah, I am getting nostalgic! Oh, brother! It has been a while since I took out that broken guitar. I wanted to get rid of it because it always reminded me of a broken side of you. But since it's a guitar you cherished so much, I just left it out of sight because it seemed like you abandoned your dream. 


        You know brother. I have a friend like you in my team! His name is Hong Joong. He is the kind of person I would go to when things get tough. He is a person I admire on both artistic and humane level. Thinking about it now, you both kind of look alike? I think you guys would get along together if you've ever meet each other. You know, now I am laughing, thanks to Hong Joong and the guys from the team. I avoid thinking about these painful memories and instead I am focusing on the dreams you couldn't achieve. I will make them happen; the boys and I will make it happen.


        When that time comes, you must wake up from the long hibernation. I want to show you all of it! I'll be back tomorrow. Good night!


        04 - YEOSANG



        Just like a midsummer night's dream.


        I was never too good with mechanics. It all started when I dismantled the speaker. Every time I felt stuffy, I would disassemble various appliances or instruments and then reassemble them back together. My parents had everything planned for me; doing the same routine at the exact same time. The only time I could go out of this cycle was when I disassembled and reassembled things. Thanks to this weird habit I met the guys. That day in that shabby warehouse, a bunch of guys I'd normally run away from, asked me if I knew how to work a drone. This whole encounter was a bit strange! I actually was lost and wandering around. The sound of music was what brought me to that place. From that day on, I went there every day.


        The best feeling was dancing to the music. Dancing was such a mind-blowing activity. Even when I saw my parents' worried faces flashing before my eyes, I just couldn't stop. 


        For the first time ever I felt alive. Hearts pounding like it is about to burst out and this tingling feeling coming up from my fingertips started to take over me. Was there a moment when I wanted something this bad? One by one, more children started to say my name. The path that I only walked with one other person became a path to many. Slowly, the word 'I' became 'ours'. However, now I must leave the 'ours'. If I back out everything will be back to normal, the scattered members and the stolen hideout. I'm sorry, guys. 


        05 - SAN



        I don't know.


        I was always laughing, but I always felt lonely. I just couldn't open up or maybe I've never had the time to open up. Every time I got closer to someone, I had to move. It's happening again today, but this time it's a little different. Now I have friends to talk to about my feelings. As soon as I saw them, I knew right off the bat, they're like me. Oh, Seong Hwa was a little different. He never tried to do anything the traditional way, he was always 'HIS' way.


        My dad said we would have to move again. It was something I was used to hearing, but this time it hit differently. Can I just leave like that now that I have a place of my own...What should I say to Woo Young? Thanks to him, thanks to my friends, I was able to perfect my dance moves. 


        Bobo, what should I do? What? You want me to do it 'MY' way?


        06 - MINGI



        The sound of his laughter.


        Music was my haven, my escape, my one and only relief. When I felt like dying, I would listen to music. I wasn't afraid of death! People around me looked at me as if I were an alien from another planet, laughing at an immature high school student wanting to die. I guess it is uncommon for someone my age to feel that way. 


        Only a few friends' names you remember throughout elementary, middle, and high school. Most of them were in elementary school. No one talked to me, but that is mainly because I didn't answer even when they try talking to me. But Woo Young was different. Not that I remember, he was with me all throughout elementary, middle, and high school. Woo Young would always come next to me during every break. Whether I answer or not, he would go on with his stories about our classmates, his favorite songs, some respected American dancers, and that music team he works with outside of school. He always tops it with that signature laugh of his, which naturally made me laugh. Out of shyness, I started calling him "Woo-Ong". Ah that unique laugh of his. He was the first friend I've ever opened up to. 


        At some point, I started eating and spending most of my time with Woo Young, it was around that time too when I followed him to the hideout for the first time; the place where I could dream. They were friends who took me as I am. We cried, laughed, and made music together. They accepted me as who I am, regardless of where I live of who my parents were. I felt exuberant for the first time in my life. But now I'm getting scared. Can I really have a dream? Will it not be taken away from me?


        07 - WOOYOUNG



        It's different this time.


        My mind has completely gone blank. Who am I? Where am I? I want to run away. 


        Will I fail again? When I was practicing the dancing alone, I was pretty confident! My practice video on social media had reached over 100,000 views. Many people contacted me and even big entertainment agencies offered me to audition for them. But once I felt their look towards me, I just couldn't move. I closed my eyes trying to escape, and then Seong Hwa's voice popped in my head, 


        "Woo Young, before you start performing on stage, remember these three things!" "Everything will be okay!" "Believe in yourself!" "You can do it!"


        "He will be too nervous to remember THREE things! What kind of psychology book did you read?"


        "Yun Ho, are you making fun of Seong Hwa again? But hey Woo Young, believing in you is the key." Hong Joong is always good at putting everything into perspective. A smile crept in my face. I felt their presence even though they were nowhere to be seen. I felt the energy back on my feet.


        I had a habit of constantly chatting to overcome stage fright and I practiced laughing to hide my shyness. It was a defense mechanism of mine to focus. I didn't care even when others made fun of it. But that only lasts for a minute, once I became aware of their scrutinizing eyes, my body just froze.


        For the first time I met Hong Joong, Seong Hwa, and Yun Ho were at the street performance. I could see that they had something I didn't have; expressiveness beyond dance techniques and showmanship that captivated the audience. When I danced with them, I wasn't self-conscious and was able to deliver my best performances. My legs are tense, the first step, the step that I was never able to do, the chain that was tying my body, was magically released. 


        08 - JONGHO



        I had it all planned.


        Winning Nationals, being the player of the year, and the youngest national basketball player...I had no other plans in my life than this one. One the first day of the injury, I was only thinking of quickly rehabilitating and getting back on the court. But, I now can't play basketball anymore. "Then what do I do now? I can't do anything but basketball!" "Let me play basketball, I'll do anything!" I begged the doctor, but it didn't work.


        I felt like I was drowning. No matter how hard I tried, I was still stuck in the exact same spot. As the time went by, I just tried to keep myself from drowning, just barely holding up. Is it okay to live like this? I know I can't! But the moment I gave up playing basketball, everything inside me was lifeless, as good as being dead.


        That lifeless look, before Yun Ho grabbing my hand, looked so much like me. My hand is throbbing from the pain. Min Gi clearly saw the fist coming his way but didn't try to avoid it. His lifeless eyes are still hunting me. 


        When Min Gi said he would quit, that our dream was a luxury, and that the time we spent together meant nothing to him, I couldn't stand but to punch him. Funny enough, it was a heart-breaking moment for me but also the time I started to dream again. 


        At that time, I didn't know how to reach out to a lost Min Gi. Where are we, where should we go?


        Z. OUTRO



        Into the New World. 


        Even though I lost my dream and family again, there was nothing I could do. Everyone left and here I am, alone again.


        On a summer day, when the hot and humid weather continued without a single drop of rain, we decided to go our separate ways. All that because our dreams of being together have become like shackles that hold us down. The scorching sun melted away even our dream of youth and made it disappear at the end of our feet. Problems were piling up like laundry that had been put off. Even if, not often, the promises we made were pushed back day by day and we forgot about each other. It was around that time when I began seeing him in my dream. 


        The man in the black fedora, whose eyes you could only see through his mask, somehow familiar, but tired eyes.


        "You lost your dream not because of the tough reality, but because you guys decided to. Get rid of the idea that the world you see is everything. There are many dimensions and many realities in this world. The world I am in, the world you are in, are all real. I want to tell you everything, but I don't have much time right now."


        "What is this?"

        "The Cromer.  The key to connecting the world."


        He had a shining hourglass in his hand.  This little hourglass was the key to connecting the world?  I carefully picked up the Cromer.  At that moment, the man went back a few steps and spat out his last words.


        "Follow your heart, the map is there."  When I looked back up from the Cromer, the man was already gone.


        I then opened my eyes.  It was all a dream.  I fell asleep alone in the hideout where no one was looking for me.


        While I tried to hide my lonely heart and turn around, I saw something shiny on the desk right in front of the couch where I was lying.  It's the Cromer I saw in my dream.

        Wasn't it a dream?  While looking at the Cromer, I inadvertently turned it around.  The sand in the hourglass began to flow back from the bottom to top.


        The iron door then opened and I could hear the footsteps coming closer one by one.  The guys then gathered around me with the same puzzled face.

        <p style="font-size: 2.0em; text-align: center;"><strong>ZERO : FEVER Pt.2</strong></p>
        A. INTRO

        The Cromer in my hand flashed, but I was still in the hideout. Members who are looking at me were the same too.


        It was like an unbelievable dream to hear about the various dimensions from the man wearing a black fedora and to see the Cromer in my hand.


        Right then, an unknown voice came from outside. As the sound neared, giants dressed in white suddenly appeared, breaking the hideout door. 


        They were wearing masks that covered their entire face and did not feel like people. They were looking at the Cromer. 


        01 - HONGJOONG

        It did not matter where this place was or whether this place was really located in a different dimension. What matters now is that those dangerous white-clad giants are out for the Cromer in our hands and that we cannot go back home if we lose the Cromer. I had to protect the Cromer and the members at the same time, but that was more like a gamble.


        Right that moment, a broken piece of glass under my foot caught my eye. I received the Cromer from Yun Ho and started to provoke the giants. "I'll give you the Cromer," I shouted and threw what I had in my hand through the window. The members who were watching from behind were shocked. 


        As the sparkling piece flew away in an arc, the white-clad giants ran towards it in haste. At the same time, I yelled, "Run away!"


        02 - SAN

        The place around the hideout was very similar to where we used to stay. If I had not faced the strange creatures, I would not have believed all the sayings about the different dimensions and the Cromer. 


        Fortunately, we escaped the hideout safely, and thanks to being familiar with the surroundings, we were able to find our way halfway down in the dark. 


        Visible spaces were similar to the reality we knew but were also slightly different. Under the cliff where Woo Young saved our Bobo in the past, there used to be a valley and a gigantic rock on top but here, no sounds of water flowing could be heard nor could the gigantic rock be seen. Same, yet strangely different. 


        By the time I was immersed in such thoughts, I could hear the members laughing. The members, who had been taking a break for a while, were playing with each other, relieved that the Cromer was safe. What Hong Joong had thrown out the window was a piece of glass similar to the Cromer, not the real Cromer. 


        03 - WOOYOUNG

        The child who saved me was a girl who matched well with the moonlight.


        The girl willingly invited us to her house. Tired of being chased and running away, we fell asleep immediately and, in the meantime, the girl healed my injured ankle. 


        The white-clad giants, who had been fooled by the glass fragments, attacked us again while we were resting in the middle of the forest. As the giants dragged me away by my ankle, all the members rushed to save me and so we ended up losing the Cromer. After they took the Cromer away and turned their eyes away, stones rolled over from the cave in the forest. When we ran towards it, a girl in the cave gestured between the rocks. 


        The girl had a brother. The boy said she could not speak because the white-clad giants took away the girl's voice. They introduced themselves as the Grimes siblings. 


        04 - SEONGHWA

        'One day they suddenly disappeared.' The Grimes siblings looked at us with sad eyes.


        According to the Grimes siblings, the central government here established a stable future policy for the entire human race by running AI simulations. They put the blame on human emotions for causing crimes and terrorism that threaten humanity and so the key to their policy was to control the variables called human emotions. 


        A bill to lower human emotions below the thresholds by using advanced technology and a bill to ban the arts, which greatly affects human emotions, had been passed. 


        Consequently, the central government had achieved high growth under a strong control policy, and people enjoyed material affluence. However, laughter disappeared from their faces and only efficiency and logic became the priority in this society.


        As those days continued, men wearing black fedora began to appear one day. They sung and performed here and there and that was said to have the power to attract people. Being stimulated by these men, people who escaped the control began to appear. People from various fields formed a resistance against the central government and called themselves the 'Black Pirates.'


        The central government put the men in Black Fedora on the wanted list, but they repeatedly failed to arrest them due to them being able to teleport using the Cromer. However, at least, by putting in the new Android Guardians - probably the white-clad giants who came to catch us - the government succeeded in capturing the men in the Black Fedora. 


        The Black Pirates and the resistance, all that does not matter. What is important is that we need the Cromer to return home, and that we lost our Cromer to the Android Guardians. 


        05 - YEOSANG

        To my beloved father,


        Father, I'm walking towards the 'Strictland' where I may not be able to come back.


        Now that I'm walking on a bumpy road after always having walked on a beautiful and straight road, my feet keep on throbbing. My feet are sore, but I still feel good. That is because I'm with my friends and I'm walking towards a place that I've decided on my own.


        Everyone says this is a new world but somehow, I'm familiar with the scenery here. The city I faced after coming down from the woods, I could only see people who were running without taking a single look at the sky, as if they were being chased, people who took the escalators like products being placed on machines, people who removed unnecessary smiles and only talked about their needs, and people who are only looking at small machines, having forgotten how to see each other face to face.


        I thought that maybe this place is not a new world, but that I'm just taking a microscopic look at the world I was living in.


        Father, I know you were shocked to see me singing and dancing with these friends. But I really wanted to escape the world I've lived in, the world I've been trapped in. I love my parents so much, but I have never been happy in your world. 


        When we were kicked out of the garage that we have been using as our hideout and had to be separated, what was more painful to me was that my father was the one who drove us out. I became the person who took happiness away from the friends who have willingly invited me to their world. I regretted that if they haven't met me from the beginning, this situation wouldn't have happened. I resented you, father. 


        Father, thus I will not return to the world you have created. It's not that I don't love you but that I don't want to blame you anymore.


        Your son, Yeo Sang.


        06 - MINGI

        To find the Cromer, we must go to the Android Guardian's bunker, but the only person who knows the bunker is Left Eye, the manager of the Strictland dump. So, we had no choice but to come to this place.


        As if they were continuously burning trash, the yellow smoke, which is said to cause hallucinations, was constantly soaring. Perhaps because of that, the man named Left Eye was mumbling to himself in the air. Whew...how do we locate the Android bunker from that person?


        Thanks to nosy Woo Young, we decided to find out the location of the Android bunker as well as regain the voice of the Grimes girl. That dude is always so unnecessarily nosy like that. 


        By what we have heard from Hong Joong and the Grimes siblings, that Left Eye man seems to have his own story too. Whatever, there's no one without a story. 


        Anyway, we split into teams. Members who will go into a pile of trash that looks like a cave to find the voice and members who will convince Left Eye to find out the location of the Android bunker. I was in the latter. 


        07 - JONGHO

        Boing boing. I heard a basketball bounce. I thought I misheard.


        To find the girl's abandoned voice, I slowly entered the cave with a thin string tied around my body and a gas mask on my face. (I don't even know how someone can abandon a voice and find it back, but they say it's possible because of the new energy extraction thing.)


        I have never seen the shape of a voice before. When I asked the Grimes boy if it has a shape or color, he said that it looks like a bead with a blue condensed energy inside. The bead the boy had told us was shining deep inside the yellow smoke.


        Then, I heard the basketball bounce again. When I stopped walking, a basketball rolled in front of my feet. 'Victory is mine. J.H.' It was my ball. When I looked up, I was standing in a stadium.


        "What are you doing? Pass it!"

        My teammate shouted at me. Is it déjà vu...? I blanked out. The whistle rang in the stadium. I think I had a strange dream for a bit. I was looking for something, but I couldn't remember what it was. The game started again. I ran into the court. 


        08 - YUNHO

        Left Eye, who ran a small but unique brand shop after studying fashion design, was often disqualified from interviews at the fashion house due to his unfriendly appearance. However, he had great skills and was a warm person with a passion. Until he lost his daughter.


        His daughter was hit by a speeding car while she was reaching out her hand to save a flower that had bloomed on the road. People thought moving forward quickly was more important that looking around. Even after seeing the child on the street after getting hit by the car, people were busy passing by, pretending not to have seen anything. During that time, the child died slowly. Left Eye is said to have become furious and fallen into despair when he had belatedly learned of this truth and has become a completely different person ever since. 


        After losing his daughter, he met the illusion of his daughter while being intoxicated by the smoke that creates delusions at Strictland's dump. And while he was wandering around in the dump, he was selected by the Android Guardian to become the manager of the dump.


        It reminded me of my brother the whole time I heard his story. I empathized with Left Eye's feelings a little bit. Left Eye reminded me of when I had lost my brother. Despite my original intentions to find out about the Android bunker, I personally wanted to help him out as well.


        To do so, we had to lure him to a place where the smoke was not severe. We had to make him realize that the daughter he was looking at was not real but an illusion. 


        Z. OUTRO

        The safety strap tied to Jong Ho's body stopped and no longer moved Worried Yeo Sang went into the trash cave wearing the last remaining gas mask to find out the situation.

        
        The game that caused Jong Ho's ankle injury was going on in front of his eyes. Jong Ho dismissed all the things that had happened as mere illusion and déjà vu and ran more fiercely to erase the disgrace of that past.

        
        Left Eye started to attack the members. Running away from Left Eye who was chasing them, they secretly lured him into a smoke-free space. When his daughter's illusion disappeared, he became even more furious. Everyone was unsure what to do, but then Yun Ho shouted amid the silence. "Your daughter is dead!"


        Everyone looked at Yun Ho in surprise. "You're denying it because you don't want to believe it, but aren't you already aware of the truth?" Yun Ho accused him once again.


        "I'll kill you!" Left Eye let out a shriek and swung a big bat at Yun Ho. 

        
        "Jong Ho!" When Yeo Sang had arrived, Jong Ho was intoxicated with illusion and was running furiously toward the cliff. 
       
        <p style="font-size: 2.0em; text-align: center;"><strong>ZERO : FEVER Pt.3</strong></p>
        A. INTRO

        The fourth industrial revolution stimulated the advances of science and technology. It also brought an expansion of human lifespan to 200 years. As the human lifespan increased, so did compulsory education. 40 years of education was required to learn basic knowledge and simple principles for living in this world.  


        The central government desired to construct their own utopian society by using an AI system, thereby making it possible to remove and take control of every unpredictable variable. It succeeded in predicting all the possible outcomes allowing the government to completely take over but of course there was one problem they could not solve - human emotions. 


        By applying deep learning technology, the AI that identified the new variable as a bug, cultivated a new market platform for estimating individual energy, which was known as something unpredictable, and trading it. As the government prohibited all kinds of art and exercised control over the new energy trading platform, sensitivity, emotion, and free will gradually faded away, and humanity fell to components for maintaining the world. 


        01 - JONGHO

        A referee announced the restart of the game. My teammate intercepted the ball and passed it to me. With my great dribbling skill, I went across the court. I attempted a lay-up from my rival's blocking. The ball hung on the rim then fell in. 'Yes. I've turned the game around.' With excitement, I landed on my feet from my successful shoot when all of a sudden, the floor lay in front of my eyes. 'Have I sprained my ankle?' My head dimmed out. Just before I crashed to the floor someone grabbed my arm. 


        "Jong Ho!"


        A familiar voice. One I have definitely heard before. Who could it be? As my eyes started to regain focus, the figure of the person holding my arm started to form. A doctor. The doctor seemed to think deeply before telling me about my ankle. It was somewhere along the lines that I had no problem living a normal life, but basketball would not be an option anymore. What all my colleagues could do was leaving me with pitiful eyes, I freed myself from the doctor's strong hold of my arm and yelled at my colleagues as they were distancing. 'Please take me with you! Please, don't leave me here!' I screamed at the top of my lungs desperately. Then again, I hear it,


        "Jong Ho! Jong Ho Choi!"


        I could see faintly Yeo Sang's face behind the doctor's shoulders. He reached out his arm to hold me which stopped me frantically moving. He raised my body up and put the gas mask from his face to mine. After inhaling in and out a few times, I began to see my surroundings more clearly. We were sitting at the end of a cliff. Speechless, I looked up at Yeo Sang with complete confusion. He held my hand and told me the Grimes girl found her voice back. Then with a warm smile,


        "Let's get out of here."


        02 - YUNHO

        The bat that Left Eye hit dodged me by an inch and smashed into an abandoned window. The broken pieces scattered into the air. I looked at him without a blink. 


        He would only swing the bat even more recklessly. Everything that hit the bat shattered to nothing. I slowly walked towards him. I hear the members' voices trying to stop me. But a strange form of pity inside of me, an unexplainable emotion on top of that led me fearlessly to stand in front of him. Left Eye was still holding tight to his bat, but his pupils were shaking. It looked as if the hallucination was fading. 


        "It's not your fault."


        With the drop of his bat, Left Eye fell to the floor like a lifeless toy.


        "You had no thoughts of harming anyone in the first place."


        He looked up with sorrowful eyes and began to let go of his tears - together with the emotions he had locked up. He would have lived many days with the burden of guilt after his daughter died. What if, just what if I didn't send her there that day. What if I was there with her, what it, what if...


        Looking at him felt like seeing me stripped of everything in front of a mirror. 


        03 - MINGHI

        "Those boys will be able to save the Black Pirates."


        Sailing towards the Android Guardian's bunker, I came out to the deck as the members fell asleep. I hear Grimes boy's voice full of conviction from a distance. Not wanting to join in their conversation, I quietly hid. They were watching a video of Left Eye's daughter dancing and were missing the times when they could sing and dance as much as they wanted. They comforted themselves by saying they would soon save the Black Pirates, and all will return to normal.


        "Look at the sea." shouted Grimes girl with her returned voice. The sea absorbing a bright orange color from the sunset  swayed beneath. It was beautiful. 


        "I was missing this in my life." said Left Eye adding that he was blind by the past wandering relentlessly. They watch the sea for a while in complete silence. As if all the concerns and worries of this world had disappeared, the Grimes siblings started humming a song. Gradually getting louder, Left Eye playfully danced. Although a bit of a laugh, it was wonderful. I didn't realize I left out a small laugh.


        The calm wind tickled my hair. The sea shone as if embracing a pearl. As time passed, Left Eye and the Grimes siblings were singing and dancing together. Someone said, 'Dancing defines at least the smallest will to live. So, people dance in the brim of hopelessness.'


        That's right, I could have lived without realizing this. I could not see the present because it was disturbed by past misfortunes.


        The hopeless sun has hidden behind the horizon and the stars of hope have made their appearance in the sky. The sway of the orange-lit sea faded as the waves embraces the shining stars.  


        04 - WOOYOUNG

        The late afternoon of the following day, we finally arrived on the island. From the elongated shadows of the afternoon sun, I could see pensions and sunbeds. When I stepped onto the sand, I could feel heat rising. The island was considered a tourist paradise in the past. However, nobody had visited this island for their holidays anymore since taking a rest and trip became meaningless and worthless in this world. 


        To escape quickly, Left Eye and the Grimes siblings stayed in the ship. We walked down the island to look for the place, called the Android Guardian bunker. And we easily found the place, which was blowing off golden yellow steam on this isolated island. When we got there, it was a gallery in the middle of the island. Gallery...They banned all kinds of art - funny of them to settle and build their bunker there. We passed along the empty lobby and went towards the exhibition. The golden yellow steam continually spurted from where an arrow indicated an exhibition route. 


        Some drunk Android Guardians were laid on the floor. And at the end of its view, I could see the men in Black Fedora were in a glass prison. 


        05 - HONGJOONG

        There was a man at the end of the smoky road. To be more specific, they were there, the men in Black Fedora that we met in our dreams. One person was leaning on the wall, hardly on their feet and my instinct said that I must save them.


        I threw myself to the glass wall. It did not move. I bumped into it again. The man finally heard the noise and saw me. 


        "Finally, you are here." he said, and he barely took off his mask. As I saw his face, I was in shock. He was me. The man had exactly the same face as mine.


        "Listen, we called you here." In the midst of these strange incidents, I could only shake my head. 


        "We are captured here, and somebody has to do our work. You may have noticed it. This world needs a change."


        "Why does it have to be us? Why do we share the same face?" I kept questioning him and tried to break the glass wall between us. But not even a small crack.


        "I don't have enough time to tell you the whole story. We are going to be seen by the guardians when the smoke fades. Do what I do." The man put his hand on the glass wall and told us to copy him. So we put our hands like he did.


        "We all face walls. Sometimes, we think that our lives would be happier without walls but that is not true. It we earn things easily, we could lose them easily." The man and I faced each other, and I felt some indescribable energy swirling near us, regardless of this unbelievable reality - the men with the same faces as us, endless questions about this world and everything. Soon after, we were wearing their black suits without even noticing. 


        06 - SAN

        When I was dazed by this black suit thing, I heard the voice of the man who has the same face as Hong Joong from the other side of the wall. "You have to run before the smoke fades." he shouted.


        The Android Guardian was burning new energy in the center of the hall. It was people's memories. I picked some of the memories that were not yet burnt from the floor. 


        A memory of confessing love to my lover.

        A memory of walking my dong on the beach.

        A memory of a first trip with my friends. 


        They were all valuable and unforgettable memories. These memories were the source to live and hope. Android Guardians were burning the hope of people and they were drunk from the smoke. I felt a surge of anger coming over me. All of a sudden, Seong Hwa shouted,


        "I can't see Yeo Sang!"


        07 - SEONGHWA

        After Yeo Sang disappeared, we were all in a panic and ran instantly to the lobby. Fortunately, Yeo Sang also ran to us from the opposite exhibition at the same time. With relief, we moved toward the exhibition. While looking back, Yeo Sang threw a shining object. The object was the Cromer.


        It was just a short moment of celebration that we are soon going back home when the crowd of Android Guardians came up to us behind Yeo Sang. The biggest guardian grabbed Yeo Sang's neck. He threatened us saying that if we do not hand over the Cromer, he would break Yeo Sang's neck. There was no way. When Hong Joong, holding the Cromer attempted to approach Yeo Sang, the Android Guardians ordered not to come near and just to throw over the Cromer from a distance. 


        "Don't hand it over! Once we give it to them, they will take us too!" Yeo Sang shouted. It was the worst situation for us. If we did not hand it over, Yeo Sang would be in danger. If we just hand it over, everyone would be caught. We cannot let Yeo Sang sacrifice for 7 members. What can I do?


        Hong Joong seemed to have the same thought looking at Yeo Sang and us by turns. Hong Joong began to speak about his decision. He said that he would throw the Cromer over to them if they would let Yeo Sang go between us and them. 


        08 - YEOSANG

        This Android Guardian could get us whenever he wanted us in this gallery. I don't doubt that. Is there any way to save myself and get the Cromer? No. These guys are everywhere. It was my fault. I should have been more careful. My friends would not have been all scattered if I had not met them at first. Then we could have not been left in this weird and dangerous place.


        While regretting my careless behavior, I arrived in the middle of the guardians and my members. The Android Guardians shouted to Hong Joong to pass the Cromer. I saw the Cromer in the hands of Hong Joong. 


        What do we know about that sandglass? I asked myself and an answer popped in my head. It may be a gamble but there was no other way.


        Hong Joong threw the Cromer to the guardian. The Cromer darted through the air, and I quickly snatched and turned it. The Android Guardians seems confused, and they immediately started to chase after me. So I smashed the Cromer. The glass broke down and the sand splashed everywhere. I was being dragged away and Hong Joong tried to grab my hand. The light flashed. 


        Z. OUTRO

        "One, two, three, four, five, six...seven." San's quivering voice echoed in the heavy air of dawn. When we woke up, we were in the warehouse where our journey began, and everything was remaining the same. 


        San could not believe that there were only seven of them. He wiped his tears and tried to get himself together. Everyone was silent, they were only staring into each other's eyes. 


        "Jong Ho, Woo Young, Min Gi, Seong Hwa, Hong Joong, and I..." San repeatedly shook his head. He mumbled to count again and again with a crying voice then he moaned. A shadow of despair fell on their faces. 


        "What would happed to Yeo Sang? Like the Black Pirate, what if he's been..." Woo Young couldn't finish his sentence. A heavy silence filled the space, and no one could answer his question.


        Hong Joong stood up from the couch. He opened and showed his hands full of blood with fragments of glass and dirty sand to the members. He dusted his hands off. Broken pieces fell down and down. 


        "We shouldn't have been there then nothing would have happened..." 


        Knock Knock, there was a knocking sound from an old door. Hard-faced Hong Joong opened the door. Nobody was there. Something bumped into the door and fell onto the floor.


        "This is Yeo Sang's drone."

        "Who drove this here?"


        Hong Joong swept dirt from the drone and placed it on the top of a drawer. He stared at the lights coming from the slightly opened door. 


        We all surely felt it. Yeo Sang is alive.
        
        <p style="font-size: 2.0em; text-align: center;"><strong>ZERO : FEVER Epilogue</strong></p>
        A. INTRO

        "Saving humanity from the doom that's about to strike"

        A Trio caught stealing a Mayan relic was revealed as 'Sciensalvar' a new religious organization. 


        The security arrested the trio red-handed. The trio were attempting to steal a Mayan relic from 'The Mayan Civilization' exhibition at the National Museum of Korea. Seoul Yongsan Police Station is investigating suspects A(31), B(28), and C(21) for the crime attempt of special larceny. The trio are suspected of stealing the exhibited relic from 'The Time, Destiny, and Prophecy of the Mayan Civilization' at 10:05 AM, on the 10th. 


        The reporter behind the case interviewed suspect A's crime motive. Suspect A stated that "I had to steal the relic to save humanity before they face the world's end." It was later found that the trio are believers of the religion, "Sciensalvar'. It is suspected that the trio committed the crime under the influence of Henry Jo, the religious leader. 


        Sciensalvar is a new religion and was established in 1999 by a scientist named Henry Jo. This religion believes that humans are the collection of energy, and human concerns from an uncertain future can be resolved by science. Henry Jo frequently mentioned the Mayan relic, shaped in an hourglass, in official statements. Henry Jo also mentioned that the energy condensed inside of it will be the key to saving humanity. 


        The Mayan relic Henry Jo mentioned is an hourglass artifact that imitates the moon's movement. There are many speculations for the exact purpose of the artifact among experts. However, one clear established theory is that the relic, crafted through an uncommon metallurgy technique, was used for ceremonial purposes. 


        01 - SAN

        A week has passed since we came back here without Yeo Sang. We stayed at this place, where Android Guardians do not exist, before we left to the other dimension. That street and people, all still looked the same as always. But the only thing that changed is the time zone. Simply put, we have returned to the past.


        This was the moment before we gathered at our agit, not too long before Yun Ho's older brother's car accident. We assumed that the time zone was twisted when the Cromer broke, and Yun Ho was thrilled. Probably because his brother was brought back to life from the tragic accident. I can understand Yun Ho, but deep down in my heart, I felt bitter against him. Whether we are in the past or the present, one thing was clear. We may be alive, but Yeo Sang isn't here with us. Since the Cromer was broken, there's no way for us to be back there. 


        We were hopelessly wasting time, then Seong Hwa rushed and shouted, "This is the Cromer, right?" He showed an article featuring the attempted robbery of the Mayan relic exhibited at the National Museum of Korea, 'The Hourglass that Captures the Lunar Movement'. It was the Cromer!


        02 - SEONGHWA

        "If we think back, the broken Cromer, I got in my dream, was from the man with the black fedora. It means, that Cromer was existing in their dimension. It would be possible that there is another Cromer in this dimension. Let's find the Cromer to find Yeo Sang and put it back to the original place!" Hong Joong yelled. However, other members were against Hong Joong's idea, saying it is too dangerous and illegal.


        "Whether it is legal or illegal, what about Yeo Sang? You are telling me that you want us to leave him there?"


        If it were me in the past, who was stuck up and scared to break the rules, I would have reacted the same as the other members when Hong Joong suggested his idea. Maybe this made me even madder. But now, I'm not the person who I used to be. Saving Yeo Sang was my top priority.


        "We decided not to be stuck in the past. When we left to another dimension, we all made up our mind. Didn't we?" We do know we are not in the present. So, we must go back to make everything right.


        After giving some thought, one by one, the members started to agree with stealing the Cromer. As everyone was coming together, Yun Ho quietly said, "I want to stay here. I can't leave my brother."


        03 - JONGHO

        As much as I believed in Yun Ho, his statement came as a shock. I walked around our agit to pull myself together. Min Gi quietly came out and walked with me. He probably felt the same.  


        "I respect Yun Ho's decision."


        I looked at Min Gi perplexed. He carefully went on. "When I thought that I may lose my grandmother, everything felt meaningless, even my dreams and our members. I believe it will be even worse for Yun Ho. He already lost his brother once. He'd never want to let him go."


        At that moment, I remembered when I punched Min Gi. When Min Gi told us he wanted to quit, saying that our dreams are meaningless, I felt betrayed and swung my fist. Obviously, my heart was instantly flooded with regret...


        "It's too late to say this now, but I didn't want to give up at all."


        He said that the only reason he'd made up his mind to give up was his grandmother, his only family member who had collapsed on that day. The fact that he is having a great time with our members while his grandmother is suffering haunted him. I was able to finally understand Min Gi's perspective after he shared his story. I knew that I could never fully understand what Yun Ho has gone through, but I assumed that he had a hard time as well. He should be conflicted between finding his brother and saving Yeo Sang. I am sure he is suffering from it.


        After having a long discussion, we chose to respected Yun Ho's choice. No one can be forced to decide. 


        04 - YUNHO

        Everyone should be in front of the museum by now. Why am I so nervous? I'm sure everything is going as we planned.


        My brother scolded me for checking my phone every minute. Full of embarrassment, I put down my phone. I started to massage his left leg, telling him everything was fine. 


        "You are so weird! You've changed so much! Well, I like it a lot better than when you were wandering around on your motorcycle...But I still can't get used to this sudden change in the last two weeks."


        I understand what he said. Well, I came back from the future.


        "I think God gave you perfect hands at the cost of giving you legs that need a bit of help." I said.


        I imitated my brother playing guitar as he gave me a curious look. He laughed out loud and asked me to massage his left leg harder. Since birth, he had a dysfunctional right leg, so my brother's left leg would always be swollen as it is doing all of the leg work.


        "Well, if my legs are good, I would never imagine myself sitting here to play the instrument. Maybe some deficiencies are a blessing in disguise, giving insight. Right?" 


        He finished talking and turned on the TV in the corner of the room, and headline news came out. It was about Henry Jo, the leader of Sciensalvar, breaking into the National Museum of Korea to steal Mayan relics with hundreds of Sciensalvar's believers. Some boys who were trying to stop them from stealing the relic, and now they are held as hostages. I jumped up. The hostages were my members. I took out my motorcycle key from the cabinet and yelled at my brother, 


        "Stay inside. You should stay inside no matter what!"


        05 - WOOYOUNG

        I thought Sceinsalvar was a religious group. But why...

        Why is Henry Jo pointing his knife at my throat? How did his happen?


        4 PM, we met up in front of the museum and planned to enter the museum in two groups of three. As closing time approached, the security guards were loosening up. One group was responsible for catching the guards' attention while the other group steals the Cromer. We planned to go get Yeo Sang as soon as we stole the Cromer. However, even before entering the museum, our plan fell apart. Among the crowd of people in red coming out of the exhibition all, a man in a black techwear outfit was holding the Cromer. He had a long white beard, a black mole on this right cheek, and large goggles. It was Henry Jo, the leader of Sciensalvar.


        We had to get the Cromer back from him. If we miss this opportunity, there may be no way back. Right then, some high school girls with red blankets on their shoulders passed by me. Without giving any thought, I took their blanket and put it over my head, and then joined the group of Sciensalvar believers. Leaving the faces of the embarrassed high school girls behind, the members also joined the group covered with blankets.


        We gradually approached Henry Jo. As we reached close enough to snatch the Cromer...Bang! The police shot a blank fire shot and blocked Henry Jo and the Sciensalvar believers. At that moment, I reached towards the Cromer...But Henry Jo pointed a blade at my throat even more quickly. He whispered in my ear, holding back his laughter. "I just needed a hostage, so thank you for coming!"


        06 - HONGJOONG

        'Think Hong Joong. Think!'

        My head blacked out.


        My head stopped because of this fear I've never felt before. Bang! The police shot another blank fire shot. As the final warning, the police yelled that if the hostages were not released, they would fire shots immediately. As the believers started to murmur, Henry Jo yelled not to be swayed. 


        At that moment, a group of bikers ran toward the museum with a loud exhaust sound. Six bikers began to circle the crowed of Sciensalvar. The believers started to get nervous about the riders' unknown intention. Henry Jo shouted, but the motorcycles were too loud to hear anything. Then, a familiar sticker caught my eyes. 'ATEEZ YH'. It was Yun Ho! The other riders must be Yun Ho's friends. 


        I intuitively knew Yun Ho's plan. As Henry Jo lost control over his believers, he turned towards the crowd.


        "Woo Young!!!"


        I wasn't sure if Woo Young heard me, or he intuitively knew it was Yun Ho, but Woo Young snatched the Cromer and started to run. As soon as we ran out of the group of believers, Yun Ho and the riders seated us on their motorcycles and ramped up.


        We could see Henry Jo running away along while the police were trying to control the believers. 


        07 - MINGI

        "Ah, I knew you'd come back!" I shouted with excitement behind Yun Ho.


        As I was shouting with joy, I heard Hong Joong saying, "There's a car behind you!!" The six motorcycles suddenly turned their directions, and everyone fell to the ground. The car, coming to crush us, was overpowered by its own momentum and flipped to the pedestrian walk, hitting the pedestrians. Yun Ho's eyes trembled as he saw the pedestrians lying on the ground. 


        "Brother!" Yun Ho screamed as he ran to the pedestrian. It was Yun Ho's brother on the ground. He seemed like he was heading towards the museum, after seeing Yun Ho's motorcycle on the news. Yun Ho's brother slowly opened his eyes and asked. "Is it 5:07 right now?" I checked my phone, and it was 5:07 PM. "Your diary said that I got hit by a car at 5:07 PM." Yun Ho looked at his brother, startled. His brother went on saying, "Sorry. I read your journal on the desk. I knew something was going on, but you never told me what you were going through." He painfully continued breathing. "It didn't make any sense, so I thought it was a lie. I guess it wasn't."


        "We need to go to the hospital right now." Yun Ho wiped his tears and tried to pull his brother, but his brother grabbed his arm. Yun Ho held on this his brother's hand as if he'd never let his brother go. "There's something I need to tell you...It wasn't your fault that I got injured back then, and even now, it isn't your fault. So leave me in the past and move on with your own life." Yun Ho was weeping. His brother slowly patted Yun Ho's head. "I love you, my brother. You know what I always say, right? You're doing your best just by going through the day. I was happy enough for the last two weeks. I appreciate it." Then, Yun Ho's brother passed out. Yun Ho put his head down on his brother's chest and wailed. 


        Henry Jo stumbled out of the driver's seat of the overturned car. Blood was running down slowly on Henry Jo's face because of his head injury. Henry Jo stared at the Cromer in Woo Young's hand. He then began to run towards Woo Young with a knife. Yun Ho quickly threw his fist at Henry Jo and yelled. "Turn the Cromer!" Henry Jo snatched the knife that he dropped when he fell down. "Hurry!" Right at the moment when Henry Jo raging towards us, Woo Young turned the Cromer. 


        08 - YEOSANG

        How long have I been in this glass room? It felt like an eternity being in this tube without any light. I found the whole lines of Resistances, who revolted against the government, standing in front of my glass room with their biological energy stolen. Android Guardians covered them with black fabric. Maybe they did not want to see the undead Resistances. The worst part was that the Grimes siblings were among the covered Resistances. 


        The Grimes siblings and Left Eye ran to the art museum after seeing the light that the Cromer emitted when it shattered. Left Eye was able to escape the bunker, but he lost his right arm. The Grimes siblings got caught and lost their biological energy.


        I don't know how much time has passed. The pain was so great that I desired to lose my emotions instead. I wished that guardians would kill me. 


        When my train of thoughts went that far, I heard a trumpet sound somewhere. The guardians, surveilling me, busted out. I heard beating and moaning outside. I started beating at the glass tube without even knowing. "Somebody please get me out of here! Please!"


        The light that I hadn't seen for ages slid in when the door opened. Men in black fedoras were fighting with Android Guardians behind the opened door. "Hey, Yeo Sang." I heard a warm voice calling my name. A guy came near my glass room and pulled down his black mask. Tears of relief burst out of my eyes. It was Seong Hwa. 


        Z. OUTRO

        -The underground hideout of the Resistance organization 'Black Pirate.'-


        A signal game from an old small machine. A one-armed man rushed in and sat down in front of the old machine. The one-armed man held up a pen to write down the codes. It was Left Eye. After suffering from anther loss, he looked rather fragile.


        "...  ._  _._ _     _ _ _._ _     _.  ._  _ _  .

        ._  _  .  .  _ _.."


        Left eye interpreted the Morse Code he wrote down. The light of hope spread on his face gradually. Left Eye turned to the people and shouted, "They're back! They came back!"


        The cheers of 'Black Pirate' echoed in the underground hideout.


        The messy handwriting of Left Eye on the paper reads:


        "SAY MY NAME. ATEEZ."

       <p style="font-size: 2.0em; text-align: center;"><strong>The World Ep.1 : MOVEMENT</strong></p>
        A. INTRO

        Weeeeeeing!!!!!!!


        A loud alarm sound echoed in the plazas, streets, schools, and buildings. The Guardians monitoring people from everywhere were the first to respond to the sound. People walking on the street, office workers doing their business, and students studying, all stopped what they were doing, got up, and turned to the highest monitor. 


        Looking down from the sky, the whole world looked like a well-made set. People with blank faces, well-organized roads, and buildings. Pretty and neat world, but there was no life in it. In the middle of the cold dull buildings surrounded by still mannequin-like people, a mellifluous voice echoed.


        Z. A perfect world. Being perfect, our world is safe. A small error is a crack, and a crack leads to pain. Pain, pain is an unnecessary emotion and a negative element in life. We want to protect you all.


        From the streets, companies, schools, and plazas, Z's roaring voice came out of the speaker. A yellow light lit up next to the ears of people listening with dry faces and blinking their eyes. Looking closely, it was the light from a small chip stuck under the ear.


        Z. A world without cracks is always beautiful. You living your life in your position are the world itself. Do not doubt yourself. You are always right. We are right because you are right.


        Smiles spread on people's faces. But no one's eyes were smiling. It was just the facial muscles that moved like a machine that obeyed commands.


        Z. Keep that in mind. The government works for you. The government is committed to you. All of this...is for you.


        At the end of Z's words, the crowd classed their hands all together and cheered.


        "Z! Z! Z! Z!"


        At that point when the voices of people shouting for Z overflowed the world, music began to play out of nowhere with a crackly noise from the speaker. Soon after, along with the sound from the megaphone, Z's voice was swallowed up by the gradually increasing sound of music, and the yellow light that flashed next to people's ears faded away. The Guardians who stood among the crowd began to look around as if they were looking for someone. For the first time, the feeling of 'confusion' crossed the faces of those who were puzzled by the sound of the song. 


        When the man standing in the plaza feeling somebody's presence looked to the left, Hong Joong, wearing a Black Fedora, smiled at him. The man didn't know Hong Joong, but unknowingly spit his name out of his mouth. 


        "A...TEEZ...?"


        01

        "Look, once you see us, you can never forget us." said Min Gi, who appeared to the man's right. The man's eyes lit up with life. Then Min Gi threw something from his hand to the man. The man who reflectively received the object, flying in an arc, opened his hand. It was a small square-shaped machine. Inside the machine was written in small letters.


        "There is a chip under your ear. Let the breaker touch the chip."


        In the middle of the street appeared Woo Young and Yeo Sang, on the top of the building Seong Hwa and San, and in the school, Yun Ho and Jong Ho. To the music, ATEEZ started singing and dancing. People who first looked blankly at it began to shake their bodies unconsciously in response to the music. The Black Pirates began spreading flyers in the sky and handing out breakers on the ground. People picked up flyers and read them.


        You are valuable by yourself. No one can define you, and no one can control you. Being alive is imperfect, and it's beautiful to be imperfect. Read poetry, draw pictures, listen to music, dance, and sing. Therein lies your own answer. [Black Pirates]


        02

        The people who listened to ATEEZ's music, watched their performance, and read the message in the flyers instinctively touched the chips with an unfamiliar feeling under their ears. For the first time, they realized the chips were implanted in their bodies.  


        The Guardians were eager to control people and capture ATEEZ, but as ATEEZ used the Cromer moving space to space instantly, it was difficult to catch them. Meanwhile, people put the breaker on chips under their ears. With a crackling, small spark, small particles popped out of the machine and entered into the chip. 


        The Guardians began to drive the ATEEZ members to one side. From school to street, from street to plaza, ATEEZ danced their final dance to the end of the music and disappeared in an instant, right at the moment when they were about to be caught by the Guardians who were reaching out to them. 


        The faces of those who put the machine on the chip were filled with chaos and fear.


        The people running away and the Guardians chasing them, the people returning to their work with the same dry face even in the mess, and...among them, one hand picked up a breaker that had fallen on the ground and put it into the pocket. 


        03

        Cheers overflowed in the underground bunker of the Black Pirates. Because this plan also succeeded. ATEEZ and the Black Pirates were celebrating themselves eating food with a background of upbeat music.


        "I was worried about how to block the control system developed with new energy...Awesome, Left Eye."


        Then Left Eye said shyly, scratching his head at San's praise. "There were a lot of failed chips of the government in the waste rolled into the Strictland dump, so we were lucky."


        "If we put this machine on the chip, does it lead to the Black Link we use?"


        "Yes. But not right away. Because each person's will is important. All we do is get them out of the government-controlled link. After that, it is left to their own will."


        When Jong Ho asked if it is a matter of choice, Left Eye continued. "Right. They will not even know that this machine connects not only people but also the Guardians to the Black Link. They'll think of it as just a breaker that blocks them from the control link. Since the safety of the Black Pirates is also important."


        "But why? Forced link connections are more efficient." Other members nodded and looked at Left Eye in response to Min Gi's suggestion to save more people by forcing the link to be connected. 


        04

        "I've lived in this would for a long time, so I know. At first, I felt fear when I met you and remembered the memories and feelings of love and other emotions of the past that I had forgotten. Just like when you guys first came to the world. As unknown is always feared."


        "That's why you give them time. Giving themselves time to overcome the chaos and to decide, until the Guardians find out that the control link has been blocked."


        Then Left Eye nodded quietly drinking a glass of wine.


        "When people become self-reliant, a signal goes to the Black Link we use, Then, the Black Pirates, scattered all over the place, contact them..." 


        "What if someone chooses to stand on the side of the government even after getting their feelings back?" 


        "We can't force them. Because the fear is big. No one knows what will happen if I'm the only one against it. We can't dangerously force someone who wants to follow the flow. That's not different from the central government that says only themselves are right."


        05

        "You haven't figured out the location of Z yet, have you?" When Hong Joong looked back at the Black Pirates, everyone stared at them with questioning eyes. The Black Pirates shook their heads with awkward faces.


        It was not easy to find out where Z was located because it was information that even the Guardians did not know unless they were high-ranking members of the government. Undoubtedly, Z is the ruler of this world, at the same time, the symbol of the Z World. Therefore, his safety was the top priority to prevent terrorism. 


        "For now, that's the last step. Let's start with what we can do now." Everyone nodded at Seong Hwa's words. 


        To install mirrors and remove the coverings blocking the windows ATEEZ decided to infiltrate the symbolic place that is establishing this world. 


        06

        A mirror is a window through which one can perceive oneself. In the early days, the government did not know the importance of mirrors, so they just tried only to control the emotions with new energy. However, as people looking at the mirror and recognizing themselves kept getting out of control, they removed all reflective objects, including mirrors.


        So were the windows. To look out the windows at the landscape is to open the possibility of freedom and is a door that recognizes oneself and others and sees the world. So old buildings were blocked with curtains, coverings, and sheets, or in buildings built afterward, there were no windows at all. Furthermore, a large dome was placed in each zone to block out the solar heat and then intake of vitamins and nutrients, made by being exposed to light, was controlled through medicine. As this dome also served as a blocker and boundary between zones, it was an extremely important means of control for the government.


        With the Cromer, ATEEZ and the Black Pirates moved freely across the areas, which allowed them to touch people's hearts with their performance, but that was not enough. The control of the government became increasingly systematic. Even humans who became aware of the control with the emotions rising within them, were either controlled again or taken to the Guardians and transported to the Guardians' bunker.


        Now, the only way ATEEZ and the Black Pirates had to go was to 'make as many people aware as possible at once'. The first target point to install mirrors and remove the coverings of the entire building was the Prestige Academy, which was called the 'best school' of this era. 


        07

        An emergency signal rang inside the underground bunker to alert an intruder within a 1km radius. Everyone's eyes were on the monitor and there was a short moment of tension. A young boy was crying alone, shouting "Help, Black Pirates!"  


        The boy took a sip of hot tea and looked at the members with slightly relaxed eyes and said, "Please, save my older brother."


        On the way to school, the boy saw the performance of ATEEZ and the Black Pirates for the first time and got out of control through a breaker. "It was terrifying." said the boy. It was because he then realized how bleak and violent the school and the world are when he saw them after having emotion for the first time.


        The boy told, returning home that night, he carefully brought up this story to his older brother, who attended the same school, and his older brother tried to report him to the Guardians, so the boy unwittingly put the breaker on his older brother's chip. The boy thought his older brother would understand his intention after going through the same process he did, but the reaction was different. The older brother who felt his emotions for the first time shouted as if in pain, trembled, and looked at his younger brother with blaming eyes. 


        08

        "Do you know the Guardians Island?" Tears welled up in the boy's eyes again. The members looked at Yeo Sang. The place where Yeo Sang was kept, "Guardians Island" is apparently a facility for re-educating the socially maladjusted. However, in reality, it was a place to dispose of people who rebelled against the central government system, and other various things such as art and instruments that stimulate human emotions. This does not apply to those who have completed 40 years of education and are being used in their respective positions, but those who have regained their emotions - those who recover their emotions and act as Resistance - have been caught by the Guardians and then disposed of there. So, it was a place that the members and the Black Pirates knew well. However, they did not know that children who were not even the Resistance would be taken to Guardians Island. 


        To complete the 40-year education curriculum, people must take the final graduation exam. During this exam, they will be investigated on what kind of part to be used in the society and if they fail to pass the emotional test they are judged as defective and will be sent to Guardians Island. 


        The boy cried again. As his older brother, who was about to take the graduation exam, could be taken to Guardians Island because of him, he desperately accessed the Black Link of the Black Pirates and found a nearby area believed to be a bunker. 


        Z. OUTRO

        "The exam is not the problem, we have to save him right away, even tomorrow. That's how school is like, easy to be targeted when one seems different from the crowd."


        Min Gi, who had a hard time at school, intuitively caught the danger. The boy nodded. "There is a student organization in school. Since the Guardians and teachers cannot monitor all of the students, they selected the best students and built this organization to monitor others. But as our school organization is certified by Mr. Z..., no by Z directly to head the organization, they might notice it before even taking the exam."


        The members became complicated. There was a high possibility that it would not end with just saving his older brother. As it must be something really turning the whole school upside down. If they decided to go to another school, not the Prestige Academy, where they have thoroughly researched for installation of mirrors and removal of coverings...the Prestige Academy infiltration plan thereafter could be dangerous or impossible. 


        "What school do you go to?"


        The boy who grasped the atmosphere said with a worried face.


        "Prestige Academy."


        There were no words, but they spoke with their eyes.


        "That's perfect. We were planning to go there, too."
                
        <p style="font-size: 2.0em; text-align: center;"><strong>The World Ep.2 : OUTLAW</strong></p>
        A. INTRO

        Prestige Academy


        With his anxious face hoping that the members might help, they boy said, "Prestige Academy." Yun Ho smirked.


        "That's perfect. We were planning to go there, too."


        Prestige Academy. Boasting smooth, slippery walls like that of a spaceship, its curved buildings from an enormous circle enclosing a large quad in its center. When looked at from the sky, it appears as a fortress with buildings built tightly together like walls blocking outsiders fro entering. 


        And in truth, for an outsider entering this place is no easy task. After checking your entry ID at the main gate, you must pass through numerous inspection stations to finally enter. In a way, it's a system similar to that of the immigration offices used to move between countries in World A. While only a school, security is kept strict as only the most distinguished talents of World Z can attend the illustrious academy. 


        In this world, children are required to undergo various tests at a state-certified hospital within six months of birth. After six months of age, a child's natural temperament and talents reveal themselves and it is considered the parents' obligation to nurture their children according to their innate growth potential. The children who have been identified as 'talented' are able to enter Prestige Academy and are then placed in one of five classes depending on the results of their entrance examination. 


        Class 1 is raised to work in the government. They are the ones who will be responsible for researching and implementing systems for better efficiency and control of society in the future.

        Class 2, which includes future Guardians, is trained to control people and punish those who defy control according to government guidelines.

        Class 3 is taught to classify new humans following the system, and then educate them accordingly.

        Class 4 is fostered to handle various tasks necessary for human survival. For example: overseeing new energy exchanges, charging control chips, or the supply and manufacturing of essential energy.

        Class 5 is in charge of city management, sanitization, and organization, and therefore receives and eduction reflective of such. 


        The children enrolled in Prestige Academy are educated and trained in these five classes before being aptly deployed throughout society after graduation.


        01

        Their promise to save the boy's brother aside, as a key pillar supporting the systems of this society, Prestige Academy was the ideal target. By awakening the many children raised there, World Z's ruling class would be damaged from within - they could shake the system from its roots.


        Dressed in security uniforms, Min Gi and Woo Young lead a group of freshmen who had just entered the school. With the help of hacking by Left Eye and the Black Pirates, the members were able to sneak into the school in disguise and scattered throughout the complex, each performing their own roles. Min Gi and Woo Young, who infiltrated the academy's security workforce, were acting as entrance guards after having divided freshmen into their respective classes to avoid suspicion from Guardians and others on the security team. Although they couldn't talk to each other, as they had to pretend to have no emotions, the two exchanged glances without anyone noticing, comforting each other's nerves. 


        Just then, they boy's brother, who they recognized from a photo shared to them by the boy, stopped in front of Min Gi. Min Gi let him pass, but was quick to send a signal to the group, tapping a transmitter on is waist before the next student came. 


        'He just entered the school.'


        Receiving the signal, Woo Young chased after the boy's brother with his eyes. His uneasiness was clear even from just his steps. Through the transmitter hung at his belt, Woo Young sent a signal to the group as well"


        'He's passing through the hallway on the right.'


        The boy's brother went up the stairs. It was clear he was heading up to the classroom intended for the eldest grade of Class 2.


        'He's going up to the classroom. Confirm contact timing.'


        The boy's brother arrived at the classroom and sat down. Maintaining a blank face, he acted as stiff as possible. He placed his glass tablet in the center of the desk and his pen exactly 7.5 cm away in a parallel position as usual. Sitting straight upright as though he were a machine, he gazed at a blank monitor. So far no one seems to notice my emotions, the boy's brother thought with a sense of relief.


        "Meet me in the restroom on the left side of the first floor."


        The boy's brother turned back in surprise at the low voice he heard from behind him. Was there always someone like this in my class...? He thought for a moment. Thinking back, he realized that in the 40 years of attending this school he had never once looked closely at the faces of the people around him. Without the need to exchange emotions, there was no reason to talk to one another face-to-face. And, for the first time in his life he made eye contact with someone other than his family or school faculty. Yeo Sang's deep eyes seemed to whisper to the boy's brother, 'it's okay.' Have I been caught?, he thought. As if in response to the boy's brother's confusion, Yeo Sang flashed the breaker in his hand with a small smile. The action said it all, Yeo Sang knew that he could feel emotions. It was then that Yeo Sang stood up and walked out of the classroom. The boy's brother, who didn't yet know if Yeo Sang was a friend or foe, watched him with a befuddled expression. He quickly turned back and looked around the classroom. He questioned, did anyone see me? But no one did. Just like the boy's brother had done before, the students sat at their desks either adjusting their set up or focused on their own work. Only the sound of objects chattering around, not voices, echoed in the classroom. That's right, no one here is interested in me, he thought and stood up as if he had made a decision. 


        02

        In the corner at the end of the first-floor hallway, he could see a restroom with the lights turned off. Questioning whether walking around in the empty hallway in itself would be an action that seemed suspicious, the boy's brother paused for a moment in worry. Just then a long shadow appeared from behind.


        "Don't worry. We're here to help you."


        It was Seong Hwa. Seeming slightly relieved by Seong Hwa's smile, the boy's brother stepped forward carefully. Seong Hwa followed behind the boy, as if to protect him. He sent a signal to the other members, 


        'I've made contact with the boy's brother.'


        When they entered the restroom, Yeo Sang was there to greet them. Seong Hwa locked the door just in case anyone else tried to come in. Now it was just the three of them: Yeo Sang, Seong Hwa, and the boy's brother. The room fell quiet. The only sound the boy's brother could hear was the pounding of his own heart. He put his hand over his chest. The boy's brother, who was never taught emotion, didn't know what to call the feeling of his heart racing. Is this 'nervousness'? He thought for a moment.  


        "Your younger brother came to the Black Pirates' bunker last night. He was worried that you might get sent to the Disposal Site and asked us to come save you. You know the Black Pirates, right?"


        The boy's brother nodded slowly as if to say he understood the situation. My only way out of this is to follow them, but what does that make the last 40 years of my life? What have I been living for this whole time? And what if I do survive by following them? Then what? What comes next? What if following them leads to something worse? These complex thoughts tangled up in his head and bothered him. Yeo Sang and Seong Hwa knew the boy's brother was feeling conflicted, but there was no time to waste. They explained to the boy's brother that the Black Pirates planned to rescue him. ATEEZ and the Black Pirates' goal was to awaken as many people as possible at Prestige Academy and create the opportunity for them to choose their own paths. It was inevitable that the sudden rush of new emotions would cause some chaos and confusion. 


        "Emotions, confusion. Why would we need those? All it means is that a lot of people will have to go through the same thing as I am right now."


        "Chaos. Pain. They're not necessarily bad things. You need to feel them to move forward, it's something all people go through. That's what growth is. What's clear is that the feeling of growing through pain is a new, precious experience of yours. It was the same for all of us."


        The boy's brother stated at Yeo Sang's outstretched hand. His racing heart gradually started to calm down. He wondered what this emotion was called. The boy's brother didn't know what it was but he could feel the warmth flowing through his blood. He cautiously reached out and grabbed Yeo Sang's hand. 


        "Class will start soon, let's just go back to the classroom for now..."


        BANG BANG BANG!


        Suddenly the bathroom door shook. The three looked at the shaking door anxiously. 


        BANG BANG BANG! Someone outside beat hard on the door.


        "Open the door right now. Otherwise, I will refer you to the disciplinary committee immediately."


        The boy's brother, who was still holding Yeo Sang's hand, quickly pulled away and moved back. Then, with a painful sigh he recited, "Thunder..."


        03

        "Thunder?"


        His eyes shook as Seong Hwa repeated the name back to him. BANG BANG BANG! As the door began to shake again, the boy's brother sprang up as if by reflex and unlocked the door. Outside stood a group of students in neat uniforms. One each of their chests was a symbol inscribed with the word 'THUNDER.' 


        "Why are the three of you all gathered here? With the door locked at that."


        From the crowd of students came a girl's clear voice. The group parted to each side as a female student walked forward. Is this the student group the younger brother had mentioned? And she must be their leader, Yeo Sang thought as he recalled the frightened boy from the day before. The female student, who did in fact appear to be in charge of the group, stood in front of Yeo Sang, Seong Hwa, and the boy's brother.


        The female student who looked as though she were the personification of 'cold,' stared at Yeo Sang with a fierce gaze. "You don't look familiar."


        Yeo Sang handed over the ID card he had prepared in advance. When a male student nodded confirming his name was on the student list, the female student then turned to Seong Hwa. For a while now Seong Hwa had been staring at the girl with a look of disbelief. In other words, with a face revealing clear emotion. Panicked, Yeo Sang moved to block the girl's view. 


        "I think the door needs repairing. I never intentionally locked it, but it wouldn't open and it took me a while to grasp the situation." 


        The female student pushed aside Yeo Sang's shoulder and looked at Seong Hwa again, as if she no longer cared for an explanation of the situation. Seong Hwa was still starting at the girl and the boy's brother had his head down, his hands shaking. Emotions. These were clearly displays of emotion. The girl slowly approached the boy's brother. He swiftly tried to grab his trembling hands behind his back, but the female student grabbed them first. The girl looked down at his very slightly trembling hands with cold eyes. More and more the boy's brother was losing the ability to hid his emotions. His breath shuddered and his face was frightened as if he was on the verge of bursting into tears. At that very moment, when it seemed like it was all over even before the operation had really begun, Seong Hwa snatched the girl's wrists, "Why are you here?"


        In Seong Hwa's question was a hint of nostalgia. The girl looked back at him with an unchanged expression. She wasn't able to understand the intent of his question. Yeo Sang was the same - he couldn't understand what Seong Hwa was thinking. 


        However, Yeo Sang did know that they needed to get out of this situation as soon as possible and he quickly thought up an excuse using the logic system of World Z. "It's inefficient for us to use our time without a good reason like this. Class will start soon, so would you please let us leave."


        At Yeo Sang's words, the Thunder group turned to their leader. The girl raised her free hand signaling permission for them to go, and the group moved out of the way as Yeo Sang took the boy's brother out into the hallway. Pulling her wrist out from Seong Hwa's grasp the girl asked, "What exactly do you mean? Do you not know what kind of group Thunder is?" Seong Hwa snapped out of his confusion and looked at the girl. In this world, it was dangerous to harbor emotions. He touched the bracelet on his wrist, trying to calk himself down. The bracelet was engraved with the words 'Be Free.'


        04

        Hiding his turbulent emotions, Seong Hwa asked the girl again. "Is there a problem with us using the restroom? I don't think the other students and I did anything wrong, so why did Thunder come all the way to this remote restroom?"


        Looking at Seong Hwa speaking with a steady expression, it seemed as if the female student's face shook very slightly. Is she...feeling some kind of emotion? Avoiding Seong Hwa's eyes, the girl said, "It's Thunder's duty to patrol the school. We need to keep an eye on anyone who might be 'emotional.' This is just one of the places in school we're required to check." Seong Hwa examined the girl's face without answering. He wanted to find confirmation of the slip in expression he saw before, but her face had returned to its original coldness. "Class starts soon, return to the classroom for now. I'll let you off with a warning this time but if you get caught again, I'll have to refer you to the disciplinary committee for an emotion test." The female student, the head of Thunder, turned and the rest of the Thunder members followed her. 


        Seong Hwa went out into the hallway, watching the back of the girl as she walked away. The strong, cold looking girl was the one that Seong Hwa had been looking for for so long. Though of course, the same girl in World A and Wold Z seemed very different. 


        That girl he had once encountered back in World A. He came across her by chance, on a day when the rules of life, logic, and efficiency were weighing down his thoughts. She danced freely, letting her body move along to the music playing on the street. After meeting her, Seong Hwa came to realize many things, and everything changed. But on the day he finally decided to muster up his courage and speak to the girl he had been observing from afar, she was gone. Only a bracelet engraved with 'Be Free' was left in the spot where she had once danced. For a long time after, Seong Hwa would often go and wait for her there but she never appeared again. What should I cal this feeling? Is it admiration, gratitude, or curiosity? He wondered. Although still unsure what his feelings were, he continued to look and wait for her. But Seng Hwa never expected that he would meet her in World Z, as the head of the student group Thunder, a group considered elite even within Prestige Academy, which only the best talents of World Z - and the ones most loyal to the system of control - could join. He didn't know whether to be happy or sad. However, just as she had changed his life and set him free that one day, Seong Hwa was determined to save her from this world. 


        05

        That afternoon, taking advantage of the empty campus while the students were in class, the members installed various devices they had prepared in advance throughout the academy. They hid smoke bombs in places they had scouted out, just in case on an emergency.


        The class bell rang and the members were waiting in preparation for the upcoming performance at each of their locations when an urgent signal came: 'The boy's brother has disappeared!'


        It was from Yeo Sang. When the class bell rang, the boy's brother bounded out of the classroom like a bullet before Yeo Sang could talk to him. Yeo Sang quickly chased after him, but he had already disappeared into the crowd of students that had moved out into the hallway. 


        Seong Hwa, who was moving down to the first floor with the younger brother, was flustered by the signal and stopped. The boy asked in surprise, "Who disappeared? My brother?!"


        At that moment, one of the students heading towards the quad shouted.


        "What are you doing up there?"


        At the same time, the members received another alarm signal. It was Woo Young, 'It looks like he's going up to the top floor!"


        As a thought crossed his mind, Hong Joong looked at Min Gi and San worriedly. Just then, the boy shook off Seong Hwa's hand and dashed out into the quad as if he knew what his older brother was thinking.


        Woo Young hurriedly climbed the stairs up to the top floor. Wind blew in from a broken window in the middle of the hallway, bright red drops of blood falling from the broken pieces of glass. Looking up, Woo Young saw the boy's brother standing on a narrow railing attached to the window. The boy's brother looked down at his feet. Students gathered in the quad under him and the dizzying buildings. The looked up at him with dull expressions.


        "I had only one day left before graduation. Just one day and my 40 years of schooling would be complete. But you Sense Offenders have stirred up people and influenced my brother, and now you've made a mess of me, too. My life is ruined!"  


        "No life is ever ruined! This won't solve anything!"


        "If I don't pass the test, I'll be dragged away to the Disposal Site. If that's not a ruined life, then what is?!"


        He shot at Woo Young with intensifying emotions. As he looked back at Woo Young, his foot, which had barely been fixed on the ledge, slipped, swinging in the air before it caught. the railing again. The boy's brother's breathing was unsteady. 


        "At the very least I was confirmed for Class 2. I could have been an Guardian! But now...but now...now everything's all wrong."


        "Until now you've lived within the guidelines set by the government, believing that's your limit. Listen to me, you're just confused. Because this is your first time feeling emotion. That confusion is something that everyone goes through as a part of their lives. By going through it, you're choosing your own path for yourself. You've been a puppet so far, but from now on you can live your own life. I guarantee it, and we'll be there to help you."


        "Yeah, maybe you guys are right. But even if you are, I don't want to live a life that's different from everyone else."


        Tears streamed down his face. With one of his hands that had been gripping the window frame, he wiped the running water he felt on his cheek. Water is coming out of my eyes? What is this? I knew something was wrong with my mind, but I guess my body is broken now too, he thought. 


        "Brother!!"


        A familiar voice came from below. The boy's brother looked down at the quad and among the dull faces there was only one that showed emotion. It was his younger brother. He could tell it was him even from a distance. The same water was flowing down his brother's face. In the midst of all those same, achromatic faces, his younger brother's face which was full of emotion, seemed to shine. It was as if his brother's feelings were being projected on him. He closed his eyes tightly. 


        06

        "Is this really what you want?"


        Yun Ho, who had appeared without him knowing, stood next to Woo Young and called out the boy's brother. Yun Ho was panting as if he had run up in a hurry.


        "How should I know? I've never felt 'want' for anything before. I'm just trying to finish everything before I'm dragged off to the Disposal Site."


        "What about your brother? Do you think your brother wants you to die?"


        Woo Young grabbed Yun Ho's shaking shoulder. He knew very well just what a brother's death meant to Yun Ho. 


        The boy's brother's eyes shook at Yun Ho's words. He looked down again. His younger brother looked up at him with a saddened face and shouted, "Brother, no! Please!! I just wanted to help you!"


        Just then, Guardians ran out of the building into the quad, heading towards the younger brother.


        "No..." The boy's bother called out quietly. "The Guardians will take my brother away, save him - "


        Hurriedly turning back towards Yun Ho and Woo Young, the boy's brother's feet slipped before he could finish his sentence. His body fell into the air and his hand, which had been desperately grasping the window frame, finally slipped. It was only an instant, but every moment seemed to move slowly as if time was being dragged out. With nothing to rely on, his body fell and he struggled to seize hold of something, but with only the air around him, it was all to no avail. Woo Young, who was watching in shock, stretched out his arm towards the boy's brother, but only touched his fingertips - he was already too far away to catch.


        The younger brother, Hong Joong, San, Min Gi, Jong Ho, Seong Hwa, and Yeo Sang, who were watching the scene from below in the quad, could only shout in a stunned manner. Seong Hwa, who was standing closest to the younger brother, quickly covered the screaming boy's eyes. It was at that moment, a light shined behind Woo Young's body that was half stretched out the window. The Guardians, who were running towards the younger brother, stopped at the flash and looked up. One of the Guardians called out,


        "Quantum Energy...It's the Cromer!"


        When Woo Young looked back, Yun Ho had disappeared along with the flashing Cromer. Yun Ho reappeared in the air for an instant, snatching the boy's brother's waist when he was only five meters from the ground. With a flash of light, he disappeared again before materializing in front of Seong Hwa and the boy. With the boy's brother, of course. 


        "Brother!"


        Seeing his brother safe in front of him, the boy burst into tears and, as soon as Seong Hwa let go of his hand, ran to hug him. The brothers hugged. They held each other close, shedding hot tears. Through each other they felt a desperate sense of relief, love, and what "life" was.


        07

        "What a relief. Or...maybe not."


        Jong Ho said, as he approached the other members who were watching the two brother's warmly. As the members looked at Jong Ho, he struggled pointing behind him with his chin. Having caught news of the Cromer, Guardians were rushing in from all over. Seong Hwa made eye contact with the female Thunder leader standing among them. On the surface, there was no change in her expression, but Seong Hwa felt it. It's like she was smiling. 


        "Guess it can't be helped." Min Gi shrugged and smiling playfully "Let's go!!!"


        The group looked at each other and shouted together as they dispersed to their respective positions using the Cromer. Woo Young, who had come down to the quad half a beat late, called out as if he was upset at the members who had already disappeared.


        "Are you going to do this without me?"


        A Guardian stretched out his arm towards Woo Young's back, but there was a spark! With a flash, Woo Young disappeared to his position.


        Beep! With the sound of a loudspeaker, groovy music starting with the sound of a rough, low bass guitar filled the air. Along with the music, a large black tent covered the building. A blinding darkness overtook the people for a moment. Then, colorful neon-colored paintings appeared around the buildings and tents. A splendid fantasy world unfolded around the A marking inscribed in the center of the ceiling. Breakers fell like shooting stars from above the impassive people. As if bewitched, the emotionless students and faculty reached out and grabbed the breakers like they were catching falling stars. Those who brought the breaker up to the chip under their ears were flooded with waves of emotions. It was nauseating at first, but they were soon amazed by the beautiful world that unfolded before their eyes. As ATEEZ and the Black Pirates appeared and disappeared in the dark, the Guardians could do nothing but jump after them helplessly. The paintings that filled the dark world then disappeared in an instant, and a ball filled with light fell from the ceiling to the center of the quad. Everyone's eyes were on the ball. The moment it touched the floor, the ball shot out beams of light, exploding like a light bomb. The light reflected on the walls of the building, and then shining walls showed people's reflections much like a mirror. Those who had regained their emotions walked slowly towards the mirror-like walls of the building. As if they were unfamiliar with their own faces, they touched their hands to their reflections and actual faces, comparing the two. 


        Even those who had not yet used the breaker, upon seeing so many people in the same space do so, began to follow suit. With so many people awakening at the same time, the Guardians were confused, and unable to decide who they should catch. Just then, the tent disappeared and ATEEZ reappeared among the students.


        The music changed and the members danced and sang joyfully. People gathered around then, cheering, singing, and dancing along with the group. It was almost like a concert hall that could only be seen in World A. In World Z, where music, dance, and art had disappeared long ago, this type of scene was something from centuries past.


        The boy and his brother, standing at the front of the crowd, looked up and smiled brightly at the members. For the first time, their smiles were so bright. Like flower petals in the air, ATEEZ leaflets scattered in all directions. The students picked up and read the leaflets. Within minutes, the world at Prestige Academy was completely changed.


        The Guardians, trying to get a hold of the situation, rushed toward the members. Their leader called over the radio, "Catch anyone who's awakened. We need hostages."


        The Guardians caught the awakened in front of them at random.


        "The awakened caught now will be immediately disposed of without replacing their chip. If you want to save them, put down the Cromer and come here slowly." 


        08

        Caught in the arms of the Guardians, the awakened struggled to get away. The members stopped dancing and looked at each other, troubled. No matter how important their goal was, they couldn't risk to the death of innocent people. The members slowly approached the Guardians with their hands up, holding the Cromer. The music faded. Just then, when the boy, his brother, and the newly awakened thought it was all over after seeing the members surrounded - Boom!


        Smoke bombs detonated throughout the campus with an explosive beat. Red, orange, yellow, green, blue, purple, a rainbow of smoke bombs burst and spread out in beautiful harmony with music, obstructing people's view. The members, who had used the chaos to rescue the students caught by the Guardians, opened the escape route they had secured in advance and ushered people outside. Everything was as planned. The members gave each other high-fives and smiled. 


        Then, a scream came from behind. Seong Hwa looked back reflexively, and through the thinning smoke he saw the younger boy caught in the grasp of one of the Guardians. "Where's the boy's brother?" 


        The members, who were already stepping outside, turned back in confusion at Seong Hwa's question, shouting through the thin smoke.


        "He's outside!" "He's with me! Let's get out of here!"


        When Seong Hwa didn't answer, worried, San and Yeo Sang returned to the quad. They could see Seong Hwa's back walking into the smoke. Past him they saw a Guardian half-hidden by the haze carrying the boy. San and Yeo Sang went to help them but were held back by people who couldn't escape and were grasping aimlessly in the chaos. They needed help too.


        Seong Hwa, who had been running toward the boy, stopped abruptly. Yeo Sang and San, while working to get the remaining people out, looked at Seong Hwa bewildered. Seong Hwa stating at someone who had grabbed his arm. It was her. The female leader of Thunder.


        Seong Hwa followed the girl as she pulled him along. The two of them disappeared into the different-colored smoke, All too late, San and Yeo Sang ran into the smoke that the Guardian and the boy had disappeared into, but no one was there. 


        No Sogn Hwa, no boy, no female student.


        There was only Yeo Sang's voice anxiously calling out to Seong Hwa. 


        Z. OUTRO

        The secretary stepped out of Z's office and opened the door. The principal of Prestige Academy and the Guardian leader, who had been waiting outside, walked into the office. Z sat back in a large throne-like chair. 


        Z. There's not much to say. The principal should take responsibility for this situation.


        The principal, whose security protocols for the school were breached during the attack by ATEEZ and the Black Pirates, had no excuse. He was prepared to be demoted and waited for his sentence without a word. 


        Z. Has a replacement been found?


        "Yes. A replacement was found and is on standby to start working right away." Z nodded at the secretary's words.


        Z. Originally, I was going to send you off to a sanitarium, but as an individual in an important position such as 'principal', I've decided to dispose of you quietly so as not to create another excuse for the Sense Offenders.


        "That you." The principal repeated the greeting to Z without really knowing what it meant to be grateful.


        Z. Take care of it.


        The Z-Only Guardians deployed to protect Z immediately took out their guns and shot the principals head and heart. The principal died instantly on the spot. 

        <p style="font-size: 2.0em; text-align: center;"><strong>The World Ep.FIN : WILL</strong></p>
         A. INTRO

        The scenery at the square has changed considerably from when ATEEZ performed just a few months ago. Sense Offenders graffiti symbolizing 'Wake Up' and 'Be Free' decorates the streets, covered with concealment screens installed by the forces trying to suppress them. The world is divided into the systemized and those outside the system, with each group fighting more intensely to win and stop the other. Unable to identify the faces of all the individual criminals, but having detained the men in black fedoras, the government has moved beyond simply denouncing the Black Pirates as a terrorist group and encouraging people to turn them in - plastered across the city are wanted posters of ATEEZ with the members' faces and government announcements declaring that [Those who attempt to induce emotion will be deemed associates of the Black Pirates and, for the people's safety, executed immediately without being sent to the Disposal Site.] 


        A car moved across the dilapidated square and stopped in the center. The Guardians that filed out of the car moved in perfect order. With practiced skill, they set up something on the display that had been built in the middle of the square. A rope was lowered, tied, and pulled. Brushing off their hands and taking a step back from the display, the Guardians looked up at what they had installed. Content with their work, they got back in their car. As the Guardians' car disappeared, silence fell over the square. The small sound of footsteps began to break through the silence. Several Sense Offenders that had been hiding in the alley slowly walked out. Some slumped down in their spot, unable to reach the display before bursting into tears. Under the square frame of the display, feet swayed in the air. Sense Offenders that had been someone's family, someone's lover, someone's friend. Following the government's announcement, now, when Sense Offenders are caught drawing graffiti or distributing breakers they are no longer sent to the Disposal Site. Instead, they are swiftly executed, then hung up in the square for everyone to see. It is an exemplary caution and declaration aimed at the ever-growing Sense Offenders who tirelessly try to change the world: If you continue to resist, this could be you.


        Rather than fall into silence, the square filled with sobs of sadness and anger. Clinging to those people who had once shone so brightly, all they can do is pledge that they will not let those sacrifices go to waste. We can no longer live in a world like this. We've already lost our loved ones, we cannot afford to lose any more. No longer can we let our children live in a world like this. With the same heart and mind the people cried, determination burning through their red eyes. We must let the Black Pirates and ATEEZ know. We are here.


        The raid on Prestige Academy has created a small but significant fissure in this world. That one performance, while strictly censored and kept under tight control, spread by word of mouth and through the Sense Offenders. It gradually split the world into two. And, the story returns back to right after the Prestige Academy raid when the Black Pirates returned to the bunker. 


        01

        Despite the mission being a success, the members gathered in the Black Pirates' bunker with an air of desolation. The boy's brother was asleep in the corner, tired from crying.


        "Seong Hwa wasn't taken away by force. I'm sure I saw it, he walked away on his own. But why...?" Yeo Sang answered San's mumbling as if he was wondering himself. "Seong Hwa looked surprised the moment he first saw her in the school restroom. His expression was almost...taken aback? And his face when he grabbed her hand and walked off in the quad, it was like he found someone he missed. That look was so odd I kept thinking about it. It's the same look Seong Hwa gets when he talks about the girl with the 'Be Free' bracelet he was looking for back in our dimension." Dumbfounded, the members shouted at Yeo Sang that that didn't make any sense. Yeo Sang started as if he was about to say something before suddenly looking at the CCTV outside the bunker and pointing, "Oh? It's Seong Hwa!"


        "What happened? Did you really follow her of your own accord? Just because she looks like that girl? Tell me that's not it?"


        Only then did Seong Hwa realize the members had misunderstood him. The members looked at Seong Hwa, their eyes all filled with disappointment.


        "It's not like that."


        They avoided his gaze as if they didn't want to hear what he had to say next. Seong Hwa paused and saw the boy's brother lying in the corner behind the members. Seeing him fast asleep with such a tired face, Seong Hwa understood the members' agitation. Calmly steadying his breath, Seong Hwa continued in a serious tone. 


        "I'll cut to the chase. We can save the boy."


        02

        One by one, they began to look at Seong Hwa with half-belief, half-doubt. Seong Hwa took a paper out of his inner coat pocket and spread it on the table. It was an unfamiliar map.


        "Thunder is a group made up of elite candidates poised to lead this world one day, and an organization like us. A resistance. The girl put a GPS in the boy's pocket before he was taken by the Guardians. We think he was taken to the Disposal Site. And this is a map of it."


        They all studied the map on the table. It was far too detailed and specific to be fake.


        "The Black Pirates have been around since long ago, so why not just join them? Why go to the trouble of setting up a separate organization called Thunder and secretly working behind the Black Pirates' back? And what makes you believe that Thunder, an elite group among elites, is actually a resistance?" Hong Joong asked, unable to clear his doubts about the girl. Seong Hwa replied with a confident voice, "To find the location of Z, something only the upper class knows." There were short sighs followed by a moment of silence. 


        Not only Hong Joong, who had just aggressively pressed Seong Hwa with interrogating questions, but all the members' expressions changed visibly.


        Z's location was something that for so long had eluded the Black Pirates despite all their efforts. Z only ever contacted the citizens of World Z online through controlled broadcasts of video and audio. Government assistants and lower-ranked officials are stationed widely, sometimes even among ordinary citizens, and while the Black Pirates managed to secure some suspects and coax them through emotion-inducing breakers in an attempt to find Z's hideout, the only information they were able to obtain was that Z resides in the center of the city where this world's top class works and never leaves the building. Those who work in Z's hideout are selected from only the most elite and their access to the outside world is restricted after selection. Since the Android Guardians, known as the Imperial Watch, are not humans with emotions, emotion-inducting devices are useless on them, and thus the group had presumed finding Z's hideouts nearly impossible. 


        As Prestige Academy is made up of only the most elite, there was a higher possibility that more people there than in any other class would be able to awaken emotion on their own and hide those emotions successfully. Thunder's purpose had evolved into this: Disguised as a government-approved school organization, the group could gather internal information on their world in plain sight, increasing their current safety and probability of success. And above all, to secure information on Z's hideout - information necessary for a revolution. 


        The control over everything that triggers emotion in this world began with Z, the leader of the pseudo-religious scientific organization called Scienslavar, and the organization's AI simulation for the 'best solution.' They created a political party under the catchphrase "The pursuit of a peaceful world without religious conflict and terror through emotional control." The party grew in size, passed the Emotional Regulation Act, and as a result, Z effectively took control over this world. Under his control, the world's class system solidified and they began disposing of humans deemed 'defective.' Z's hideout, where all political subordinates are gathered, acts as a control tower and is a fundamental place to this world. For this reason, it is a place the Black Pirates needed to eliminate - a place even more symbolically important than Prestige Academy.


        While they still weren't sure how much they could trust Thunder, the members were determined in their next goal: going to the Disposal Site and saving the boy, the most urgent issue of the moment. 


        03

        The Head Guardian of the Z Imperial Watch traced the path of blood that flowed to his feet back to the cold face of the principal of Prestige Academy with his eyes. The thought crossed his mind that he too might end up like this one day, but he gazed at the scene without much emotion.


        Z. Now that we've set the bait, the Black Pirates will go to the Disposal Site to save the child. Take care that no mistakes like this are repeated at the Disposal Site. Or you'll be the one replaced this time. 


        "Understood. I'll handle it without problem," replied the Head Guardian in a voice void of emotion.

        
        The Head Guardian brought with him over 100 Android Guardians to the Disposal Site. As the entrance closed, a kaleidoscope of blue butterflies fluttered in through the closing door and flew along the path of the Guardians. As the Guardians pass by, Red Humans working at the Disposal Site lower their heads to greet them. In rag-like clothes with skin reddened by the furnace, the appearance of Red Humans is so hideous they now resemble goblins more than people. At a crossroads, the Guardians walk to the left and the butterflies scatter. One of them flutters into a hallway on the right. At the end of that hallway is a row of small rooms blocked by bars. Each room is packed with people, making the space look even tinier than it is. These are people soon to be disposed of and an air of desperation fills the room. They've been marked as defective for harboring feelings or having physically impaired bodies. When the small butterfly suddenly appeared before them, the people sitting there helplessly were unable to take their eyes off it. A few stood up, grasping the bars of the cage to gaze at it fluttering down the hallway. Was it some hallucination brought by hope? The butterfly exited the end of the hallway. In a boiling furnace shooting out hot air, remains of disposed human bodies float to the surface before sinking down again, melting into the incinerator. Red Humans stand on a bridge above and use an unmelting stick to stir. The butterfly looks down at the scene, rising above to an execution platform that connects to yet another hallway. It gently sits on the execution platform as though it were a diving board. The body of the butterfly fluttering its wings a few times looks odd.


        Upon closer inspection, it becomes apparent that it is not a living creature, but an animatronic. And at the end of said animatronic's body, was a camera. 


        04

        "The GPS signal leads here, but why don't I see anything?" Yeo Sang said, operating the butterfly-shaped drone from a van stationed in the darkness of an alleyway near the Disposal Site. The monitor's screen showed the inside of the Disposal Site illuminated by the butterfly drone, and the members gathered to check the inside of the facility against the map they received from Thunder. 


        "Either way, it shows that his location is somewhere inside. I'm sure we'll find him when we get in. Guardians who aren't part of Z's Imperial Watch don't carry individual weapons. As long as we move swiftly, we have a good chance of winning. But it's imperative we get there before he's disposed of so let's move as planned." The members, nodding at Hong Joong's words, sat down and fastened their seat belts with determined faces. With the sound of a powerful engine starting, the headlights flashed on, illuminating the darkness. Grabbing the steering wheel, Min Gi violently stomped down on the gas pedal and left the alley, racing through the parking lot near the Disposal Site. Speeding forward without hesitation, the van crashed through the parking lot fence, sending it flying onto some cars parked in a row. Beep, beep, beep. Car alarms burst sporadically from each car, and the silent area around the Disposal Site filled with noises in an instant. At the disturbance, the Guardians inside the Disposal Site whipped around. Panicked by the sudden disturbance now of all times, just when the Guardians were visiting, Red Humans rushed outside to the parking lot to recover the situation. As the Red Humans ran out, the members took the opportunity to sneak inside, wrapping chains around the closed door handles and securing them tightly with locks - to prevent the Red Humans from entering again. Running to the hallway on the left, Hong Joong, Yun Ho, Yeo Sang. and Jong Ho were faced with Guardians running toward them. The fighting began as Guardians rushed at them as if they had been waiting for this attack. The four members fought back with weapons prepared by Left Eye, but the other members who were in charge or moving the prisoners to the bunker had the Cromer. Without the Cromer, the physical strength of the members fighting the Guardians was inevitably reduced. As Hong Joong was knocked to the floor by a Guardian's fist, he heard the click of a gun cocking from above his head. The members looked at Hong Joong with uneasy expressions. Yun Ho, Yeo Sang, and Jong Ho could hear guns click above them as well and the members, surrounded by Guardians, carefully stood up, their backs together. Guardians stood around them staring at them with guns pointed. 


        Meanwhile, Seong Hwa, Min Gi, San, and Woo Young, who were moving the imprisoned people back to the bunker of the Black Pirates, suddenly heard a noise through the closed door and froze. Feeling intuitively that something had gone wrong, Woo Young guided the people shaking in fear inside the bunker. The sounds of shouts and screams were growing closer. 


        "The Guardians have weapons. Currently, all members are surrounded. We need backup from the Cromer." Jong Ho's soft voice called over the radio. 


        If the Guardians at the Disposal Site were armed, the members would need the Cromer. But they also couldn't just leave the people they had barely managed to save alone here. Something was definitely going on outside the bunker doors. 


        San picked up the radio and said, "Trouble on the Pirate Bunker side as well. Hang in there a little longer. We'll be right there."


        At the moment, the bunker door burst open. A Pirate member covered in blood hurried and shouted, "The Pirate Bunker's been exposed to the Guardians! We need to evacuate now--"


        A beam saber flew in from behind cutting the Pirate member down his back. With a wretched cough, blood spurred out from his mouth and he fell forward. Behind the fallen member, armed with mean sabers, the Guardians stood and looked at the members. 


        05

        "Where the heck did the leak come from?" Woo Young whispered in a low voice, unable to make sense of the situation. For the safety of the bunker we made sure this place was hidden, and hidden well, so just how did the Guardians get a hold of this location? It would be impossible without an inside spy. "Seong Hwa...Please tell me you didn't share the location of the bunker with the Thunder girl, right?" Seong Hwa couldn't answer Min Gi's question.


        He had been so sure of the girl's feelings, but that might have been a misjudgment. 


        "Ahhh!"


        A scream was heard over the execution stand. It was the boy's voice. The boy was being held captive by the Guardian. The Head Guardian, his gun aimed at Hong Joong, spoke: "Tell the members with the Cromer to come over here. I'll give you 10 minutes. Or this kid...well you know what'll happen." He set a timer for 10 minutes. 


        Hong Joong, who had been agonizing over the desolate situation for a while now, picked up his radio and relayed to the members in the bunker, "They're holding the boy hostage. I think all four of you should get over here right now, within 10 minutes." 


        While the members at the Pirate Bunker knew they needed to quickly solve the situation on their side and head to the Disposal Site, with so many Guardians closing in on them, the fight was unlikely to end easily. Skillfully using the Cromer's spatial movement ability, the members knocked down the Guardians one by one. Then, in just a split second, Seong Hwa was struck in the side by a flying beam saber and fell to the ground. Min Gi ran immediately towards Seong Hwa, trying to take out the Guardian and stop the attacks flying toward his fellow member, but in that same moment, another Guardian struck Min Gi as well. Min Gi and Seong Hwa collapsed, then San and Woo Young followed, coughing up blood on the floor. Having successfully pushed back agains the members, the Guardians's strikes came down on them like bombs. 


        Many thoughts passed through the minds of Hong Joong, Yun Ho, Yeo Sang, and Jong Ho, as they were dragged helplessly though the Disposal Site to the execution area, and likewise through the minds of Seong Hwa, Min Gi, San, and Woo Young as they were kicked down by Guardians into the bunker floor. 


        It was as if their lives were flashing before their eyes.


        They met the men in the black fedoras and came to this world, and, like it was some kind of fate, ended up carrying on the mission they left behind. Ironically, here in heavily restricted World Z they remembered the dreams and emotions that, under the pressure of reality, they had begun to forget back in World A. And somehow, for someone other than themselves, They ended up running to this point, determined to save these people that had all but resigned themselves to a desolate life in this world. Through many performances they realized just how much impact their songs and dances, which they had considered dull and insignificant, have on people. They were happy to fight alongside the Black Pirates as ATEEZ, but that all ends today.


        Just then. With the sound of a zap, a Guardian fell to the floor of the bunker. 


        06

        For a moment, the Guardians' attacks stopped. When Woo Young barely managed to look up, he saw people in ridiculous masks with thin, long sticks flooding into the bunker. The other members were also confused. As they were all wearing the same ridiculous masks making them impossible to identify, the members didn't know whether these people were friends or foes. 


        When the masked figure standing at the front raised their stick and pulled the handle, a zap of electricity was released. It seemed like some kind of modified electric shocker. The figure swung the stick forward as if wielding a baton and the masked people behind them let out a cry and began running forward. The members, already covered in blood, curled up and closed their eyes tightly, preparing to be struck. Zap, snap, crack. Sounds of electricity were heard sporadically, followed by the thump of something falling to the floor. Bang, bang. The members cautiously opened their eyes to find the masked figures attacking the Guardians, taking them out all at once with electric shock waves. Broken Guardians laid stiff on the floor. The lead masked figure approached the members and stretched out a hand. Seong Hwa took the figure's hand and stood up. Then, Ming Gi, San, and Woo Young also took the hands of the masked people and stood up as well. 


        "I'll evacuate the people here to somewhere safe. Come here when you're done at the Disposal Site."


        The masked figure had a modified voice and handed a note to Seong Hwa before running towards the Guardians still attacking behind the members. 


        For now, it looked like these masked people were there to help them. And if that was the case, there was no time to linger. They needed to head to the Disposal Site and help the members in trouble. San picked up the Cromer. Flash! Just as the Cromer lit up, the boy's brother, who had been hiding in the corner, also threw himself toward the light.


        "Looks like they're not able to come over." The Head Guardian loaded the gun he was aiming at the boy's had. "I assume the rest of the members are in the bunker now? So it's safe to say that not only the Black Pirates, but all the people you rescued and all your members must have been taken care of. The Guardians were already at your bunker before you infiltrated the Disposal Site. I was sure the Black Pirates had all been dealt with, but I gave you 10 minutes just in case to check if any remaining members with the Cromer were left alive. But if they couldn't come here in 10 minutes, that means they're not in the position to help you. Looks like we won't need to wait any longer. Ten minutes is already up anyways."


        The number on the Head Guardian's timer was decreasing. 00:03, 00:02, 00:01...The alarm went off loudly as the timer struck 00:00. Just then, when they thought they would lose the boy and all was in vain, Seong Hwa, Min Gi, San, and Woo Young appeared with a flash of light. They quickly appeared in front of the Guardians gathered in the back and disappeared again, repeating this until, before anyone knew it, they had taken all the guns the Guardians were holding and thrown them into the furnace. 


        Then the Head Guardian, who was holding into the boy, grabbed the boy by his neck, lifting him up with one hand and lowering him close to the furnace. 


        He shouted, "Do you want me to melt him feet-first like this? Everybody get on your knees!"


        The members, who had been fighting the Guardians with their fists, halted their attacks and knelt down one by one. At the Head Guardian's nod, other Guardians restrained the members with rope. Despair fell over the group. 


        At that moment, another person was watching this scene from behind. The boy's brother, having heard over the radio that the boy was being held hostage, could no longer hide in the bunker, and threw himself behind the members when the Cromer flashed. He watched the situation unfold, holding his breath as he hid. These people who had saved him, these people who had stopped fighting to protect his brother and knelt on the ground - he knew he should step up and help them. Just in case, he took out the portable jackknife he brought for self-defense out of his pocket and held it in his hand. He laid the jackknife down on the floor and pushed it hard toward Yun Ho in the back. The jackknife slide across the floor until it hit Yun Ho's foot and stopped. The slight bump caused Yun Ho to glance at his feet out the corner of his eyes and there was the jackknife. When he looked along the line of the knife back to its source, Yun Ho saw the boy's brother staring back at him. They still had a chance. Slightly relieved, Yun Ho grabbed the jackknife, avoiding the Guardian's surveillance. Careful not to make a sound, he began sawing through the rope tied around him. Then he handed the jackknife to Seong Hwa at his side. Carefully, Seong Hwa began to cut through his own rope. 


        Having captured all the members and obtained the Cromer, the Head Guardian dropped the boy to the execution stand floor unharmed. The members were relieved that they boy was safe, at least for now. The boy let out a heavy sigh of relief and raised his upper body to look at the Head Guardian. 


        "Am I done with my role now?"


        "As expected of an elite student, your acting was excellent. If all ends in success, Z promised that he would not deal with you brothers as Sense Offenders but, as a special exception, allow you to return to your existing class or higher after refitting your control chips."


        The members and the boy's brother, who had overheard the Head Guardian's conversation with the boy, looked back at the boy, confused. As if feeling their gaze, they boy turned his body toward the members. With an innocent, if not frightening, face the boy spoke.


        "I'm sorry. It was just so hard to find the Black Pirates' bunker. So I came over hear first and asked for help. It'd be nice if you didn't hide yourselves so well. You wanted to make your group more accessible to the people, didn't you?"


        As everyone was looking back to the child with disbelief, Seong Hwa, who just handed over the jackknife to San, pulled from his sleeve the note he received from the masked figure in the bunker. He opened it and saw it was a map, and on that map was written: Thunder.


        07

        The prisoners rescued from the Disposal Site shuffled into the luggage compartment of a large bus. The masked figure pleaded with the curled-up, hidden people to be patient and closed the door. Then, after looking around to make sure no one was watching, they removed their mask. It was the girl, the leader of Thunder. She took off her work clothes to reveal a school uniform underneath, a uniform that only the most elite students of World Z were allowed to wear. 


        The other masked people took off their masks and clothes as well. They revealed the same faces the members saw back in the Prestige Academy restroom. The girl fixed her hair and got on the bus.


        The bus ran along the road before stopping in front of a checkpoint to the city center. Guardians stopped the bus for a short while. From the exterior of the bus, they saw the faces of people through the bus windows. They were faces and clothing that guaranteed themselves and needed no inspection.


        The Guardians tapped the rear of the bus and the vehicle started again. Thanks to their status, the group passed the checkpoint with ease.

        
        When his older brother, who had just woken to emotion, panicked in fear at the thought of being disposed of, the boy first tried contacting the Black Pirates through the Black Link, hoping he could find their bunker and ask them for help. But when he was unable to find it, he gave up, leaving only a message on the Black Link and resorted to hiding in the Disposal Site. When my brother's dragged here, I'll save him somehow.


        The boy hid all night, but around the time the sun rose, he received a message from none other than his older brother asking why he didn't come back last night, and went home, relieved. Without much thought, the boy turned on his computer to find a message. It had come in via the Black Link. The Black Pirates had seen his message and responded with the rough location of their bunker, along with assurance that if the boy were to call for help from the Black Pirates while in the area, and the monitoring staff determined the situation was all clear, they would help him. It was then that the boy changed his mind. 


        The fear he felt staying overnight at the Disposal Site and seeing the facility for himself had changed his mind. He ran to the Head Guardian and asked him to make an exception of himself and his older brother, both who had found emotion, if he promised to uncover the location of the Black Pirates' bunker.


        Yun Ho and the members, who had believed the boy's desperate plea to save his brother, felt deeply betrayed.


        "When I said I didn't need emotions to live in this world, you said something to me. You said that when the fear passed, I'd see a different world! You were right. The faces of people with different facial expressions, the world seen through the window now that the screens have been removed, and the feeling of seeing myself in the mirror for the first time. You must know it all even better than me, you woke to emotion first."


        "Brother..."


        Seeing his brother criticize his choice, the boy was shaken.


        "When I thought I had to die, when I almost died, these people were the ones who saved me. How can you do this to them after seeing all that with your own eyes?"


        "I didn't have a choice. If I wanted to live and save you too."


        "It might have been different if I had never known, but now that I know emotion, I can't go back to how I was before anymore. It's okay to make a wrong choice. It's okay to make mistakes. You can turn it around. You just have to make the right choice next time. Come here. That side's not right."


        For a moment, the boy looked down at the Head Guardian's foot beside him and turned to look at his brother, whose hand was stretched out to him. When the younger boy didn't budge, the older brother moved slowly toward him. They boy looked at the members with a sad face. Yes, everyone lives by making mistakes. Depending on whether you choose to turn it around at the next opportunity or cover up your mistakes with more wrong choices can make all the difference in one's life. The members knew it better than anyone else. They looked at the boy, hoping in earnest that he would make the right choice that would erase their feelings of betrayal. The boy, whose eyes were shaking violently, moved to approach his brother as if he had made a decision. The Head Guardian moved his head and the Guardians standing behind him sprung to catch the boy's brother. All the while, Yeo Sang, who had freed his legs from the ropes, secretly positioned himself to trip the Guardians. The Guardians feel forward, tangled among themselves, and the boy's brother quickly ran to the boy, avoiding them. Just before their hands could reach, with a snap, the Head Guardian grabbed the boy by the back of his collar. Before the members could do anything, the Heads Guardian kicked the boy's brother, sending him falling below the execution platform.


        "No! Brother!"


        The boy bit down on the Head Guardian's arm and jumped under the execution platform to where his brother fell. At the same time, the members, moving their free limbs, pushed the Guardians into the furnace. Min Gi started the Cromer. 


        Min Gi, appearing in the air above the furnace and below the execution platform, had to make a lot of judgements in just that short moment. Could he save both the boy and his brother, and if he could only save one, who? Just as Min Gi reached out to the boy's brother below him, the boy's brother's lower body slipped into the furnace. The boy's brother closed his eyes as if telling Min Gi to go save his younger brother. With a sorrowful heart, Min Gi turned his head and snatched the boy falling from above. The boy looked at his brother, who was sucked into the furnace and screamed.


        Min Gi put the boy down in a safe place and using the Cromer ran to the members who were in the midst of a fight with the Guardians. The members, full of anguish from having watched the boy's brother fall into the furnace, threw the few remaining Guardians into the incinerator. The boy looked at the furnace, stunned. At the very furnace that had devoured his brother in only an instant. His choice has made a mess of everything. Tears poured from his eyes.


        The boy's tears fell and evaporated on the surface.


        Now only the Head Guardian was left. Just as the Head Guardian chased after Hong Joong, who was holding the Cromer..."Die!!!" The boy ran toward the Head Guardian from behind at full speed. Using that momentum, he grabbed the Head Guardian, carrying the two of them off of the execution platform. 


        Hong Joong tried with one arm to hold onto the boy, but it was not enough. For an instant, Hong Joong's gaze met the boy's eyes stained with tears.


        The boy mouthed to Hong Joong quietly, "I'm sorry."


        Dragged down by the boy, the Head Guardian fell into the furnace. Hong Joong had no choice but to sit back and look down at the surface of the furnace in despair.


        Then, the building shook with a distant bang. Seong Hwa checked the time. "I know how you feel, but...We need to get out of here first. The bomb's about to go off."


        "We should go, too." San picked up the Cromer. As the flash of the Cromer spread inside the Disposal Site, a series of bombs went off. A blue butterfly sitting still on the side of the execution stand emitted a red light and burst apart. Blue butterflies that had been located throughout the building burst and in an instant the Disposal Site collapsed. Remains of the building fell in the boiling furnace as the Disposal Site sank to the floor. 


        08

        There was a garden in front of Thunder's main base. In it, two similar looking trees were planted. The ATEEZ members dressed in black suits, the Black Pirates, and Thunder members bowed silently in front of the two trees. Behind the trees, which resembled the two brothers, were other flowers and trees bearing the names of the Black Pirate members lost in the flight "I will not let your sacrifices be in vain. I promise."


        It may have been Yeo Sang's words, but it was also everyone's will. Fireflies glittered over the heads of the grieving people. As if in response to everyone's hearts, the fireflies circled over the people's heads once more before climbing high up into the sky. The fireflies seemed just like stars to the people, and so they looked at them for a long time. Like they were making a wish on a star. 


        This place, a small village in a lush, grassy forest far away from the government's surveillance, was the place where the Grimes siblings first met long ago. According to the girl, the leader of Thunder, one day, by chance, she came across the Grimes siblings singing on the street and for the first time in her life, she understood "beauty." While the raw emotion she had only ever understood in her mind before felt unfamiliar at first, as time passed, she realized the truth that something essential had been taken from humanity.


        "Did you realize that while you were attending Prestige Academy?" She stopped for a moment, lost in thought, as she showed Seong Hwa around the village.


        "At the time, I had already been chosen as an excellent talent and was a member of Thunder. I was also already selected as the next group leader."


        Exceptionally smart, she flawlessly acted the part of an elite student to avoid any suspicion that she was an impure person. And on the day that Thunder received Z's achievement award, she made a resolution. 


        "Only a limited number of people ever met Z. Maybe if I were to become the head of Thunder, and enter society with such a career, someday I would meet the ever-elusive Z. At least that's what I wanted to think..."


        She turned her head and looked into Seong Hwa's eyes.


        "I want to live in a world where I can enjoy beauty."


        Behind her resolute gaze, he felt a strong sense of determination and belief. Suddenly, he remembered the girl back in World A and felt his heart beat loudly. Worried that she might hear it too, Seogn Hwa avoided her gaze and walked forward. She followed Seong Hwa quietly.


        World A and World Z. These two worlds seem very different, but they felt somehow connected. The men with the black fedora's who look just like themselves. They were men who, just like the members from World A - even if we were only dreaming - danced and sang to evoke happiness in people. While we may seem like totally different, we are in fact the same. The same was true of the girl. The girl with the Be Free bracelet danced freely with no care or worry as to how she looked to other people. Seong Hwa, mesmerized by the beauty, saw himself in her and from that day on, started to walk a new path free from restricting rules and principles. The Thunder girl, she reminds me of the girl from our world. And she reminds me of myself, Seong Hwa thought. Moved by the feeling of beauty stirred within her after listening to the songs of the Grimes siblings, she started on a new path away from the principles and rules of this world. The moment he first saw her at Prestige Academy, behind the girl's cold exterior, Seong Hwa had clearly felt that heart - that very yearning for beauty.


        "Since becoming the leader of Thunder, no students were branded as Sense Offenders or sent to the Disposal Site. I would always just intimidate with empty words like the time I first saw you in the restroom." As she said that, she laughed softly. 


        "What about the other Thunder members? Did you all come to an agreement?"


        "I carefully approached anyone I thought was experiencing emotion. Because it's dangerous. Anyway, while that was happening, I came into contact with some people who knew the Grimes siblings. After the siblings had their souls taken away at the Guardian's bunker, groups of people who knew the siblings or were awakened thanks to them, gathered to hold a funeral. And we decided to build our base here in this place where the siblings once hid. Through all this, I also learned about the existence of the Black Pirates and heard stories about ATEEZ. I really wanted to contact you, but we, a smaller group than you, had to move more carefully. But I didn't expect to see you at the school."


        People passed the Seong Hwa and the girl. Thunder and a group of Black Pirates were pitching in carrying food to the people they had rescued from the Disposal Site. "I thought the Black Pirates were fighting alone, but I'm glad Thunder's here too. Just like how we didn't know about Thunder, maybe there are a lot of other people in the world who think the same as us. They could be fighting alongside us right now." Seong Hwa's reflection on Thunder's existence giving him strength resonated with the girl's heart. Did I make the wrong choice? A small whisper of doubt had always existed hidden deep in her heart, but Seong Hwa's words changed that worry into conviction. Conviction that she had made the right choice.


        Z. OUTRO

        After ATEEZ and the Black Pirates' surprise performance - labeled terrorism by the government - at Prestige Academy, the institute was temporarily closed down as the ruined curtains were discarded and mirrors removed. The building was remodeled as a panopticon structure with a surveillance tower in the center to help strengthen overall control. The students were transferred to nearby schools according to their grades, and Thunder's leader was moved to a distinguished school of similar level with Prestige Academy. Having passed the emotion detection test - with the help of a present from Left Eye, a device that keeps one's heart rate steady - and completing the remainder of her exams with top marks, the girl successfully graduated without a problem.


        As she was by far the most superior candidate, she was picked up by the government and appointed as Z's protocol manager. On her first day of work, the girl, who had until that point maintained her composure so well, began to tremble at the thought of finally reaching her goal. This was a place sensitive to outside intrusion, if her cover was blow here she would be shot on the spot. Looking in the mirror, she cleared her head and took a deep breath. 'It's okay. You've done fine so far.' she said, looking at herself in the mirror. 


        The Guardians came to pick her up in front of her house and the girl followed them out and into their car. 'Just where is his hiding place...It must be in a difficult place to find,' she thought to herself as she chased the scenery outside the car window with her eyes. She memorized the way looking at the surrounding buildings and signs, knowing she would have to describe it accurately and in detail. 'Why are we going her?' The car ran along a familiar road headed for the city square. She didn't expect Z's office to be this close. They headed into the underground parking lot of the tall central bank building in the middle of the city square and entered a private space marked "Authorized Personnel Only. All others are prohibited from entering." They stopped between the walls that hid the surrounding space. The girl got out of the car and entered a hidden corridor, following the Guardians. They took an elevator in the middle of the hallway. The Guardian pressed the button to the penthouse and the elevator rushed up at a high speed. Ding! With a clear bell, the elevator door opened, and the girl walked along the long corridor feeling as if she had come to another world. The sound of the Guardian's footsteps and her own footsteps echoed in the cave-like space. After passing through the hallway through a checkpoint searching for dangerous items such as guns and knives, they walked along a long hallway again. Though the windows on both sides, she saw people working in each room. They looked like fish trapped in an aquarium. After passing through the corridor and reaching the end, she was met with a large door. As if it had been wacthing her, the large door opened as soon as she stopped before it. The refined office on the other side felt suffocating in contrast to its enormous size. All the walls of the room were glass. Charged energy molecules lined the room.


        Upon first hiring an office worker to his team, Z always inspected the people with his own eyes. That was the real final test. Only after passing the test, were they able to receive their ID card that served as a pass - the pass, which is required to be worn by everyone in the office, also functions as a monitor complete with camera and audio. 


        Z. Which of these many molecules is yours?


        He questioned her, sitting across a high-backed chair. This must be Z. She swallowed, careful not to make a sound. 


        "I don't quite understand what you mean."


        Energy molecules shone beyond the glass wall. They were particles of emotional energy linked to the chip in one's ear. At one point, the light emitted by them was even more intense, but as the Sense Offenders' protests intensified, the energy of those who had turned against the government disappeared, making the light weaker. 


        Z turned his chair and looked at her. She gazed at him with resolute eyes. Slowly raising from his chair, Z walked toward her with a dim smile on his face as if the final test had already begun.


        Z. You were looking around outside the car. And then in the hallway. And now at the molecules that are beyond this glass wall, you're looking at them with curiosity. Curiosity is also an emotion. Curiosity is dangerous, you know. 


        Z grabbed her chin with one hand. He studied her expression, moving her face in his hand.


        Z. Would your molecule be here? Or...Is it already gone?


        Oh, the road here was already the test. Don't tell me that all our plans have failed? Is this how I die? She felt her blood run cold with fear. But it was still too early to judge. The fact that Z asked a question means that the results are still inconclusive. I have to keep my composure. I must not be caught.


        "What is 'Curiosity'?"


        In response to the girls answer, Z took his hand off her chin as if he was amused by her retort. He waited, looking at her mouth as if to see if she would keep talking.


        "That was not an emotion, but a thought. I was looking at the structure to figure out where I'm going to work. My molecule is here, of course. Feel free to check for it now, if you must."


        Z ordered the Guardian with his eyes. The Guardian checked the chip next to the girl's ear to see if it worked. There was no reason for her to be shaken. A long time ago, when her chip lost its light due to emotional awakening, she discovered her own way to avoid being caught at school. She manipulated the chip to turn on and control her emotions right at the moment she wanted and turn off releasing her emotions at the moment when she didn't need it. The chip responded to the Guardian's hand and emitted and yellowish glow. Only then did Z smile with satisfaction.


        Z. So what do you think of the Sense Offenders?


        She answered with a cold face, "They are unnecessary impurities." 


        FIN.  

        <p style="font-size: 2.0em; text-align: center;"><strong>The World Epilogue : To the End</strong></p>
        
            My dear ATEEZ,  
            The sibling tree we planted together has grown much taller than me. It might not seem like a big deal, but shortly after you left this place,
            the tree trunk got badly split. I quickly put a splint on it and wrapped it well, but I was worried it might die.
            Fortunately, it has grown well, so it's that impressive?  
            
            Looking at the much-grown sibling tree reminded me of the child and his older brother.  
            "If they had grown up, would they have looked like this? Would they have been this sturdy and strong?"  
            I asked you this question to myself.
            I imagined your playful yet proud responses. Only then did it hit me in a concrete way: The reality that you had left for your world, and the fact that I could no longer see you.  
            
            Until I passed Z's test with flying colors, no one expected that we would part so suddenly.
            We were so fuced on being happy that I was accepted into Z's protocol management position and the next mission.
            Indeed, the protocol management position was the best way to access the system Z had built. And the hint you gave me was a huge key.
            The leader of Sciensalvar, Henry Jo.  
            Knowing the idenity of someone who looked like Z helped me find the system password.
            (Did I mention that there were records of Z accessing your world there? When Z briefly had the Cromer, it seems he met Henry Jo in your world. If my memory is correct, it was 1999 in your world.)  
            While it was difficult to access the system, the system itself was designed with a simple structure.
            It wasn't that hard, since after the central government took emotional energy, all humans were no different from programmed machines. The structure of a dictatorship is obvious. 
            We decided to use the well-built system itself. We just turned things upside down. 'Wag the dog', a strategy where the tail wags the dog's body to grab the head and take control.
            By tweaking the input values of chips planted in people's ears, the tail became the head, and the head became the tail. Do you remember?
            Z desperately searched for the Guardians while surrounded by people in the square. It was so pathetic that I thought I was the villain at that moment?! What a joke...  
            
            So... What I'm saying is... If I hadn't been swayed by that pathetic act, we wouldn't have let you go. Just when I couldn't pull the trigger, Z took and old man standing nearby hostage, and as always, you used the Cromer to save the hostage, but Z used that to take your Cromer.
            Then Z immediately threw the Cromer to the ground. Probably intending to escape. You all ran towards the falling Cromer reaching out to stop it, but just as you touched it, the Cromer hit the ground and shattered into pieces. 
            You all ran towards the falling Cromer reaching out to stop it, but just as you touched it, the Cromer hit the ground and shattered into pieces.
            As the flash was about to engulf you and Z, I realized what it feels to be overwhelmed with rage.
            I pulled the trigger at Z, who was clinging to SEONGHWA to somehow survive.  
            
            After the flash disappeared, Z fell to the ground of the square with a thud. But you guys... You were gone.  
            
            You probably returned to your world, right?
            Even though you're not in our world, kids who followed your music, dance, and performanced have become another ATEEZ, remembering you.
            You're not here, but ATEEZ is still here.  
            Oh, by 'here', I mean 'the zone liberated from control'.
            After Z disappeared and you left, a lot has happened.
            We were divided into those who decided to live freee from emotional control and those who decided to continue under the system's emotional control.
            We tried to make a unified decision, but it wasn't easy. 
            After a prolonged period of indecision, we decided to respect each other's decisions. We couldn't force htem to believe what we believed was right.
            We chose to coexist peacefully and divided into the 'Liberation Zone' and 'Control Zone', each establishing its own order.
            It's sad to think that, over time, we might become different nations, but what can we do?
            If I may be just a bit greedy, I just hope we don't treat each other with violence or coercion.  
            
            Thunder's headquarters now acts as the interim government of the 'Liberation Zone'. So, unlike before, it's become a place where people frequently come and go.
            The sibling tree stands in the most visible spot in the garden, and the injured trunk has healed, leaving bumpy scares.
            I wondered if the scars were too unsightly and whether I should cover them with a ribbon, but then a child walking with his parents saw the sibling tree and said this.  
            "Oh?! These trees have unique patterns unlike other trees. Wow, they're pretty."  
            'Patterns? Now that I think about it, I've only ever thought of them as scars, not patterns.'
            These patterns created by the scars distinguish the sibling tree from other trees. Scars can become unique patterns.
            Realizing that made me look forward to the 'Liberation Zone' that will have unique patterns in the future, and to myself.  
                    
            I'm writing this letter because I miss you, but I don't know if it can cross the universe to reach you, if we can hear from you, or even if there is a way to send it.  
                    
            I wonder if you safely arrived back home. When the first Cromer broke, you said you arrived in the past.
            Did you arrive on time this time? Are you still dancing and singing together there? I hope all your wishes come true:
            finding your family, gaining independence from your strict father, standing on stage, meeting many people, and making lots of money.
            You've changed many people's lives, so I'm sure you've succeeded.
            Whatever it may be, I hope you remain 'free' without being too tied down, just like she said, the one who resembles me. :)  
                    
            I miss you all. The Black Pirates, Thunders, Left Eye, and everyone in the Liberation Zone all miss you. Will there be a day when we can meet again?  
            Hoping for that day...  
            
            - Your Thunder
                    
        <p style="font-size: 2.0em; text-align: center;"><strong>Golden Hour Pt.1</strong></p>

                       
        00. INTRO

        After the red moon rises 


        In the aftermath of Z’s disappearance, there was not a person in World Z who didn’t know of ATEEZ. The people split into two factions-those who decided to free themselves from emotional control and those who chose to stay under it. The Black Pirates and Thunder established a self-sustaining order so that these two factions would be able to coexist. 


        This world was entrusted to those who love and care for it,

        And as for us, we returned to our world. 


        Yet, even after we returned, those feeling of excitement lingered. 

        The memories of our adventures and battles together remained vivid in our minds, as tangible as if they had been engraved on our skin. 


        Making the most of those vivid memories, we decided to dream together once again.




        Since then, three years have passed.

        And now, we’re living outside our dreams.


        01. HONG JOONG

        Each of them brought out their savings, gathering enough to rent the most affordable practice room to dance, sing in. In this world, their home world, the group-ATEEZ-was nobody, but when they looked in the mirror, their reflections reminded them of a time when they were nothing short of heroes in that other world. No, it was more like they were “drunk” on those memories of themselves. And just like the high of a good time drinking always fades when the morning comes, they were left to confront reality with a bad hangover. It takes money to dream, and with the need to work to make a living, their days spent gathered in the practice room became less and less. Even when they did gather, it was rare for all of the members to be present. But it’s not as though Hongjoong could blame them for being busy with work. All he could do to ease his disappointment was to greet them with a bittersweet, “That’s too bad. Let’s do what we have to do now and try again next time!” Everyone knows it’s impossible to live on dreams alone-acknowledging this hard truth is what it means to become an adult. All Hongjoong wanted was to maintain his relationship with the members, yet while he did his best to invite them out to eat for a quick get-together, even that wasn’t easy. Soon, even meeting once or twice a year began to feel like an accomplishment.


        During his free time, Hongjoong worked part-time, practiced on his own, and kept a diary. While writing his diary, he suddenly realized that his memories from World Z were beginning to fade. And so, he decided to record his and the other members’ experiences on his personal blog. Inspired by comments like, “Is this a new novel? I’m dying to read what comes next!” what began as Hongjoong‘s travel diary, evolved into a detailed story akin to an epic Science Fiction tale. His blog readers increased exponentially as the story progressed, and it wasn’t long before he was approached by a publisher. Hongjoong’s story was published as a book, which went on to become a best seller, and soon his days were filled with reader meet and greets, special lectures, and appearances on various TV programs.


        As Hongjoong gained recognition as a popular writer among young readers through TV and social media, his backstory of how he originally dreamed of becoming an idol to use his fame and find his long-lost family became well known too. And it just so happened, Hongjoong’s newfound fame did reunite him with not one, but two, long-lost family members: his father, who contacted him after seeing him by chance on a TV show, and his mother who looked up videos on the author after reading his book. At long last, his dreams of reuniting with his family came true. Good fortune and a reunited family, a career that he could be proud of, and fame. Hongjoong had clearly achieved all that he had ever dreamed of. He was blessed.


        Only when he left the room, sure that the door was completely shut behind him, did his smile slip and a deep sigh unintentionally sweep out of him. The sigh was so loud that it shocked even Hongjoong himself, “Is this what I truly wanted?”


        02. Seong Hwa

        "My daughter’s crazy about that book, so I gave it a read too, but who in their right mind would put up with 40 years of school just to be a Guardian? The whole thing sounds a bit absurd, don’t you think?” The fire chief said, glancing at the copy of Hongjoong‘s novel on Seonghwa’s desk. Looking at the chiefs expression-he was clearly fishing for Seonghwa’s agreement-but Seonghwa didn’t quite know how to respond. 


        If he answered honestly, with something like, “It might sound absurd to you, but my friends and I were actually there. We saw an experienced it all, in person”, the chief would think he was out of his mind. As Seonghwa was mulling over the best way to retort, the dispatch bell rang.


        For a long time, the memories of all the people Seonghwa failed to save in World Z haunted him. Even if the boy and the boy’s brother willingly joined ATEEZ’s cause, their deaths, along with those of the Black Pirates and the Thunder members who lost their lives to the Guardians’ attacks, as well as the corpses of the Sense Offenders that hung as a warning in the square, remained burned as an after image in his eyes. Each time he saw a similar face or silhouette walking down the street his heart would break again. And every time that happened, Seonghwa remembered her: The girl who left behind the Be Free bracelet and disappeared, the leader of Thunder. What would she have done?


        Knowing her, she would have told him to move and find a way to save himself first. Saving oneself is the first step in saving other people. “Fine. Then I’ll start by saving myself from this anxiety.” So, Seonghwa began studying how to rescue people in different kinds of crises. While studying, he came across material made for aspiring firefighters preparing for the firefighter exam. As practice time together with the members became less frequent, it was only natural for Seonghwa to take the test. For better or worse, he passed. Studying was easy enough-Seonghwa had always been systematic by nature and good at planning, and he made it through the Candidate Physical Ability Test easily thanks to his regular exercise and dancing regimes.


        That’s how Seonghwa became a firefighter. The hobby he began to calm his anxiety became his job. Sure, it wasn’t his dream, but that also wasn’t a good enough reason for him to give it up. The impact of his job was clear and real compared to the vague dreams he shared with the members, and he just couldn’t find any justification to quit. Fighting flames and rescuing people in crises was more rewarding than he had expected. It didn’t come with cheers and applause like performing on stage, but in their place, he was rewarded with the simple, heartfelt gratitude, and praise of those he saved, and their families. 


        And, thanks to his welcoming face and striking physique, Seonghwa was selected as the Fire and Disaster Headquarters’ yearly calendar model. Posing for the camera, he felt both pleasantly nervous and oddly empty. For so long, he had wanted nothing more than to be photographed and seen, but could never make that dream come true… How ironic that he could do so now, but only as a firefighter. 


        That day, Seonghwa returned to his office at the fire department and read HongJong’s novel that had been sitting on his desk.


        03. Yun Ho

        People gathered around the campfire, listening to Yunho’s singing and the sound of his guitar. With their eyes closed, they savored the melody. “The lyrics of Yunho’s song reminds me of a novel I read recently,” remarked one of the students. Behind the professors and students settled near the fire, a sandstorm raged. 

        Yunho was currently in Egypt.


        At first, Yunho tried his best to attend whenever the members gathered, but he realized early on that it wouldn’t be easy to keep up with their regular meetings. In World Z, they were heroes. That world may have been full of just as many struggles and hardships, but the shared goals were specific, and the enemy was clear-cut. But as for World A, this world here… there was still hardship, but the source of that hardship was elusive and unclear. Uncertain who the real enemy was, at times it felt like the whole world was against them, yet other times it did not. Yunho practiced hard, auditioned, and busked, but as the days went on, he began to see this world as even colder than World Z. People stared at the phones in their hands with apathetic expressions, quickly moving from video to video, always on the hunt for some new and fast stimuli. The human sounds of laughter and crying could only be heard from the other side of those screens. They danced intensely to their music loudly blasting from a speaker, but the people passing by barely spared them a glance before turning back to their phones. The members were taken aback. Had the passerby stared at them without emotion, like the people of World Z, it would have further ignited their passion. But they didn’t know how to react to these people who would stop and watch for only a second or take a short video without listening to their song through to the end.  No, to be honest, it hurt. It’s usually like that though. The higher you’ve climbed, the more painful the fall. 


        Never having experience such pain before, none of the members were able to recognize it as such, leaving them to bear their scars alone. Overtime, Yunho found that he enjoyed singing and dancing with the members less and less. Perhaps the other members felt this way too, but there was no way for him to know.


        As the number of times they talked about their dreams began to decrease and the period between gatherings in their practice room gradually grew longer, Yunho’s interest naturally began to change. By chance, he came across the Cromer, something he had thought only existed in World Z, at an exhibition on the Mayans civilization in World A. He was at once fascinated by these mysterious relics and remains. Seeing them, Yunho was sure there were even more relics and secrets somewhere out there, still waiting to be discovered. 


        As you know, stepped into the ancient pyramid, his thoughts ran wild. Maybe, just maybe, if he could find more other worldly artifacts, he would be able to travel to another world and go on an adventure with the members once again.


        04. Yeo Sang

        His employees call him, Young and Rich, Tall and Handsome. Yeosang, who built his fortune investing in stock, was finally able to start a business of his own without his father‘s help. Though he didn’t want to admit it, his natural ability to read the flow of money reminded him of his father. The small start-up he generously invested in grew into a unicorn, and through his careful investment skills, he was able to transform the small, one-man business into a large scale operation in just three years. 


        “So you majored in classical music, and that’s what eventually sparked your interest in pop music, but I’m curious as to what lead you down this path. Was there any specific event that inspired you?” a Business Globe reporter asked YeoSang. “I realized that while blindness is both enchanting and noble, there are times it becomes a trap,” Yeosang answered vaguely before falling into thought.


        After returning to this world, Yeosang could feel that the members had subtly, but definitely, changed. It was almost like finally realizing it was time to let go after blindly clinging to a one-sided love for so long. Before meeting the men in the black fedoras – before leaving for World Z – they were boys, and now they’ve come out the other side of the tunnel as adults. Only when he was able to see how the members had changed, did Yeosang realize he too had grown.


        Until now, their hard work and efforts toward their dreams felt noble because they blindly excepted those dreams as if they were divine missions entrusted to them alone. It felt like those dreams were the only right path. Therefore, living for anything other than those dreams seemed cowardly and shameful, like excepting defeat, and that is exactly how the members felt before leaving for World Z. They were caught in the trap of blindness.


        However, while in World Z, they came to learn just how precious emotions, art, dreams, and hopes all are, and at the same time, just how terrible blind belief can be. Upon returning to this world, the members agreed to continue pursuing their dreams as they always had, each of them holding the seed of new and diverse possibilities in their hearts. Yeosang knew this and believed that the members, consciously or not, must’ve felt the same.


        While money might seem contrary to art, art would not exist without money. Historically, art was created for the enjoyment of nobles and aristocrats, and in protest of this truth, even more forms of art were born. Money was the group‘s biggest obstacle in achieving their shared dream, and Yeosang decided to tackle it head-on. In only a short time, he reinvented himself as a leader of the investment world. While he focused on sure profits for the most part, occasionally he would invest in the arts, even if he risk losing money. One of those investments was Hongjoong’s novel. 


        05. San

        "Growing up moving from place to place, I always dreamed of picking a spot and setting down roots for myself somewhere. But thinking back on it now, I think drifting may have been written in my life fortune right from the start.” San said to himself, amid the salty wind of Jeju. The fixtures in the food truck rattled as if they were clapping back at San’s words. His tanned skin showed just how long he’d wandered about. 


        As he watched the members go their separate ways one by one, San could neither hold them back nor storm out and leave them. He had nowhere else to go. One day, after a lackluster practice- with more than half the members absent as they were too busy with their own lives- San found himself strolling down the alleyway, guided by his empty heart. He sat down on a small bench in front of a discreet old mom-and-pop corner store and cracked open a can of beer. “What do you call that feeling when you’re not quite sad, but not quite happy? When you’re sad but feel like your misery is almost laughable?” As he muttered to himself out of habit, he heard a voice from beside him. “What’s a youngster like yourself doing out here? It’s not even night yet.” It was the old man from the snack stall across the street. Instinctively, San asked him, “Hey Mister, was it always your dream to run a snack stall?” The old man seemed to get mad, retorting, “Dreams? Gah, you do what you can to put food on the table.” San asked again, “Do you think I can get by living without making my dreams come true?” The old man’s eyes met with San’s. “Dreams ain’t bad, but there are lots of other, more important, things in life. Sharing love, eating together, and cleaning up your own messes. Make sure you throw everything away right when you’re done.” At this, San noticed the black bag the old man had thrown at him earlier. Inside the bag were a steamy fresh sun-dae and a roll of kimbap. The sight of a young man drinking beer on an empty stomach must have worried him. 


        Taking a bite of sun-dae, San began talking to himself again. He decided that he wanted to know more about those other important things in life: “Sharing love, eating together… cleaning up your own messes.” So, San started a food truck. As he wandered around, he saw people eat together and share delicious food with those they loved. And sometimes, San even ate and talked with them, too. He met a wide variety of people - dreamers, dream seekers, those whose dreams had changed or come true, those living outside their dreams, and people with no dreams at all… That is how he came to learn the truth, the truth that most live their lives without ever achieving their dreams. “So why didn’t anyone ever teach us how to live outside of our dreams?” San thought. And he came to an answer of his own. Maybe I need to learn to welcome the reality I’ve been given even if it’s not the reality I wanted. 


        06. Min Gi

        People say, in this day and age, it’s impossible to make it big unless you’re born into good fortune from the start, but MinGi proved them wrong. On his way to the practice room, he got cast on the street by a high-end designer, and in no time had made his debut in a fashion magazine as a professional model. MinGi, who was in a tough spot at the time, thought of it only as a lucrative part-time job, but that very magazine spread quickly caught the attention of famous brands and turned him into an in-demand model. He learned to walk the runway as easily as if it were a new dance. Soon he was walking for top brand fashion shows, decorating the cover of one of the world’s four major fashion magazines, and working as an official ambassador for the global brand that called him their muses. The streets were filled with ads and videos featuring MinGi as their model. 


        As his van ran down the road decorated with his pictures - MinGi holding a hamburger, MinGi modeling cosmetics, MinGi in the trendiest new clothes - MinGi was once again preoccupied with his social media accounts. He was uploading the photo he had just taken in Garosu-gil as he moved on to his next schedule. By the time the fashion world had started to pay attention to MinGi, his OOTD looks were already popular on social media. His photos and unique styling that made inexpensive outfits look like luxury goods were popular amount men as date outfit inspiration, and among women as candid-cool boyfriend shots. MinGi had built a reputation for himself as an influencer. With each social media update came thousands, millions of likes and silly comments such as, ‘You’re so cool!,’ ‘Do you guys know what MinGi’s MBTI is? I.C.O.N.’ Just then, another notification popped up among the rest: he’d just been paid the advertisement fee for last month’s shoot. Even at a glance, he could tell it was a huge amount of money. MinGi was now so rich that his past struggles with poverty seemed like another lifetime ago. Above all, MinGi was glad that he didn’t have to worry about his grandmother’s hospital bills anymore. He might not be an idol, but being an icon like this was good enough for him. 


        MinGi realized just how narrow-minded and limited his view of the world had been. “Yeah, things are good now,” he muttered to himself, gazing out the van window. He gaze was drawn to a group of boys busking on the street outside. The boys, who danced and sang clumsily but passionately, met each other’s eyes and laughed with each changing movement. MinGi was hypnotized by the group and stared at them blankly. As the red light turned to green and the car started again, the boys faded away into the distance. At that time, MinGi was overcome with the sense that he had crossed a river he could never cross again. 


        On the far side of that river were those times he had spent running recklessly, passionately toward his dreams, those times when it didn’t matter if anyone acknowledged him, and it was enough to simply have fun. Where MinGi stood now was a place where results and achievements trumped passion and spirit, a place where value could be bought and sold. While MinGi wondered if ‘this is what it must be like to become an adult,’ he couldn’t erase that vague feeling of longing. Just as he opened up his social media to distract himself, a video of HongJoong’s reunion with his family appeared on his feed. 


        07. Woo Young

        If you were to ask him why he chose to be a flight attendant of all things, WooYoung would answer this:


        A friend from my hometown once drunkenly said, “Is the stage really that special? 

        A teachers classroom could be their stage…The old man announcing sales at the 

        supermarket is on stage...So are the flight attendants giving presentations on 

        emergency life vests! Idols and actors aren’t the only ones giving performances on a 

        stage!” Those words stuck with me and before I knew it, 

        I had signed up for flight attendant training. 


        And, if you want to call him, insane, he would retort: ‘So what if I am?!’ in many ways, WooYoung wasn’t in his right mind at the time. All he knew was that he wanted a stage of his own, at that very moment. It didn’t matter where.


        Maybe it was some kind of post-travel side effect. Using the Cromer to fight Z and the Guardians, constantly moving around and performing, those days were days that filled them with a rush of dopamine and adrenaline. Of course, those performances came with hardship and were part of a greater revolution, but a performance is a performance, no matter what the cause. WooYoung’s jitters were always followed by a wave of excitement that shot energy through his nerves, so much so that he often found himself, wondering, ‘Was that really stage fright?’


        But returning to World A, that excitement disappeared, and a looming feeling of anxiety began to take its place. It was as if he had finished an immersive game, and now, turning the console off, had to return to reality. Though WooYoung and the members tried to do what they could, they would never be able to perform as they had as ATEEZ in World Z. Making a stage for themselves wasn’t so easy here. Just when WooYoung felt as though he’d never stand on stage again, his drunk friend offered him those words of comfort. 


        As someone who hates conflict and prefers to maintain peace, WooYoung was well suited to his job as a flight attendant. His calming, pleasant face matched his uniform perfectly, and he set passengers at ease as he welcomed them with an air of sophistication. While the plane prepares for takeoff, the flight attendants moved to their assigned positions and demonstrate how to wear seatbelts, respirators, and life jackets according to the announcement, but passengers rarely ever pay attention. To remedy this, WooYoung’s airline was planning a new style of announcement more like an event, and WooYoung volunteered to lead. In place of the usual announcement, and exciting melody played over the cabin speakers.  Passengers who had been sleeping or flipping through movies, turned and looked with interest at WooYoung and the crew standing in the aisleway. With practiced ease, WooYoung delivered the announcements, including the destination and flight time, through song, rap, and dance.  When the announcement was finished, the passengers broke out in applause. ‘Exactly! This is what I made for!’ WooYoung thought with a bright smile. WooYoung’s eyes were drawn to a few people in the crowd who cheered and clapped louder than the rest.


        It’s just so happened that YunHo and MinGi were on the exact same plane.


        08. Jong Ho

        While recording vocal guides as a part-time job, JonHo began studying songwriting and musical composition on his own and spent his days creating original songs. At first, he wrote songs that the members could record and practice together, but, as everyone got busy, it became harder and harder to work together as a group. For his convenience, JongHo began writing solo songs, and becoming an idol with the members no longer seemed feasible, he turned to the path of a singer-songwriter. JonHo had already given up one dream due to injury-his dream of being a basketball player. He couldn’t stand to lose another. 


        He had posted the songs he created on MusicCloud, when a major music label reached out, impressed with JongHo’s songs. ‘Will I finally be able to debut as a singer?’ JongHo was excited, but as it turned out, the label was interested in an old group song he had uploaded long ago-a song he had recorded with the members-and wanted him to write a track for their upcoming idol group. While it was a bittersweet win,  JongHo had no reason to refuse their offer. He would finally be able to make music his career and be recognized for his hard work. Whole JongHo started as a songwriter, it wasn’t long before he was entrusted with the roles of idol vocal coach and producer as well. He was neither an idol nor a singer-songwriter, but he was satisfied. He was working alongside idols and singer-songwriters and that was enough for him. He had found a way to continue working with music. While JongHo was no longer the one standing in the spotlight, he was willing to become the deep darkness that made those on stage shine even brighter. 


        One day, while recording with a second-year idol group, an argument broke out. What started with one member complaining, “I’m tired. I can’t do this anymore,” soon escalated into a full-fledged fight despite JongHo’s best efforts to de-escalate the situation.  “Hey! If you were just going to give up on your dream like this, you shouldn’t have started in the first place!” Another member yelled. This riled up the first boy even more, and he grabbed the member by the collar, spitting back, “What do you know? We might be stuck together every day, but don’t act like you know me!”  JongHo stepped in and split up the boys before the fight turned physical, giving them each time to calm down. The boy who had complained burst into tears and cried, “I can’t tell you everything but, my family is going through a really hard time right now, and being away from them like this hurts so much.”  JongHo did his best to comfort and sympathize with the distressed boy.


        He was reminded of a time long ago when MinGi had threatened to quit, JongHo had gotten so mad that he had punched him in return. ‘I was so young and selfish back then,’ JongHo thought to himself. ‘How is everyone?’ JongHo recalled the other members. Sitting in the empty recording studio, he played that old group song and raise the volume. The sound of the members voices pierced through his heart. 

        <p style="font-size: 2.0em; text-align: center;"><strong>Golden Hour Pt.2</strong></p>     

        "Hey, I've been meaning to ask you - What's that thing you have stuck on 

        there?"


        A female student, stuffing a piece of buldak kimbap in her mouth, questioned.


        "Is it the food truck's motto? Or your's, oppa?"

        "Don't call the store owner 'oppa!' Have some respect! I apologize for my 	

        daughter, sir."

        "Please, I call all handsome men oppa. And maybe you just came here for 

        the first time today, Mom, but I'm a regular. Oppa and I are very close."


        The mother, embarrassed by her daughter's shamelessness, smiled awkwardly as she met San's eyes. He was busy gathering bite-sized pieces of bulgogi kimbap into a bowl.


        San			"It's something the owner of some snack stall told me three years or so ago 

        when I was worried that my dreams might not come true. Dreams are fine 

        and all, but there are many other, more important things in life."


        "Like...sharing love, eating together...and cleaning up your own mess."


        As if pondering the meaning of what San just said, the female student read the memo aloud. For the first time in a long while, San also looked at the old memo posted on the inside wall of his food truck. It was the first thing he stuck to its inner walls after buying the used truck three years ago, when the members, one by one, had started moving on their own paths. He started this food truck wanting to know if - like the owner of that stall said - a life outside of one's dreams was worth living.



        "So running a food truck like this wasn't your dream?"


        The female student asked.


        San			"If I'm being honest, not it wasn't. Not really."


        "Does that make you sad? That you're doing something other than your 

        dream?"


        The girl's mother tried to interject, but San just laughed, saying it was okay.


        San			"No, I like it. Of course, there are still times I miss those moments..."


        The girl spoke loudly as if to tell her mother to listen.


        "See! So you can live happily without achieving your dreams! My mom 

        always says you have to achieve your dreams, that a life without achieving 

        your dreams is a life wasted, and so I have to study! Always study, study, 

        study. Her nagging drives me crazy."

        "Enough, stop eating, and go to your after-school classes! Sorry for all the 

        trouble, sir. The food was great!"


        The mother, no longer able to hold back and wary of the ongoing conversation, finally stood up and urged her daughter away. San watched as the female student stuffed her cheeks full of the remaining kimbap, still chewing it as her mother dragged her away. He smiled.


        San 			"I used to think that, too."


        A new customer approached, and San greeted them with a friendly face. Seeing the expectant faces of hungry customers as they ordered, making food he hoped they'd enjoy, and watching them eat until they were full and happy - There's a kind of happiness in this too, San thought.




        Meanwhile, a plane bound for Incheon was getting ready to take off In Dubai. Woo Young, a second-year flight attendant, was busy preparing the special safety announcement he had put together for K Airlines. The airline, concerned that the passengers weren't paying enough attention to the flight attendants' in-flight safety announcement, planned a new event based on an Idea of Woo Young's in place of the usual simple demonstration.


        While he knew all he needed to do was match a few small movements to the announcement's song and rap, Woo Young's mouth had gone dry from nervousness - It had been a long time since he'd been on stage. He clenched his hands into a fist, stretched them slowly, and shook them out, but it did nothing to help calm his nerves. Taking a deep breath, Woo Young closed his eyes.


        He recalled those times - three years ago from now - when the members, dressed in black fedoras, would perform as they used the Cromer to disappear and reappear in and out of space. It was a time when his stage fright had felt like a distant memory from a past life. Yes, he had acted with a sense of duty, wanting to save the people from Z's control, but it was more then that. Those dreams of his that were out of grasp in World A, were achievable in World Z. There, the world was his stage, and each and every performance was thrilling. The performances of Woo Young and the members reminded the people, whose emotions had been suppressed and controlled, of the feelings they had lost. Their reactions, full of laughter and tears, had ignited Woo Young's heart. 


        Z, backed into a corner, broke the Cromer in his attempt to flee, and, as a result, Woo Young and the members were thrown back into this world before they could see the climax of their movement. But it was fine. If he could do all that there, there was nothing he couldn't do here, too, Woo Young had a thought. The members came together again and prepared as a performance group. Jong Ho, who was studying music composition, wrote their songs, and Hong Joong and Min Gi came up with the lyrics. Woo Young and Yun Ho put together the choreography. Yeo Sang, who - thanks to his Investments - had the most money to spare, set up their performance room, and Seong Hwa and San oversaw the planning and marketing. Through busking and performances at small, local events, they did their best to make even one fan.


        But that was the extent of it. And as days without progress dragged on, the members' motivation slowly began to fade. Their dreams didn't, in fact, lead to any real jobs. Like a long-dead romance waiting for one side to finally let go, their days dragged on in a state of arrested development, and the members' worries only grew. We used to fly high as ATEEZ in World Z, but had fallen into obscurity in this place. It was impossible to stop the members, who urgently needed money to get by, from leaving to look for a part-time job and earn a living. Though no one said it out loud, they all felt that the days when they could persuade each other with the mere promise of their shared ream would soon pass. Back then, whenever he went out to drink with friends from his hometown, Woo Young would whine over and over about how he wanted to be on stage. Then one time, his friend drunkenly shot back:


        "Is the stage really that special? A teacher's classroom could be their stage... 

        The old man announcing sales at the supermarket is on stage...So are the 

        flight attendants giving presentations on emergency life vests! Idols and 

        actors aren't the only ones giving performances on a stage!"


        Woo Young, thinking this was just his friend's way of shutting him up, disregarded the comment. But his friend when on:


        "If you miss performing that much, then stop whining about it and do 	

        something! Go find your own stage!"


        Fueled by his friend's call for him to take action, Woo Young's blood boiled and a strange courage overcame him. "That's right! I'll go find my own stage!" The friends cheered together and, before he knew it, Woo Young had signed up for flight attendant training.


        Not wanting to waste the money he had spent of FA training classes, Woo Young began attending the flight attendant academy. To his surprise, he was praised for his talent and soon found himself enjoying training. He was proud that the other students applauded him and the school held him up as an example. Yes, maybe it was praise that Woo Young had wanted. Driven by praise and recognition, Woo Young became a full-fledged flight attendant in record time. It wasn't until after this thirst for acknowledgement had been quenched that he remembered what it was that he really wanted to do: music. It wasn't performing on a stage, but music that he wanted to do. To match his voice and movements to instruments, for someone to listen to his story. But when he finally looked back, he was already an established flight attendant. And so, Woo Young recalled his friend's words again: "Find the stage. Find your own stage..." Make it for yourself..."


        At that time, K Airlines was in the process of planning a new format for their in-flight safety announcement, and Woo Young sent in a proposal for the project. He suggested a music-based performance, and his idea was adopted. 


        "Woo Young, we're just about ready to run the announcement."


        At the words of his fellow flight attendant, Woo Young opened his eyes. It might not be much, but it was still a stage - the stage Woo Young had longed for. This shaking feeling he was experiencing now was the very feeling he had missed so much. There was nothing to be afraid of. Woo Young stood In the aisle.


        Woo Young 	"We're about to take off. In preparation for departure, please direct your 

        attention to the flight attendants in the cabins they go over our safety 

        procedures." 


        Woo Young's announcement rang over the pre-recorded music playing from the in-flight speakers. Soon, the beat began to change and the announcement transformed into a rap and melody. Passengers who had been dozing off or scrolling through the selection of in-flight movies, and children who had been whining to their parents, all turned to look at Woo Young.


        Information on seat belts, life jackets, oxygen masks, and emergency exits was delivered through witty lyrics, and the communicative performance immediately drew the attention of the audience - the flight's passengers. Even those who had laughed out of awkwardness at first, soon joined in on the fun of the performance. Some even stood up from their seats, swayed their shoulders, and clapped. The youngest audience enjoyed the performance the most, as they stopped their crying and laughed along. Some passengers even filmed the performance on their personal smartphones. 


        Woo Young, who felt like he hadn't performed before an audience in so long, ended the in-flight safety performance by disappearing and reappearing in an instant like he used to in World Z - Of course, without the Cromer it was just a simple trick of diversion planned with a fellow flight attendant. 


        After a moment of silence, the cabin burst into thunderous applause and cheers. All around, passengers shouted praise at Woo Young, saying, "This is the best announcement I've ever seen!" or "I'm so glad I got to start my vacation with you!" and "I was sad about my holiday being over, but you made me feel so much better!" Woo Young, who was busy thanking - and calming - the passengers who were now more excited than he was, stopped in front of two familiar faces. 


        Yun Ho		"Hey, is it really okay for a safety announcement to be this cool?"

        Min Gi		" I know. I fell for him and nearly asked for his number."


        It was Yun Ho and Min Gi.


        The K Airlines flight crossed the night sky and the bright lights of the cabin dimmed. Passengers, tired from the long flight, began to fall asleep. Aside from the noise of a few odd people going to and from the restroom, the cabin was quiet. The three men gathered in one corner in hushed excitement.


        Woo Young	"Huh. What're the odds?"

        Min Gi		"I was supposed to take an earlier flight home after the fashion show in 

        Dubai, but it was overbooked. I needed to get back for our appointment 

        tomorrow, and this was the next best flight I could get."

        Woo Young	"And there were only economy seats left? What if someone recognizes you!"

        Min Gi		"I was worried about that too, but this was the last one open before the 

        weekend. Still, it worked out. Right? I get to see you and Yun Ho!"


        Even though they were in the galley, where only flight attendants came and went, Min Gi covered his face with his hat and stayed alert for prying eyes. Within just three years, Min Gi had become the hottest model and influencer in the world. 


        Back when the members were still practicing together, Min Gi, who needed money for his grandmother's hospital bills and family's living expenses, began taking on a number of odd jobs. On his way to the practice room, Min Gi was cast on the street by a high-end designer - the brand was still in its start-up stage at the time - who was looking for a new face to model for them. Min Gi was selected to star in a pictorial introducing the brand's new collection.


        That season's outfits and pictorials became a hot topic in the fashion world online, so much so that Min Gi was even featured on the cover of one of the world's top fashion magazines. He was hailed as a muse to global brands and was chosen to finish their collections' runway shows - though he had no experience walking whatsoever. As the saying goes: Those who can, do. Those who can do it looking good? Well, they go on to rule the world. A YouTuber with over 1 million subscribers posted Min Gi's photos on their personal SNS as an example of their ideal boyfriend's style, and it soon ignited a heated social debate on the use of private images without permission. Like this, Min Gi's pictures naturally gained exposure, and, as the original controversy surrounding them disappeared, he evolved into a famous figure associated in the public mid with the so-called "boyfriend shot."


        Yun Ho		"After the conference in Egypt, I was on my way back to Korea via 

        Dubai. When I saw it was a K Airlines flight, I thought of contacting you, Woo 

        Young, but who knew we'd end up meeting like this! And Min Gi, too."


        Yun Ho had started studying again and went on to college, and the Cromer was the reason why. Once he'd learned that the Cromer - something he'd thought could only be found in the mystical World Z - existed here, as well, he became fascinated with relics, ancient ruins, legends, and myths. "There must be more relics out there, just like the Cromer, that can't be explained by our world's history, theory, and research alone," Yun Ho had said. 


        Woo Young was reminded of a conversation he had one day walking with Yun Ho. If this world is really made up of multiple dimensions, just as the men in the black fedoras had told them, then there must be more relics and artifacts out there that only those who know of World Z can recognize. 


        "Does he want to go back to world Z? Now that the Cromer's broken, is he 

        looking for some other key that will lead him back?"


        Woo Young wanted to ask Yun Ho a lot of questions, but chose to cheer him on instead. Entering the archaeological department must have been hectic enough for him already. 


        Yun Ho		"By the way, you were really cool back there. It reminded me of when we 

        used to perform together as ATEEZ."

        Min Gi		"I filmed it all on my phone, so let's all rewatch it together at Yeo Sang's 

        place tomorrow."

        Woo Young	"Hey, it's supposed to be Hong Joong's congratulatory party. Don't waste 

        time watching a video of me."

        Yun Ho		"Why not? I'm sure everyone will love it. We always end up just talking about 

        the past when we meet, anyway. If anything, I'm worried your video will get 

        everyone too fired up and they'll want to start dancing again."

        Min Gi		"He's not wrong, and you know what? Jong Ho's a producer now. Who 

        knows, he might just offer you a solo after watching it."

        Woo Young	"Cut it out. Stop messing with me"


        Min Gi smirked mischievously as if to say, "try me," and Woo Young responded with a look of fake hurt. Yun Ho watched them both and laughed. Though it'd been a year since they last met, and though they each now had their own busy lives, in front of each other they transformed into the same young boys they had always been. With silly jokes only they would ever get, they soothed their longing for each other that had long been locked away inside. 




        At the same time, in Seoul, South Korea. Cursing and shouting, not music, blasted out of a recording studio near Hongdae. 


        "If that's how you're gonna act, then get the h*ll out already! Stop dragging 

        us into your mess. Do you know how many idols disappear not even a year 

        after debuting? Even if we f*ing risk our lives for this job, who knows how 

        many people will ever actually care!"

        "No, that's not what I - For starters, I joined this company because I thought 

        they'd make me an actor. H*ll, like I knew I'd become an idol like this! 				Ha...Don't act like you know what I'm going through."


        The six-month-old group, for which Jong Ho worked as their exclusive producer, was preparing for their upcoming mini album. While in the studio recording songs, all the member's volatile emotions that had accumulated since their debut exploded into an argument, which raged on despite the best efforts of those around them to stop it. An engineer, who could not longer stand to watch the children fight in his recording booth, moved to stop them, but Jong Ho stepped in and held him back.


        Jong Ho		"It's better they let it all out now than hold it in and suffer in silence."


        It wouldn't be easy for family members to work together all day long - let alone young adults, teens who had barely just hit puberty, thrown together only because they share the same goal. Understanding Jong Ho's intentions, the engineer sat down again. And, unaware of the adults watching them, the children continued to fight. 


        "What?! If you don't want to be part of this, you should have told the 

        company before debuting! Let me guess, you didn't have the guts to start 

        out as an actor and thought you'd take the easy path to fame by debuting as 

        an idol first. If that's what you decided, then take responsibility for that 

        decision! You're an Idol now, so f*ing work to make your face known before 

        whining! You've only just started, and you're already like this?! What're you 

        going to do?" 


        "What do you think I am? Some kind of machine? I'm human too. I need time 

        to think through all my troubles and decisions. But, it's just work and 

        practice, work and practice every. single. day. I don't have time to think 

        about myself or make commitments. 

        Considering all that, can't I waiver or doubt things a little?"


        Jong Ho		"At this rate, I doubt we'll be able to finish recording today. There's still room 

        in the schedule, so let's try again some other time."


        The boys' argument showed no sign of slowing down and Jong Ho decided to postpone the recording. The engineer headed out of the studio first, offering Jong Ho a comment of support for his troubles on his way out.


        "And you think we aren't just as busy? What do you think the rest of us are 

        doing? Playing around?"

        "You've never liked me, even back when we were trainees. Is that why you're 

        acting like this to me?"

        "What?!"

        "You always listen to the other members whenever they complain about their 

        troubles. Whether it was family stuff, not being able to debut with friends 

        from their trainee days, or anything else."

        "...Seriously? How old are you?"


        Jong Ho		"That's enough. Everyone, get out here."


        Once the other members had all left for the dorms, the two boys sat in front of Jong Ho and cried. Jong Ho guessed they each had been holding on to their own struggles.


        One of the boys, having come from a difficult family background, was desperate to cling to his idol career - something he had worked so hard to achieve - and the opportunities it might bring. As desperate as he was, he was also probably anxious. And, the only way to relieve his worries in this industry where the future was both uncertain and out of his hands, was to work as hard as he possibly could. He must have hoped the other members would feel the same, and when confronted by his friend who didn't, could no longer hold back his own overflowing anxiety. Although Jong Ho didn't know everything the boy had been through, he did know the feeling of desperation born from anxiety. He had once exploded at Min Gi in a similar way.


        The other boy, who dreamed of becoming an actor, must have stumbled across the path of an idol on the way to his real dream. While he may have started this career hoping that, as his face became more well known, it would eventually lead to opportunities in acting, he was probably taken aback by the reality of this world that demands hard work paid in sweat and tears. He was behind in singing and dancing compared to the other members, who dreamed of being idols, and he must have been worried about the choice he made. But, as busy as they were, it would have been hard to even bring up his concerns. Sure, one could criticize the boy for choosing the path of an idol when that was never his dream. But Jong Ho, who had become a music producer as a means to achieving another goal himself, was no different.


        As their crying died down, Jong Ho recalled these past three years. Inspired by the Grimes Siblings, Jong Ho began composing music little by little and when they returned to this world, he began studying it in earnest, hoping to make songs the members could sing together. While it was a little awkward, he enjoyed asking the members' opinions and modifying each song little by little. That magical moment, when the members' voices were paired with the melody he'd made, brought a sense of accomplishment he had not felt elsewhere. Even when the other members grew busy with their own lives, Jong Ho couldn't let go of music. Jong Ho had already been forced to give up his dream - basketball - once due to injury, and had worked so hard to find the new one. If he couldn't achieve it with the members, he would find a way to cling to it on his own, even as a singer-songwriter.


        That's how Jong Ho was eventually scouted by his current agency, who was so impressed by the songs he uploaded to MusicCould, that they asked if he could write a song for their upcoming idol group. While he was a bit disappointed they hadn't offered to sign him as a singer, he had no reason to refuse the offer. It was a way for him to continue his career in music, and, for the first time, his efforts had been recognize. Jong Ho, who started as a singer-songwriter, soon became the idol group's vocal coach and producer, as well.  He was neither an idol or a singer-songwriter, but he had hope that, as long as he never gave up on music, the chance would still present itself one day. For now, he spent his days satisfied with the opportunities given to him.


        Jong Ho		"From now on, how about we work out from time to time and try building up 

        our physical strength."


        The two children raised their heads and looked up at Jong Ho, confused.


        Jong Ho		"Neither of you wants to hurt the other, it's just that you have your problems,

        and you have yours. Am I right?"


        They nodded and, out of the corner of their eyes, scanned the face of the boy sitting next to them. As their irritation faded, fatigue, sadness, confusion, and guilt took its place.


        Jong Ho		"I heard that kindness also require stamina. You're both so tired that you're 

        overcome with anxiety and confusion. But it's thanks to all your hard work 

        that you were able to debut and were offered all these new opportunities, 

        too. I know it's impossible to really understand each other's struggles, but 

        let's at least try to be kind to each other. How about it?"


        The boys replied "yes" at the same time, and awkwardly handed each other tissues. "They're still just kids," Jong Ho thought as he smiled quietly. The two boys, who had fought so ferociously until just now, were smirking and exchanging friendly banter. Looking at them, Jong Ho couldn't help but he reminded of his own members. 


        He went to close his eyes for a moment, but fatigue washed over him and, before he knew it, it was 1 am. Jong Ho hurried to organize his computer files, and buried among those numerous files, one in particular caught his eye: It was his first song. Maybe it was the boy's fight, or that he was going to see his own members for the first time in a while tomorrow, but for some reason, that song - which he had not played even once since they split - called out to him today. "Should I try listening to it again?" Jong Ho hesitated for a moment before mustering up a little courage and playing that first song.


        Jong Ho		"Hmm...Yeah, I can't do this."


        Jong Ho shuddered at the melody which now seemed so unrefined from its very start. In his memory, it had been a pretty good song, but now he realized how much he had glamourized it. Unable to listen anymore, he went to turn the music off, but hesitated at Yeo Sang's soft voice. Then Woo Young's melodic voice followed and Jong Ho gave up on turning off the music. As Yeo Sang and Woo Young, Seong Hwa and Yun Ho, Min Gi and Hong Joong, San and Jong Ho's voices came and went, an image as clumsy as a colorful drawing unfolded in his mind. The members' voices pierced his heart. It felt as though, unknowingly, he had unleashed a certain long-gone and now unattainable past.


        Only then did Jong Ho realize that he had unwittingly ended one period of his life and started another. Listening to the music of a past he could never get back, he longed for those clumsy but oh-so-beautiful times, and shed a tear.


        It was then, RINGGG! A fire alarm went off and shook Jong Ho form his memories. "Wha - What's going on?!" Jong Ho faltered at the loud noise, and someone burst through the recording studio door. Standing in the open doorway was none other than Seong Hwa - outfitted in fire protective gear.


        Jong Ho		"Seong Hwa...?"

        Seong Hwa	"Can't you hear the alarm?! Hurry! We need to get out of here!"


        A stray cigarette butt had caught fire to a bag of garbage, which in turn spread to the vines that decorated the outer wall of the building. The fire grew and began eating away at the building's exterior. "Fortunately, a delivery man saw it all and immediately called 119. We were able to extinguish the fire before there was too much damage," Seong Hwa continued as he took off his red helmet.


        Seong Hwa	"Thankfully, the fire didn't spread too much, but had you stayed there you 

        might have been suffocated by the smoke. The next time you hear a fire 

        alarm go off, get out right away. There's nothing more important than your 

        life."

        Jong Ho		"Yes, yes, I get it. You're really a full-fledge firefighter now, huh?"


        Jong Ho smiled happily at Seong Hwa's nagging, which he hadn't heard in so long, and handed Seong Hwa a drink. Seong Hwa smiled back, as if he had missed these familiar interactions with the group's youngest member. Looking at Seong Hwa's soot-smudged face, Jong Ho asked.


        Jong Ho		" How's the firefighter job? Do you enjoy it?"


        Seong Hwa finished another sip of his drink and seemed to think for a moment, before replying with a smile:


        Seong Hwa	"It's great! Very rewarding. But more importantly, I get to save people. It's 

        really great."


        Jong Ho understood. He knew that the afterimage of all the people they couldn't save in World Z had long haunted Seong Hwa. The Boy and his Brother that they were unable to save at the Disposal Site. The many members of the Black Pirates and Thunder who had fought bravely alongside ATEEZ only to have their fates changed by the Guardians' attacks. The eyes of those Sense Offenders hung as an example in the square. Jong Ho remembered that the image of Seong Hwa's back, the other member frozen in place each and every time he encountered someone who reminded him of them.


        Seong Hwa	"Want me to tell you something interesting?"


        Jong Ho met his eyes slightly, as if to say that he was ready to listen, Seong Hwa began describing those who had just become firefighters. There is a time when a sense of duty and a desire to save people becomes a kind of "passion in and of itself. During this time, new firefighters - as if they have never known fear - would do anything to save even just one more person. They would dive into the heart of a fire or risk their lives. Then, they make a mistake and realize they might actually die like this. That's when they finally come to understand their seniors' advice, Seong Hwa continued.


        Seong Hwa grit his teeth and repeated the words he had heard over and over again as a student:


        Seong Hwa	"Saving oneself is the first step in saving other people. 

        Believe it or not, that's why I decided to become a firefighter. I thought that if 		

        I could just pull myself out of my own misery, I would be able to do anything."


        At first, he began studying how to rescue people in various crisis situations. Just learning how to react to various emergencies helped calm his anxiety. Then, while studying, he came across material made for aspiring firefighters preparing for the firefighter exam. The members were meeting to practice together less and less, and making use of his new-found free time, Seong Hwa decided to take the test himself. The hobby he began to calm his anxiety, soon became his job. He found its specific demands and tasks were more comforting than vague dreams. And while it didn't come with cheers and applause like performing on stage, in their place, he was rewarded with the simple, heartfelt gratitude of those he'd saved and their families. 


        Jong Ho		"That's good to hear."


        Jong Ho meant that sincerely. He looked at Seong Hwa's face in the clear light. Seong Hwa stared back at Jong Ho in the same manner. Jong Ho, the baby of the group, suddenly looked all grown up. "Even Jong Ho's an adult now. It's strange. It makes me feel proud, but also sorry." Seong Hwa thought quietly to himself.


        Jong Ho		"You're coming tomorrow, right?"

        Seong Hwa	"Nope."

        Jong Ho		"Wait, really? Why can't you come? This'll be our first time getting together in 

        nearly a year."

        Seong Hwa	"It's already past midnight. So yeah, I won't be going tomorrow, but I'll be 

        sure to make the party today. It's Hong Joong's party - there's no way I'd 

        miss it."

        Jong Ho		"Oh, come on!"


        In Jong Ho's face, now annoyed at the older boy's mischief, was the echo of the maknae Seong Hwa knew. Only then did Seong Hwa put his arm around Jong Ho's shoulders and ruffle his hair, as if happy to finally reunite with the group's youngest.




        In an antique villa, far removed from the city center and hidden by lush trees tinted by the pink light of golden hour, laughter echoed about. Inside the villa dining room, eight men dressed comfortably sat around a large table decorated with all kinds of dishes from land and sea. Eight wine glasses collided in the air.


        Yeo Sang		"I really put a lot of thought into this menu for you guys, but all you've been 

        eating is San's stuff, I'm hurt."

        San			"That's bold coming from the guy who just swiped another piece of my 

        kimbap."

        Yeo Sang		"Well, you know. You can't beat this kind of nostalgic flavor."

        Woo Young	"Come on guys, let's try one of the other dishes before Mr. Fancy Villa Owner 

        gets upset."

        Hong Joong	"How did you manage to look this sexy on a plane? I thought I was watching 

        a performance of Britney Spears' Toxic or something."

        Woo Young	"Hey! I thought I told you guys not to show them that!"


        Min Gi and Yun Ho, shrugging in fake remorse, explained how they had no choice but to show the others Woo Young's video, which had already begun spreading on social media. Woo Young's ears were red with embarrassment, but he looked through the video's comments in high spirits, and San took the opportunity to tease Woo Young again. Hong Joong, who had been watching the members with a smile, suddenly remembered the books in his bag and hurriedly took them out. He passed a copy to each of the members, who had flipped through them with thrill. On the first page was a simple letter with Hong Joong's handwritten signature.


        Yun Ho		"So book no. 2 is finally out! Congrats, Hong Joong! You did great!"

        Min Gi		"I heard you were already offered licensing deals in 30 countries or 

        something? I saw it in an article."

        Hong Joong	"It's all thanks to you guys. If anything I'm sorry. It's our story, but I'm the only 

        one making money off of it all."

        Jong Ho		"What're you saying? You're the only one of us who'd ever be able to retell it 

        all in such an exciting way like this."


        The others nodded in agreement. For no reason in particular, Hong Joong touched the cover of his book. On the cover was an image of Z's office, with Z and the Guardians on the right, and the Thunder members and Prestige Academy students on the left. In front were eight men wearing black fedoras, engraving with the name ATEEZ. That's right - Hong Joong's novel was based on their real adventures. In short: it was his and the member's travel diary.


        One day, after returning to this world, Hong Joong suddenly realized that his memories from World Z were beginning to fade. Perhaps that's what it meant to live in the present. What were once vibrant and colorful memories, would soon be condensed into a single color and simplified as "good past times." And so, Hong Joong began writing. He wanted to retain those magical moments that he could never visit again as vibrant memories. His diary, a blog, was soon filled with comments like, "Is this a new novel? I'm dying to read what comes next!"


        For the fist time, Hong Joong began to consider how the series of events he had experienced with members might seem to others. "Most people would probably assume this is a science fiction or fantasy novel, not a travelog." What began as Hong Joong's diary, evolved into a detailed story akin to an epic novel, and his blog readers increased exponentially as the story progressed. It wasn't long before he was approached by a publisher, and his story was printed as a novel, which went on to become a bestseller. Before he knew it, Hong Joong built a name for himself as a famous writer beloved by young readers.


        His days were filled with reader meet and greets, special lectures, and appearances on various TV programs. On a talk show that introduced writer's personal lives, Hong Joong said, "I originally dreamed of becoming an idol, hoping vaguely that, if I became famous enough to appear on TV, I might meet my long-lost family again. But I never imagined that this would all happen to me as a writer." His sincere story - and the dance he showed off at the request of the host - became a hot topic. Hong Joong's father, who happened to watch the show, and his mother, who learned about him through his novel, reached out to him. At long last, his dream of reuniting with his family finally came true.


        Hong Joong	"My mom is so into Min Gi these days. She even follows you on social 

        media."

        Min Gi		"Really? Do you want me to surprise her with a video call or something? I'd 

        be more than happy to."

        Seong Hwa	"In that case, would you mind calling my fire department chief, as well? Ever 

        since he found out we're close, he's been too nice to me."


        The members burst into laughter seeing Hong Joong's mother fangirling over Min Gi on the phone. Seong Hwa tried to contact the department chief for a video call with Min Gi, as well, but, busy as ever, he didn't answer his phone. Min Gi left a little video greeting for him instead.


        San			"I saw so many ads with Min Gi on my way here today. He's everywhere! Do 

        you know what it made me think of?"

        Jong Ho		"What?"

        San			"It's so over the top, it almost reminds me of Z."


        Jong Ho, looking around Yeo Sang's villa, laughed at San's joke. It was an inside joke that only made sense to those familiar with World Z and the nature of Z's rule. It also meant that Min Gi's star power was so great that it was akin to brainwashing. 


        The dining room let out into a short hallway that connected to the living room. Beyond a large window framed by curtains was a dark, blue night. Next to the window, in an antique cabinet, a familiar frame and broken glass object caught Woo Young's eyes.


        Woo Young 	"Hey, isn't this the Cromer?"


        The remaining pieces of the broken Cromer, which Yeo Sang had taken back with him, had reconstructed decently well. It looked almost like a piece of modern art. When the Cromer shattered and the members were forced back to this world, Woo Young had thought Yeo Sang odd for picking up its useless broken pieces. Now, Woo Young felt as though he were the odd one.


        Yun Ho		"Huh? Wait, I think I recognize that. It's that thing Left Eye gave us!"


        Yun Ho cried out, looking at a ruby-colored stone in a compartment next to the Cromer.


        Jong Ho		"It's that thing! That - He gave it to us saying it was something thrown away 

        at the Strickland Disposal Site along with the voices of the Grime Siblings."

        San			"Yeo Sang, you mean you took this without telling the rest of us?"

        Yeo Sang		"What're you talking about? I asked you over and over which one of us 

        should take it."


        Everyone was shocked  by Yeo Sang's sudden remarks. Yeo Sang continued, "I asked you all again and again in both World Z and World A, but either you weren't listening or changed the subject on me. I had no choice but to bring it back myself." When the members questioned "When? When did you ask us?" Yeo Sang replied:


        Yeo Sang		"Don't you remember me asking you all 'What should we do with Sopro?"

        [Sopro, Portuguese for 'breath,' 'a gust of air.']

        Woo Young	"Sopro?"


        At that, the members finally recalled Yeo Sang asking them, "Who's going to take care of Sopro?" "What about Sopro?" "Guys, Sopro..." None of them knew at the time that he was referring to this ruby stone, and they all had brushed him off. Now feeling bad, the members touched Sopro aimlessly and changed the subject.


        San 			"You know, Yeo Sang, your villa really is huge. It's so nice! You can really tell 

        you make a lot of money."

        Seong Hwa	"I know. You've got enough room to play soccer in here."


        The members chided Seong Hwa for his old man-like comment, and looked around the living room.


        In just three years, Yeo Sang had become the definitions of Young and Rich, Tall and Handsome. Having built his fortune investing in stocks, Yeo Sang was finally able to start a business of his own without his father's help. The start-up he generously invested in grew into a unicorn, and through his careful investment skills, he was able to transform the small, one-man business into a large-scale operation. Though he didn't want to admit it, his natural ability to read the flow of money reminded him of his father. While money might seem contrary to art, art would not exist without money. Historically, art was created for the enjoyment of nobles and aristocrats, and in protest of this truth, even more kinds of art were born. Money was the group's biggest obstacle in achieving their dream, and Yeo Sang decided to tackle it head-on. He reinvented himself as a leader of the investment world.


        The members, who had naturally moved to the living room, shared stories with each other, drank wine, and drunkenly reminisced about their times in World Z, their memories spread out on the table before them. Their uncensored true faces, which had grown used to hiding behind their masks as refined members of society, burst out wildly. The members were as excited as if they had just moved through space with the Cromer - as if they'd gone back to their days as the men in the Black Fedoras.


        Yeo Sang		"Do you guys remember that time? Back during our performance at Prestige 

        Academy, when Min Gi missed the beat and his colored smoke bomb went 

        off first?"

        San			"Yeah. I was worried that I was the one who messed up our rhythm."

        Hong Joong	"To be honest, I was worried that we wouldn't be able to make it home. I kept 

        thinking, what if one of us got injured or something happened...Everything 

        seemed so hard at the time, but looking back on it now - things were good 

        back then."

        Woo Young	"I know, I remember that first time I got injured and how the Grimes Siblings 

        helped me. The first time we met Left Eye...I almost even miss the Guardians 

        now."

        San			"I hope Thunder's doing okay. It's a shame we never got a change to say 

        goodbye."

        Yun Ho		"I wonder what happened after we left. Were the people finally able to break 

        free of control, did the rebellion succeed...Do they still remember ATEEZ? Or, 

        do you think we've already been forgotten?"

        Min Gi		"Maybe, you never know. Time keeps moving over there, too. We might 

        already have become a thing of the past. It's not like we spend all our time 

        thinking about ATEEZ either."

        Jong Ho		"Even if that's the case, it's still a little sad to think about."


        There was a moment of silence. Although they were all here in the same place, each member was immersed in their own thoughts. Music filled the room, breaking the silence. It was Jong Ho. He played a song from the music he had kept from their performances in World Z. Excitement filled the room again. Some members even started to dance, saying they remembered their choreography from back then. A few other songs played, and finally, the fist song Jong Ho had written for the members upon returning came on.


        This time, a different kind of silence came over the members. ATEEZ, who had been nothing short of heroes in World Z, had been thrown back into World A and forced to live as commoners again. Still, they had been so sure they could make it here, too. After all, just think of all they had accomplished in World Z! However, the lingering thrill of their adventures had faded faster than they had hoped. This song was one they sang together at the very end of that time. They hadn't understood just how much they had changed before and after leaving World Z, but now they all did.


        Woo Young 	"Why don't we give it one last try?"


        Woo Young blurted out the thoughts no other member had the courage to speak, not even as a joke. Sipping his drink by himself and listening to music, he looked very drunk. Hong Joong responded as if to soothe him:


        Hong Joong	"Ahahaha, yeah, that might be fun. You know, a reader actually said the 

        same thing at a book concert of mine a while back. They said they'd heard 

        us perform at a local event a long time ago. They were a fan. It kind of made 

        me sad to hear that."

        Yun Ho		"You know, Yeo Sang makes a lot of investments in the arts. He could 

        probably handle our production. And Jong Ho can make our songs. And 

        Min Gi will be our center?"


        "It's so nice getting together like this. We should really do It at least once a month. Hey, you know let's go on a trip together sometime!" The others tried to brush aside Woo Young's words with their usual drunken promises, but this time Jong Ho responded seriously:


        Jong Ho		"To be honest, I like the idea. I already have some songs written."

        Woo Young	"Looking back, I always wondered if we really did everything we could. At 

        first, we all had our own family problems, and because of that, we ended up 

        drifting apart before we ever really started. Then, the next time we got 

        together and tried and it didn't work out, we all gave up so easily and moved 

        on to our own jobs. Let's do it for real this time. Give it one last go. Doesn't it 

        bother you? To just accept defeat like this?"


        Woo Young thought he had been adjusting well to his life as a flight attendant. But when he danced and sang to the in-flight safety announcement, he realized that was not the case. He had been forcing himself to eat tofu, when what he really wanted was steak. Sure they were both proteins, but they were not the same. 


        Yeo Sang		I don't consider my current life to be 'defeat.'"

        Woo Young	"So, then, you think we've all achieved our dreams?"

        Yeo Sang 	"Let me put it this way: You think any life that doesn't follow your original 

        dream is a failure, then? Something to be ashamed of?"


        The members grew pale at the suddenly charged atmosphere of the conversation.


        Yeo Sang was frustrated with Woo Young, who clung blindly to his obsession with dreams. And while blindness is at times both enchanting and noble, there are other times when it becomes a trap. The reason why hard word and effort put towards one's dream feel so noble, is that dreams can often seem like a sort of divine mission - and many people blindly accept them as such.


        If you believe that the only way to live is to follow your dreams, it's only natural that anything else would feel frightening and shameful, like a failure. The sense of defeat the members felt before arriving in World Z, was that exactly - the trap of blindness. But what they learned in World Z was not that they could be heroes, but the importance of emotions and art, dreams, and hope. And that blind belief in anything leads to grave consequences. At least, that's how Yeo Sang saw it, and he had hoped the members felt the same.


        Yeo Sang		"Grow up. How long do you plan on acting so recklessly?"


        "Until we fail for good, I want to keep giving it my all" "We never really tried," "You're just running away, afraid to face the fact that we've fallen this far, and using the need to 'make a living' as an excuse." "Your real failure is being afraid to fail." Those words echoed in Woo Young's mind. But, Yeo Sang's cold and cynical retort shattered him before he was ever able to sort though his thoughts.


        Woo Young	"Maybe it's that you don't even have the courage to be reckless. But the 

        others might. Why are you getting in my way without even listening?"

        Yeo Sang		"Can't you tell?"


        Yeo Sang stood up from his seat as if to say, "Go ahead. Ask." Woo Young looked at the other members, believing that at least one of them would respond positively, "Let's try it again together." But each member only turned their eyes away from Woo Young's gaze. Woo Young felt like a fool.


        Jongh Ho	"Woo Young, I really did meant it. It want to...but let's organize our schedules 

        first and then..."

        Woo Young	"No, forget it. This was supposed to be a celebration, and I messed 

        everything up. I'm sorry, guys. I'm just a little drunk...I'll head out first..."


        Pressing back his tears, he kicked away his seat and stood up. The members rushed over to comfort Woo Young and his broken heart, but it was too late. Woo Young walked away quickly into the darkness.




        There were two hours left before the first train. Woo Young, forced to wait until then, shivered as he sat on the bench at the train station. "Ugh, why does he have to live so far out of the city." It was late spring, but the night was still cold. Woo Young regretted running out of Yeo Sang's villa so hastily. He debated buying some apology snacks at the convenience store and returning to the villa, but no matter how he thought about it, returning to Yeo Sang's house would only hurt his pride. 


        Woo Young	"Is being reckless a crime? There are so many reckless people in the world. 

        Like all the people who fall in love knowing they'll break up in the end. Does 

        he think they're all just immature fools? And why is recklessness immature?"


        He talked to himself and tried to calm his stormy heart. Yeo Sang's words were made even more painful by the other members' gazes. They seemed to imply: "We are not the same." It was as though he alone remained trapped in a long tunnel and the members looked back at him from the other side, as if saying, "Why are you still there?"


        Woo Young	"Since when did they all become so spineless? Their passion, spirit...where 

        did it all go?"


        Woo Young tilted his head back and looked up at the night. Even in the murky sky, starts shone. "Could one of those lights be World Z?" As he thought that, a reddish star appeared, twinkling through the clouds.


        Woo Young	"Sopro."


        Woo Young unconsciously was reminded of the ruby-colored stone. The stone that sat in the living room cabinet of Yeo Sang's villa. 




        "Sopro is a sort of magical spirit that synchronizes the feelings of those who 

        hold it with those who draw breath around them. According to legend, one of 

        the four priest guardians of Halazia gathered the breaths of all of Halazia to 

        create it."


        Left Eye turned Sopro carefully in his hand and explained. They were sailing to the Android Guardian's bunker to look for the lost Cromer. One of the younger Grimes Siblings, reaching for the stone without hesitation, chimed in: "Then, we should use it to awaken the emotions of the people and Guardians!" Left Eye stopped him and offered a cautious thought.


        "Why was something as precious as this thrown away at the Strickland 

        Disposal Site?"


        An elder sister of the Grimes Siblings replied to Left Eye:


        "It must have been swept up and thrown away along with the countless 

        particles of emotion or our voices. I doubt they knew what it was and just 

        tossed it away."


        Left Eye turned his head to the side and examined the stone which shone the enchanting color of blood.


        "Legends are just legends. It might be dangerous. Let's only use this as a 

        last resort."




        Woo Young, returning quietly to the villa where the members slept, headed to the living room, he passed a table covered with empty bottles and leftovers, went to the antique cabinet, and picked up Sopro. 


        Woo Young	"So if I use this...I can sync my and the members' emotions?"


        Sopro's red light wavered as though in response to Woo Young's question. Holding the stone tightly in his fist, Woo Young brought his hand to his heart and earnestly prayed: "It's as though they've all forgotten what it was like to be happy. Reignite our passion like it was back then, and let us be happy together again. Please."


        Red light spilled from the gaps of his fingers, a ruby aurora dancing throughout the dark room.    

         
        """, unsafe_allow_html=True)
    st.caption("All rights to KQ Entertainment")


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
            Evidence of this theory is that there are studies of the universe and sand in The Treasure Ep.2 album scans. Further evidence is that from this point on it does not seem as though both groups are working together, and it seems HALATEEZ is more in the shadow.
                
              
            The lyrics indicate the butterfly effect, something that is referenced throughout the Treasure series.  
            "Dream of being on top and the bottom can be changed with one difference"  
            
            :orange-background[**Intro: Long Journey**] 
            Throughout this first album, ATEEZ is embarking on their journey in the Strictland Black Fedora revolution, unaware many of their actions are being manipulated by HALATEEZ.   
            :orange-background[**Treasure**]    
            This song mirrors Precious, later in Treasure Epiloge. It marks the "beginning" of ATEEZ's journey. They are just barely following their own paths.
            ATEEZ have accepted their places in the Men in the Black Fedora's revolution and remain in Strictland to bring emotions back.  
            
            They're still looking for HALATEEZ, which indicates that they did not join up with them after the events of Say My Name.   
            "To find the you that I saw in my dream"  
                
            :orange-background[**Pirate King**]  
            Yeosang can be seen in the opening moves breaking out of his jail cell from the Say My Name MV.  
            *The lyrics further indicate that the Treasure series takes place after the ZERO : FEVER series*  
            *"We dance like turbulence"*  
                  
            :orange-background[**Twilight**]  
            ATEEZ seem unaware of any sort of manipulation but do believe that HALATEEZ is sharing their own memories with ATEEZ to help them succeed.  
            "When our memories combine, it's an infinity bigger than us. I'll go into your memory. I remember clearly. Inside you, even fog can't stop me"  
            :orange-background[**Stay**]  
            I personally believe Stay is HALATEEZ and will be giving the lore analysis with that in mind.  
            HALATEEZ mention that they are manipulating ATEEZ and giving them an illusion of the world  
                "When I'm not by your side, when the illusion is empty, I'll let you see and hear me"
              
            :orange-background[**My Way**]  
            For the first time, ATEEZ start to struggle to remember their pasts.  
                "So when the memories that stood by me start to collapse one by one... I don't look back"  
            
                
            <div style="display: flex; justify-content: center; gap: 20px;">
                <div style="flex: 1; text-align: center;">
                    <p style="font-size: 2.0em;"><strong>TREASURE EP.2 : ZERO TO ONE</strong></p>
                
            :orange-background[**HALA HALA**]  
            HALATEEZ gives us the first look at their past, showing that they once were the same as ATEEZ. This lyric indicates their start in Treasure/Pirate King  
                "Rewinding on film, our starting point is still there...In the middle of the desert, the feet that became many"  
            In general, this song indicates that something is repeating.  
                "A flashing light that has rekindled"    
            :orange-background[**Desire**]  
            The manipulation and corruption of ATEEZ starts to become evident as they start to get obsessed with their goal.  
            "I'm going blind, I gotta have it somehow."  
            :orange-background[**Light**]  
            ATEEZ indicates that currently they're only meeting HALATEEZ in their dreams. If this is true, this means there must be two cromers in play. One for ATEEZ, and one for HALATEEZ to use to go to ATEEZ's dreams.  
                "I gently close my eyes and pray that I can meet you"  
            
            :orange-background[**Promise**]  
            I believe that Promise is sung by HALATEEZ and will be writing this analysis with that assumption.  
            HALATEEZ tries to comfort ATEEZ, who is starting to lose themselves in the manipulation as seen in Desire.
                "I won't let go of your hand"  
                
            <div style="display: flex; justify-content: center; gap: 20px;">
                <div style="flex: 1; text-align: center;">
                    <p style="font-size: 2.0em;"><strong>TREASURE EP.3 : ONE TO ALL</strong></p>
                
            :orange-background[**Utopia**]  
            ATEEZ sees the "dream" that HALATEEZ has for Strictland, which is a Utopia. They decide to help HALATEEZ overthrow the Strictland government to realize this utopia.
            HALATEEZ showed this future to ATEEZ in a manipulated dream  
                "I saw it, felt it in my dream that day"  
                "I had a dream, it's waiting for us"  
            
            The end of Utopia is strange, and I'm not sure what it means. The mood suddenly shifts and the choreography suggests something sinester or sad.  
            :orange-background[**Illusion**]   
            This is one of my favorite songs in the lore. It has some of the most lore in any ateez song. Buckle up.  
            **This song happens while ATEEZ is asleep dreaming**, and is a dream given to them by HALATEEZ, *who are present throughout the dream as a mask or hat can be seen throughout the video*.  
            The entire song is phrased as, "I'm dreaming, don't wake me up". However, there is this lurking feeling that something is wrong.  
            Most of the song is filled with happy go lucky phrases like, "Let's party all night long", "Please don't wake me up", "It's dazzling".  
            However, hidden under the layers of the song are more sinister phrases that start to indicate that ATEEZ is noticing something is wrong.  
                "Life and death keep repeating"  
                "I don't know what day it is"  
                "It's talking to me from soemwhere"  
                "Where am I? Who are you?"  

            And in the background of the chorus, they're shouting, "Let me free".  
            My theory is that the illusion that HALATEEZ is putting on for ATEEZ is starting to fade, and ATEEZ are becoming aware that they don't really understand what's been happening, and they don't remember what they've done. Or what they've been made to do.  
            
            :orange-background[**Crescent**]  
            Crescent ends with a woman saying, "Open your eyes". To indicate previous songs are a dream, someone will say "Open your eyes." This is consistent through many ATEEZ songs.  
            :orange-background[**Wave**]  
            ATEEZ is now awake and no longer in their dream controlled by HALATEEZ. However, they're still aware that somethings wrong.  
                "Remember time keeps passing"  
            The song is about ATEEZ pushing through these doubts and continuing to help the Black Fedoras.  
            :orange-background[**Aurora**]   
            :orange-background[**Dancing Like Butterfly Wings**]  
            In later music videos, the butterfly effect is strongly suggested to be at play. This would indicate that something happens early on in the Treasure series to affect the end of the series.  
                
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

elif option == "**Suggestions**":
    with st.form("request_form"):
        request_note = st.text_area("")
        submitted = st.form_submit_button("Submit Suggestion")
        
        if submitted and request_note.strip():
            with open("suggestions.txt", "a") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] Request: '{request_note}'\n")
            st.success("Request submitted!")
            
else:
    st.write("this page is currently under construction")

