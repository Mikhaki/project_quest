import random
import sys

class Player:
    def __init__(self):
        self.health_points = 70
        self.intellect_points = 40
        self.social_points = 20
        self.study_at_home_town_bonus = False
        self.exhausted = False
        self.game_over = False

    def change_hp(self, points):
        self.health_points += points
        if self.health_points > 100:
            self.health_points = 100
        print(f"Здоровье изм. на {points}, всего {self.health_points}")
        if 0 <= self.health_points <= 20:
            print("Низкий уровень здоровья, будьте осторожны")
        if self.health_points <= 0:
            print("Достигнут критический уровень здоровья. Игра окончена.")
            self.end_game("Вот что бывает, когда не думаешь о своём здоровье...")

    def change_int(self, points):
        self.intellect_points += points
        print(f"Интеллект изм. на {points}, всего {self.intellect_points}")
        if self.intellect_points <= 0:
            print("Интеллект опустился до нуля. Игра окончена.")
            self.end_game("Вы забыли, каково это - учиться...")

    def change_soc(self, points):
        self.social_points += points
        if self.social_points > 100:
            self.social_points = 100
        print(f"Социальные пойнты изм. на {points}, всего {self.social_points}")
        if self.social_points <= 0:
            print("Критический уровень социальных навыков. Игра окончена.")
            self.end_game("Социальная изоляция - худшее наказание... наказали вы себя сами.")

    def end_game(self, ending_text):
        print(f"\n=== Концовка ===\n{ending_text}\n")
        self.game_over = True
        sys.exit()

player = Player()

class Achievements:
    def __init__(self):
        self.lesson_count = 0
        self.extra_curriculum_count = 0
        self.right_answer_count = 0
        self.wrong_answer_count = 0

        self.no_wrong_answers = False
        self.no_right_answers = False
        self.all_right_answers = False
        self.all_wrong_answers = False
        self.been_at_all_lessons = False
        self.max_truant = False
        self.attend_extra_lesson = False

        self.sport_lesson_count = 0
        self.truant_count = 0

        self.sport_enthusiast = False
        self.social_butterfly = False
        self.scholar = False
        self.health_lover = False
        self.volunteer_vanguard = False

    def answer_achievement(self):
        if self.right_answer_count == 5:
            self.all_right_answers = True
            print("Получено достижение: вы ответили верно на все возможные вопросы")
        if self.wrong_answer_count == 5:
            self.all_wrong_answers = True
            print("Получено достижение: вы ответили неправильно на все возможные вопросы")

    def attend_lessons(self):
        if (self.right_answer_count + self.wrong_answer_count == 5
                and self.attend_extra_lesson):
            self.been_at_all_lessons = True
            print("Получено достижение - ударник: вы побывали на каждой паре (даже на чужих)")
        if (self.right_answer_count + self.wrong_answer_count == 3
                and not self.attend_extra_lesson):
            self.max_truant = True
            print("Получено достижение - прогульщик: вы пропускали пары каждый раз, когда была возможность")

    def check_gameplay_achievements(self):
        if self.sport_lesson_count >= 2 and not self.sport_enthusiast:
            self.sport_enthusiast = True
            print("Получено достижение - фанат фитнеса: здоровое тело - здоровый ум... или как там?")

        if player.social_points >= 80 and not self.social_butterfly:
            self.social_butterfly = True
            print("Получено достижение - душа компании: связи помогут вам, когда ничто другое не поможет")

        if player.intellect_points >= 120 and not self.scholar:
            self.scholar = True
            print("Получено достижение - академический гений: вы полагаетесь на свою приверженность науке")

        if volunteer_day.accepted and not self.volunteer_vanguard:
            self.volunteer_vanguard = True
            print("Получено достижение - образцовый волонтёр: вас ценят за ваше неравнодушие.")


achievement = Achievements()


