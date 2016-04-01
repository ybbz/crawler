  # encoding=utf-8

  import mysql.connector
  import pandas as pd
  import seaborn as sns
  import matplotlib.pyplot as plt

  # connect database
  conn = mysql.connector.connect(host="hostname", user="username", passwd="password", db="database")
  cursor = conn.cursor()
  # query data
  cursor.execute('select count(*),max(reply),min(reply),max(watch),min(watch) from ibeike')
  values1 = cursor.fetchall()
  print("ibeike:totally" + str(values1[0][0]) + "data")
  list = [('highest reply', values1[0][1]), ('lowest reply', values1[0][2]), ('hightest watch', values1[0][3]),
          ('lowest watch', values1[0][4])]
  # draw picture
  budget = pd.DataFrame(list, columns=['type', 'count'])
  sns.set_style("darkgrid")
  bar_plot = sns.barplot(x=budget["type"], y=budget["count"], palette="muted", order=budget["type"].tolist())
  plt.show()


  # query data
  cursor.execute('select count(id),groups from ibeike group by groups')
  values2 = cursor.fetchall()
  values2.append((values1[0][0], 'all sort'))
  result = sorted(values2)
  result.reverse()
  # draw picture
  budget = pd.DataFrame(result, columns=['count', 'sort'])
  sns.set_style("darkgrid")
  bar_plot = sns.barplot(x=budget["sort"], y=budget["count"], palette="muted", order=budget["sort"].tolist())
  plt.xticks(rotation=30)
  plt.show()
