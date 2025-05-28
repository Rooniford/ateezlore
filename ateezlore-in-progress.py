import pandas as pd
import streamlit as st
import numpy as np

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


option = st.sidebar.radio("Pages",["**Home**", "**Timeline**", "**Characters and Objects**", "**TREASURE**", "**ZERO : FEVER**", "**THE WORLD**", "**Golden Hour**", "**Circle Theory**", "**Motifs**"])
if option == "**Timeline**":
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

elif option == "**Home**":
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
            
        """, unsafe_allow_html=True)

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

else:
    st.write("this page is currently under construction")