class Questions:
    def __init__(self, question_text, right_answer, text_right_answer, text_wrong_answer, day):
        self.question_text = question_text
        self.right_answer = right_answer
        self.text_right_answer = text_right_answer
        self.text_wrong_answer = text_wrong_answer
        self.day = day

    def trigger(self):
        print(self.question_text)
        answer = input("Введите правильный ответ (цифра): ")
        if answer == self.right_answer:
            print(self.text_right_answer)
            player.change_int(10)
            player.change_soc(5)
            achievement.right_answer_count += 1
        else:
            print(self.text_wrong_answer)
            print("Правильный ответ:", self.right_answer)
            player.change_int(5)
            player.change_soc(-5)
            achievement.wrong_answer_count += 1


question_1 = Questions(
    """Гиперфонема - это:
1) долгая фонема
2) фонема под ударением
3) фонема, которая не бывает под ударением""",
    "3",
    "Да, это правильное определение гиперфонемы.",
    "Увы, ответ неверный.",
    1)

question_2 = Questions(
    """Единицей фонетического членения речи является:
1) синекдоха
2) синтагма
3) семема""",
    "2",
    "Именно так!",
    "Ответ неверный. Кажется, вы запутались в определениях.",
    2)

question_3 = Questions(
    """Имя автора теории генеративной грамматики:
1) Noam Chomsky
2) Nom Chompsky
3) Nim Chimpsky""",
    "1",
    "Правильно! Хорошо, что вы помните не только теорию, но и тех, кто сделал вклад в развитие науки.",
    "Неверно. Вы потеряли грань между мемами и суровой реальностью лингвистической теории.",
    3)

question_4 = Questions(
    """К индоевропейской семье языков не относят:
1) албанский
2) финский
3) готский""",
    "2",
    "Отлично! Ваш одногруппник-фанат уральских языков готов пожать вам руку.",
    "Неверно! Стоит повторить теорию по языкам мира.",
    4)

question_5 = Questions(
    """Какая из грамматических категорий в русском языке для имен существительных является классифицирующей?
1) падеж
2) число
3) род""",
    "3",
    "Хорошо! Изучая иностранные языки, не забывайте про свой родной.",
    "Неправильный ответ. Ох уж эти грамматические категории...",
    5)

question_6 = Questions(
    """Электрический” и “электронный” это..:
1) типичные онимы
2) частичные синонимы
3) просто паронимы""",
    "3",
    "Верно! Это действительно было просто.",
    "Неправильно! Кажется, вы снова не подготовились к семинару по лексикологии.",
    6)

question_7 = Questions(
    """Выберите неправильное утверждение:
1) буква не является знаком
2) аккомодация  происходит между звуками разного типа
3) “глокая куздра” была придумана Л. В. Щербой""",
    "1",
    "Преподаватель доволен вашим ответом.",
    "Неверно!",
    7)

question_list = [question_1, question_2, question_3, question_4, question_5, question_6, question_7]


class RandomEvents:
    def __init__(self, name):
        self.name = name
        self.day = 0
        self.happened = False
        self.check = False
        self.accepted = False

    def day_check(self, day):
        if self.day == day:
            self.check = True


transport_event = RandomEvents("transport_event")
lecturer_ill = RandomEvents("lecturer_ill")
sport_lesson = RandomEvents("sport_lesson")
volunteer_day = RandomEvents("volunteer_day")
truant_offer = RandomEvents("truant_offer")

random_event_list = [transport_event, lecturer_ill, sport_lesson, volunteer_day, truant_offer]

x = [2, 3, 4, 5, 6]
random.shuffle(x)
for i, event in enumerate(random_event_list):
    event.day = x[i]
    print(event.day)


def introduction():
    print("Поздравляем! Вы поступили в наш университет. В целях сбора статистики ответьте на три вопроса:")
    a = int(input("Вы поступили в университет, находящийся в вашем родном городе? Да / Нет (1, 2) "))
    b = int(input("Вы получили место на бюджетной основе? Да / Нет (1, 2) "))
    c = int(input("Вы узнали о нашем вузе от друзей / знакомых / родственников? Да / Нет (1, 2) "))
    if a == 1:
        player.study_at_home_town_bonus = True
    if b == 1:
        player.change_int(10)
    if c == 1:
        player.change_soc(10)
    print(f"""Благодарим за ответ! (Статистика:
    Здоровье: {player.health_points}
    Интеллект: {player.intellect_points}
    Социальные навыки: {player.social_points})""")
    # print(player.study_at_home_town_bonus, player.intellect_bonus, player.social_skill_bonus)
    return player


