import matplotlib.pyplot as plt

decades = [1980,1990,2000,2010,2020]
omapops = [314255,357807,409868,408958,478182]
nolapops = [557515,496938,483663,343829,390144]
lincolnpops = [171932,192722,227701,258379,289102]
kcpops = [448159,435121,442369,459787,495327]

# As a Line Graph
plt.plot(decades, omapops, color='blue', label='Omaha')
plt.plot(decades, nolapops, color='red', label='New Orleans')
plt.plot(decades, lincolnpops, color='orange', label='Lincoln')
plt.plot(decades, kcpops, color='violet', label='Kansas City')

plt.title('City Populations')
plt.xlabel('Decades')
plt.ylabel('Population')
plt.legend()

plt.show()

# As a Bar Graph
plt.bar(decades, nolapops, color='red', label='New Orleans')
plt.bar(decades, kcpops, color='violet', label='Kansas City')
plt.bar(decades, omapops, color='blue', label='Omaha')
plt.bar(decades, lincolnpops, color='orange', label='Lincoln')

plt.title('City Populations')
plt.xlabel('Decades')
plt.ylabel('Population')
plt.legend()

plt.show()