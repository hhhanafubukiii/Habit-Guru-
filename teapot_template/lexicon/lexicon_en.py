HELP_FILE_EN = open(r"D:\For TeaPot_tg\Texts\help_en.txt", 'rb')

# английский лексикон бота
DICTIONARY_EN = {
    'QUOTE_ANS': {'QUOTE_LIST': {1: "<i>Thomas Garvey, owner of England's first tea shop.</i>\n---------------\n"
                                    "<i><b>«Tea boosts muscle tone, making the body strong. It helps with headache "
                                    "and dizziness, lifts your spirits and chases away the slumber. "
                                    "Tea clears kidney stones and sand, if consumed with honey instead of sugar, "
                                    "it eases breathing in colds. This drink helps improve eyesight. Tea relieves "
                                    "fatigue, making a person cheerful.»</b></i>",
                                 2: f"<i>Liu Zhen Liang</i>\n---------------\n"
                                    "<i><b>«Tea elevates the palate and helps you achieve refinement of "
                                    "will.»</b></i>",
                                 3: f"<i>Henry James, American writer</i>\n---------------\n"
                                    "<i><b>«There are few hours in a person's life that are more enjoyable than "
                                    "the time devoted to evening tea.»</b></i>",
                                 }
                  },
    'USUAL_COMMANDS_ANS': {'HELP_ANS': HELP_FILE_EN.read(),
                           'USUAL_MES_ANS': "Send me a command from <strong>the command list.</strong>\n<strong>The "
                                            "list of commands can be viewed with the /help instruction.</strong>"
                           },
    'MEME_ANS': {'MEME_PHOTO_DICT': {1: "https://avatars.dzeninfra.ru/get-zen_doc/5323197"
                                        "/pub_635b931f6f19516f07f19522_635b94b8c8b9af558ecbb342/scale_1200",
                                     2: "https://sun9-37.userapi.com/impf/wgdNV-ZyrsHezsHufKZ_TkMjPghAN-AUbc2T9w"
                                        "/ofSC64PxygA.jpg"
                                        "?size=469x600&quality=96&sign=423789055e18e53e8a69d87e60eb50f6&type=album",
                                     3: "https://avatars.dzeninfra.ru/get-zen_doc/5249897"
                                        "/pub_635b931f6f19516f07f19522_635b9533749697368b60fc1d/scale_1200",
                                     4: "https://cm.author.today/content/2022/12/28"
                                        "/53f73b8cc7d04cb9aa4ee2261dc981e2.jpg?width=750&rmode=max",
                                     5: "https://sun9-21.userapi.com/impf/Ke9L0JW7DuVIItUSIhtZS58ZvD_CDlOZWo3suA"
                                        "/RLwkJHRR5I0.jpg"
                                        "?quality=95&as=32x23,48x35,72x52,108x78,160x116,240x174,360x260,480x347,"
                                        "540x390,640x463,720x521,"
                                        "1080x781&sign=591cf1b69e4cc11fd3614c7778398648&from=bu&u"
                                        "=q55TMWO7UWegiDTG_8g47RLkynDnbx56BSodNqynZRw&cs=604x437",
                                     6: "https://bryansktoday.ru/uploads/common/933a9ec5117e9435_XL.jpg",
                                     7: "https://memozg.ru/img/posts/4241_65cbc23cb3ec7.webp",
                                     8: "https://encrypted-tbn0.gstatic.com/images?q=tbn"
                                        ":ANd9GcRUV01peDcsFUP973nWhg5fEhuUfMv5vUF7zA&s",
                                     9: "https://encrypted-tbn0.gstatic.com/images?q=tbn"
                                        ":ANd9GcTTGBEsC8fhHP694fwryGBI54anXBN5o1HZXg&s",
                                     10: "https://kartinkof.club/uploads/posts/2022-03/1648242078_10-kartinkof"
                                         "-club-p-mem-pyu-chai-10.jpg",
                                     11: "https://kartinkof.club/uploads/posts/2022-03/1648242080_13-kartinkof"
                                         "-club-p-mem-pyu-chai-13.jpg",
                                     12: "https://kartinkof.club/uploads/posts/2022-03/1648242072_5-kartinkof"
                                         "-club-p-mem-pyu-chai-5.jpg"
                                     }
                 }
}