def morning():
    if player.study_at_home_town_bonus:
        print("Родители как всегда разбудили вас и отправили завтракать. После вкусного домашнего завтрака вас отвезут в университет.")
        player.change_hp(10)
    else:
        print("Звонит будильник, пора вставать, завтрак сам себя не съест.")
        d = int(input("Что будете есть сегодня? Приготовим / купим готовый / купим кофе / не будем есть (1, 2, 3, 4)  "))
        if d == 1:
            print("Вкусный и полезный завтрак")
            player.change_hp(10)
        elif d == 2:
            print("Не самый полезный выбор, но все еще довольно вкусно")
            player.change_hp(5)
        elif d == 3:
            print("Не питательно, зато бодрит")
        else:
            print("Вот бы люди умели питаться энергией солнца, а не едой...")
            player.change_hp(-5)
    print()
    print("Пора выдвигаться в путь.")


def lesson():
    print("Начинаются занятия.")
    print("Вопрос от преподавателя: ")
    for i, el in enumerate(question_list):
        if i == day:
            el.trigger()
    print("Вы набрались опыта и стали чуть умнее. Продолжайте усердно учиться, и экзамен покажется лёгким.")
    print("Занятия подошли к концу")


def extra_curriculum():
    answer = input("Начинаются внеучебные занятия. Чуть позже мы добавим задания, а пока что просто нажмите enter.")


def evening():
    print("Вы наконец добрались до дома")
    f = int(input("Чем займетесь? дз / свои дела (1, 2)  "))
    if f == 1:
        print("Пожалуй, стоит потратить время на учебу.")
        player.change_int(10)
        player.change_hp(-5)
    else:
        print("Никогда не стоит забывать про себя любимого.")
        player.change_hp(5)
        player.change_int(-5)
    print("Занимаясь делами, вы не заметили, как закончился день. Время ложиться спать")


def bus_or_car_event():
    if player.study_at_home_town_bonus:
        print("Вашу машину остановила полиция для проверки документов. По какой-то причине она затянулась. Дальше придется добираться своим ходом")
    else:
        print("О нет! Автобус сломался... Придется добираться до корпуса пешком.")
    player.change_hp(-5)
    e = int(input("Что будете делать? Опоздание на пару / прогул пары (1, 2)  "))
    if e == 2:
        truant()
    else:
        late_lesson()


def ill_lecturer():
    print("Хм... Препода слишком долго нет. Кажется, из учебного офиса так и не пришло письмо о том, что он заболел и пары сегодня отменяются.")
    f = int(input("Чем займетесь? Слушать лекцию другого потока / Прогул (1, 2)"))
    if f == 1:
        print("Решено сходить на лекцию другой группы. Внезапно, вы получили удовольствие от роли вольнослушателя и с пользой провели время. Полученные знания обязательно однажды пригодятся вам (но это не точно)")
        player.change_hp(-5)
        player.change_int(10)
        achievement.attend_extra_lesson = True
        achievement.check_gameplay_achievements()
    else:
        truant()


def late_lesson():
    print("Вы опоздали на пару. Препод посчитал это за неуважительное отношение к его предмету.")
    player.change_soc(-5)
    player.change_int(5)


def truant_event():
    print("К вам подошли друзья. Они хотят пропустить пару и пойти погулять.")
    g = int(input("Пойдете с ними? да / нет (1, 2)  "))
    if g == 1:
        truant()
    else:
        lesson()


def truant():
    print("Вы решили оставить занятия")
    player.change_soc(5)
    player.change_int(-10)
    achievement.truant_count += 1
    achievement.check_gameplay_achievements()

