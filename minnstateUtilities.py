#   minnstateUtilites.py
#   4/30/2020
#   Brian R Steele
#
#   information about Minnstate campuses and schools to assist
#	with related classes.
#



    
# Dictionary with campus and school information
# Don't repeat yourself.
system_info = {
    'Minnesota State' : ['Minnstate', 
            '', 'http://minnstate.edu', '30 East 7th Street', 'St. Paul', 'MN', '55101-7804'],
    'Rochester Community & Technical College' : ['RCTC', 
            '306', 'http://rctc.edu', '851 30th Ave SE','Rochester', 'MN','55904-4999'],
    'Rochester Community and Technical College' : ['RCTC', 
            '306', 'http://rctc.edu', '851 30th Ave SE','Rochester', 'MN','55904-4999'],
    'Normandale Community College' : ['Normandale', 
            '156','http://normandale.edu', '9700 France Avenue South', 'Bloomington', 'MN', '55431']
    
    }

def populateCampusInformation(campus_instance):
   """
       Populates a campus object with campus information
       
       :param campus_instance: a campus object
   """ 
   
   if campus_instance.name in system_info.keys():
       
       if (campus_instance.street_address == None):
           campus_instance.street_address = system_info[campus_instance.name][3]
       
       if (campus_instance.city == None):
           campus_instance.city = system_info[campus_instance.name][4]
       
       if (campus_instance.state == None):
           campus_instance.state = system_info[campus_instance.name][5]
       
       if (campus_instance.postal_code == None):
           campus_instance.postal_code = system_info[campus_instance.name][6]


def populateSchoolInformation(school_instance):
   """
       Populates a school object with school information
       
       :param school_instance: a school object
   """ 
   
   if school_instance.full_name in system_info.keys():
       
       
       
       if(school_instance.abbreviation == None):
           school_instance.abbreviation = system_info[school_instance.full_name][0]
       
       if(school_instance.id_number == None):
           school_instance.id_number = system_info[school_instance.full_name][1]
       
       if(school_instance.url == None):
           school_instance.url = system_info[school_instance.full_name][2]
       
       if (school_instance.street_address == None):
           school_instance.street_address = system_info[school_instance.full_name][3]
       
       if (school_instance.city == None):
           school_instance.city = system_info[school_instance.full_name][4]
       
       if (school_instance.state == None):
           school_instance.state = system_info[school_instance.full_name][5]
       
       if (school_instance.postal_code == None):
           school_instance.postal_code = system_info[school_instance.full_name][6]
