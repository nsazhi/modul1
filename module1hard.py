grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
table = {}
list_students = sorted(students)
sum1 = sum(grades[0])
len_grades1 = len(grades[0])
mean1 = sum1/len_grades1
table.update({list_students[0] : mean1})
sum2 = sum(grades[1])
len_grades2 = len(grades[1])
mean2 = sum2/len_grades2
table.update({list_students[1]: mean2})
sum3 = sum(grades[2])
len_grades3 = len(grades[2])
mean3 = sum3/len_grades3
table.update({list_students[2]: mean3})
sum4 = sum(grades[3])
len_grades4 = len(grades[3])
mean4 = sum4/len_grades4
table.update({list_students[3]: mean4})
sum5 = sum(grades[4])
len_grades5 = len(grades[4])
mean5 = sum5/len_grades5
table.update({list_students[4]: mean5})
print(table)
