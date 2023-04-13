f = '{"Name":"Lorem","Allergies":"ipsum", "id": "4CF73749"}'
l = f.split(":")
e = l[3]

e = e.rstrip(e[-1])


print(e)