from dashboard.models import User, Skill, UserSkill

user_1 = User(email="zhuxiaofengWWW@gmail.com", password="purpleTeam",
        first_name="John", last_name="Shay",
        phonenumber="7739881897", bio="I'm a graduate student majored in BME. I love cooking. And because of my major, I need to learn a kind of programming language. I think Java is prety commono. Other language is fine, too.")
user_1.save()

user_2 = User(email="zhuxiaofengwww@126.com", password="purpleTeam",
        first_name="Thomas", last_name="Gu",
        phonenumber="8478078707", bio="My name is Thomas. My interest lies at Cartoon and all things relative with cartoon. Also I'm a student of McComic. I enjoy coding!")
user_2.save()

user_3 = User(email="zhuxiaofengWWW@sina.com", password="purpleTeam",
        first_name="Jiachen", last_name="Xu",
        phonenumber="7739881897", bio="I'm a Chinese boy and I really enjoy Chinese food. Aside from my strength above, I still enjoys eating delicious food. So anything about eating, I'm more than glad to discuss with you!")
user_3.save()

user_4 = User(email="zhuxiaofengwww@sohu.com", password="purpleTeam",
        first_name="Hyojun", last_name="Lee",
        phonenumber="7739881897", bio="I'm an American girl. I like to making friends with different kind of people. I ike party. So if you are interested in my strength or a party girl, jion me!")
user_4.save()

user_5 = User(email="ddzhuxiaofengwww@sohu.com", password="purpleTeam",
        first_name="Xiaofeng", last_name="Xu",
        phonenumber="7739881897", bio="I'm a Chinese girl, who is crazy about shopping.")
user_5.save()

user_6 = User(email="ddzhuxiaofengwww@sohu.com", password="purpleTeam",
        first_name="Zhiyuan", last_name="Sun",
        phonenumber="7739881897", bio="I'm a software Engineer with extensive exp and management skills and works for a hi-tech telecommunication company. I like making friends. :) ")
user_6.save()

user_7 = User(email="ddzhuxiaofengwww@sohu.com", password="purpleTeam",
        first_name="Hanson", last_name="Eve",
        phonenumber="7739881897", bio="I'm a software engineer graduate from Northwestern. I like cooking and dancing. ")
user_7.save()

user_8 = User(email="ddzhuxiaofengwww@sohu.com", password="purpleTeam",
        first_name="Yang", last_name="Zhang",
        phonenumber="7739881897", bio="I a Chinese girl. I  was born in Sichuan, China which is famous for its great weather and delicious food. I will get my bachelor degree in Information Science. Designs, Open Source, Web Standards are mostly what interest me every time. ")
user_8.save()

skill_1 = Skill(skill_name="Dancing")
skill_1.save()
skill_2 = Skill(skill_name="Java")
skill_2.save()
skill_3 = Skill(skill_name="Cooking")
skill_3.save()
skill_4 = Skill(skill_name="Table Tennis")
skill_4.save()
skill_5 = Skill(skill_name="Python")
skill_5.save()

uskill_1 = UserSkill(user=user_1, skill=skill_4, scale=1)
uskill_1.save()
uskill_2 = UserSkill(user=user_1, skill=skill_2, scale=2)
uskill_2.save()
uskill_3 = UserSkill(user=user_1, skill=skill_3, scale=8)
uskill_3.save()
uskill_4 = UserSkill(user=user_2, skill=skill_2, scale=4)
uskill_4.save()
uskill_5 = UserSkill(user=user_2, skill=skill_3, scale=5)
uskill_5.save()
uskill_6 = UserSkill(user=user_2, skill=skill_4, scale=6)
uskill_6.save()
uskill_7 = UserSkill(user=user_3, skill=skill_3, scale=2)
uskill_7.save()
uskill_8 = UserSkill(user=user_3, skill=skill_2, scale=8)
uskill_8.save()
uskill_9 = UserSkill(user=user_3, skill=skill_4, scale=9)
uskill_9.save()
uskill_10 = UserSkill(user=user_4, skill=skill_3, scale=2)
uskill_10.save()
uskill_11 = UserSkill(user=user_4, skill=skill_4, scale=4)
uskill_11.save()
uskill_12 = UserSkill(user=user_4, skill=skill_1, scale=7)
uskill_12.save()
uskill_13 = UserSkill(user=user_4, skill=skill_2, scale=10)
uskill_13.save()
uskill_14 = UserSkill(user=user_5, skill=skill_3, scale=2)
uskill_14.save()
uskill_15 = UserSkill(user=user_5, skill=skill_4, scale=7)
uskill_15.save()
uskill_16 = UserSkill(user=user_6, skill=skill_2, scale=6)
uskill_16.save()
uskill_17 = UserSkill(user=user_6, skill=skill_1, scale=2)
uskill_17.save()
uskill_18 = UserSkill(user=user_6, skill=skill_3, scale=4)
uskill_18.save()
uskill_19 = UserSkill(user=user_6, skill=skill_4, scale=10)
uskill_19.save()
uskill_20 = UserSkill(user=user_7, skill=skill_3, scale=2)
uskill_20.save()
uskill_21 = UserSkill(user=user_7, skill=skill_2, scale=10)
uskill_21.save()
uskill_22 = UserSkill(user=user_8, skill=skill_3, scale=1)
uskill_22.save()
uskill_23 = UserSkill(user=user_8, skill=skill_4m scale=10)
uskill_23.save()

