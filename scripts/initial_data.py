from dashboard.models import User, Class, Topic, Post
import datetime

user_1 = User(email="farquharsonWWW@gmail.com", password="purpleTeam",
	 first_name="Deborah", last_name="Farquharson",
	phonenumber="2249881897", bio="Senior Java Swing Developer Java, Swing, Java RMI")
user_1.save()


user_2 = User(email="aCramond@sina.com", password="purpleTeam",
	 first_name="Amee", last_name="Cramond",
	phonenumber="8478078707", bio="Senior Microsoft Dynamics CRM Developer Consultant")
user_2.save()


user_3 = User(email="gToroosian@u.northwestern.edu",password="purpleTeam",
	 first_name="Greg", last_name="Toroosian",
	phonenumber="8478078523", bio="Linux Systems Programmer, Leading Futures Trading Firm; Linux, Kernel, Sockets, Reporting Scripts")
user_3.save()


user_4 = User(email="rRydbeck@fgcu.edu",password="purpleTeam",
	 first_name="Rachael", last_name="Rydbeck",
	phonenumber="7739661897", bio="'The Organic Gourmet' Chef, Author, Speaker, Cooking Classes, Wellness Coach")
user_4.save()

user_5 = User(email="aDulany@gmail.com",password="purpleTeam",
	 first_name="Andrew", last_name="Dulany",
	phonenumber="9149881897", bio="Account Executive at Technology Business Research.I'm currently researching in preparation for a possible role as Marketing Director for a professional soccer team.")
user_5.save()



class_1 = Class(class_name="EECS 212 (formerly 310*) Mathematical Foundations of Computer Science", professor_firstname="Hendrix", professor_lastname="William", class_time="24,1100,1220",manager=user_1)
class_1.save()

class_2 = Class(class_name="EECS 214 (formerly 311*) Data Structures and Data Management", professor_firstname="Scheuermann", professor_lastname="Peter", class_time="135,1200,1250",manager=user_1)
class_2.save()

class_3 = Class(class_name="EECS  336 - Design & Analysis of Algorithms", professor_firstname="Hartline", professor_lastname="Jason", class_time="24,1530,1650",manager=user_1)
class_3.save()

class_4 = Class(class_name="EECS  339 - Introduction to Database Systems", professor_firstname="Peter", professor_lastname="Dinda", class_time="135,1600,1650",manager=user_1)
class_4.save()

class_5 = Class(class_name="EECS 394 - Software Project Management", professor_firstname="Riesbeck", professor_lastname="Chris", class_time="135,1000,1050",manager=user_1)
class_5.save()

topic_1=Topic(topic_title="Today's class is awesome", topic_content="I really enjoyed today's class. I learned a lot of things about graphs which i've been facinated with.", topic_author=user_3, class_id=class_1)
topic_1.save()
topic_2=Topic(topic_title="Did anyone get the question about Binary Search Tree?", topic_content="I am so confused, what does the professor mean by O(logn)?", topic_author=user_2, class_id=class_2)
topic_2.save()
topic_3=Topic(topic_title="Does anyone want to study together for next week's exam?", topic_content="Does anyone want to study together for next week's exam? I'll be in the MUDD library most of the time for the weekend, come on and join me.", topic_author=user_4, class_id=class_2)
topic_3.save()
topic_4=Topic(topic_title="I really like the on-time walker...", topic_content="I'm not a member of that team, but I really like their idea. And i have a suggestion for them: make it look better!!", topic_author=user_2, class_id=class_5)
topic_4.save()
topic_5=Topic(topic_title="Last project was killing me!!!!", topic_content="I just submitted the project, it spent me like 2 days. anyone has the same feeling?", topic_author=user_5, class_id=class_4)
topic_5.save()
topic_6=Topic(topic_title="Hartline looks so cool today!", topic_content="He looks great in that purple suit.", topic_author=user_3, class_id=class_3)
topic_6.save()


post_1=Post(post_content="Yeah, I like today's class too.", post_author=user_2, topic=topic_1)
post_1.save()

post_2=Post(post_content="I didn't get today's class at all, how could your guys like it?", post_author=user_1, topic=topic_1)
post_2.save()

post_3=Post(post_content="I hate this class!", post_author=user_4, topic=topic_1)
post_3.save()

post_4=Post(post_content="You can refer to the textbook form page 100 to 150, it explains the problem clearly", post_author=user_1, topic=topic_2)
post_4.save()

post_5=Post(post_content="I didn't get it neither...", post_author=user_3, topic=topic_2)
post_5.save()

post_5=Post(post_content="The book really helps, thank you Deborah.", post_author=user_4, topic=topic_2)
post_5.save()

post_6=Post(post_content="I will study the exam in the library too, let's do it together", post_author=user_2, topic=topic_3)
post_6.save()

post_7=Post(post_content="I don't have time... I will go to Florida....", post_author=user_3, topic=topic_3)
post_7.save()

post_8=Post(post_content="I didn't finish it yet. Can I email you a few problems I have?", post_author=user_2, topic=topic_5)
post_8.save()

post_9=Post(post_content="Yeah.. I like him so much!", post_author=user_4, topic=topic_6)
post_9.save()