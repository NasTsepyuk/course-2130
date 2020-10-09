import logging

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

from weather_api import WeatherAPI
from tokens import YANDEX_WEATHER_API_KEY, TELEGRAM_KEY

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


WEATHER_CONVERSATION_COMMANDS = ['current', 'forecast']
WEATHER_COMMAND_SELECTION = 0
WEATHER_RETURN = 1


def start(update, context):
    """Send a message when the command /start is issued."""

    update.message.reply_text('Welcome to my weather API bot')
    update.message.reply_text('Send me /weather ')


def get_weather_start(update, context):
    reply_markup = telegram.ReplyKeyboardMarkup([[telegram.KeyboardButton('send my location', request_location=True)]])
    update.message.reply_text('Send me the coordinates or /cancel', reply_markup=reply_markup)
    return 0


def coordinates_handler(update, context):
    reply_markup = telegram.ReplyKeyboardMarkup(
        [[telegram.KeyboardButton(item) for item in WEATHER_CONVERSATION_COMMANDS]]
    )
    update.message.reply_text('Thank you. You location is captured', reply_markup=reply_markup)
    # find and save location property in update
    # you can use `context.user_data["location"]` to save user data
    context.user_data["location"] = update.message.location
    return 1


def weather_handler(update, context):
    lat = context.user_data["location"]['latitude']   # updated
    lon = context.user_data["location"]['longitude']  # updated
    if update.message.text == WEATHER_CONVERSATION_COMMANDS[0]:
        update.message.reply_text('current weather', reply_markup=telegram.ReplyKeyboardRemove())
        # TODO: send a current weather from yandex there
        weather_reply = WeatherAPI(YANDEX_WEATHER_API_KEY).get_current_weather(lat=lat, lon=lon)
        update.message.reply_text('\n'.join([f'{key}: {value}' for (key, value) in weather_reply.items()]))


    elif update.message.text == WEATHER_CONVERSATION_COMMANDS[1]:
        update.message.reply_text('forecast', reply_markup=telegram.ReplyKeyboardRemove())
        # TODO: send a forecast of weather from yandex there
        weather_reply_dict = WeatherAPI(YANDEX_WEATHER_API_KEY).get_forecast(lat=lat, lon=lon)
        weather_reply = []
        for day_forecast in weather_reply_dict:
            weather_reply.append(', '.join([f'{key}: {value}' for (key, value) in day_forecast.items()]))
        update.message.reply_text('\n'.join(weather_reply))
    return ConversationHandler.END


def cancel(update, context):
    update.message.reply_text('Ok, thank you for your attention!', reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def start_telegram_bot() -> object:
    updater = Updater(TELEGRAM_KEY, use_context=True)
    dp = updater.dispatcher
    # setup commands
    dp.add_handler(CommandHandler("start", start))

    event_conversation = ConversationHandler(
        entry_points=[CommandHandler("weather", get_weather_start)],
        states={
            0: [MessageHandler(Filters.location, coordinates_handler)],
            1: [MessageHandler(Filters.regex(f'^({"|".join(WEATHER_CONVERSATION_COMMANDS)})'), weather_handler)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    dp.add_handler(event_conversation)
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    weather_api = WeatherAPI(YANDEX_WEATHER_API_KEY)
    start_telegram_bot()
