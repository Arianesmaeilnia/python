shop_data = {"shop_name" : "tech_store" ,"daily_sales " : [120,50,300,80,150]}


total_sales = 0

for sale in shop_data["daily_sales "] :

    total_sales = total_sales + sale

shop_data[ "totalrevenue"] = total_sales

if total_sales > 500:
    shop_data [ "performance"] = "excelent"
else : shop_data[ "performance"] = "normal"


print(shop_data)