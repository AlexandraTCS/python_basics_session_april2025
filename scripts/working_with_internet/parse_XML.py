from xml.dom import minidom

# Sample XML data
xml_data = '''<?xml version="1.0" encoding="UTF-8"?>
<students>
    <student id="1">
        <name>John Doe</name>
        <age>20</age>
        <major>Computer Science</major>
        <gpa>3.8</gpa>
    </student>
    <student id="2">
        <name>Jane Smith</name>
        <age>22</age>
        <major>Mathematics</major>
        <major>Computer Science</major>
        <gpa>3.9</gpa>
    </student>
    <student id="3">
        <name>Michael Johnson</name>
        <age>21</age>
        <major>Physics</major>
        <gpa>3.7</gpa>
    </student>
</students>'''

def print_student_data(student):
    student_id = student.getAttribute("id")  # Get the 'id' attribute
    name = student.getElementsByTagName("name")[0].firstChild.nodeValue
    age = student.getElementsByTagName("age")[0].firstChild.nodeValue
    majors = student.getElementsByTagName("major")
    major_list = [major.firstChild.nodeValue for major in majors]
    gpa = student.getElementsByTagName("gpa")[0].firstChild.nodeValue
    # Print the student's details
    print(f"ID: {student_id}")
    print(f"Name: {name}")
    print(f"Age: {age}")        
    print(f"majors: {', '.join(major_list)}")
    print(f"GPA: {gpa}")
    print("-" * 30)



# Parse the XML data
dom = minidom.parseString(xml_data)

# Access the root element
root = dom.documentElement
print("Root Element:", root.tagName)

# Get all <student> elements
students = root.getElementsByTagName("student")

# print out the document node and the name of the first child tag name
print("Student Information:")
# Iterate through the <student> elements
for student in students:
    print_student_data(student)



