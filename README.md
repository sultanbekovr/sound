# sound

Проект реализованный на Django, DRF, SQlite, PostgreSQL, Docker.

Данный проект позволяет слушать, скачать, загрузить музыку.

Что реализовано:
Аторизация с помощью Google и Spotify
Создание JWT токенов
Собственная авторизация
CRUD альбомов, треков, плейлистов, соц. сетей, лицензии,  
Свой permission
Коментарии к трекам

Более подробно:
У модели пользователя проверка расщирения загружаемого файла и размера(не более 5мб)
Автогенерация пути для медиа(в файле services)
Реализация авторизации с помощью гугл:
  Получаем данные в клиентской стороны, передаем их в наш сериализатор GoogleAuth, далее проверяем данные на валидность, после проверки передаем данные
  в check_google_auth, с помощию библиотеки гугл проверяем валидность токена, после проверки с помощью get_or_create создаем либо получаем пользователя с бд,
  после получаения обьекта пользователя, мы ппередаем его айди в create_token. В данной функции с помощью timdelta задаем время жизни токена и возвращаем
  словарь с user_id, access_token, token_type, Access token будет генерироваться в функции create_access_token, туда мы передаем айди пользователя и время 
  жизни токена. С помощью библиотеки jwt вызывая encode мы передаем наш словарь, секрет кей и алгоритм шифрования. Возвращаем сгенерированный токен.
Свой permission:
  наследуемся от IsAuthenticated и в функции has_object_permission проверяем является ли пользотваель автором. Если пользоваетль который обрщается и
  пользователь который создал эту запис в бд, то мы возврщаем True.
