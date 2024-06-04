carList = ["Gene", "Lex", "Infini", "Lambor", "Linc"]
print("현재 차종:", carList)

carList.append("Merce")
print("(1) Merce 차종 추가:", carList)

carList.remove("Lex")
print("(2) Lex 차종 단종:", carList)

carList.append("Gene-2019")
print("(3) Gene 2019년형 추가:", carList)

print("(4) 두 번째로부터 네 번째 개발한 모델:", carList[1:4])
