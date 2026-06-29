**Resources**

[[]][Home](http://www.rsyslog.com)

[[]][Official documentation](http://www.rsyslog.com/doc/master/index.html)

[[]][Package information](https://packages.gentoo.org/packages/app-admin/rsyslog)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ru:Rsyslog "wikipedia:Ru:Rsyslog")

[[]][GitHub](https://github.com/rsyslog/rsyslog)

[[]][[#rsyslog](ircs://irc.libera.chat/#rsyslog)] ([[webchat](https://web.libera.chat/#rsyslog)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/ru:rsyslog)

[[]]This article has some todo items:\

-   add simple IPv6 example
-   wikify
-   add systemd

**Rsyslog** --- это система с открытым исходным кодом для высокопроизводительной обработки логов. Это не просто системный журнал, а универсальный инструмент, который может принимать данные из множества источников и отправлять их в различные места назначения.

Rsyslog поддерживает пересылку логов через IP-сеть, в базы данных, на почту и так далее, расширяя стандартные возможности протокола syslog благодаря мощным возможностям фильтрации. Это позволяет адаптировать конфигурацию под конкретные нужды.

## Contents

-   [[1] [Установка]](#.D0.A3.D1.81.D1.82.D0.B0.D0.BD.D0.BE.D0.B2.D0.BA.D0.B0)
    -   [[1.1] [USE флаги]](#USE_.D1.84.D0.BB.D0.B0.D0.B3.D0.B8)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Конфигурация]](#.D0.9A.D0.BE.D0.BD.D1.84.D0.B8.D0.B3.D1.83.D1.80.D0.B0.D1.86.D0.B8.D1.8F)
    -   [[2.1] [Переменные окружения]](#.D0.9F.D0.B5.D1.80.D0.B5.D0.BC.D0.B5.D0.BD.D0.BD.D1.8B.D0.B5_.D0.BE.D0.BA.D1.80.D1.83.D0.B6.D0.B5.D0.BD.D0.B8.D1.8F)
    -   [[2.2] [Файлы]](#.D0.A4.D0.B0.D0.B9.D0.BB.D1.8B)
        -   [[2.2.1] [Конфигурационные файлы]](#.D0.9A.D0.BE.D0.BD.D1.84.D0.B8.D0.B3.D1.83.D1.80.D0.B0.D1.86.D0.B8.D0.BE.D0.BD.D0.BD.D1.8B.D0.B5_.D1.84.D0.B0.D0.B9.D0.BB.D1.8B)
    -   [[2.3] [Критичность]](#.D0.9A.D1.80.D0.B8.D1.82.D0.B8.D1.87.D0.BD.D0.BE.D1.81.D1.82.D1.8C)
    -   [[2.4] [Объекты]](#.D0.9E.D0.B1.D1.8A.D0.B5.D0.BA.D1.82.D1.8B)
    -   [[2.5] [Фильтрация]](#.D0.A4.D0.B8.D0.BB.D1.8C.D1.82.D1.80.D0.B0.D1.86.D0.B8.D1.8F)
    -   [[2.6] [Локальное логирование]](#.D0.9B.D0.BE.D0.BA.D0.B0.D0.BB.D1.8C.D0.BD.D0.BE.D0.B5_.D0.BB.D0.BE.D0.B3.D0.B8.D1.80.D0.BE.D0.B2.D0.B0.D0.BD.D0.B8.D0.B5)
    -   [[2.7] [Удаленное логирование]](#.D0.A3.D0.B4.D0.B0.D0.BB.D0.B5.D0.BD.D0.BD.D0.BE.D0.B5_.D0.BB.D0.BE.D0.B3.D0.B8.D1.80.D0.BE.D0.B2.D0.B0.D0.BD.D0.B8.D0.B5)
        -   [[2.7.1] [Клиент]](#.D0.9A.D0.BB.D0.B8.D0.B5.D0.BD.D1.82)
        -   [[2.7.2] [Сервер]](#.D0.A1.D0.B5.D1.80.D0.B2.D0.B5.D1.80)
    -   [[2.8] [Логирование в базу данных]](#.D0.9B.D0.BE.D0.B3.D0.B8.D1.80.D0.BE.D0.B2.D0.B0.D0.BD.D0.B8.D0.B5_.D0.B2_.D0.B1.D0.B0.D0.B7.D1.83_.D0.B4.D0.B0.D0.BD.D0.BD.D1.8B.D1.85)
    -   [[2.9] [Сервисы]](#.D0.A1.D0.B5.D1.80.D0.B2.D0.B8.D1.81.D1.8B)
        -   [[2.9.1] [OpenRC]](#OpenRC)
-   [[3] [Шаблоны]](#.D0.A8.D0.B0.D0.B1.D0.BB.D0.BE.D0.BD.D1.8B)
-   [[4] [Использование]](#.D0.98.D1.81.D0.BF.D0.BE.D0.BB.D1.8C.D0.B7.D0.BE.D0.B2.D0.B0.D0.BD.D0.B8.D0.B5)
    -   [[4.1] [Запуск]](#.D0.97.D0.B0.D0.BF.D1.83.D1.81.D0.BA)
    -   [[4.2] [Проверка конфигурационных файлов]](#.D0.9F.D1.80.D0.BE.D0.B2.D0.B5.D1.80.D0.BA.D0.B0_.D0.BA.D0.BE.D0.BD.D1.84.D0.B8.D0.B3.D1.83.D1.80.D0.B0.D1.86.D0.B8.D0.BE.D0.BD.D0.BD.D1.8B.D1.85_.D1.84.D0.B0.D0.B9.D0.BB.D0.BE.D0.B2)
-   [[5] [Удаление]](#.D0.A3.D0.B4.D0.B0.D0.BB.D0.B5.D0.BD.D0.B8.D0.B5)
-   [[6] [Устранение проблем]](#.D0.A3.D1.81.D1.82.D1.80.D0.B0.D0.BD.D0.B5.D0.BD.D0.B8.D0.B5_.D0.BF.D1.80.D0.BE.D0.B1.D0.BB.D0.B5.D0.BC)
-   [[7] [См. также]](#.D0.A1.D0.BC._.D1.82.D0.B0.D0.BA.D0.B6.D0.B5)
-   [[8] [Внешние источники]](#.D0.92.D0.BD.D0.B5.D1.88.D0.BD.D0.B8.D0.B5_.D0.B8.D1.81.D1.82.D0.BE.D1.87.D0.BD.D0.B8.D0.BA.D0.B8)

## [][Установка]

### [][USE флаги]

### [USE flags for] [app-admin/rsyslog](https://packages.gentoo.org/packages/app-admin/rsyslog) [[]] [An enhanced multi-threaded syslogd with database support and more]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+gcrypt`](https://packages.gentoo.org/useflags/+gcrypt)               Add support for encrypted log files using dev-libs/libgcrypt
  [`+openssl`](https://packages.gentoo.org/useflags/+openssl)             Build the OpenSSL network stream driver (requires dev-libs/openssl)
  [`+ssl`](https://packages.gentoo.org/useflags/+ssl)                     Add support for encrypted client/server communication (requires net-libs/gnutls)
  [`+uuid`](https://packages.gentoo.org/useflags/+uuid)                   Include UUIDs in messages (requires sys-apps/util-linux)
  [`clickhouse`](https://packages.gentoo.org/useflags/clickhouse)         Build the ClickHouse output module (requires net-misc/curl)
  [`curl`](https://packages.gentoo.org/useflags/curl)                     Enable http_request() function in RainerScript (requires net-misc/curl)
  [`dbi`](https://packages.gentoo.org/useflags/dbi)                       Build the general database output module (requires dev-db/libdbi)
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`elasticsearch`](https://packages.gentoo.org/useflags/elasticsearch)   Build the Elasticsearch output module (requires net-misc/curl)
  [`gnutls`](https://packages.gentoo.org/useflags/gnutls)                 Build the GnuTLS network stream driver (requires net-libs/gnutls)
  [`imdocker`](https://packages.gentoo.org/useflags/imdocker)             Build the docker input module (requires net-misc/curl)
  [`imhttp`](https://packages.gentoo.org/useflags/imhttp)                 Build the http input module (requires www-servers/civetweb)
  [`impcap`](https://packages.gentoo.org/useflags/impcap)                 Build the pcap input module (requires net-libs/libpcap)
  [`kafka`](https://packages.gentoo.org/useflags/kafka)                   Build the Apache Kafka input/output module (requires dev-libs/librdkafka)
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)             Build the GSSAPI input and output module (requires virtual/krb5)
  [`kubernetes`](https://packages.gentoo.org/useflags/kubernetes)         Build the kubernetes modify plugin (requires net-misc/curl)
  [`mdblookup`](https://packages.gentoo.org/useflags/mdblookup)           Build the MaxMind DB lookup message modify plugin using dev-libs/libmaxminddb
  [`mongodb`](https://packages.gentoo.org/useflags/mongodb)               Build the MongoDB output module (requires dev-libs/mongo-c-driver)
  [`mysql`](https://packages.gentoo.org/useflags/mysql)                   Build the MySQL database output module (requires virtual/mysql)
  [`normalize`](https://packages.gentoo.org/useflags/normalize)           Build the normalize modify module (requires dev-libs/libee and dev-libs/liblognorm)
  [`omhttp`](https://packages.gentoo.org/useflags/omhttp)                 Build the http output module (requires net-misc/curl)
  [`omhttpfs`](https://packages.gentoo.org/useflags/omhttpfs)             Build the httpfs output module (requires net-misc/curl)
  [`omudpspoof`](https://packages.gentoo.org/useflags/omudpspoof)         Build the udpspoof output module (requires net-libs/libnet)
  [`postgres`](https://packages.gentoo.org/useflags/postgres)             Build the PostgreSQL database output module (requires dev-db/postgresql)
  [`rabbitmq`](https://packages.gentoo.org/useflags/rabbitmq)             Build the RabbitMQ output module (requires net-libs/rabbitmq-c)
  [`redis`](https://packages.gentoo.org/useflags/redis)                   Build the Redis output module using (requires dev-libs/hiredis)
  [`relp`](https://packages.gentoo.org/useflags/relp)                     Build the Reliable Event Logging Protocol (RELP) output module (requires dev-libs/librelp)
  [`rfc3195`](https://packages.gentoo.org/useflags/rfc3195)               Build the rfc3195 input module (requires dev-libs/liblogging)
  [`rfc5424hmac`](https://packages.gentoo.org/useflags/rfc5424hmac)       Build the rfc5424hmac modify module (requires dev-libs/openssl)
  [`snmp`](https://packages.gentoo.org/useflags/snmp)                     Build the snmp modify and output module (requires net-analyzer/net-snmp)
  [`systemd`](https://packages.gentoo.org/useflags/systemd)               Build the journal input and output module (requires sys-apps/systemd)
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`usertools`](https://packages.gentoo.org/useflags/usertools)           Installs the user tools (rsgtutil, rscryutil\...) corresponding to the set USE flags
  [`xxhash`](https://packages.gentoo.org/useflags/xxhash)                 Enable xxHash support in fmhash module (requires dev-libs/xxhash)
  [`zeromq`](https://packages.gentoo.org/useflags/zeromq)                 Build the ZeroMQ input and output modules (requires net-libs/czmq)
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-15 16:34] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Установка [[[app-admin/rsyslog]](https://packages.gentoo.org/packages/app-admin/rsyslog)[]]:

`root `[`#`]`emerge --ask app-admin/rsyslog`

** Warning**\
Не рекомендуется запускать более одного системного логгера на одном хосте, так как другие локальные логгеры могут быть отключены или удалены.

## [][Конфигурация]

### [][Переменные окружения]

Список всех переменных окружения, которые можно узнать, введя команду: [rsyslogd]

-   `RSYSLOG_DEBUG` --- опции CSV: `debug`, `debugondemand`, `lologtimestamp`, `nostdout`, `outputtidtostderr`. Используйте `RSYSLOG_DEBUG=help` для получения дополнительной информации.
-   `RSYSLOG_MODDIR` --- полный путь к директории с используемыми модулями (по умолчанию [/usr/lib/\<GNU-trigraph\>/rsyslog])
-   `RSYSLOG_DEBUGLOG` --- полный путь к файлу журнала отладки (по умолчанию отсутствует)
-   `RSYSLOG_DEBUG_TIMEOUTS_TO_STDERR` --- интервал времени для вывода отладочной информации (в секундах).
-   `RSYSLOG_DFLT_LOG_INTERNAL` --- используется тестовым стендом и определенными последовательностями запуска. Значение \`1\` эквивалентно `$processInternalMessage=on`
-   `LISTEN_PID` --- полный путь к файлу с идентификатором процесса (`PID`)

[/etc/rsyslog.conf] может содержать ключевые слова параметра [environment], которые создают дополнительную переменную окружения.

Модули также могут использовать другие переменные окружения для изменения своих характеристик обработки. Смотрите исходный код конкретных модулей на наличие системных вызовов `getenv()`.

### [][Файлы]

Файлы, которые считываются командой: [rsyslogd]

-   [/etc/rsyslog.conf] --- файл конфигурации [rsyslogd]
-   [/usr/lib/x86_64-linux-gnu/rsyslog/] --- библиотека модулей для [rsyslogd]
-   [/proc/self/ns/net]
-   [/var/run/netns/%s]
-   [/dev/urandom] --- устройство источника случайных чисел ядра

Файлы, которые создаются командой: [rsyslogd]

-   (различные файлы журналов)
-   [/dev/console]
-   [/run/rsyslog.pid%s]

#### [][Конфигурационные файлы]

Существует три формата файла [/etc/rsyslog.conf]: расширенный, базовый, устаревший.

  ----------------- --------------------- ----------
  Тип формата       Используемые версии   Описание
  **расширенный**   7.0 до 8.2338+
  **базовый**       5.0 до 6.9999
  **устаревший**    до 4.999
  ----------------- --------------------- ----------

На этой странице рассматриваются как базовые, так и продвинутые аспекты.

Базовая конфигурация rsyslog:

[FILE] **`/etc/rsyslog.conf`**

    $IncludeConfig /etc/rsyslog.d/
    $FileCreateMode 0640

    *.info;mail.none;authpriv.none;cron.none                -/var/log/messages
    authpriv.*                                              /var/log/secure
    mail.*                                                  -/var/log/maillog
    cron.*                                                  -/var/log/cron
    *.emerg                                                 .*

Обычно сообщения записываются в файлы, которые должны быть указаны с полным путем. Rsyslog использует простой синтаксис фильтрации для входящих сообщений. Сообщения syslog классифицируются по категории (facility) и уровню критичности (severity). Согласно [RFC5424](http://www.ietf.org/rfc/rfc5424.txt) определены следующие уровни критичности:

### [][Критичность]

  -------------- --------- --------------------------------------
  Числовой код   Уровень   Описание
  0              emerg     система непригодна для использования
  1              alert     требуется немедленное действие
  2              crit      критические условия
  3              error     ошибки
  4              warning   предупреждения
  5              notice    нормальное, но значимое событие
  6              info      информационные сообщения
  7              debug     отладочные сообщения
  -------------- --------- --------------------------------------

### [][Объекты]

Список объектов (facilities), используемых rsyslog. Большинство названий объектов понятны сами по себе. Объекты local0 - local7 обычно используются, например, для сетевых журналов узлов и сетевого оборудования. В целом, это зависит от ситуации, как классифицировать журналы и назначать их объектам. Рассматривайте объекты скорее как инструмент, чем как директиву для выполнения.

Объекты можно настроить в соответствии с потребностями пользователя:

  -------------- ---------- -----------------------------------------
  Числовой код   Объект     Описание
  0              kern       сообщения ядра
  1              user       пользовательские сообщения
  2              mail       почтовая система
  3              daemon     системные демоны
  4              auth       сообщения безопасности/авторизации
  5              syslog     сообщения, генерируемые самим syslogd
  6              lpr        подсистема принтера
  7              news       подсистема сетевых новостей
  8              uucp       подсистема UUCP
  9              cron       демон планировщика
  10             security   сообщения безопасности/авторизации
  11             ftp        демон FTP
  12             ntp        подсистема NTP
  13             logaudit   аудит журналов
  14             logalert   предупреждения журнала
  15             clock      демон часов (примечание 2)
  16             local0     для локального использования 0 (local0)
  17             local1     для локального использования 1 (local1)
  18             local2     для локального использования 2 (local2)
  19             local3     для локального использования 3 (local3)
  20             local4     для локального использования 4 (local4)
  21             local5     для локального использования 5 (local5)
  22             local6     для локального использования 6 (local6)
  23             local7     для локального использования 7 (local7)
  -------------- ---------- -----------------------------------------

  : Объект

### [][Фильтрация]

Список с примерами команд для фильтрации:

-   Перенаправить все входящие сообщения от всех объектов и со всеми уровнями критичности в [/var/log/syslog]:

<!-- -->

     *.* -/var/log/syslog

-   Отфильтровать сообщения с уровнем критичности \"crit\" и сохранить их в файл [/var/log/critical]:

<!-- -->

     *.crit -/var/log/critical

-   НЕ перенаправлять объекты mail, authentication и cron в [/var/log/messages], обратите внимание на ключевое слово **none**:

<!-- -->

     mail.none;authpriv.none;cron.none -/var/log/messages

### [][Локальное логирование]

Включить локальное логирование от всех объектов, чтобы видеть локальные события.

     $ModLoad imuxsock.so

### [][Удаленное логирование]

Чтобы использовать удаленное логирование на syslog-сервер, укажите клиенту логировать на определенный сервер или серверы, а серверу принимать сообщения, отправленные клиентами. Перед настройкой выберите протокол. Сообщения syslog могут быть отправлены с использованием UDP или TCP. UDP является протоколом по умолчанию и поддерживается на большинстве платформ. Не все платформы поддерживают TCP для syslog.

#### [][Клиент]

Чтобы включить отправку syslog-сообщений по UDP, добавьте следующую строку в файл [/etc/rsyslog.conf]. В этом примере rsyslog отправляет все объекты и все приоритеты *\*.\** с использованием протокола UDP *@* на удаленный сервер *192.0.2.1*

     *.*       @192.0.2.1

Чтобы включить поддержку TCP для syslog-сообщений, добавьте следующую строку в файл конфигурации rsyslog, TCP включается добавлением *@@*.

     *.*       @@192.0.2.1

При желании можно использовать имена хостов вместо IP-адресов.

** Important**\
Замените `192.0.2.1` на IP-адрес удаленного сервера rsyslog, который настроен и работает для приема любых syslog через соответствующий номер порта с использованием UDP или TCP.

Ниже приведен пример конфигурации syslog-клиента для отправки syslog-сообщений на удаленный сервер через TCP.

[FILE] **`/etc/rsyslog.conf`**

    $ModLoad imuxsock.so
    *.*   @@192.0.2.1:10514

    *.info;mail.none;authpriv.none;cron.none      /var/log/messages
    authpriv.*                                    /var/log/secure
    mail.*                                        /var/log/maillog
    cron.*                                        /var/log/cron
    *.emerg                                       *
    uucp,news.crit                                /var/log/spooler
    local7.*                                      /var/log/boot.log

#### [][Сервер]

Чтобы обеспечить прием журналов по UDP и запустить сервер на порту 514.

     $ModLoad imudp
     $UDPServerRun 514

UDP не является надежным протоколом. Для большей надежности запустите сервер с поддержкой логирования по TCP.

     $ModLoad imtcp
     $InputTCPServerRun 10514

Чтобы привязать UDP-порт к интерфейсу IP, настройте следующую запись, убедитесь в правильной последовательности определений при привязке к интерфейсу:

     $ModLoad imudp
     $UDPServerAddress 192.0.2.1 # эта запись ДОЛЖНА быть перед директивой $UDPServerRun
     $UDPServerRun 514

Простая конфигурация (в базовом формате) будет выглядеть так:

[FILE] **`/etc/rsyslog.conf`**

    $ModLoad imuxsock.so
    $ModLoad imtcp.so
    $InputTCPServerAddress 192.0.2.1
    $InputTCPServerRun 10514
    $ModLoad imudp.so
    $UDPServerAddress 192.0.2.1
    $UDPServerRun 514
    *.info;mail.none;authpriv.none;cron.none      /var/log/messages
    authpriv.*                                    /var/log/secure
    mail.*                                        /var/log/maillog
    cron.*                                        /var/log/cron
    *.emerg                                       *
    uucp,news.crit                                /var/log/spooler
    local7.*                                      /var/log/boot.log

### [][Логирование в базу данных]

Rsyslog поддерживает логирование в следующие базы данных:

-   [MariaDB](https://wiki.gentoo.org/wiki/MariaDB "MariaDB")
-   [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL")
-   [PostgreSQL](https://wiki.gentoo.org/wiki/PostgreSQL "PostgreSQL")
-   Oracle

После выбора базы данных, в которую будут сохраняться журналы, необходимо включить соответствующий USE-флаг и переустановить rsyslog перед продолжением. В этом примере используется база данных MySQL.

** Note**\
Следующие шаги предполагают работающий сервер базы данных MySQL, запущенный на localhost; для деталей установки следуйте статье [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL").

Пакет содержит SQL-скрипт с именем createDB.sql для создания структуры базы данных.

[FILE] **`/usr/share/rsyslog/scripts/mysql/createDB.sql`**

    CREATE DATABASE Syslog;
    USE Syslog;
    CREATE TABLE SystemEvents
    (
            ID int unsigned not null auto_increment primary key,
            CustomerID bigint,
            ReceivedAt datetime NULL,
            DeviceReportedTime datetime NULL,
            Facility smallint NULL,
            Priority smallint NULL,
            FromHost varchar(60) NULL,
            Message text,
            NTSeverity int NULL,
            Importance int NULL,
            EventSource varchar(60),
            EventUser varchar(60) NULL,
            EventCategory int NULL,
            EventID int NULL,
            EventBinaryData text NULL,
            MaxAvailable int NULL,
            CurrUsage int NULL,
            MinUsage int NULL,
            MaxUsage int NULL,
            InfoUnitID int NULL ,
            SysLogTag varchar(60),
            EventLogType varchar(60),
            GenericFileName VarChar(60),
            SystemID int NULL
    );
    CREATE TABLE SystemEventsProperties
    (
            ID int unsigned not null auto_increment primary key,
            SystemEventID int NULL ,
            ParamName varchar(255) NULL ,
            ParamValue text NULL
    );

Импортируйте файл [/usr/share/rsyslog/scripts/mysql/createDB.sql] для создания базы данных `Syslog`.

`user `[`$`]`mysql -u root -p < /usr/share/rsyslog/scripts/mysql/createDB.sql`

Создайте пользователя базы данных для базы данных Syslog:

`mysql>``GRANT ALL ON Syslog.* TO rsyslog-user@localhost IDENTIFIED BY - 'MySecretPassword'; `

`mysql>``FLUSH PRIVILEGES; `

Чтобы обеспечить поддержку логирования в базу данных SQL, включите нужный модуль в [/etc/rsyslog.conf]

     $ModLoad ommysql.so

Сообщите rsyslog пересылать все данные в базу данных, добавьте следующее в конец файла [/etc/rsyslog.conf]:

     *.* :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword

Наконец, перезапустите сервер rsyslog, чтобы применить новые настройки

`root `[`#`]`/etc/init.d/rsyslog restart`

### [][Сервисы]

** Warning**\
Существует значительный конфликт между **systemd** и **rsyslogd**: старайтесь не смешивать их обоих, или, что еще хуже, не настраивать их на передачу сообщений друг другу (100% загрузка ЦП). Для максимальной гибкости и безопасности используйте **rsyslogd**.

#### [OpenRC]

Чтобы добавить демон [rsyslogd] в уровень запуска по умолчанию, чтобы логирование начиналось вместе с системой:

`root `[`#`]`rc-update add rsyslog default`

После завершения установки rsyslog должен работать из коробки с настройками по умолчанию; по крайней мере для локального логирования.

Чтобы запустить демон [rsyslogd]:

`root `[`#`]`rc-service rsyslog start`

Проверьте файл [/var/log/messages] на наличие записей syslog:

`root `[`#`]`tail -f /var/log/messages`

    2024-01-30T23:24:27.462647+01:00 server rsyslogd: [origin software="rsyslogd" swVersion="8.2212.0" x-pid="2404" x-info="https://www.rsyslog.com"] start

## [][Шаблоны]

Многие поставщики по-разному форматируют свои syslog-сообщения. Если сетевое оборудование логирует на центральный сервер rsyslog, разница в логировании будет легко заметна. После некоторого времени сбора журналов будет сложно фильтровать сообщения syslog-сервера по определенным параметрам:

-   Дата
-   Объект
-   Критичность
-   Хост
-   Syslogtag
-   ProcessID
-   MessageType
-   Сообщение

Чтобы унифицировать syslog-сообщения в определенный или предпочитаемый формат, Rsyslog использует шаблоны, которые разбирают входящие сообщения и \"переписывают\" их в желаемый формат.

Для поддержания простой и модульной конфигурации, шаблоны хранятся в директории [/etc/rsyslog.d/]. Чтобы включить файлы, хранящиеся в директории rsyslog.d, добавьте следующую строку в файл [/etc/rsyslog.conf]:

     $IncludeConfig /etc/rsyslog.d/*.conf

Шаблоны должны быть сохранены в директории [/etc/rsyslog.d/].

`root `[`#`]`cd /etc/rsyslog.d/`

** Important**\
Следующие шаблоны работают очень хорошо, но не являются идеальными.

Вот простой шаблон для хоста Cisco IOS, который логирует в rsyslogd:

[FILE] **`/etc/rsyslog.d/template_cisco.conf`**

    $template mysql_cisco, "insert into SystemEvents (Message, Facility, FromHost, Priority, DeviceReportedTime, ReceivedAt, InfoUnitID, SysLogTag) values ('%msg:R,ERE,1,DFLT:%[A-Z0-9_-]+: (.*)--end%', %syslogfacility%, '%fromhost%', %syslog
    priority%, '%timereported:::date-mysql%', '%timegenerated:::date-mysql%', %iut%, '%msg:R,ERE,0,DFLT:%[A-Z0-9_-]+:--end%')",SQL

Здесь простой шаблон для хоста ScreenOS, который логирует в rsyslogd:

[FILE] **`/etc/rsyslog.d/template_netscreen.conf`**

    $template mysql_netscreen, "insert into SystemEvents (Message, Facility, FromHost, Priority, DeviceReportedTime, ReceivedAt, InfoUnitID, SysLogTag) values ('%msg:R,ERE,1,DFLT:[a-zA-Z0-9-]+: (.*)--end%', %syslogfacility%, '%fromhost%', %s
    yslogpriority%, '%timereported:::date-mysql%', '%timegenerated:::date-mysql%', %iut%, '%msg:R,ERE,0,DFLT:[a-zA-Z0-9-]+:--end%')",SQL

Здесь простой шаблон для Linux-хоста, который логирует в rsyslogd:

[FILE] **`/etc/rsyslog.d/template_linux.conf`**

    $template mysql_linux, "insert into SystemEvents (Message, Facility, FromHost, Priority, DeviceReportedTime, ReceivedAt, IntoUnitID, SysLogTag) values ('%msg%', %syslogfacility%, '%HOSTNAME%', %syslogpriority%, '%timereported:::
    date-mysql%', '%timegenerated:::date-mysql%', %iut%, '%syslogtag:R,ERE,1,FIELD:(.+)(\[[0-9]\]).*--end%')" ,SQL

Настройте rsyslogd, какой предопределенный шаблон применять к какому объекту, добавьте следующие ссылки на шаблоны в конец файла [/etc/rsyslog.conf]:

-   Все сообщения, поступающие на объект **local4**, являются сообщениями Cisco IOS:

<!-- -->

     local4.* :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword;mysql_cisco

-   Все сообщения, поступающие на объект **local5**, являются сообщениями ScreenOS:

<!-- -->

     local5.* :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword;mysql_netscreen

-   Все сообщения, поступающие на syslog, считаются Linux-сообщениями, и игнорируют объекты **local4** и **local5**, у которых есть свои собственные шаблоны:

<!-- -->

     *.*;local4.none;local5.none :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword;mysql_linux

Следующий пример показывает, как файл [/etc/rsyslog.conf] может выглядеть на syslog-**сервере** с работающими шаблонами:

[FILE] **`/etc/rsyslog.conf`**

    $ModLoad imudp
    $UDPServerRun 514
    $ModLoad ommysql.so
    $IncludeConfig /etc/rsyslog.d/*.conf

    *.info;mail.none;authpriv.none;cron.none    -/var/log/messages
    authpriv.*                  /var/log/secure
    mail.*                      -/var/log/maillog
    cron.*                      -/var/log/cron
    *.emerg                     *
    uucp,news.crit                  -/var/log/spooler
    local7.*                    /var/log/boot.log

    local4.* :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword;mysql_cisco
    local5.* :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword;mysql_netscreen
    *.*;local4.none;local5.none :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword;mysql_linux

Перезагрузите сервер rsyslog, чтобы применить новые изменения:

`root `[`#`]`/etc/init.d/rsyslog reload`

Дополнительные примеры можно найти [здесь](http://www.rsyslog.com/doc/rsyslog_conf_templates.html).

## [][Использование]

Существует только один исполняемый файл, демон под названием [rsyslogd].

### [][Запуск]

Параметры командной строки НЕ встроены в [rsyslogd]. Для этого выполните просмотр страницы руководства:

`user `[`$`]`man rsyslogd`

    [Вывод команды man rsyslogd]

### [][Проверка конфигурационных файлов]

Чтобы проверить синтаксис файлов конфигурации ([/etc/rsyslog.conf]) для rsyslogd, проверьте файл конфигурации, выполнив:

`root `[`#`]`rsyslogd -N1`

    rsyslogd: version 8.2302.0, config validation run (level 1), master config /etc/rsyslog.conf
    rsyslogd: End of config validation run. Bye.

Чтобы проверить конфигурационные файлы в тестовой среде без root-прав, выполните:

`user `[`$`]`/usr/sbin/rsyslogd -N1 -f /usr/share/doc/rsyslog/examples/rsyslog.d/console.conf`

    rsyslogd: version 8.2302.0, config validation run (level 1), master config /usr/share/doc/rsyslog/examples/rsyslog.d/console.conf
    rsyslogd: End of config validation run. Bye.

## [][Удаление]

Удаление пакета [rsyslog] (инструментария и библиотеки) можно выполнить, запустив:

`root `[`#`]`emerge --ask --depclean --verbose app-admin/rsyslog`

## [][Устранение проблем]

Проверьте, запущен ли процесс syslog:

`root `[`#`]`ps ux | grep rsyslog`

    root     9161  0.0  0.0 1323652  3424 ?        Sl   00:51   0:00 /usr/sbin/rsyslogd -c5 -i /var/run/rsyslogd.pid -f /etc/rsyslog.conf

Проверьте сетевую конфигурацию:

`root `[`#`]`ss -tulpn | grep rsyslog`

    udp   UNCONN 0      0            0.0.0.0:514       0.0.0.0:*    users:(("rsyslogd",pid=1710,fd=6))
    udp   UNCONN 0      0            0.0.0.0:514       0.0.0.0:*    users:(("rsyslogd",pid=1710,fd=4))
    udp   UNCONN 0      0               [::]:514          [::]:*    users:(("rsyslogd",pid=1710,fd=7))
    udp   UNCONN 0      0               [::]:514          [::]:*    users:(("rsyslogd",pid=1710,fd=5))

Проверьте с помощью команды logger, поступают ли сообщения на syslog-сервер:

`user `[`$`]`logger -t test my syslog-test-message`

Следующее сообщение должно появиться в файле [/var/log/messages], если rsyslog работает правильно:

`root `[`#`]`tail /var/log/messages`

    ...
    2011-11-23T00:47:05+01:00 Rsyslogserver test: my syslog-test-message

## [][См. также]

-   [Metalog](https://wiki.gentoo.org/wiki/Metalog "Metalog") --- an alternative syslog daemon
-   [Sysklogd](https://wiki.gentoo.org/wiki/Sysklogd "Sysklogd") --- utility that reads and logs messages to the system console, logs files, other machines and/or users as specified by its configuration file.
-   [Syslog-ng](https://wiki.gentoo.org/wiki/Syslog-ng "Syslog-ng") --- a powerful, highly configurable monitoring and logging daemon.

## [][Внешние источники]

-   [Официальная документация](https://www.rsyslog.com/doc/master/index.html)
-   [Шаблоны Rsyslog HOWTO](http://www.rsyslog.com/doc/rsyslog_conf_templates.html)
-   [RFC 5424 - Протокол Syslog](https://tools.ietf.org/html/rfc5424)