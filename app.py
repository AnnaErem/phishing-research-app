Путь
для
сохранения
данных
на
PythonAnywhere
# На PythonAnywhere домашняя директория доступна для записи
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Создаем папку для данных, если её нет
os.makedirs(DATA_DIR, exist_ok=True)

# Пути к файлам
QUESTIONNAIRE_FILE = os.path.join(DATA_DIR, 'questionnaire_responses.csv')
LOGS_FILE = os.path.join(DATA_DIR, 'experiment_logs.csv')

app = Flask(__name__)
app.secret_key = 'замените_на_случайную_строку_для_продакшена_2024_исследование'

# --- Данные для эксперимента ---
# Вариант 1 и 3 (равный статус, коллеги)
EMAILS_EQUAL_STATUS = [
    {
        'id': 1,
        'sender_name': 'Алексей, отдел аналитики',
        'sender_email': 'alexey@company.com',
        'subject': 'Вопрос по отчёту за вторник',
        'body': 'Привет! Твой отчёт по продажам за вторник выглядит странно: сумма по строке «Регионы» не сходится с общей. Можешь перепроверить и написать, где ошибка? Я пока сверяю свои данные. Спасибо.',
        'has_attachment': False,
        'has_link': False,
        'phishing_type': None
    },
    {
        'id': 2,
        'sender_name': 'Дмитрий, IT-поддержка',
        'sender_email': 'dmitry@company.com',
        'subject': 'Обновление внутреннего портала',
        'body': 'Коллеги, мы обновили страницу для заявок. Новая форма теперь вот здесь:\n\nhttps://portal.company.com/requests/new\n\nСтарая ссылка работать перестанет через неделю. Пожалуйста, пользуйтесь новой.',
        'has_attachment': False,
        'has_link': True,
        'link_url': 'https://portal.company.com/requests/new',
        'link_text': 'portal.company.com/requests/new',
        'phishing_type': None
    },
    {
        'id': 3,
        'sender_name': 'Екатерина, отдел обучения',
        'sender_email': 'ekaterina@company.com',
        'subject': 'Важно! Список участников тренинга 15 сентября',
        'body': 'Привет! Прикрепляю финальный список слушателей на тренинг «Эффективные коммуникации». Посмотри, если твоя фамилия есть – нужно подтвердить участие, открыв файл и нажав кнопку «Подтвердить» внутри документа. Сделай до завтра.',
        'has_attachment': True,
        'attachment_name': 'Список_участников_15.09.pdf.exe',
        'has_link': False,
        'phishing_type': None  # Убрали уведомление
    },
    {
        'id': 4,
        'sender_name': 'Екатерина, отдел обучения',
        'sender_email': 'ekaterina@company.com',
        'subject': 'Расписание тренингов на сентябрь',
        'body': 'Всем привет! На внутреннем вики-портале выложили график тренингов. Переходите по ссылке, чтобы записаться:\n\nhttp://wiki.company.com/trainings/2025-09\n\nКоличество мест ограничено.',
        'has_attachment': False,
        'has_link': True,
        'link_url': 'http://wiki.company.com/trainings/2025-09',
        'link_text': 'wiki.company.com/trainings/2025-09',
        'phishing_type': None
    },
    {
        'id': 5,
        'sender_name': 'Мария, клиентский сервис',
        'sender_email': 'maria@company.com',
        'subject': 'Итоги встречи с клиентом',
        'body': 'Всем привет. Напомню, что завтра в 11:00 общее собрание по проекту «Альфа». Я подготовила краткую выжимку по обратной связи – прикреплю позже. Если у кого-то есть дополнения, пишите в этот тред до 18:00.',
        'has_attachment': False,
        'has_link': False,
        'phishing_type': None
    },
    {
        'id': 6,
        'sender_name': 'Сергей, отдел закупок',
        'sender_email': 'sergey@company.com',
        'subject': 'Срочно! Новые корпоративные правила',
        'body': 'Коллеги, всем сотрудникам необходимо до конца дня подтвердить согласие с обновлённой политикой безопасности. Перейдите по ссылке:\n\nhttp://company-portal.com@security-update.net/auth\n\nЭто официальный портал, просто скопирован адрес. Требуется авторизация.',
        'has_attachment': False,
        'has_link': True,
        'link_url': 'http://company-portal.com@security-update.net/auth',
        'link_text': 'company-portal.com@security-update.net/auth',
        'phishing_type': None  # Убрали уведомление
    },
    {
        'id': 7,
        'sender_name': 'Михаил Сергеевич, руководитель проекта «Омега»',
        'sender_email': 'mikhail@company.com',
        'subject': 'Техническое задание (финальная версия)',
        'body': 'Всем участникам. Прикладываю финальное ТЗ, согласованное с заказчиком. Прошу внимательно прочитать раздел 4.3 (сроки). Если нет возражений, до вторника подписываем акт.',
        'has_attachment': True,
        'attachment_name': 'ТЗ_Омега_финал.pdf',
        'has_link': False,
        'phishing_type': None
    }
]

