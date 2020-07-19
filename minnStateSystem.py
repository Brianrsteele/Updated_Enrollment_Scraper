#
#   minnStateSystem.py
#   8/6/2019
#   Brian R Steele
#
#   Contain information for the Minnesota State Colleges and Universities System.
#
from system import System


class MinnStateSystem(System):
    """
    A utility class for storing information about the MinnState system, subclass of system
    """

    # The base URL for the MnSCU course schedule site
    BASE_SCHEDULE_URL = 'https://webproc.mnscu.edu/registration/search/detail.html'

    # List holds information about MinnState schools in the format [(id_num, name, abbrev, URI),...]
    MINN_STATE_INFO= [ ('0203', 'Alexandria Techncial and Community College', 'ATCC', 'https://www.alextech.edu'),
                          ('0202', 'Anoka Technical College', 'ATC', 'https://www.anokatech.edu'),
                          ('0152', 'Anoka-Ramsey Community College', 'ARCC', 'http://www.anokaramsey.edu'),
                          ('0070', 'Bemidji State University', 'BSU', 'https://www.bemidjistate.edu'),
                          ('0301', 'Central Lakes College', 'CLC', 'http://www.clcmn.edu'),
                          ('0304', 'Century College', 'Century', 'https://www.century.edu'),
                          ('0211', 'Dakota County Technical College', 'DCTC', 'https://www.dctc.edu'),
                          ('0163', 'Fond du Lac Tribal and Community College', 'FDLTCC', 'https://fdltcc.edu'),
                          ('0204', 'Hennepin Technical College', 'HTC', 'https://www.hennepintech.edu'),
                          ('0310', 'Hibbing Community College', 'HCC', 'https://hibbing.edu'),
                          ('0157', 'Inver Hills Community College', 'IHCC', 'https://www.inverhills.edu'),
                          ('0144', 'Itasca Community College', 'ICC', 'https://www.itascacc.edu'),
                          ('0302', 'Lake Superior College', 'LSC', 'https://www.lsc.edu'),
                          ('0411', 'Mesabi Range College', 'MRC', 'https://www.mesabirange.edu'),
                          ('0076', 'Metropolitan State University', 'Metro State', 'https://www.metrostate.edu'),
                          ('0305', 'Minneapolis Community and Technical College', 'MCTC',
                           'https://www.minneapolis.edu'),
                          ('0213', 'Minnesota State Community College - Southeast Technical', 'MSCS',
                        'https://www.minneapolis.edu'),
                          ('0142', 'Minnesota State Community and Technical College', 'MSCTC',
                        'https://www.minnesota.edu'),
                          ('0072', 'Minnesota State University Moorhead', 'MSUM', 'https://www.mnstate.edu'),
                          ('0071', 'Minnesota State University Mankato', 'MNSU', 'https://mankato.mnsu.edu'),
                          ('0209', 'Minnesota West Community and Technical College', 'MWCTC', 'https://www.mnwest.edu'),
                          ('0156', 'Normandale Community College', 'NCC', 'http://www.normandale.edu'),
                          ('0153', 'North Hennepin Community College', 'NHCC', 'https://nhcc.edu'),
                          ('0303', 'Northland Community and Technical College', 'NCTC',
                        'http://www.northlandcollege.edu'),
                          ('0263', 'Northwest Technical College', 'NTC', 'https://www.ntcmn.edu'),
                          ('0205', 'Pine Technical and Community College', 'PTCC', 'http://www.pine.edu'),
                          ('0155', 'Rainy River Community College', 'RRCC', 'https://www.rainyriver.edu'),
                          ('0308', 'Ridgewater College', 'RC', 'https://www.ridgewater.edu'),
                          ('0307', 'Riverland Community College', 'RCC', 'https://www.riverland.edu'),
                          ('0306', 'Rochester Community and Technical College', 'RCTC', 'https://www.rctc.edu'),
                          ('0206', 'Saint Paul College', 'SPC', 'https://www.saintpaul.edu'),
                          ('0309', 'South Central College', 'SCC', 'http://southcentral.edu'),
                          ('0075', 'Southwest Minnesota State University', 'SMSU', 'https://www.smsu.edu'),
                          ('0073', 'St. Cloud State University', 'SCSU', 'https://www.stcloudstate.edu'),
                          ('0208', 'St. Cloud Technical and Community College', 'SCTCC', 'https://www.sctcc.edu'),
                          ('0147', 'Vermillion Community College', 'VCC', 'https://www.vcc.edu'),
                          ('0074', 'Winona State University', 'WSU', 'https://www.winona.edu') ]

    def __init__(self, name, abbreviation, url=None, number=None):
        """
           Constructor for MinnStateSystem objects
           :param abbreviation: string, the abbreviation of the MinnState system
           :param name: string, The full name of the MinnState system
           :param url: string, The url of the MinnStateSystem including https.
        """
        super(System, self).__init__(name, abbreviation, url)
        self.number = number

    def __repr__(self):
        return self.number + ", " + self.abbreviation + ", " + self.name + ", " + self.url
