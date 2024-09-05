import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname: str, password: str):  # переработан c опросом всех пользователей до первого верного
        # (учтено замечание Тюрина Романа)
        hash_obgect = hashlib.sha256(password.encode('utf-8'))
        hash_password = hash_obgect.hexdigest()
        found_user = False
        for user in self.users:
            if nickname == user.nickname and hash_password == user.password:
                found_user = True
                self.current_user = user
                break
        if not found_user:
            print(f'Пользователь {nickname} не найден, пройдите регистрацию')

    def log_out(self):
        self.current_user = None

    def register(self, nickname: str, password: str, age: int):
        hash_obg = hashlib.sha256(password.encode('utf-8'))
        hash_password = hash_obg.hexdigest()
        new_user = User(nickname, hash_password, age)
        new_user_found = False
        for user in self.users:
            if user.nickname == new_user.nickname:  # если пользователя нет в списке - записываем
                print(f'Пользователь {nickname} уже существует')
                new_user_found = True
                break
        if not new_user_found:
            self.users.append(new_user)
            self.log_out()
            self.log_in(nickname, password)  # текущий пользователь вход в систему

    # метод add - для добавления в базу новых фильмов (внесены исправления по замечанию)
    def add(self, *videos_list):
        video_found = False
        for new_video in videos_list:
            for save_video in self.videos:
                if new_video.title == save_video.title:  # если видео есть в списке
                    video_found = True
                    break
            if not video_found:
                self.videos.append(new_video)
            else:
                print('Фильм: ', new_video.title, 'обнаружен в базе и не был повторно записан')

    def get_videos(self, find_title):
        found_video_title = []
        for video in self.videos:
            if find_title.casefold() in video.title.casefold():
                found_video_title.append(video.title)
        return found_video_title

    def watch_video(self, name_video):
        video_not_base = False
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if name_video == video.title:
                    if video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        video_not_base = False
                    else:
                        for sec in range(video.time_now, video.duration):
                            print(sec + 1, end=' ')
                            time.sleep(1)
                        print('Конец видео')
                        video_not_base = False
                else:
                    video_not_base = True
        if video_not_base:
            print('Не правильно введено название фильма')


#  Код для проверки:
if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)
    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
