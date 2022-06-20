---
created: 2022-06-15T20:13:32 (UTC +03:00)
tags: []
source: https://wiki.termux.com/wiki/Working_with_APKs
author: 
---

# Работа с APK-файлами - Termux Wiki

> ## Excerpt
> From Termux Wiki

---
From Termux Wiki

Jump to: [navigation](https://wiki.termux.com/wiki/Working_with_APKs#mw-navigation), [search](https://wiki.termux.com/wiki/Working_with_APKs#p-search)

Вы когда-нибудь хотели создать свое собственное приложение для Android, созданное на смартфоне и планшете? Теперь вы можете легко скомпилировать множество выбранных приложений, которые уже были успешно созданы, установлены и протестированы в [Termux](https://github.com/termux) на устройстве. Вы можете скопировать и вставить следующее в Termux, чтобы установить [BuildAPKs](https://github.com/BuildAPKs ) на устройстве:

```
   pkg install curl 

   curl -O https://raw.githubusercontent.com/BuildAPKs/buildAPKs/master/setup.buildAPKs.bash

   bash setup.buildAPKs.bash



```

[![APKsBuiltInTermux.png](https://wiki.termux.com/images/thumb/2/25/APKsBuiltInTermux.png/320px-APKsBuiltInTermux.png)](https://wiki.termux.com/wiki/File:APKsBuiltInTermux.png)

  
[Скрипты в этих каталогах](https://github.com/BuildAPKs/buildAPKs/tree/master/scripts/) можно создавать тысячи APK-файлов на устройстве с помощью Termux на смартфонах Amazon и Android, планшетах, телевизорах и Chromebook. Вы можете использовать скрипты BASH, расположенные [здесь](https://github.com/BuildAPKs/buildAPKs/tree/master/scripts/bash/build ), чтобы начать создавать APK-файлы на устройстве.

В [build.github.bash](https://raw.githubusercontent.com/BuildAPKs/buildAPKs.github/master/build.github.bash ) скрипт bash работает напрямую с API GitHub. Чтобы увидеть, как этот скрипт запрашивает данные у api, вы можете использовать \` grep curl ~/buildAPKs/build.github.bash \` после установки BuildAPKs. Эта команда:

```
~/buildAPKs/build.github.bash BuildAPKs
```

должен попытаться собрать все наборы пакетов Android [BuildAPKs](https://github.com/BuildAPKs?tab=repositories ) может предложить.

The [db.BuildAPKs repository](https://github.com/BuildAPKs/db.BuildAPKs) assits in parsing repositories for AndroidManifest.xml files located at GitHub. The ~/buildAPKs/opt/db/[BNAMES file](https://github.com/BuildAPKs/db.BuildAPKs/blob/master/BNAMES) holds built APK statistics: GitHub login, date stamp, repository projects download size, build time, the number of AndroidManifest.xml files found and how many APKs were successfully built on device for each login that successfully built at least one APK on device from Github with BuildAPKs.

Вы можете создавать браузеры и файловые менеджеры Android в Termux, выполнив команду "build.команда browsers.bash` один раз [BuildAPKs](https://github.com/BuildAPKs ) устанавливается.

## See Also

-   [Ant](https://wiki.termux.com/wiki/Ant "Ant")
-   [Development Environments](https://wiki.termux.com/wiki/Development_Environments "Development Environments")
-   [Editors](https://wiki.termux.com/wiki/Editors "Editors")
-   [Gradle](https://wiki.termux.com/wiki/Gradle "Gradle")
-   [IDEs](https://wiki.termux.com/wiki/IDEs "IDEs")

Перевод выполнить не удалось

Отсутствует подключение к интернету

Переведено 100%

Переведено на Русский

Перевести картинки