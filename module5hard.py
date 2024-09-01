import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users and hash(password) in self.users:
            self.current_user = nickname
        else:
            print('Пользователь не найден, пройдите регистрацию')

    def register(self, nickname, password, age):
        if not self.users != []:  # если список пуст - записываем
            self.users.append(User(nickname, password, age))
            self.current_user = [nickname, User(nickname, password, age)]
        else:
            _user_found = False
            for i in self.users:
                if nickname == i.nickname:
                    _user_found = True
                    break
            if not _user_found:
                self.users.append(User(nickname, password, age))
                self.current_user = [nickname, User(nickname, password, age)]
            else:
                print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *videos_list):  # метод добавления в базу новых фильмов
        for new_videos in videos_list:
            if not self.videos != []:  # если список пуст - записываем первый
                self.videos.append(videos_list[0])
                # print('Записан первый фильм в базу:', videos_list[0].title)
            else:
                for video_in_base in self.videos:
                    if new_videos.title == video_in_base.title:
                        # print('Фильм: ',new_videos.title, 'обнаружен в базе и не был повторно записан')
                        break
                    else:
                        self.videos.append(new_videos)
                        # print('Записан новый фильм в базу:', new_videos.title)
                        break

    def get_videos(self, find_word):
        _videos = []
        for i in self.videos:
            _title = i.title
            if find_word.casefold() in _title.casefold():
                _videos.append(i.title)
        return _videos

    def watch_video(self, name_video):
        video_play = None
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in self.videos:
                if name_video == i.title:
                    video_play = i
            if not video_play:
                pass
            elif video_play.adult_mode:  # добавлено 01.09.2024
                if self.current_user[1].age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for j in range(video_play.duration):
                        print(j + 1, end=' ')
                        time.sleep(0.3)
                    print('Конец видео')

    def print_title(self):  # для проверки алгоритма выводит наименования фильмов
        print("В базе записаны следующие фильмы:")
        for title in self.videos:
            print(title.title)

    def print_cu(self):  # для проверки алгоритма выводит имя и возраст текущего пользователя
        print(f'текущий пользователь :{self.current_user[0]}, ему {self.current_user[1].age}')


#  Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# v3 = Video('Лучший язык программирования 2024 года', 200)  # добавлен для расширения метода add

# Добавление видео
ur.add(v1, v2)  # , v3)
# ur.print_title()  # запись в атрибут класса UrTube videos произведена и их названия следующие:

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
#  ur.print_cu()  # добавлено для наглядности
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
#  ur.print_cu()  # добавлено для наглядности
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user[0])  # исправлено ТЗ, т.к. метод не может быть и атрибутом "current_user"

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
