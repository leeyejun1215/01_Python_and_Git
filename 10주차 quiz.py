# 선 그래프
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title('선 그래프')
plt.xlabel('X 값')
plt.ylabel('Y 값')
plt.grid(True)
plt.show()

# 막대 그래프
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]

plt.bar(categories, values, color='skyblue')
plt.title('막대 그래프')
plt.xlabel('카테고리')
plt.ylabel('값')
plt.show()

# 히스토그램
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('히스토그램')
plt.xlabel('값')
plt.ylabel('빈도')
plt.show()

# 원 그래프
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [25, 30, 20, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('원 그래프')
plt.axis('equal')  # 원형으로 표시
plt.show()

# 산포도 그래프
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='purple')
plt.title('산포도 그래프')
plt.xlabel('X 값')
plt.ylabel('Y 값')
plt.show()

# 상자 그림
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)  # 정규 분포를 따르는 100개의 데이터

plt.boxplot(data)
plt.title('상자 그림')
plt.ylabel('값')
plt.show()


# 열 지도
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 12)

plt.imshow(data, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.title('열 지도')
plt.show()
