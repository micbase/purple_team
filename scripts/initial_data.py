from dashboard.models import User, Group, Membership, Event
import datetime

user_1 = User(email="zhuxiaofengWWW@gmail.com", password="purpleTeam",
	 first_name="Deborah", last_name="Farquharson",
	phonenumber="7739881897", bio="Senior Java Swing Developer Java, Swing, Java RMI")
user_1.save()


user_2 = User(email="aCramond@sina.com", password="purpleTeam",
	 first_name="Amee", last_name="Cramond",
	phonenumber="8478078707", bio="Senior Microsoft Dynamics CRM Developer Consultant")
user_2.save()


user_3 = User(email="gToroosian@u.northwestern.edu",password="purpleTeam",
	 first_name="Greg", last_name="Toroosian",
	phonenumber="8478078707", bio="Linux Systems Programmer, Leading Futures Trading Firm; Linux, Kernel, Sockets, Reporting Scripts")
user_3.save()


user_4 = User(email="rRydbeck@fgcu.edu",password="purpleTeam",
	 first_name="Rachael", last_name="Rydbeck",
	phonenumber="7739881897", bio="'The Organic Gourmet' Chef, Author, Speaker, Cooking Classes, Wellness Coach")
user_4.save()

user_5 = User(email="aDulany@gmail.com",password="purpleTeam",
	 first_name="Andrew", last_name="Dulany",
	phonenumber="7739881897", bio="Account Executive at Technology Business Research.I'm currently researching in preparation for a possible role as Marketing Director for a professional soccer team.")
user_5.save()



group_1 = Group(group_name="CyberCoders", description="We are a technology driven business and the technical landscape here is both advanced and constantly changing as we explore new and more effective ways of creating our products.", manager=user_1)
group_1.save()

group_2 = Group(group_name="BankersAccuity", description="Passionate about Java, Big Data, and Innovative Development? Outstanding Activities available at Accuity!", manager=user_2)
group_2.save()

group_3 = Group(group_name="GQR", description="Discuss the current state of affairs and plan for the future of KVM, its surrounding infrastructure, and management tools.", manager=user_3)
group_3.save()

group_4 = Group(group_name="Yummy Recipes", description="Delicious, healthy meals made easy. Whether you are a great cook or just a wanna-a-be or even if you hate to cook...you will love the taste and ease of your Yummy Recipes!", manager=user_4)
group_4.save()

group_5 = Group(group_name="National Soccer Coaches Association of America", description="This group will connect people who are members of the NSCAA or interested non-NSCAA members who are soccer coaches", manager=user_5)
group_5.save()

membership_1=Membership(member=user_1,group=group_1, status=1)
membership_1.save()
membership_2=Membership(member=user_2,group=group_2, status=1)
membership_2.save()
membership_3=Membership(member=user_3,group=group_3, status=1)
membership_3.save()
membership_4=Membership(member=user_4,group=group_4, status=1)
membership_4.save()
membership_5=Membership(member=user_1,group=group_2, status=2)
membership_5.save()
membership_6=Membership(member=user_2,group=group_3, status=1)
membership_6.save()
membership_7=Membership(member=user_3,group=group_4, status=1)
membership_7.save()
membership_8=Membership(member=user_4,group=group_1, status=1)
membership_8.save()
membership_9=Membership(member=user_1,group=group_3, status=1)
membership_9.save()
membership_10=Membership(member=user_2,group=group_4, status=2)
membership_10.save()
membership_11=Membership(member=user_3,group=group_1, status=1)
membership_11.save()
membership_12=Membership(member=user_4,group=group_2, status=1)
membership_12.save()


event_1=Event(group=group_1, event_name="Prototyping for Success, Power and Unlimited Riches", end_time=datetime.datetime(2013, 11, 1, 1, 2, 3, tzinfo=None), start_time=datetime.datetime(2013, 11, 2, 1, 2, 3, tzinfo=None), location="Chicago", status=1,
	details="In advertising, the best way to sell in a concept has always been to show it. Create a storyboard. Do a sketch. But today, some of the biggest ideas are digital, and to effectively convey them, traditional prototyping tools fall short. So creatives have had to get a lot more, well, creative. They are coming up with imaginative ways to articulate the richness and magic of interactive experiences. Here, Google Creative Lab shares examples and advice to help bring your idea to life.")
event_1.save()

event_2=Event(group=group_1, event_name="A powerfully simple way to monitor your Web & Mobile applications", end_time=datetime.datetime(2013, 11, 8, 1, 2, 3, tzinfo=None), start_time=datetime.datetime(2013, 11, 12, 1, 2, 3, tzinfo=None), location="Chicago", status=1,
	details="Responsible for design and development for a wide range of satellite sub-systems, like Adaptive Coding & Modulation and Automatic Uplink Power Control systems in order to optimize over-the-air transmission and prevent weather-related fading from causing communication on the link to be disrupted.Designed, implemented and delivered a Scheduler Server for inbound and outbound Quality of Service management which involves the monitoring and adaptation of Satellite Remote Terminals quality levels.")
