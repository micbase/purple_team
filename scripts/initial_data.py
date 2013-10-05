from dashboard.models import User, Skill, UserSkill

user_1 = User(email="zhuxiaofengWWW@gmail.com", password="purpleTeam",
	 first_name="John", last_name="Shay",
	phonenumber="7739881897", bio="I'm a freshman student of EECS department")
user_1.save()
skill_1 = Skill(skill_name="Dancing")
skill_1.save()

user_2 = User(email="zhuxiaofengwww@126.com", password="purpleTeam",
	 first_name="Tylor", last_name="Smith",
	phonenumber="8478078707", bio="Dance Instructor")
user_2.save()
skill_2 = Skill(skill_name="Java")
skill_2.save()

user_3 = User(email="zhuxiaofengWWW@sina.com",password="purpleTeam",
	 first_name="Julia", last_name="Linken",
	phonenumber="7739881897", bio="Chef")
user_3.save()
skill_3 = Skill(skill_name="Cooking")
skill_3.save()

user_4 = User(email="zhuxiaofengwww@sohu.com",password="purpleTeam",
	 first_name="Andrew", last_name="Bush",
	phonenumber="7739881897", bio="Senior Software Engineer")
user_4.save()

user_5 = User(email="ddzhuxiaofengwww@sohu.com",password="purpleTeam",
	 first_name="BBAndrew", last_name="ABush",
	phonenumber="7739881897", bio="Engineer")
user_5.save()

skill_4 = Skill(skill_name="Table Tennis")
skill_4.save()

uskill_1=UserSkill(user=user_1,skill=skill_4,scale =1)
uskill_1.save()
uskill_2=UserSkill(user=user_2,skill=skill_2,scale=2)
uskill_2.save()
uskill_3=UserSkill(user=user_3,skill=skill_3,scale=3)
uskill_3.save()
uskill_4=UserSkill(user=user_4,skill=skill_4,scale=4)
uskill_4.save()
uskill_5=UserSkill(user=user_1,skill=skill_2,scale=5)
uskill_5.save()
uskill_6=UserSkill(user=user_2,skill=skill_3,scale=6)
uskill_6.save()
uskill_7=UserSkill(user=user_3,skill=skill_4,scale=7)
uskill_7.save()
uskill_8=UserSkill(user=user_4,skill=skill_1,scale=8)
uskill_8.save()
uskill_9=UserSkill(user=user_1,skill=skill_3,scale=9)
uskill_9.save()
uskill_10=UserSkill(user=user_2,skill=skill_4,scale=10)
uskill_10.save()
uskill_11=UserSkill(user=user_5,skill=skill_4,scale=10)
uskill_11.save()
uskill_12=UserSkill(user=user_5,skill=skill_3,scale=1)
uskill_12.save()
