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
    'Alexandria Techncial and Community College' : ['ATCC', '0203', 'https://www.alextech.edu', '', '', '', ''],
    'Anoka Technical College' : ['ATC', '0202', 'https://www.anokatech.edu', '', '', '', ''],
    'Anoka-Ramsey Community College' : ['ARCC', '0152', 'http://www.anokaramsey.edu', '', '', '', ''],
    'Bemidji State University' : ['BSU', '0070', 'https://www.bemidjistate.edu', '', '', '', ''],
    'Central Lakes College' : ['CLC', '0301', 'http://www.clcmn.edu', '', '', '', ''],
    'Century College' : ['Century', '0304', 'https://www.century.edu', '', '', '', ''],
    'Dakota County Technical College' : ['DCTC', '0211', 'https://www.dctc.edu', '', '', '', ''],
    'Fond du Lac Tribal and Community College' : ['FDLTCC', '0163', 'https://fdltcc.edu', '', '', '', ''],
    'Hennepin Technical College' : ['HTC', '0204', 'https://www.hennepintech.edu', '', '', '', ''],
    'Hibbing Community College' : ['HCC', '0310', 'https://hibbing.edu', '', '', '', ''],
    'Inver Hills Community College' : ['IHCC', '0157', 'https://www.inverhills.edu', '', '', '', ''],
    'Itasca Community College' : ['ICC', '0144', 'https://www.itascacc.edu', '', '', '', ''],
    'Lake Superior College' : ['LSC', '0302', 'https://www.lsc.edu', '', '', '', ''],
    'Mesabi Range College' : ['MRC', '0411', 'https://www.mesabirange.edu', '', '', '', ''],
    'Metropolitan State University' : ['Metro State', '0076', 'https://www.metrostate.edu', '', '', '', ''],
    'Minneapolis Community and Technical College' : ['MCTC', '0305', 'https://www.minneapolis.edu', '', '', '', ''],
    'Minnesota State Community College - Southeast Technical' : ['MSCS', '0213', 'https://www.minneapolis.edu', '', '', '', ''],
    'Minnesota State Community and Technical College' : ['MSCTC', '0142', 'https://www.minnesota.edu', '', '', '', ''],
    'Minnesota State University, Moorhead' : ['MSUM', '0072', 'https://www.mnstate.edu', '', '', '', ''],
    'Minnesota State University, Mankato' : ['MNSU', '0071', 'https://mankato.mnsu.edu', '', '', '', ''],
    'Minnesota West Community and Technical College' : ['MWCTC', '0209', 'https://www.mnwest.edu', '', '', '', ''],
    'Normandale Community College' : ['NCC', '0156', 'http://www.normandale.edu', '', '', '', ''],
    'North Hennepin Community College' : ['NHCC', '0153', 'https://nhcc.edu', '', '', '', ''],
    'Northland Community and Technical College' : ['NCTC', '0303', 'http://www.northlandcollege.edu', '', '', '', ''],
    'Northwest Technical College' : ['NTC', '0263', 'https://www.ntcmn.edu', '', '', '', ''],
    'Pine Technical and Community College' : ['PTCC', '0205', 'http://www.pine.edu', '', '', '', ''],
    'Rainy River Community College' : ['RRCC', '0155', 'https://www.rainyriver.edu', '', '', '', ''],
    'Ridgewater College' : ['RC', '0308', 'https://www.ridgewater.edu', '', '', '', ''],
    'Riverland Community College' : ['RCC', '0307', 'https://www.riverland.edu', '', '', '', ''],
    'Rochester Community and Technical College' : ['RCTC', '0306', 'https://www.rctc.edu', '', '', '', ''],
    'Saint Paul College' : ['SPC', '0206', 'https://www.saintpaul.edu', '', '', '', ''],
    'South Central College' : ['SCC', '0309', 'http://southcentral.edu', '', '', '', ''],
    'Southwest Minnesota State University' : ['SMSU', '0075', 'https://www.smsu.edu', '', '', '', ''],
    'St. Cloud State University' : ['SCSU', '0073', 'https://www.stcloudstate.edu', '', '', '', ''],
    'St. Cloud Technical and Community College' : ['SCTCC', '0208', 'https://www.sctcc.edu', '', '', '', ''],
    'Vermillion Community College' : ['VCC', '0147', 'https://www.vcc.edu', '', '', '', ''],
    'Winona State University' : ['WSU', '0074', 'https://www.winona.edu', '', '', '', ''],
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