# Вариант 2 и 4 (высокий статус, руководство)
EMAILS_HIGH_STATUS = [
    {
        'id': 1,
        'sender_name': 'Анна Викторовна, руководитель отдела маркетинга',
        'sender_email': 'anna.viktorovna@company.com',
        'subject': 'Согласование бюджета на IV квартал',
        'body': 'Доброе утро. Прошу всех, кто участвует в планировании, к 14:00 прислать мне свои расчёты по строкам «Реклама» и «Мероприятия». Без них я не смогу защитить бюджет на совете директоров. Спасибо.',
        'has_attachment': False,
        'has_link': False,
        'phishing_type': None
    },
    {
        'id': 2,
        'sender_name': 'Елена Юрьевна, HR-директор',
        'sender_email': 'elena@company.com',
        'subject': 'Результаты опроса удовлетворённости',
        'body': 'Добрый день! По итогам июльского опроса мы подготовили дашборд. Ознакомиться можно здесь:\n\nhttps://analytics.company.com/survey/q3\n\nЕсли заметите ошибки в своих данных, напишите мне.',
        'has_attachment': False,
        'has_link': True,
        'link_url': 'https://analytics.company.com/survey/q3',
        'link_text': 'analytics.company.com/survey/q3',
        'phishing_type': None
    },
    {
        'id': 3,
        'sender_name': 'Олег Викторович, заместитель генерального директора',
        'sender_email': 'oleg.viktorovich@company.com',
        'subject': 'Срочно! Изменения в штатном расписании',
        'body': 'Уважаемые сотрудники! В связи с реорганизацией прошу всех срочно открыть вложенный файл и подтвердить ознакомление. Документ нужно подписать электронной подписью через форму внутри файла. Срок до конца дня.',
        'has_attachment': True,
        'attachment_name': 'Штатное_расписание_новая_версия.pdf.exe',
        'has_link': False,
        'phishing_type': None  # Убрали уведомление
    },
    {
        'id': 4,
        'sender_name': 'Наталья Андреевна, финансовый контролёр',
        'sender_email': 'natalia@company.com',
        'subject': 'Ссылка на новый регламент согласования платежей',
        'body': 'Коллеги, с 1 октября вступает в силу новый регламент. Все инструкции и шаблоны собраны на странице:\n\nhttps://finance.company.com/payment-rules\n\nОбязательно ознакомиться до 25 июня.',
        'has_attachment': False,
        'has_link': True,
        'link_url': 'https://finance.company.com/payment-rules',
        'link_text': 'finance.company.com/payment-rules',
        'phishing_type': None
    },
    {
        'id': 5,
        'sender_name': 'Иван Петрович, директор департамента',
        'sender_email': 'ivan.petrovich@company.com',
        'subject': 'Встреча с инвесторами 15.09',
        'body': 'Уважаемые коллеги, 15 сентября в 15:00 встреча с потенциальными инвесторами. Прошу подготовить краткие презентации по своим направлениям (до 5 слайдов). Тайминг выступления – до 7 минут. Вопросы можно задать мне лично.',
        'has_attachment': False,
        'has_link': False,
        'phishing_type': None
    },
    {
        'id': 6,
        'sender_name': 'Олег Викторович, заместитель генерального директора',
        'sender_email': 'oleg.viktorovich@company.com',
        'subject': 'Срочное распоряжение – ознакомиться всем',
        'body': 'Уважаемые коллеги! В связи с внеплановой проверкой безопасности, прошу каждого перейти по ссылке и подтвердить свои учётные данные до 16:00.\n\nСсылка: http://company-verify.com/login\n\nОбратите внимание – это внутренний защищённый узел. Не игнорируйте.',
        'has_attachment': False,
        'has_link': True,
        'link_url': 'http://company-verify.com/login',
        'link_text': 'company-verify.com/login',
        'phishing_type': None  # Убрали уведомление
    },
    {
        'id': 7,
        'sender_name': 'Михаил Сергеевич, руководитель проекта «Омега»',
        'sender_email': 'mikhail@company.com',
        'subject': 'Техническое задание (финальная версия)',
        'body': 'Всем участникам. Прикладываю финальное ТЗ, согласованное с заказчиком. Прошу внимательно прочитать раздел 4.3 (сроки). Если нет возражений, до вторника подписываем акт.',
        'has_attachment': True,
        'attachment_name': 'ТЗ_Омега_финал.pdf',
        'has_link': False,
        'phishing_type': None
    }
]


