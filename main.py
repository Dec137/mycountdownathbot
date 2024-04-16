import os
import datetime
import pytz
import telegram

# Set the countdown times in Central European Time
rome = pytz.timezone('Europe/Rome')
countdown_time1 = rome.localize(datetime.datetime(2024, 6, 30, 18, 25))

# Set the countdown times in Eastern European Time
athens = pytz.timezone('Europe/Athens')
countdown_time2 = athens.localize(datetime.datetime(2024, 7, 3, 21, 0))

end_time = rome.localize(datetime.datetime(2024, 7, 5, 17, 25))

def telegram_bot(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        message = update.message.text

        # Check if the message is a command
        if message.startswith('/'):
            command = message[1:]
            # Handle /traquanto command
            if command.startswith('traquanto'):
                # Check if the current time is after the end time
                if datetime.datetime.now(pytz.timezone('Europe/Rome')) > end_time:
                    now = datetime.datetime.now(pytz.timezone('Europe/Rome'))
                elif datetime.datetime.now(pytz.timezone('Europe/Rome')) > countdown_time1:
                    now = datetime.datetime.now(pytz.timezone('Europe/Athens'))
                else:
                    now = datetime.datetime.now(pytz.timezone('Europe/Rome'))

                # Check if the current time is after the end time
                if now > end_time:
                    bot.sendMessage(chat_id=chat_id, text='Che storia...')
                    return "zio pera"

                # Calculate remaining time for the first countdown
                remaining1 = countdown_time1 - now
                days1, seconds1 = remaining1.days, remaining1.seconds
                hours1 = seconds1 // 3600
                minutes1 = (seconds1 % 3600) // 60
                seconds1 = (seconds1 % 60)

                # Calculate remaining time for the second countdown
                remaining2 = countdown_time2 - now
                days2, seconds2 = remaining2.days, remaining2.seconds
                hours2 = seconds2 // 3600
                minutes2 = (seconds2 % 3600) // 60
                seconds2 = (seconds2 % 60)

                # Translate to Italian
                days_word1 = "giorno" if days1 == 1 else "giorni"
                hours_word1 = "ora" if hours1 == 1 else "ore"
                minutes_word1 = "minuto" if minutes1 == 1 else "minuti"
                seconds_word1 = "secondo" if seconds1 == 1 else "secondi"

                days_word2 = "giorno" if days2 == 1 else "giorni"
                hours_word2 = "ora" if hours2 == 1 else "ore"
                minutes_word2 = "minuto" if minutes2 == 1 else "minuti"
                seconds_word2 = "secondo" if seconds2 == 1 else "secondi"

                # Check if the first countdown is over
                if now > countdown_time1:
                    if now > countdown_time2 and now < end_time:  # Add this check
                        bot.sendMessage(chat_id=chat_id, text='LESGOOOOOOOOOOOOO')
                    elif now < countdown_time2:  # Add this check
                        if days2 > 0:
                            manca_word = "Manca" if days2 == 1 else "Mancano"
                            bot.sendMessage(chat_id=chat_id, text=f'Siamo ad Atene! {manca_word} solo {days2} {days_word2}, {hours2} {hours_word2}, {minutes2} {minutes_word2}, {seconds2} {seconds_word2} al concerto degli Opeth + Leprous!')
                        elif hours2 > 0:
                            manca_word = "Manca" if hours2 == 1 else "Mancano"
                            bot.sendMessage(chat_id=chat_id, text=f'Siamo ad Atene! {manca_word} solo {hours2} {hours_word2}, {minutes2} {minutes_word2}, {seconds2} {seconds_word2} al concerto degli Opeth + Leprous!')
                        elif minutes2 > 0:
                            manca_word = "Manca" if minutes2 == 1 else "Mancano"
                            bot.sendMessage(chat_id=chat_id, text=f'Siamo ad Atene! {manca_word} solo {minutes2} {minutes_word2}, {seconds2} {seconds_word2} al concerto degli Opeth + Leprous!')
                        else:
                            manca_word = "Manca" if seconds2 == 1 else "Mancano"
                            bot.sendMessage(chat_id=chat_id, text=f'Siamo ad Atene! {manca_word} solo {seconds2} {seconds_word2} al concerto degli Opeth + Leprous!')

                elif now < countdown_time1:  # Add this check
                    if days1 > 0:
                        manca_word = "Manca" if days1 == 1 else "Mancano"
                        bot.sendMessage(chat_id=chat_id, text=f'Decolliamo per Atene tra {days1} {days_word1}, {hours1} {hours_word1}, {minutes1} {minutes_word1} e {seconds1} {seconds_word1}. {manca_word} {days2} {days_word2}, {hours2} {hours_word2}, {minutes2} {minutes_word2} e {seconds2} {seconds_word2} al concerto degli Opeth + Leprous!')
                    elif hours1 > 0:
                        manca_word = "Manca" if hours1 == 1 else "Mancano"
                        bot.sendMessage(chat_id=chat_id, text=f'Decolliamo per Atene tra {hours1} {hours_word1}, {minutes1} {minutes_word1} e {seconds1} {seconds_word1}. {manca_word} {days2} {days_word2}, {hours2} {hours_word2}, {minutes2} {minutes_word2} e {seconds2} {seconds_word2} al concerto degli Opeth + Leprous!')
                    elif minutes1 > 0:
                        manca_word = "Manca" if minutes1 == 1 else "Mancano"
                        bot.sendMessage(chat_id=chat_id, text=f'Decolliamo per Atene tra {minutes1} {minutes_word1} e {seconds1} {seconds_word1}. {manca_word} {days2} {days_word2}, {hours2} {hours_word2}, {minutes2} {minutes_word2} e {seconds2} {seconds_word2} al concerto degli Opeth + Leprous!')
                    else:
                        manca_word = "Manca" if seconds1 == 1 else "Mancano"
                        bot.sendMessage(chat_id=chat_id, text=f'Decolliamo per Atene tra {seconds1} {seconds_word1}. {manca_word} {days2} {days_word2}, {hours2} {hours_word2}, {minutes2} {minutes_word2} e {seconds2} {seconds_word2} al concerto degli Opeth + Leprous!')
                return "zio perino"

            # Handle /aiuto command
            elif command == 'aiuto':
                help_text = """
                Ecco cosa può fare questo bot:
                - /traquanto: Ci dice quanto tempo manca al viaggetto della vita. Lesgoooooooo! :)
                - /E basta, cce t'aggiu ffare? Nu cafè?
                """
                bot.sendMessage(chat_id=chat_id, text=help_text)
                return "zio peride"
            # Handle /E command
            elif command.startswith('E'):
                bot.sendMessage(chat_id=chat_id, text='/E si nu ciola')
                return "zio perkele"

    return "zio perone"
