import requests

methods = [{"method":"GET"},{"method":"POST"},{"method":"PUT"},{"method":"DELETE"}]

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Без параметра ответ: " + response.text)


response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "HEAD"})
print(f"HEAD and head " + response.text)
print(response.status_code)

num = 0
while num < 4:

    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type",params=methods[num])
    print(f"GET and {methods[num]['method']} " + response.text)

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=methods[num])
    print(f"POST and {methods[num]['method']} " + response.text)

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=methods[num])
    print(f"PUT and {methods[num]['method']} " + response.text)

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=methods[num])
    print(f"DELETE and {methods[num]['method']} " + response.text)

    num = num + 1


