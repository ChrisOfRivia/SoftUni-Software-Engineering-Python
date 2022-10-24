companies = {}

while True:
    company_and_id = input()
    if company_and_id == 'End':
        break
    split = company_and_id.split(" -> ")
    company = split[0]
    id_num = split[1]
    if company not in companies:
        companies[company] = []
    if id_num not in companies[company]:
        companies[company].append(id_num)

for company in companies.keys():
    print(company)
    for ids in companies[company]:
        print(f'-- {ids}')