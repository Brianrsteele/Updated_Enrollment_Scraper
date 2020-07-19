import bs4
import requests
from lxml import etree
import campus
import course
import department
import datetime
import faculty
import minnstateUtilities
import meetingTime
import room
import section
import semester
import school
import textbook
import timeUtilities
from orca.orca import start



# read an example html file as a string
with open('sample_pages/fees_textbooks.html', 'r') as file:
  page_file = file.read()

# create an etree object in lxml
dom = etree.HTML(page_file)

#create a campus object


# find the name of the campus where the 
# course meets 
# strip whitespace, and get rid of '.
# create Campus object'
campus_name_raw = dom.xpath('//*[@id="main"]/table[3]/tbody/tr[2]/td[1]/text()')
campus_name = campus_name_raw[1].strip()[:-1]
currentCampus = campus.Campus(campus_name)

# find the name of the school
# strip whitespace
# create School object
school_name_raw = dom.xpath('//*[@id="main"]/table[3]/tbody/tr[1]/td[1]/text()')
school_name = school_name_raw[1][1:].strip()[:-1]
currentSchool = school.School(school_name)

location_name_raw = dom.xpath('//*[@id="main"]/table[3]/tbody/tr[2]/td[2]/text()')
location_name = location_name_raw[1].strip()[:-1]



# find the name of the room
# Strip whitespace
# create Room object
room_raw = dom.xpath('//*[@id="main"]/table[2]/tbody/tr[2]/td[4]/text()')
room_name = room_raw[0].strip()
currentRoom = room.Room(room_name)

# find the name of the department
# strip whitespace
# create Department object
department_raw = dom.xpath('//*[@id="main"]/table[1]/tbody[2]/tr/td[3]/text()')
department_abbreviation = department_raw[0].strip()
currentDepartment = department.Department(department_abbreviation, school = currentSchool)

# find the course number
# strip whitespace
course_number_raw = dom.xpath('//*[@id="main"]/table[1]/tbody[2]/tr/td[4]/text()')
course_number = course_number_raw[0].strip()

# find the course title
# Strip whitespace
course_title_raw = dom.xpath('//*[@id="main"]/table[1]/tbody[2]/tr/td[6]/text()')
course_title = course_title_raw[0].strip()

# find the course description
# assuming course description is the longest value in the list
description_raw = dom.xpath('//*[@id="main"]/text()')
longest_index = 0
for i in range(len(description_raw)):
    if len(description_raw[i].strip()) > longest_index:
        longest_index = i
description = description_raw[longest_index].strip()


# separate prerequisites from description
if "(Prerequisites:" in description:
    description, prerequisites = description.split("(Prerequisites:")
    description = description.replace('\n', '')
    prerequisites = prerequisites[2:-2]
else:
    prerequisites = "Error"
    
# Find the credit hours
# Strip white space
credit_hours_raw = dom.xpath('//*[@id="main"]/table[1]/tbody[2]/tr/td[10]/text()')
credit_hours = credit_hours_raw[0].strip()

# find the course level
# strip white space
course_level_raw = dom.xpath('//*[@id="main"]//text()[contains(.,"Undergraduate") or contains(.,"Graduate")]')
course_level = course_level_raw[0].strip()
        
# find the mnTC goals
# strip whitespace and store as array
#mntc_goals_raw = dom.xpath('//*[@id="main"]//ul//text()[contains(.,"Goal")]')
mntc_goals_raw = dom.xpath('//*[@id="main"]//text()[contains(.,"Goal")]')



mntc_goals = []
for goal in mntc_goals_raw:
    if goal.strip().startswith("Goal"):
        mntc_goals.append(goal.strip())


# Create Course
currentCourse = course.Course(currentDepartment, course_number, course_title,\
                               description, credit_hours, course_level, mntc_goals, prerequisites)


        
# Create Semester and section
semester_raw = dom.xpath('//*[@id="main"]/h1/text()[2]')
semester_clean = semester_raw[0].split(',')[0].strip()
semester_name = semester_clean.split(' ')[0]
semester_year = semester_clean.split(' ')[1]

currentSemester = semester.Semester(semester_year, semester_name)

section_raw = semester_raw[0].split(',')[1].strip()
section_number = section_raw.split(' ')[1]

#find the beginning date of the section
start_date_raw = dom.xpath('//*[@id="main"]/table[2]/tbody/tr[2]/td[1]/text()')
start_date_raw = start_date_raw[0].strip()
begin_date = start_date_raw.split("-")[0].strip()
startDate = datetime.datetime.strptime(begin_date, "%m/%d/%Y")



# find the end date of the section
end = start_date_raw.split("-")[1].strip()
endDate = datetime.datetime.strptime(end, "%m/%d/%Y")


# this is not dealing with multi line meeting datees
meeting_days_raw = dom.xpath('/html/body/div[2]/div[1]/div/div[1]/table[2]/tbody/tr[2]/td[2]//text()')
meeting_days_list = []
for day in meeting_days_raw:
    if len(day.strip()) > 0:
        meeting_days_list.append(day.strip())

# this is not dealing with multi line meeting dates
meeting_times_raw = dom.xpath('//*[@id="main"]/table[2]/tbody/tr[2]/td[3]/text()')

if meeting_times_raw[0].strip() == "Arranged":
    start_time = "Arranged"
    end_time = "Arranged"
