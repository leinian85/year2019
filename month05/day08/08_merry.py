import pandas as pd

left = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'student_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'class_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
    'gender': ['M', 'M', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'F'],
    'score': [60, 77, 68, 90, 55, 56, 88, 84, 86, 90]
})
right = pd.DataFrame(
    {'class_id': [1, 2, 3, 5],
     'class_name': ['ClassA', 'ClassB', 'ClassC', 'ClassE']})

df = pd.merge(left, right)
print(df)

print("#" * 50, ' 透视')
# 透视表,以classid与gender字段进行分组
r = df.pivot_table(index=['class_id', 'gender'],
                   margins=True,
                   values=['score'])
print(r)

r = df.pivot_table(index=['class_id'],
                   columns=['gender'],
                   values=['score'],
                   # aggfunc='max',
                   margins=True)
print(r)
