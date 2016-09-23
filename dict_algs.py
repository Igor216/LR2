ivan  = {
	"name":"ivan",
	"age":34,
	"children":[{
		"name":"vasja",
		"age":12,
	}, {
		"name":"petja",
		"age":10,
	}],
}
darja = {
	"name":"darja",
	"age":41,
	"children":[{
		"name":"kirill",
		"age":21,
	}, {
		"name":"pavel",
		"age":21,
	}],
}
emps=[ivan, darja]
name=[]
for i in emps:
	for j in i["children"]:
			if j["age"]>18:
				name.append(i["name"])
				break
print(name)
