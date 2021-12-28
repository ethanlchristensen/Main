import matplotlib.pyplot as plt

# Data From https://www.omnicoreagency.com/youtube-statistics/
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018]
users = [0.8, 1, 1.1, 1.2, 1.4, 1.5, 1.8]
colors = ['red','orange','yellow','#00ff00','b', 'indigo','violet'] # notice we can use the word, character, or hex

# Start of creating a Bar Graph with Single Bar color
plt.title('Number of YouTube Users over the Years')
plt.xlabel('Years')
plt.ylabel('Users (In Billions)')
plt.bar(years, users, color='violet')
plt.show()

# Start of creating a Bar Graph with Mutli Bar color
plt.title('Number of YouTube Users over the Years')
plt.xlabel('Years')
plt.ylabel('Users (In Billions)')
# Now we will plot graph with plt.bar(x-values, y-values, color='bar-color / colors')
plt.bar(years, users, color=colors)
plt.show()

# Start of creating a line graph
plt.title('Number of YouTube Users over the Years')
plt.xlabel('Years')
plt.ylabel('Users (In Billions)')
# Next we will plot the points (x , y) with x = year and y = users.
# We will give the line a color of red and a label of Users Over the Years
# Plot points with plt.plot(x-values,y-values, color='line-color', label='line-label' *for legend*
plt.plot(years, users, color="red", label="Users Over the Years")
plt.legend() # Create a legend with the corresponding line, line color, and line label
plt.show()