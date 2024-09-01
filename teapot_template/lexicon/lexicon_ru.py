# русский лексикон бота
DICTIONARY_RU = {
    'USUAL_COMMANDS': {'/help': "Я могу помочь тебе с твоими чайными делами. "
                                "Тут имеется весь необходимый функционал бота.\n\n"
                                "Ты можешь добавлять, планировать, изменять и удалять свои чаепития с помощью "
                                "этих команд:\n\n"
                                "/showparties - показывает все твои чаепития\n/newparty - создать новую "
                                "запись\n/deleteparty - удалить запись\n"
                                "/changeparty - изменить запись\n/planparty - запланировать чаепитие"
                                "\n\nЧтобы посмотреть количество твоих чаепитий и твой уровень "
                                "Teapot:\n\n/showmyskill\n\nФункции для 'мои чаи':\n\n"
                                "/mytea - показывает список твоих чаев\n/addtea - добавляет чай в 'мои "
                                "чаи'\n/deletetea - удаляет чай из 'мои чаи'\n"
                                "/changetea - изменяет запись о чае в 'мои чаи'\n\nФункции для 'любимые чаи':\n\n"
                                "/toptea - показывает список твоих любимых чаев\n"
                                "/addtoptea - добавляет чай в 'любимые чаи'\n"
                                "/deletetoptea - удаляет чай из 'любимые чаи'\n"
                                "/changetoptea - изменяет запись о чае в 'любимые чаи'",
                       '/settings': "<b>Это настройки бота</b>",
                       '/cancel': "<b>Ты вышел</b> из создания чаепития/чая."
                                  "\n\nВсе введенные тобою данные <b>не были</b> зачтены."
                       },
    'INLINE_BUTTONS': {
        'MENU': {
            'TEA_PARTIES_BUTTON': {
                'NAME': "🫖 Мои чаепития",
                'CALLBACK': "TEA_PARTIES_BUTTON_PRESSED"
            },
            'MY_TEA_BUTTON': {
                'NAME': "🍵 Мои чаи",
                'CALLBACK': "MY_TEA_BUTTON_PRESSED"
            },
            'REMINDER_BUTTON': {
                'NAME': "📅 Мои напоминания",
                'CALLBACK': "REMINDERS_BUTTON_PRESSED"
            },
            'MY_TEAPOT_BUTTON': {
                'NAME': "🚀 Мой TeaPot",
                'CALLBACK': "MY_TEAPOT_BUTTON_PRESSED"
            }
        },
        'TEA_PARTIES': {
            'NEW_PARTY_BUTTON': {
                'NAME': "🍵 Новое чаепитие",
                'CALLBACK': "NEW_PARTY_BUTTON_PRESSED"
            },
            'SELECT_PARTY_BUTTON': {
                'NAME': "📜 История чаепитий",
                'CALLBACK': "SELECT_PARTY_BUTTON_PRESSED"
            },
            'TEAS': {
                'SHU_PUER': {
                    'NAME': "🌿 Шу пуэр",
                    'CALLBACK': "TEA_SHU_PUER_BUTTON_PRESSED"
                },
                'OOLONG': {
                    'NAME': "🏔️ Улун",
                    'CALLBACK': "TEA_OOLONG_BUTTON_PRESSED"
                },
                'SHEN_PUER': {
                    'NAME': "🍀 Шен пуэр",
                    'CALLBACK': "TEA_SHEN_PUER_BUTTON_PRESSED"
                },
                'RED_TEA': {
                    'NAME': "🎋 Красный чай",
                    'CALLBACK': "TEA_RED_TEA_BUTTON_PRESSED"
                },
                'WHITE_TEA': {
                    'NAME': "🌺 Белый чай",
                    'CALLBACK': "TEA_WHITE_TEA_BUTTON_PRESSED"
                },
                'GREEN_TEA': {
                    'NAME': "🌄 Зеленый чай",
                    'CALLBACK': 'TEA_GREEN_TEA_BUTTON_PRESSED'
                },
                'BERRY_TEA': {
                    'NAME': "🍓 Ягодный чай",
                    'CALLBACK': "TEA_BERRY_TEA_BUTTON_PRESSED"
                },
                'FRUIT_TEA': {
                    'NAME': "🍏 Фруктовый чай",
                    'CALLBACK': "TEA_FRUIT_TEA_BUTTON_PRESSED"
                }
            }
        },
        'CONFIRM': {
            'CONFIRM_BUTTON': {
                'NAME': "✅ Подтвердить",
                'CALLBACK': "CONFIRM_BUTTON_PRESSED"
            },
            'UNCONFIRM_BUTTON': {
                'NAME': "🔁 Изменить",
                'CALLBACK': "UNCONFIRM_BUTTON_PRESSED"
            }
        }
    },
    'REPLY_BUTTONS': {
        'MAIN_KB': {
            'MENU': {
                'NAME': "Меню 👀",
                'ANSWER': "Это <b>главное меню.</b>\nВыбери, куда хочешь перейти"
            },
            'SETTINGS': {
                'NAME': "Настройки ⚙️",
                'ANSWER': "Это настройки. Пока что этот пункт в разработке🔧"
            },
        },
        'SKIP_KB': {
            'NAME': '➡️ Пропустить',
        },
    },
    'PROCESS_FILL_TEA_PARTY': {

    },
    'ANOTHER_MESSAGES': {
        'usual': "Отправь мне команду из <b>списка команд.</b>"
                 "\n\nСписок команд можно посмотреть с помощью команды <b>/help.</b>",
        'photo': "Отличное фото! Но лучше отправь мне команду из <b>списка команд</b>."
                 "\n\nПосмотреть список команд можно по инструкции <b>/help</b>"
    }
}
