from lxml import etree
import campus
import course
import department
import datetime
import faculty
import meetingTime
import room
import section
import semester
import school
import textbook
import timeUtilities


# read an example html file as a string
with open('sample_pages/fees_textbooks.html', 'r') as file:
    page_file = file.read()

# create an etree object in lxml
dom = etree.HTML(page_file)

# find the name of the campus where the course meets
campus_name_raw = dom.xpath('//*[@id="main"]/table[3]/tbody/tr[2]/td[1]/text()')
# strip whitespace, and get rid of '.
campus_name = campus_name_raw[1].strip()[:-1]
#create a campus object
currentCampus = campus.Campus(campus_name)

# find the name of the school
school_name_raw = dom.xpath('//*[@id="main"]/table[3]/tbody/tr[1]/td[1]/text()')
# strip whitespace
school_name = school_name_raw[1][1:].strip()[:-1]
# create School object
currentSchool = school.School(school_name)

# find the location
location_name_raw = dom.xpath('//*[@id="main"]/table[3]/tbody/tr[2]/td[2]/text()')
# strip the whitespace
location_name = location_name_raw[1].strip()[:-1]

# find the name of the room
room_raw = dom.xpath('//*[@id="main"]/table[2]/tbody/tr[2]/td[4]/text()')
# Strip whitespace
room_name = room_raw[0].strip()
# create Room object
currentRoom = room.Room(room_name)

# find the name of the department
department_raw = dom.xpath('//*[@id="main"]/table[1]/tbody[2]/tr/td[3]/text()')
# strip whitespace
department_abbreviation = department_raw[0].strip()
# create Department object
currentDepartment = department.Department(department_abbreviation, school = currentSchool)

# find the course number
course_number_raw = dom.xpath('//*[@id="main"]/table[1]/tbody[2]/tr/td[4]/text()')
# strip whitespace
course_number = course_number_raw[0].strip()

# find the course title
course_title_raw = dom.xpath('//*[@id="main"]/table[1]/tbody[2]/tr/td[6]/text()')
# strip whitespace
course_title = course_title_raw[0].strip()

# find the course description
description_raw = dom.xpath('//*[@id="main"]/text()')
longest_index = 0
for i in range(len(description_raw)):
    if len(description_raw[i].strip()) > longest_index:
        longest_index = i
# assuming course description is the longest value in the list
description = description_raw[longest_index].strip()
# separate prerequisites from description above
if "(Prerequisites:" in description:
    description, prerequisites = description.split("(Prerequisites:")
    description = description.replace('\n', '')
    prerequisites = prerequisites[2:-2]
else:
    prerequisites = "Error"
    
# Find the credit hours
credit_hours_raw = dom.xpath('//*[@id="main"]/table[1]/tbody[2]/tr/td[10]/text()')
# Strip white space
credit_hours = credit_hours_raw[0].strip()

# find the course level
course_level_raw = dom.xpath('//*[@id="main"]//text()[contains(.,"Undergraduate") or contains(.,"Graduate")]')
# strip white space
course_level = course_level_raw[0].strip()
        
# find the mnTC goals
mntc_goals_raw = dom.xpath('//*[@id="main"]//text()[contains(.,"Goal")]')
# strip whitespace and store as array
mntc_goals = []
for goal in mntc_goals_raw:
    if goal.strip().startswith("Goal"):
        mntc_goals.append(goal.strip())

# Create Course
currentCourse = course.Course(currentDepartment, course_number, course_title,\
                               description, credit_hours, course_level, mntc_goals, prerequisites)

# Create Semester and section
semester_raw = dom.xpath('//*[@id="main"]/h1/text()[2]')
# strip whitespace
semester_clean = semester_raw[0].split(',')[0].strip()
semester_name = semester_clean.split(' ')[0]
semester_year = semester_clean.split(' ')[1]
# create semester object
currentSemester = semester.Semester(semester_year, semester_name)
# find the section number
section_raw = semester_raw[0].split(',')[1].strip()
# strip the whitespace
section_number = section_raw.split(' ')[1]
# find the beginning date of the section
start_date_raw = dom.xpath('//*[@id="main"]/table[2]/tbody/tr[2]/td[1]/text()')
# strip whitespace
start_date_raw = start_date_raw[0].strip()
begin_date = start_date_raw.split("-")[0].strip()
startDate = datetime.datetime.strptime(begin_date, "%m/%d/%Y")
# find the end date of the section and strip whitespace
end = start_date_raw.split("-")[1].strip()
endDate = datetime.datetime.strptime(end, "%m/%d/%Y")

# find the meeting dates
# this is not dealing with multi line meeting dates
# will need to be addressed
meeting_days_raw = dom.xpath('/html/body/div[2]/div[1]/div/div[1]/table[2]/tbody/tr[2]/td[2]//text()')
meeting_days_list = []
for day in meeting_days_raw:
    if len(day.strip()) > 0:
        meeting_days_list.append(day.strip())

# find the meeting times
# this is not dealing with multi line meeting dates
# and will need to be addressed
meeting_times_raw = dom.xpath('//*[@id="main"]/table[2]/tbody/tr[2]/td[3]/text()')

