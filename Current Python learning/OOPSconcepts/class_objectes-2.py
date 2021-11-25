# class Students:
#     leaves = 4
#     def __init__(self, a_name, a_section):
#         self.name = a_name
#         self.section = a_section
#
#
#     def print_details(self):
#         return "Name is {}, section in {}".format(self.name, self.section)
#
#     @classmethod
#     def leave_change(cls, new_leave):
#         cls.leaves = new_leave
#
# # #liyakhat = Students("hello", 5) # I cannot do it because we have not yet constructed the Students class...
# liyakhat = Students("liyakhat", 13)
# # liyakhat.name = "liyakhat"
# # liyakhat.section = 13
# # liyakhat.leaves = 14
# # print(liyakhat.print_details())
# # print(liyakhat.name)
# # print(liyakhat.section)
# Students.leave_change(15)
# print(liyakhat.leaves)


# class StudentDetails:
#
#     def __init__(smtg, name, rrn, marks):
#         smtg.name = name
#         smtg.rrn = rrn
#         smtg.marks = marks
#
#     def details(smtg):
#         print(f"Name: {smtg.name}, RRN: {smtg.rrn}")
#
#     def marks_mere(smtg):
#         subjects = ["Maths", "Physics", "Computers"]
#         for i in range(0, 3):
#             print(f"{subjects[i]} = {smtg.marks[i]}")
#
#
# Mere_details = StudentDetails("liyakhat", 3249257, [24, 25, 26])
#
# Mere_details.details()
# Mere_details.marks_mere()
#
# class Employee:
#
#     def __init__(self, a_name, a_id, a_leaves):
#         self.name = a_name
#         self.id = a_id
#         self.leaves = a_leaves
#
#     def details(self):
#         return f"Name: {self.name} \nID: {self.id} \nNumber of Leaves: {self.leaves}"
#
#
# mere_employee = Employee("Liyakhat", 542523, 5)
# print(mere_employee.details())

# class Empty:
#     pass
#
# smtg = Empty()
# smtg.name = "Liyakhat"
# smtg.id = 8475182
# print(smtg.name)
# print(smtg.id)
# del smtg.name
# print(smtg.name)
