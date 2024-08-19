import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Prosper Lin")
    content = """
    我是林禹安，現在在練習寫程式，以下是我的作品集
    """
    st.info(content)
text = """testing now \n
In the rapidly evolving digital age, the importance of continually learning new skills cannot be overstated. As technology advances at an unprecedented pace, the skills that were once considered cutting-edge quickly become outdated. This dynamic environment demands that individuals, regardless of their profession, adopt a mindset of lifelong learning to stay relevant and competitive.

The digital transformation has permeated every industry, from healthcare to finance, education to entertainment. As a result, the demand for new skills, particularly those related to technology, has surged. For instance, proficiency in data analysis, digital marketing, coding, and cybersecurity are now essential in many job markets. These skills not only enhance one's employability but also open doors to new opportunities, allowing individuals to pivot in their careers or explore new fields entirely.

Moreover, the rise of artificial intelligence and automation has made it imperative for workers to upskill and reskill. As machines take over routine tasks, the human workforce must focus on more complex and creative endeavors. This shift underscores the need for skills such as critical thinking, problem-solving, and emotional intelligence—abilities that machines cannot easily replicate. By embracing these skills, individuals can better collaborate with technology rather than compete against it.

The benefits of learning new skills extend beyond professional growth. Engaging in continuous learning has been shown to improve cognitive function, boost mental health, and increase life satisfaction. The process of acquiring new knowledge and abilities stimulates the brain, keeping it active and healthy. Additionally, mastering a new skill can provide a sense of accomplishment and boost self-confidence, contributing to overall well-being.

Fortunately, the digital age also offers an abundance of resources for learning. Online platforms like Coursera, Udemy, and Khan Academy provide access to courses on virtually any topic imaginable. Many of these platforms offer courses that are either free or available at a low cost, making education more accessible than ever before. Furthermore, the flexibility of online learning allows individuals to learn at their own pace and on their own schedule, accommodating even the busiest of lifestyles.

However, while the availability of learning resources is a significant advantage, it also presents a challenge: the overwhelming amount of information can make it difficult to know where to start. To overcome this, individuals should begin by identifying their goals and the specific skills they need to achieve them. From there, they can seek out targeted learning opportunities that align with their objectives.

In conclusion, the digital age has made learning new skills more crucial than ever. Whether for professional advancement, personal growth, or cognitive health, continuous learning is essential in navigating the complexities of the modern world. By embracing lifelong learning, individuals can ensure they remain adaptable and resilient in the face of change, ready to seize new opportunities as they arise.
"""
st.write(text)