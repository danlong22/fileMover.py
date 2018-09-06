#! python3

#fileAdder.py - moves the lesson plans the school gave me into the folder where I prepare my lessons
# it is a very specific application, but could conveivably be give more general applications with some small changes
# may come back and change this for more general applicaitons if I need to move around a bunch of directories again. 
import os, shutil


#this is where my lesson plans are located
os.chdir(r"c://users//daniel//desktop//Lizen Fall 2018//everyone//LizenWeeklyTeacherPlans")
for week in os.listdir():
	#gets the week number so that it can be compared to other week numbers
	weekNum = week[4:len(week)]
	#absolute path so that it can be used in shutil.copy() later
	week = os.path.abspath(week)
	#this is the where the school-provided lesson plans are located
	os.chdir(r"c://users//daniel//desktop//Lizen Fall 2018//Automated Lesson plans//lesson_plans_fall2018")
	#Reading 100, Listening 300, etc...
	for eslClass in os.listdir():
		os.chdir(eslClass)
		#week1, week2, etc...
		for lessonPlan in os.listdir():
			#for numbers 10 and up
			lessonPlanNum=lessonPlan[len(lessonPlan)-6:(len(lessonPlan))-4]
			#for numbers 1-9
			if lessonPlan[len(lessonPlan)-6]== ' ':
				lessonPlanNum = lessonPlan[len(lessonPlan)-5:(len(lessonPlan))-4]
			if weekNum ==lessonPlanNum:
				print('copying ' + lessonPlan + ' to ' + week)
				shutil.copy(lessonPlan,week)
		os.chdir('../')
	os.chdir(r"c://users//daniel//desktop//Lizen Fall 2018//everyone//LizenWeeklyTeacherPlans")