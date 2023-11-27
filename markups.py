from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from db_tools import DIAGNOSIS_DATA

main_kb = InlineKeyboardMarkup(
    [[InlineKeyboardButton(
            text=DIAGNOSIS_DATA[key]['button_text'],
            callback_data=key
      )]
     for key in DIAGNOSIS_DATA] +
    [[InlineKeyboardButton(
            text='Получить результат',
            callback_data='get_result'
      )]]
)

back_kb = InlineKeyboardMarkup(
    [[InlineKeyboardButton(
            text='Назад',
            callback_data='back'
      )]]
)

# start_kb = InlineKeyboardMarkup(
#     [[InlineKeyboardButton(
#             text='Начать',
#             callback_data='start'
#       )]]
# )


def criteria_kb(criterion_group):
    return (
        InlineKeyboardMarkup(
            [[InlineKeyboardButton(
                    text=item['button_text'],
                    callback_data=item['callback_data']
              )]
             for item in DIAGNOSIS_DATA[criterion_group]['criteria']] +
            [[InlineKeyboardButton(
                    text='Назад',
                    callback_data='back'
              )]]
        )
    )
