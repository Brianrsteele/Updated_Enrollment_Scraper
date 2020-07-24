import sectionPageScraper
import minnStateSystem

currentSystem = minnStateSystem.MinnStateSystem()

test_files = [
    'sample_pages/art-history.html',
    'sample_pages/carpentry.html',
    'sample_pages/example.html',
    'sample_pages/fees_textbooks.html',
    'sample_pages/grad-photo.html',
    'sample_pages/inclass-example.html',
    'sample_pages/mlv.html',
    'sample_pages/ojibway.html',
    'sample_pages/vet-tech.html'
]

for test_file in test_files:
    # read an example html file as a string
    with open(test_file, 'r') as file:
        page_file = file.read()
    page_scraper = sectionPageScraper.SectionPageScraper(page_file, currentSystem)

semesters = currentSystem.semesters.keys()

for key in semesters:
    print(key)
    schools = currentSystem.semesters[key].schools.keys()
    for school in schools:
        print("\t" + school)
        for dept in currentSystem.semesters[key].schools[school].departments.keys():
            print("\t\t" + dept)
            for crs in currentSystem.semesters[key].schools[school].departments[dept].courses.keys():
                print("\t\t\t" + crs)
                for sctns in currentSystem.semesters[key].schools[school].departments[dept].courses[crs].sections.keys():
                    print("\t\t\t\t" + sctns + " - "
                          + str(currentSystem.semesters[key].schools[school].departments[dept].courses[crs].sections[sctns].instructor))