event_2.save()

event_3=Event(group=group_1, event_name="Our Grads Speak Multiple Languages: HTML5, iOS & ROI", end_time=datetime.datetime(2013, 11, 20, 1, 2, 3, tzinfo=None), start_time=datetime.datetime(2014, 11, 25, 1, 2, 3, tzinfo=None), location="Chicago", status=1,
	details="Master of Science in Management Information Systems is a business degree unlike any other. It prepares graduates to impact business goals by leveraging web and mobile technology.")
event_3.save()

event_4=Event(group=group_2, event_name="TechNet Webcast: Successfully Deploy Project Server on VMware with Shared Infrastructure", start_time=datetime.datetime(2013, 11, 2, 1, 2, 3, tzinfo=None), end_time=datetime.datetime(2012, 12, 20, 1, 2, 3, tzinfo=None),status=2,
 details="Virtualizing Microsoft Project Server 2010 provides many benefits, but there are a number of decisions that you must carefully consider. This webcast highlights the key decision points around architecting a Project Server 2010 deployment utilizing VMware on shared infrastructure.")
event_4.save()

event_5=Event(group=group_2, event_name="This Is Microsoft Dynamics GP", end_time=datetime.datetime(2013, 4, 3, 1, 2, 3, tzinfo=None), start_time=datetime.datetime(2013, 5, 2, 1, 2, 3, tzinfo=None), status=2,
	details="Please join us to learn how Microsoft Dynamics GP connects the many moving parts of your organization to give you better control over and visibility into what's going on in your business. The ability to make smart business decisions can have a direct impact on your bottom line--turning higher margins into a better cash position. With liquidity, more things become possible, which ultimately leads to growth, shareholder value, security for staff, and increased job satisfaction.")
event_5.save()

event_5=Event(group=group_2, event_name="Visual Studio Team System Lab Management ", end_time=datetime.datetime(2013, 11, 12, 1, 2, 3, tzinfo=None), start_time=datetime.datetime(2013, 11, 20, 1, 2, 3, tzinfo=None), location="Chicago", status=1,
	details="This session will cover Visual Studio Team System Lab Management, including what is Lab Management, the benefits of Lab Management and implementation strategies. In addition, the session will include a basic implementation of a build/deploy/test workflow using Visual Studio and Lab Management.")
event_5.save()

event_6=Event(group=group_3, event_name="Feel your freedom", end_time=datetime.datetime(2013, 5, 20, 1, 2, 3, tzinfo=None), start_time=datetime.datetime(2013, 6, 2, 1, 2, 3, tzinfo=None), status=2,
	details="The Embedded Linux Conference Europe (ELCE) is the premier vendor-neutral technical conference for companies and developers using Linux in embedded products. This conference, now in it's 7th year, has the largest collection of sessions dedicated exclusively to embedded Linux and embedded Linux developers. ELCE is embedded Linux experts talking about solutions to your embedded Linux problems. ELCE consists of 2 days of presentations, tutorials and Bird-of-a-Feather sessions.")
event_6.save()

event_7=Event(group=group_4, event_name="Culinary training Celebrity Chef Paul Virant to deliver keynote address at Colorado Culinary Academy inaugural graduation ceremony! ", end_time=datetime.datetime(2013, 5, 20, 1, 2, 3, tzinfo=None), start_time=datetime.datetime(2013, 10, 2, 1, 2, 3, tzinfo=None), location="Chicago", status=1,
	details="Colorado Culinary Academy is much more than a cooking school. We offer professional culinary, chef and cooking school programs that allow you to enter the modern professional kitchen or other professional food-related endeavor. http://bit.ly/1eduapC")
event_7.save()

event_8=Event(group=group_4, event_name="Edinburgh International Conference ", end_time=datetime.datetime(2013, 9, 24, 1, 2, 3, tzinfo=None), start_time=datetime.datetime(2013, 10, 2, 1, 2, 3, tzinfo=None), status=2,
	details="Have the courage to feel your freedom Authentic Transformation in 100 days-Video Blogging Challenge -Day 99 mothernaturelovesyou.com To be yourself fully every day in everything that you do means to live wholeheartedly and with courage. Although we all play certain roles in our lives-mother , daughter, checkout assistant, sister, friend.....the list goes on every day.")
event_8.save()

event_9=Event(group=group_5, event_name="Soccer Business", end_time=datetime.datetime(2013, 10, 14, 1, 2, 3, tzinfo=None), start_time=datetime.datetime(2013, 10, 20, 1, 2, 3, tzinfo=None), location="Chicago", status=1,
	details="Luis Figo's Network90 rapidly becoming the online destination for the football industry. Network90: A New Place For The Industry To Meet fcbusiness.co.uk Luis Figo's Network90, the free, private members' network for the pro football industry has rapidly become the online destination for current and former players, agents, teams, associations and sports business professionals. ")
event_9.save()