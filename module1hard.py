grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# множество с неупорядоченной последовательностью имен переводим в список имен по возрастанию (алфавиту)
students_sort=sorted(students)
# g1 = grades[0]
# average1=sum(g1)/len(g1)
# g2 = grades[1]
# average2=sum(g2)/len(g2)
# g3 = grades[2]
# average3=sum(g3)/len(g3)
# g4 = grades[3]
# average4=sum(g4)/len(g4)
# g5 = grades[4]
# average5=sum(g5)/len(g5)
# dict_grades={students_sort[0]:average1, students_sort[1]:average2, students_sort[2]:average3, students_sort[3]:average4, students_sort[4]:average5}
# average_0=sum(grades[0])/len(grades[0]) # последовательно определяем средний балл студентов,
# average_1=sum(grades[1])/len(grades[1]) # поскольку списки оценок для каждого ученика заданы
# average_2=sum(grades[2])/len(grades[2]) # в алфавитном порядке
# average_3=sum(grades[3])/len(grades[3])
# average_4=sum(grades[4])/len(grades[4])
# dict_average_grades={students_sort[0]:average_0, students_sort[1]:average_1, students_sort[2]:average_2, students_sort[3]:average_3, students_sort[4]:average_4}
# print(dict_average_grades)
# создаем список со средним баллом учеников в классе в алфавитном порядке
average=[sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
# составляем словарь, где ключ - имя ученика, а значение - средний балл, и выводим его в консоль
dict_average={students_sort[0]: average[0],students_sort[1]: average[1],students_sort[2]: average[2],students_sort[3]: average[3],students_sort[4]: average[4]}
print(dict_average)