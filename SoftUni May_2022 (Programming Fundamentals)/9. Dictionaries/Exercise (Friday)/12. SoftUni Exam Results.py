submissions = {}
individual_submissions = {}

while True:
    exam_score = input()
    if exam_score == 'exam finished':
        break
    split_text = exam_score.split("-")
    if len(split_text) > 2:
        username, language, score = split_text[0], split_text[1], split_text[2]
        if language not in submissions.keys():
            submissions[language] = [username]
        else:
            submissions[language] += [username]

        if username not in individual_submissions.keys():
            individual_submissions[username] = []
        individual_submissions[username] += [int(score)]
    else:
        username = split_text[0]
        del individual_submissions[username]

print(f'Results:')
for user, score in individual_submissions.items():
    print(f'{user} | {max(score)}')
print(f'Submissions:')
for language, users in submissions.items():
    print(f'{language} - {len(users)}')