def sport():
    print("Пришло напоминание о том, что нужно посещать занятия по физре. Сегодня как раз отличный день для этого. Только тогда придется пропустить внеучебку.")
    h = int(input("Пойдем? да / нет (1, 2)  "))
    if h == 1:
        print("Нестрашно пропустить внеучебку один раз. Зачет все равно придется получать рано или поздно")
        player.change_hp(10)
        player.change_soc(-5)
        achievement.sport_lesson_count += 1
        achievement.check_gameplay_achievements()
    else:
        print("Вы решили. что физру можно закрыть позже, а сегодня можно пропустить занятие")
        player.change_hp(-5)
        extra_curriculum()


def volunteering():
    print("Вам предложили поучаствовать в мероприятии в качестве волонтера. Вам придется пропустить пары и внеучебные занятия, но зато вы получите бонусы за активность.")
    j = int(input("Что делать? волонтёрить / остаться на занятия (1, 2)  "))
    if j == 1:
        print("Сегодня у вас был тяжелый и насыщенный день, но вы явно провели время с пользой.")
        player.change_hp(-10)
        player.change_soc(15)
        volunteer_day.accepted = True
        achievement.check_gameplay_achievements()

# ========== экзамен  ==========
def exam():
    print("Учебная неделя закончилась. За ней прошла и вторая, и третья... Настало время проверить ваши знания. Время сдавать экзамен")

    if player.intellect_points <= 0:
        print("\nПлан был невероятно дерзкий! И такой же непродуманный... Не удивительно, ведь ваш интеллект достиг своей нижней границы, возможно даже превзошел ее... ")
    else:
        print("\nУдачи на экзамене! У вас есть все шансы сдать!")

    experience = 0
    options = [
        {"name": "краткий", "cost": 25, "exp": 15},
        {"name": "факт с лекции", "cost": 30, "exp": 25},
        {"name": "цитирование литературы", "cost": 35, "exp": 30},
        {"name": "как по учебнику", "cost": 40, "exp": 35},
        {"name": "мастермайнд", "cost": 45, "exp": 40}
    ]

    while experience < 100 and player.intellect_points > 0:
        print(f"\nУ вас {player.intellect_points} очков интеллекта.")
        print("Вы можете обменять очки интеллекта на варианты ответов:")
        print(f"\nТекущий прогресс: {experience}/100 опыта")
        print("Доступные варианты ответов:")

        available_options = [opt for opt in options]

        for i, opt in enumerate(available_options, 1):
            print(f"{i}. Билет: {opt['name']}, Стоимость: {opt['cost']} очков интеллекта, даёт {opt['exp']} опыта")

        print(f"{len(available_options) + 1}. Закончить экзамен досрочно")

        choice = input("Выберите вариант ответа (или поднимите белый флаг): ")

        try:
            choice = int(choice)
            if choice == len(available_options) + 1:
                if experience >= 100:
                    print("10+")
                    break
                else:
                    print(f"{experience // 10}")
                    break
            elif 1 <= choice <= len(available_options):
                selected = available_options[choice - 1]
                experience += selected["exp"]
                player.intellect_points -= selected['cost']
                print(f"\nВы выбрали вариант {choice}. Получено {selected['exp']} опыта.")
                if player.intellect_points < 0:
                    print("Кажется, рассудок вас окончательно покинул Т_Т")
                    break
        except ValueError:
            print("Пожалуйста, введите число.")

    print(f"Итоговый результат: {experience}/100 опыта")
    print(f"Осталось очков интеллекта: {player.intellect_points}")


# ========== главный цикл ==========
introduction()
for day in range(1, 7+1):
    print(f"День {day}-й.")
    for el in random_event_list:
        el.day_check(day)
        if el.check:
            print(f"Сегодня должно произойти {el.name}")
    morning()
    if transport_event.check:
        bus_or_car_event()

    if volunteer_day.check:
        volunteering()
        if volunteer_day.accepted:
            evening()
    if not volunteer_day.check or not volunteer_day.accepted:
        if lecturer_ill.check:
            ill_lecturer()
        elif truant_offer.check:
            truant_event()
        elif not transport_event.check:
            lesson()
        if sport_lesson.check:
            sport()
        else:
            extra_curriculum()
        evening()
    for el in random_event_list:
        el.check = False

achievement.answer_achievement()
achievement.attend_lessons()

exam()