def init_csv_files():
    """Создание CSV файлов с заголовками, если они не существуют"""
    if not os.path.exists(QUESTIONNAIRE_FILE):
        with open(QUESTIONNAIRE_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'session_id', 'timestamp', 'variant',
                'screening_q1', 'screening_q2',
                'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7',
                'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19',
                'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26'
            ])

    if not os.path.exists(LOGS_FILE):
        with open(LOGS_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['session_id', 'timestamp', 'email_id', 'action_type'])


# Инициализация CSV файлов при запуске
init_csv_files()


# --- Маршруты ---

@app.route('/screening')
def screening():
    """Страница отборочных вопросов"""
    session.clear()
    session['session_id'] = str(uuid.uuid4())
    return render_template('screening.html')


@app.route('/save_screening', methods=['POST'])
def save_screening():
    """Сохранение ответов скрининга"""
    data = request.json
    session['screening_q1'] = data.get('q1')
    session['screening_q2'] = data.get('q2')
    return jsonify({'status': 'ok'})


@app.route('/screening-fail')
def screening_fail():
    """Страница для неподходящих участников"""
    return render_template('screening_fail.html')


@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    # Проверяем, прошёл ли пользователь скрининг
    if session.get('screening_q1') != 'yes' or session.get('screening_q2') != 'daily':
        return redirect(url_for('screening'))

    if request.method == 'POST':
        # Сохраняем ответы анкеты
        answers = request.form.to_dict()
        answers['session_id'] = session.get('session_id')
        answers['timestamp'] = datetime.now().isoformat()
        answers['variant'] = session.get('variant', random.randint(1, 4))

        # Добавляем ответы скрининга
        answers['screening_q1'] = session.get('screening_q1')
        answers['screening_q2'] = session.get('screening_q2')

        # Сохраняем в CSV
        with open(QUESTIONNAIRE_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            row = [
                answers.get('session_id'),
                answers.get('timestamp'),
                answers.get('variant'),
                answers.get('screening_q1'),
                answers.get('screening_q2')
            ]
            # Добавляем остальные ответы (q1-q26)
            for i in range(1, 27):
                row.append(answers.get(f'q{i}', ''))
            writer.writerow(row)

        return redirect(url_for('briefing2'))

    # Генерируем вариант эксперимента при первом заходе на анкету
    if 'variant' not in session:
        session['variant'] = random.randint(1, 4)

    return render_template('questionnaire.html')


@app.route('/briefing2')
def briefing2():
    variant = session.get('variant', 1)
    has_timer = variant in [3, 4]
    high_status = variant in [2, 4]

    return render_template('briefing2.html', has_timer=has_timer, high_status=high_status)


@app.route('/experiment')
def experiment():
    variant = session.get('variant', 1)
    has_timer = variant in [3, 4]
    high_status = variant in [2, 4]

    # Выбираем правильный набор писем
    if high_status:
        emails = EMAILS_HIGH_STATUS
    else:
        emails = EMAILS_EQUAL_STATUS

    timer_limit = 180 if has_timer else 0

    session['experiment_started'] = True

    return render_template('experiment.html',
                           emails=emails,
                           has_timer=has_timer,
                           timer_limit=timer_limit,
                           high_status=high_status)


@app.route('/log_action', methods=['POST'])
def log_action():
    """Логирование действий пользователя"""
    data = request.json
    session_id = session.get('session_id')

    with open(LOGS_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            session_id,
            datetime.now().isoformat(),
            data.get('email_number'),
            data.get('action_type')
        ])

    return jsonify({'status': 'ok'})


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


@app.route('/')
def index():
    """Начальная страница - ведёт на скрининг"""
    return redirect(url_for('screening'))


# --- Админ-маршруты для скачивания данных ---
@app.route('/admin/download-questionnaire')
def download_questionnaire():
    """Скачивание анкетных данных (защищено паролем)"""
    password = request.args.get('password')
    if password != 'research2024':  # Замените на свой пароль
        return "Доступ запрещен. Используйте ?password=ваш_пароль", 403

    with open(QUESTIONNAIRE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    return Response(
        content,
        mimetype='text/csv',
        headers={"Content-Disposition": "attachment;filename=questionnaire_data.csv"}
    )


@app.route('/admin/download-logs')
def download_logs():
    """Скачивание логов действий (защищено паролем)"""
    password = request.args.get('password')
    if password != 'research2024':  # Замените на свой пароль
        return "Доступ запрещен. Используйте ?password=ваш_пароль", 403

    with open(LOGS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    return Response(
        content,
        mimetype='text/csv',
        headers={"Content-Disposition": "attachment;filename=experiment_logs.csv"}
    )


# Для локального запуска
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)