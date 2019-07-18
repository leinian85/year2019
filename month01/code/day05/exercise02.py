list_student = []
list_score = []
while True:
    name = input("学生：")
    if name == "":
        break
    score = float(input("成绩："))
    list_student.append(name)
    list_score.append(score)

lens = len(list_score)
for index in range(0, lens):
    print("姓名：%s 成绩：%.1f" % (list_student[index], list_score[index]))
print("最高分：%.1f 最低分：%.1f 平均分：%.2f" % (max(list_score), min(list_score), sum(list_score) / lens))
