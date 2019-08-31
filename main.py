import file_operations
from faker import Faker
import random

fake = Faker("ru_RU")

context = {
  "first_name": "Денис",
  "last_name": "Самборский",
  "job": "Программист",
  "town": "Красноярск"
}

skills = [
  "Стремительный прыжок",
  "Электрический выстрел",
  "Ледяной удар",
  "Стремительный удар",
  "Кислотный взгляд",
  "Тайный побег",
  "Ледяной выстрел",
  "Огненный заряд"
]

runic_letters = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

def rand_abilities(dictionary, *abilities):
  for ability in abilities:
    dictionary[ability] = random.randint(8, 14)

for charsheet in range(10):
  runic_skills = []
  context = {
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "job": fake.job(),
    "town": fake.city()
  }

  rand_abilities(context, "strength", "agility", "endurance", "intelligence", "luck")

  npc_skills = random.sample(skills, 3)

  for skill_number, skill in enumerate(npc_skills):
    skill_word = []
    for letter in npc_skills[skill_number]:
      skill_word.append(runic_letters[letter])
    runic_skills.append(''.join(skill_word))
    context['skill_{}'.format(skill_number+1)] = runic_skills[skill_number]

  file_operations.render_template("charsheet.svg", "charsheet/charsheet-{}.svg".format(charsheet), context)