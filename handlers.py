
from markups import *
from db_tools import *
from preprocessor import *
from predict_nn import model

async def start(update, context):
    if update.effective_user.id not in fetch_list('user_info', 'user_id'):
        insert_values('user_info', 'user_id', update.effective_user.id)
        insert_values('diagnoses', 'user_id', update.effective_user.id)
    else:
        set_value('user_info', 'status', 0, f'user_id={update.effective_user.id}')
    await event_loop(update, context)


async def event_loop(update, context, user_context=None):
    if not user_context:
        input_data = [
            update.callback_query.data if update.callback_query else None,
            update.message.text if update.message else None,
        ]
        user_context = {
            'user_id': update.effective_user.id,
            'status': fetch_column('user_info', 'status', f'user_id={update.effective_user.id}'),
            'message_text': next((i for i in input_data if i))
        }
    status = user_context['status']
    if status == 0:
        await main_menu(update, context, user_context)
    elif status == 1:
        await criteria_menu(update, context, user_context)
    elif status == 2:
        await input_value(update, context, user_context)


async def main_menu(update, context, user_context):
    message_text = user_context['message_text']
    if message_text in DIAGNOSIS_DATA.keys():
        set_value('user_info', 'status', 1, f'user_id={update.effective_user.id}')
        set_value('user_info', 'input_group', f'"{message_text}"',
                  f'user_id={update.effective_user.id}')
        user_context['status'] = 1
        user_context['message_text'] = '-'
        await event_loop(update, context, user_context)
    elif message_text == 'get_result':
        headers = diagnosis_columns()
        values = fetch_list('diagnoses', '*', f'user_id={update.effective_user.id}')[1:]

        our_data = pd.DataFrame(data=dict(zip(headers, values)), index=[0])
        our_data = pd.concat([our_data, data_reader('mimic_data.csv')])
        transformer = data_preprocessing(our_data).fit_transform(our_data)
        prediction = model.predict(transformer[0:1])

        await context.bot.send_message(
            chat_id=user_context['user_id'],
            text=f"Вероятность благоприятного исхода: {round(float(prediction) * 100, 2)} %",
            reply_markup=back_kb
        )
    else:
        await context.bot.send_message(
            chat_id=user_context['user_id'],
            text=f'Здравствуйте, {update.effective_user.first_name}! Это телеграм бот расчитывающий '
                 f'вероятность благоприятного исхода при попадани в отделение реанимации при помощи'
                 f'нейронной сети. \n'
                 f'Для получения результата, необходимо'
                 f'ввести как можно больше информации о пациенте, если данные не ввести значения будут взяты '
                 f'"в среднем по больнице".',
            reply_markup=main_kb
        )


async def criteria_menu(update, context, user_context):
    cur_group = fetch_column('user_info', 'input_group', f'user_id={update.effective_user.id}')
    accessible_criteria = [item['callback_data'] for item in DIAGNOSIS_DATA[cur_group]['criteria']]
    message_text = user_context['message_text']
    if message_text == 'back':
        set_value('user_info', 'status', 0, f'user_id={update.effective_user.id}')
        user_context['message_text'] = '-'
        user_context['status'] = 0
        await event_loop(update, context, user_context)
    elif message_text in accessible_criteria:
        set_value('user_info', 'status', 2, f'user_id={update.effective_user.id}')
        set_value('user_info', 'input_criteria', f'"{message_text}"',
                  f'user_id={update.effective_user.id}')
        criteria_index = accessible_criteria.index(message_text)
        accusative_form = DIAGNOSIS_DATA[cur_group]['criteria'][criteria_index]['accusative_form']
        await context.bot.send_message(
            chat_id=user_context['user_id'],
            text=f'Введите {accusative_form}',
            reply_markup=back_kb
        )
    else:
        await context.bot.send_message(
            chat_id=user_context['user_id'],
            text=f'Выберите категорию',
            reply_markup=criteria_kb(cur_group)
        )


async def input_value(update, context, user_context):
    if user_context['message_text'] == 'back':
        set_value('user_info', 'status', 1, f'user_id={update.effective_user.id}')
        user_context['message_text'] = '-'
        #user_context['status'] = 1
        await event_loop(update, context, user_context)
    else:
        if update.message and update.message.text.replace('.', '').isnumeric():
            criteria = fetch_column('user_info', 'input_criteria',
                                    f'user_id={update.effective_user.id}')
            set_value('diagnoses', criteria, update.message.text,
                      f'user_id={update.effective_user.id}')
            set_value('user_info', 'status', 1, f'user_id={update.effective_user.id}')
            user_context['message_text'] = '-'
            user_context['status'] = 1
            await event_loop(update, context, user_context)
        else:
            await context.bot.send_message(
                chat_id=user_context['user_id'],
                text=f'Введите корректное значение',
                reply_markup=back_kb
            )