# Deal with online courses with no meeting dates
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
# Create a weekly meeting list
weekly_meetings_list = []
for day in meeting_days_list:
    currentMeetingTime = meetingTime.MeetingTime(day, start_time, end_time)
    weekly_meetings_list.append(currentMeetingTime)

# Find the course status
section_status_raw = dom.xpath('//*[@id="main"]/table[1]/tbody[2]/tr/td[11]/span/text()')
section_status = section_status_raw[0]

# Find the instructor
# Create faculty list
faculty_list = []
faculty_raw = dom.xpath('//*[@id="main"]/table[2]/tbody/tr[2]/td[5]/text()')
for fac in faculty_raw:
    fac = fac.split(',')
    if len(fac) > 1:
        currentFaculty = faculty.Faculty(fac[0].strip(), fac[1].strip())
        faculty_list.append(currentFaculty)
    
# Find the Course Delivery Method
delivery_raw = dom.xpath('//*[@id="main"]/table[1]/tbody[2]/tr/td[13]//text()') 
if len(delivery_raw) == 1:
    delivery = "In-Person"
else:
    delivery = delivery_raw[1].strip()

# Find the section size (seats in the class)
section_size_raw = dom.xpath('//*[@id="main"]/table[4]/tbody/tr/td[2]/text()')
# Strip whitespace
section_size = section_size_raw[1].strip()

# Find the number of students enrolled in the section
section_enrollment_raw = dom.xpath('//*[@id="main"]/table[4]/tbody/tr/td[3]/text()')
# Strip whitespace
enrollment = section_enrollment_raw[1].strip()

# Find the refund date
full_refund_date_raw = dom.xpath('//*[@id="main"]//text()[contains(.,"Full refund")]')
# Strip whitespace
full_refund_text = full_refund_date_raw[0].strip()
date_index = full_refund_text.index("until ")
full_refund_text = full_refund_text[date_index + 6:-5]
refundDate = datetime.datetime.strptime(full_refund_text, "%B %d, %Y, %H:%M%p")

# find the last date to add and drop
last_add_date_and_drop_raw = dom.xpath('//*[@id="main"]//text()[contains(.,"last day to add")]')
# Strip whitespace
last_add_date_and_drop_text = last_add_date_and_drop_raw[0].strip()
# Split the add and drop dates into a list
last_add_date_and_drop = last_add_date_and_drop_text.split('.')
last_add_date = last_add_date_and_drop[0]
last_drop_date = last_add_date_and_drop[1]
last_add_date = last_add_date.split(" is ")[1]
last_drop_date = last_drop_date.split(" is ")[1]
# Creat the add and drop dates
lastAddDate = datetime.datetime.strptime(last_add_date, "%B %d, %Y")
lastDropDate = datetime.datetime.strptime(last_drop_date, "%B %d, %Y")

# Find the last date to withdraw
last_withdraw_date_raw = dom.xpath('//*[@id="main"]//text()[contains(.,"withdraw")]')
# Strip whitespace
last_withdraw_date_text = last_withdraw_date_raw[0].strip()
last_withdraw_date_text = last_withdraw_date_text.split(' is ')[1][0:-1]
lastWithdrawDate = datetime.datetime.strptime(last_withdraw_date_text, "%B %d, %Y")

# Find the in person tuition rate
tuition_resident_raw = dom.xpath('//*[@id="main"]/table[5]/tbody/tr[1]/td/text()')
# Strip the whitespace
tuition_resident = tuition_resident_raw[0].strip()[1:]
tuition_resident = float(tuition_resident)

# Find the out of state tuition rate
tuition__non_resident_raw = dom.xpath('//*[@id="main"]/table[5]/tbody/tr[2]/td/text()')
# Strip the whitespace
tuition_non_resident = tuition__non_resident_raw[0].strip()[1:]
tuition_non_resident = float(tuition_non_resident)

# Find the course fees
fees_raw = dom.xpath('//*[@id="main"]/table[5]/tbody/tr[3]/td/text()')
# Strip the whitespace
fees = fees_raw[0].strip()[1:]
fees = float(fees)

# Find the list of textbooks
textbooks_raw = dom.xpath('//table[@class = "plain"]//text()')
textbooks_raw_list = []
for element in textbooks_raw:
    if element.strip() != '':
        textbooks_raw_list.append(element.strip())
# each textbook is now a list with 16 elements,
# you can divide the list by 16 to get a count of
# textbooks for the course.
num_textbooks = (len(textbooks_raw_list))/16
# Create a list to hold the processed textbook data.
section_textbook_list = []
for tb in range(int(num_textbooks)):
    # Find the information for the current textbook in the list of
    # textbook data...
    textbook_info = textbooks_raw_list[(tb * 16): (tb * 16) + 16]
    # Create a textbook object
    currentTextbook = textbook.Textbook(textbook_info[5], textbook_info[3], required=textbook_info[1], \
                                        publisher=textbook_info[7], isbn=textbook_info[9], \
                                        edition=textbook_info[11], new_price=textbook_info[13], \
                                        used_price=textbook_info[15])
    # add the textbook object to the list of textbooks for the sectoin
    section_textbook_list.append(currentTextbook)

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

print("Section Information ----------------\n", currentSection.__repr__())
