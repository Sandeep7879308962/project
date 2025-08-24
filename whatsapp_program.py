import matplotlib.pyplot as plt


member_dict = {
    "Banna" : 0,
    "nikhil thakur" : 0,
    "ठाkur Shubham Singh" : 0,
    "Shiva" : 0,
    "Thakur Gourav" : 0,
    "shivraj siv da" : 0,
    "vishal broh" : 0,

}


with open("whatsapp_chate.txt","r",encoding='utf-8') as file:
    data = file.readlines()
    
for member in member_dict:
    for data_line in data:
        if(member in data_line):
            member_dict[member]+=1

member_list = []
msg_list  = []

for key,valu in zip(member_dict.keys(),member_dict.values()):
    member_list.append(key)
    msg_list.append(valu)

  
# # pie chart----

plt.pie(msg_list,labels=member_list,autopct="%1.1f%%")
plt.title("Msg percentage",color="red")
plt.show() 
    

#line chart---

total_msg = 1372

msg_percentage = []
percentage = 0
for msg in msg_list:
    percentage = round((msg / total_msg) * 100)
    
    msg_percentage.append((percentage))

plt.plot(member_list,msg_percentage,label="percentage",color="green",marker="o",markerfacecolor="black")

plt.title("Member Msg-percentage",color="red")
plt.xlabel("-Members-")
plt.ylabel("-Percentage %-")
plt.yticks(range(0, 110, 10))  
plt.legend(loc="upper right")
plt.grid(axis='y', linestyle='--')
plt.show()


# bar chart---------

total_msg = 1372
msg_percentage = []
percentage = 0
for msg in msg_list:
    percentage = round((msg / total_msg) * 100)
    
    msg_percentage.append((percentage))


plt.bar(member_list,msg_percentage,label="Msg percentage")
plt.tick_params(axis= "y")
plt.title("--Member Msg-percentage--")
plt.xlabel("Members",color="r")
plt.ylabel("Msg percentage",color="r")
plt.yticks(range(0,110,10))
plt.grid(axis="y",linestyle="--",color="green")
plt.legend()
plt.show()

# scatter plot chart-----

total_msg = 1372
msg_percentage = []
percentage = 0
for msg in msg_list:
    percentage = round((msg / total_msg) * 100)
    
    msg_percentage.append((percentage))


plt.scatter(member_list,msg_percentage,color="blue",marker="o",label="Msg percentage")
plt.title("--Member Msg-percentage--",color="red")
plt.xlabel("Members",color="r")
plt.ylabel("Msg percentage",color="r")
plt.yticks(range(0,110,10))
plt.grid(color="green")
plt.legend()
plt.show()