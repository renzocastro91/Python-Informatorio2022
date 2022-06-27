import ast
x = str({"Telefono": 65656565, "Direccion":65656565})

#print(str(x))

print(ast.literal_eval(str(x)))