else:
    meeting_times = meeting_times_raw[0].strip()
    meeting_times = meeting_times.split("-")
    start_time = meeting_times[0].strip()
    end_time = meeting_times[1].strip()
    start_time = timeUtilities.TimeUtilities.convert_to_24_hour(start_time)
    end_time = timeUtilities.TimeUtilities.convert_to_24_hour(end_time)

weekly_meetings_list = []
for day in meeting_days_list:
    currentMeetingTime = meetingTime.MeetingTime(day, start_time, end_time)
    weekly_meetings_list.append(currentMeetingTime)
    
section_status_raw = dom.xpath('//*[@id="main"]/table[1]/tbody[2]/tr/td[11]/span/text()')
section_status = section_status_raw[0]

# Create faculty list
faculty_list = []
faculty_raw = dom.xpath('//*[@id="main"]/table[2]/tbody/tr[2]/td[5]/text()')
for fac in faculty_raw:
    fac = fac.split(',')
    if len(fac) > 1:
        currentFaculty = faculty.Faculty(fac[0].strip(), fac[1].strip())
        faculty_list.append(currentFaculty)
    

delivery_raw = dom.xpath('//*[@id="main"]/table[1]/tbody[2]/tr/td[13]//text()') 
if len(delivery_raw) == 1:
    delivery = "In-Person"
else:
    delivery = delivery_raw[1].strip()

section_size_raw = dom.xpath('//*[@id="main"]/table[4]/tbody/tr/td[2]/text()')
section_size = section_size_raw[1].strip()

section_enrollment_raw = dom.xpath('//*[@id="main"]/table[4]/tbody/tr/td[3]/text()')
enrollment = section_enrollment_raw[1].strip()

full_refund_date_raw = dom.xpath('//*[@id="main"]//text()[contains(.,"Full refund")]')
full_refund_text = full_refund_date_raw[0].strip()
date_index = full_refund_text.index("until ")
full_refund_text = full_refund_text[date_index + 6:-5]
refundDate = datetime.datetime.strptime(full_refund_text, "%B %d, %Y, %H:%M%p")

last_add_date_and_drop_raw = dom.xpath('//*[@id="main"]//text()[contains(.,"last day to add")]')
last_add_date_and_drop_text = last_add_date_and_drop_raw[0].strip()
last_add_date_and_drop = last_add_date_and_drop_text.split('.')
last_add_date = last_add_date_and_drop[0]
last_drop_date = last_add_date_and_drop[1]
last_add_date = last_add_date.split(" is ")[1]
last_drop_date = last_drop_date.split(" is ")[1]
lastAddDate = datetime.datetime.strptime(last_add_date, "%B %d, %Y")
lastDropDate = datetime.datetime.strptime(last_drop_date, "%B %d, %Y")

last_withdraw_date_raw = dom.xpath('//*[@id="main"]//text()[contains(.,"withdraw")]')
last_withdraw_date_text = last_withdraw_date_raw[0].strip()
last_withdraw_date_text = last_withdraw_date_text.split(' is ')[1][0:-1]
lastWithdrawDate = datetime.datetime.strptime(last_withdraw_date_text, "%B %d, %Y")

tuition_resident_raw = dom.xpath('//*[@id="main"]/table[5]/tbody/tr[1]/td/text()')
tuition_resident = tuition_resident_raw[0].strip()[1:]
tuition_resident = float(tuition_resident)


tuition__non_resident_raw = dom.xpath('//*[@id="main"]/table[5]/tbody/tr[2]/td/text()')
tuition_non_resident = tuition__non_resident_raw[0].strip()[1:]
tuition_non_resident = float(tuition_non_resident)


fees_raw = dom.xpath('//*[@id="main"]/table[5]/tbody/tr[3]/td/text()')
fees = fees_raw[0].strip()[1:]
fees = float(fees)


textbooks_raw = dom.xpath('//table[@class = "plain"]//text()')
textbooks_raw_list = []
for element in textbooks_raw:
    if element.strip() != '':
        textbooks_raw_list.append(element.strip())
num_textbooks = (len(textbooks_raw_list))/16

section_textbook_list = []
for tb in range(int(num_textbooks)):
    textbook_info = textbooks_raw_list[(tb * 16): (tb * 16) + 16] 
    currentTextbook = textbook.Textbook(textbook_info[5], textbook_info[3], required=textbook_info[1], \
                                        publisher=textbook_info[7], ISBN=textbook_info[9], \
                                        edition=textbook_info[11], new_price=textbook_info[13], \
                                        used_price=textbook_info[15])
    section_textbook_list.append(currentTextbook)
    




print(len(textbooks_raw_list))
print(num_textbooks)


# //*[@id="main"]/table[7]

# create section object
currentSection = section.Section(currentSemester, currentCourse, section_number, \
                                 meeting_times = weekly_meetings_list, \
                                 start_date = startDate, \
                                 end_date = endDate, \
                                 status = section_status, \
                                 instructor = faculty_list, \
                                 delivery_method = delivery, \
                                 offered_through = currentSchool, \
                                 location = location_name, \
                                 size = section_size, \
                                 enrolled = enrollment, \
                                 full_refund_date = refundDate, \
                                 last_add_date = lastAddDate, \
                                 last_drop_date = lastDropDate, \
                                 last_withdraw_date = lastWithdrawDate, \
                                 nonresident_tuition = tuition_non_resident, \
                                 resident_tuition = tuition_resident, \
                                 approximate_course_fees = fees, \
                                 textbooks = section_textbook_list)

"""
        
        
        


       
     
        :param textbooks: a list of textbook object containing information about the section's textbooks.

"""

print("Section Information: ", currentSection.__repr__())










