#from datetime import date
import datetime
class Appointment(object):
   def __init__(self,day,month,year,description,aid,status):
       self.description=description
       self.day = day
       self.month = month
       self.year = year
       self.aid = aid
       self.status = status
   def __unicode__(self):
       return self.description
      
   def occursOn(self,day,month,year):
       if day == self.day and month == self.month and year == self.year:
           return True
       else:
           return False
      
class Onetime(Appointment):
   def __init__(self,day,month,year,description,aid,status):
       super(Onetime,self).__init__(day,month,year,description,aid,status)
      
   def __unicode__(self):
       return self.description
      
      
class Daily(Appointment):
   def __init__(self,day,month,year,description,aid,status):
       super(Daily,self).__init__(day,month,year,description,aid,status)
      
   def __unicode__(self):
       return self.description
      
   #function over written  
   def occursOn(self,day,month,year):
       return True
       
      
      
class Monthly(Appointment):
   def __init__(self,day,month,year,description,aid,status):
       super(Monthly,self).__init__(day,month,year,description,aid,status)
      
   def __unicode__(self):
       return self.description
      
   #function over written  
   def occursOn(self,day,month,year):
       if day == self.day and month == self.month and year == self.year:
           return True
       else:
           return False
           
class ApptAdjustment():
	counter = 1111
	def __int__(self):
		self.appList = []
		self.UserChoice = ""
	
	def getday(self):
		day = int(input('Enter a day'))
		return day
	def getmonth(self):
		month = int(input('Enter a month'))
		return month
	def getyear(self):
		year = int(input('Enter a year'))
		return year
	
	def AddAppt(self):#this function is basically to make adjustments to the appointment schedule
		day = self.getday()
		month = self.getmonth()
		year = self.getyear()
		#counter = 1111
		aid = ApptAdjustment.counter
		ApptAdjustment.counter+=1
		NewAppointTypes = input("Provide the new appointment type: "
		                        "i.e. Onetime, Daily, Monthly")
		ApptAdjustmentDescr = input("Provide new appointment description: "
		                            "i.e. Skin, Heart, General")
		status = "Active"        
		                    
		if NewAppointTypes == "Onetime":
			NewAppt = Onetime(day,month,year,ApptAdjustmentDescr,aid,status)
			#NewAppt.__init__(self, description, date)
			appList.append(Onetime(day,month,year,ApptAdjustmentDescr,aid,status))
			appList.append(NewAppt)
			print(day,month,year,ApptAdjustmentDescr,aid,status)
			#counter+=1
		
		elif NewAppointTypes == "Daily":
			NewAppt = Daily(day,month,year,ApptAdjustmentDescr,aid,status)
			appList.append(Daily(day,month,year,ApptAdjustmentDescr,aid,status))
			#self.appList.append(NewAppt)
			print(day,month,year,ApptAdjustmentDescr,aid,status)
		
		elif NewAppointTypes == "Monthly":
			NewAppt = Appointment.Monthly(day,month,year,ApptAdjustmentDescr,aid,status)
			appList.append(Monthly(day,month,year,ApptAdjustmentDescr,aid,status))
			appList.append(NewAppt)
			print(day,month,year,ApptAdjustmentDescr,aid,status)
		else:
			print("Invalid inputss")
	def remove_appointment(self):
		app_id = input("please enter the appointment ID for which appointment you which to delete ")	
		count = 0
		for app in appList:
			
			if int(app.aid) == int(app_id):
				app.status = "Cancelled"
				appList[count] = app
				#print(status)
				count+=1
				break

      
appList = []
appList.append(Daily(1, 1, 2013, "Do pushups",1001,"Active"))
appList.append(Daily(1, 1, 2013, "Floss teeth",1234,"Active"))
appList.append(Monthly(15, 12, 2012, "Backup data",3405,"Active"))
appList.append(Onetime(21, 12, 2012, "Computer Science Final Exam",4323,"Active"))
appList.append(Monthly(4, 2, 2013, "Call grandma",1330,"Active"))
appList.append(Onetime(12, 4, 2013, "See dentist",3412,"Active"))




def main():
	lii = ['A.   See all current Appointments','B. See all current Appointments on a given day',
	'C.  Make a new Appointment','D .  Cancel an existing Appointment','E.  See Appointments according to description','F.  Reload Appointment data from file',
	'G.  Exit program']
	

	
	
	print(*lii, sep = "\n")
	loo = input("Please enter your choice:")
	
	if loo == "A":
		fil = input("Save file as:")
		
		for app in appList :
			with open(fil,'a') as log_file:
				log_file.write("%i %s %i %i %s \n" % (app.month,"-",app.day,app.year,app.description)) 
				print(app.description) 
				
				#log_file.write(app.description +'\n') 
			#file.write(print(app.description))
	elif loo == "B":
		fil2 = input("Save file as:")
		day = int(input("Enter the day (0 to quit): "))
		month = int(input("Enter the month: "))
		year = int(input("Enter the year: "))
		for app in appList:
			with open(fil2,'a') as log_file:
				if day == app.day and month == app.month and year == app.year: #app.occursOn(day,month,year) :
					log_file.write("%i %s %i %i %s \n" % (app.month,"-",app.day,app.year,app.description))
					print(app.description)
				
				else:
				#print("ok")
					break;
					
	elif loo == "C":
		fil3 = input("Save file as:")
		status = "Active"
		factory = ApptAdjustment()
		mylist = factory.AddAppt()
		for app in appList:
			with open(fil3,'a') as log_file:
				log_file.write("%i %s %i %i %s \n" % (app.month,"-",app.day,app.year,app.description))
	elif loo == "D":
		status = "Cancelled"
		fil4 = input("Save file as:")	
		cancel = ApptAdjustment()
		cancelled = cancel.remove_appointment()	
		#fil4 = input("Save file as:")
		
		for app in appList :
			with open(fil4,'a') as log_file:
				log_file.write("%i %s %i %s %i %s %s \n" % (app.month,"-",app.day,"-",app.year,app.description,app.status))
				print(app.description) 	
	elif loo == "E":
		desc = input("Search by description: ")
		for app in appList:
			if str(app.description) == str(desc)  : #app.occursOn(day,month,year) :
				print(app.month,"-",app.day,"-",app.year,app.description)
				print(app.description)
			
				break;
	elif loo == "F":
		fil = input("Enter file name:")
# open the file for reading
		filehandle = open(fil, 'r')  
		while True:  
    # read a single line
			line = filehandle.readline()
			if not line:
				break
			print(line)

# close the pointer to that file
		filehandle.close()
main()

loo = input("Please enter your choice:")
while loo != "G" :

   loo = input("Please enter your choice:")
  
