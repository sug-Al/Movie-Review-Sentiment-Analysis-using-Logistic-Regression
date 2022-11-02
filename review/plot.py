import matplotlib.pyplot as plt
import seaborn as sns

# data = {'Negative reviews': 20019, 'Positive reviews': 19981}
# name = list(data.keys())
# value = list(data.values())

# plt.title("Train dataset")
# plt.xlabel("Count")
# plt.ylabel("Reviews")
# barlist = plt.barh(name, value)
# barlist[0].set_color('r')
#
# for index, value in enumerate(value):
#     plt.text(value, index,
#              str(value))

sns.set_theme(style="ticks", color_codes=True)

data1 = {'With libary train accuracy': 92.0625,
         'Without libary train accuracy': 89.31,
         'With libary test accuracy': 89.02,
         'Without libary test accuracy': 88.52
         }

# data2 = {'Without libary train accuracy': 89.31,
#          'Without libary test accuracy': 88.52
#          }

name1 = list(data1.keys())
value1 = list(data1.values())

# name2 = list(data2.keys())
# value2 = list(data2.values())

plt.title("Accuracy with/without library")
plt.ylabel("Percentage")
# plt.ylabel("")

barlist = plt.plot(name1, value1, marker='o', mfc = 'r')
# barlist = plt.plot(name2, value2)

# barlist[0].set_color('r')
# barlist[1].set_color('pink')
# barlist[2].set_color('#4CAF50')

# for index, value in enumerate(value1):
#     plt.text(value, index,
#              str(value))

plt.show()
