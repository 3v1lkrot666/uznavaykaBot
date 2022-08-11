start_message_text = '\n \
                \n <b>Добро пожаловать</b> 🖐\
                \n \
                \n  <em> В чём заключается наша работа </em> ❓ \
                \n \
                \n - Здесь наша команда максимально быстро поможет Вам сделать профессионально ту или иную работу, в сфере образования (Рефераты, Курсовые, Дипломные работы и т.д.) \
                \n \
                \n - С Вами будут работать специалисты разных областей и доводить работу до идеала, в удобные для Вас сроки \
                \n \
                \n -Здесь нет ограничения по возрасту. Не важно учитесь ли Вы в университете, в школе, либо же работаете \
                \n \
                \n 🕵️‍♂️Следующий и самый главный этап заключается в выборе самой работы и её деталей.\
                \n \
                \n <b>1️⃣ На панели меню, которое находится ниже, Вы можете правильно выбрать вид работы, который Вас интересует</b>👇'

text_cursovaya_rabota = 'Вы выбрали тип работы-курсовая работа \
\n Курсовая работа — задание, которое выполняется студентами высших и средне-специальных учебных заведений, \
обычно на втором–третьем курсах (иногда и на первом курсе) в виде рефератов, на старших — в виде исследовательской работы\
Данный тип работы предполагает:\
\n -от 25 страниц текста \
\n -оригинальность от 50%\
\n -практическая часть (при необходимости)\
\n По общему правилу структура работы включает в себя: \
Введение, две главы, в каждой из которых по два параграфа, заключение и список литературы\
\n '

text_diplomnaya_rabota = 'Вы выбрали тип работы-дипломная работа \
\n Дипло́мная рабо́та — один из видов выпускной квалификационной работы (ВКР) — \
 самостоятельная итоговая творческая работа студентов, обучающихся по программам \
 подготовки специалистов, бакалавров и магистров, выполняемая ими на последнем, выпускном курсе.\
\n Данный тип работы предполагает:\
\n -от 40 страниц текста \
\n -оригинальность от 50%\
\n -практическая часть (при необходимости)\
\n По общему правилу структура работы включает в себя: \
Введение, три главы, в двух из которых по два параграфа, заключение и список литературы \
\n '

text_nauchnaya_statya = 'Вы выбрали тип работы-научная статья \
Научная статья – это законченное и логически цельное произведение, \
освещающее какую-либо тему, входящую в круг проблем, связанных с темой диссертации.\
\n Данный тип работы предполагает \
\n -от 3 страниц текста \
\n -оригинальность от 70%\
\n К научным статьям по общему правилу предъявляются требования РИНЦа и ВАКа\
\n '


text_referat = 'Вы выбрали тип работы-реферат\
\n Рефера́т — краткий доклад или презентация по определённой теме, \
где собрана информация из одного или нескольких источников. \
Рефераты могут являться изложением содержания научной работы. \
Данный тип работы предполагает:\
\n -от 25 страниц текста \
\n -оригинальность от 50%\
\n По общему правилу структура работы включает в себя: \
Введение, две главы, заключение и список литературы \
\n '

text_laboratornaya_rabota = 'Вы выбрали тип работы-лабораторная работа \
\n Лабораторная работа – это такой метод обучения, при котором студенты под руководством \
преподавателя по заранее намеченному плану выполняют определенные практические задания\
 и в процессе их выполнения воспринимают и осмысливают новый учебный материал,\
  закрепляют изученное, применяют теоретические знания при решении практических задач,\
   формируют навыки разрешения тех или иных ситуаций. \
\n '

message_text_fake_one = f'Ожидайте идёт обработка вашего заказа'
message_text_fake_two = f'Ищем подходящего специалиста'
message_text_fake_three = f'Создаём заявку'
 #if works == 'Реферат':
      #  themes = fields.StringField(text_referat)
    #elif works == 'Курсовая работа':
        #themes = fields.StringField(text_cursovaya_rabota)
    #elif works == 'Дипломная работа':
        #themes = fields.StringField(text_diplomnaya_rabota)
    #elif works == 'Научная работа':
        #themes = fields.StringField(text_nauchnaya_statya)
    #elif works == 'Лабораторная работа':
        #themes = fields.StringField(text_laboratornaya_rabota)
    #elif works == 'Другой вариант':
        #themes = fields.StringField('2️⃣ Четко и правильно сформулируйте тему Вашей работы')
   # else:
    #    print('asd')