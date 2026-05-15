# Воспроизведение мультимедиа
# Создайте два класса:
# AudioFileMixin — требует наличие поля audio_tracks (список треков).
# Метод play_audio() выводит:
# Воспроизведение аудио для <НазваниеКласса>:
# <название трека>
# <название трека>
# VideoFileMixin — требует наличие поля video_files (список видео).
# Метод play_video() выводит:
# Воспроизведение видео для <НазваниеКласса>:
# <название видео>
# <название видео>
# Если нужное поле отсутствует — выбрасывайте AttributeError.

tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

class AudioFileMixin:
    """
    Миксин, добавляющий возможность воспроизведения аудиофайлов.
    """

    def play_audio(self):
        """
        Воспроизводит аудиотреки, указанные в атрибуте audio_tracks.

         :raise AttributeError: если у объекта отсутствует атрибут audio_tracks.
        """
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Отсутствует нужный трек")

        result = f"Воспроизведение аудио для {self.__class__.__name__}:\n"
        result += "\n".join(self.audio_tracks)
        return result



class VideoFileMixin:
    """
     Миксин, добавляющий возможность воспроизведения видеофайлов.
    """

    def play_video(self):
        """
        Воспроизводит видеоролики, указанные в атрибуте video_files.

        :raise AttributeError: если у объекта отсутствует атрибут video_files
        """
        if not hasattr(self, "video_files"):
            raise AttributeError("Отсутствует нужное видео")

        result = f"Воспроизведение видео для {self.__class__.__name__}:\n"
        result += "\n".join(self.video_files)
        return result

# Устройства
# Создайте два класса:
# MediaPlayer — поддерживает только аудио. Принимает список треков.
# Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
# Проверьте работу классов, вызвав методы воспроизведения.

class MediaPlayer(AudioFileMixin):
    """
    Класс MediaPlayer, поддерживающий воспроизведение аудио.
    """
    def __init__(self, audio_tracks: list):
        """
        Инициализирует медиаплеер.
        :param audio_tracks: список аудиофайлов.
        """
        self.audio_tracks = audio_tracks

class Laptop(AudioFileMixin, VideoFileMixin):
    """
    Класс Laptop поддерживающий воспроизведение аудио и видео.
    """
    def __init__(self, audio_tracks: list, video_files: list):
        """
        Инициализирует ноутбук.
        :param audio_tracks: список аудиофайлов.
        :param video_files: список видеофайлов.
        """
        self.audio_tracks = audio_tracks
        self.video_files = video_files

# mediap = MediaPlayer(tracks)
# mediap.play_audio()



try:
    laptop = Laptop(tracks, movies)
    print(laptop.play_audio())
    print(laptop.play_video())
except AttributeError as e:
    print(e)


