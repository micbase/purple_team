from dashboard.models import User, Skill, UserSkill

user_1 = User(email="zhuxiaofengWWW@gmail.com", password="purpleTeam",
	 first_name="John", last_name="Shay",
	phonenumber="7739881897", bio="I'm a freshman student of EECS department in Northwestern University")
user_1.save()
skill_1 = Skill(skill_name="Dancing")
skill_1.save()

user_2 = User(email="zhuxiaofengwww@126.com", password="purpleTeam",
	 first_name="Tylor", last_name="Smith",
	phonenumber="8478078707", bio="Professional Dancer/Social Media Marketing Strategist,Featured Dancer and Triple Threat")
user_2.save()
skill_2 = Skill(skill_name="Java")
skill_2.save()

user_3 = User(email="zhuxiaofengWWW@sina.com",password="purpleTeam",
	 first_name="Julia", last_name="Linken",
	phonenumber="7739881897", bio="Five years of experience as a Chef in Loews Boston Hotel")
user_3.save()
skill_3 = Skill(skill_name="Cooking")
skill_3.save()

user_4 = User(email="982388314@qq.com",password="purpleTeam",
	 first_name="Andrew", last_name="Bush",
	phonenumber="7739881897", bio="Vice-President of WaveCrest Software, Inc.")
user_4.save()

skill_4 = Skill(skill_name="Table Tennis")
skill_4.save()

uskill_1=UserSkill(uid=user_1,skill_id=skill_1,scale =1)
uskill_1.save()
uskill_2=UserSkill(uid=user_2,skill_id=skill_1,scale=10)
uskill_2.save()
uskill_3=UserSkill(uid=user_3,skill_id=skill_3,scale=10)
uskill_3.save()
uskill_4=UserSkill(uid=user_4,skill_id=skill_4,scale=4)
uskill_4.save()
uskill_5=UserSkill(uid=user_1,skill_id=skill_2,scale=2)
uskill_5.save()
uskill_6=UserSkill(uid=user_2,skill_id=skill_3,scale=6)
uskill_6.save()
uskill_7=UserSkill(uid=user_3,skill_id=skill_4,scale=7)
uskill_7.save()
uskill_8=UserSkill(uid=user_4,skill_id=skill_1,scale=1)
uskill_8.save()
uskill_9=UserSkill(uid=user_1,skill_id=skill_3,scale=6)
uskill_9.save()
uskill_10=UserSkill(uid=user_2,skill_id=skill_4,scale=7)
uskill_10.save()
uskill_11=UserSkill(uid=user_3,skill_id=skill_1,scale=2)
uskill_11.save()
uskill_12=UserSkill(uid=user_4,skill_id=skill_2,scale=10)
uskill_12.save()


