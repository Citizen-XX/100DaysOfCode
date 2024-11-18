from tkinter import Button, Label, PhotoImage, Tk, Canvas
from random import choice
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
words_choice = None
flip_timer = None

try:
    csv_records_list = pd.read_csv(
        r'Day31_FlashCardApp_Project/data/words_to_learn.csv').to_dict(orient='records')
    print('Previous Data Found, Loading Data...')
except FileNotFoundError as e:
    print(f'No Previous Data Found, Starting Fresh: {e}')
    csv_records_list = pd.read_csv(
        r'Day31_FlashCardApp_Project/data/french_words.csv').to_dict(orient='records')

# print(csv_records_list)
# df = pd.read_csv(
#     r'Day31_FlashCardApp_Project/data/french_words.csv')
# words_dicts_list = [{data.French: data.English} for _, data in df.iterrows()]
# print(words_dicts_list)

# Card Flipper


def timer_and_flipper(english_word):
    flash_card_canvas.itemconfig(card_image, image=back_card_img)
    flash_card_canvas.itemconfig(card_title, text='English', fill='white')
    flash_card_canvas.itemconfig(card_word, text=english_word, fill='white')

# Random Word Picker


def random_word_picker():
    global words_choice, flip_timer
    window.after_cancel(flip_timer)
    words_choice = choice(csv_records_list)
    french = words_choice['French']
    english = words_choice['English']
    flash_card_canvas.itemconfig(card_title, text='French', fill='black')
    flash_card_canvas.itemconfig(card_word, text=french, fill='black')
    flip_timer = window.after(3000, timer_and_flipper, english)
    flash_card_canvas.itemconfig(card_image, image=front_card_img)
    return words_choice

# Data Was Known


def data_was_known():
    words_choice = random_word_picker()
    # print(len(csv_records_list))
    csv_records_list.remove(words_choice)
    # print(pd.DataFrame(csv_records_list))
    pd.DataFrame(data=csv_records_list).to_csv(
        r'Day31_FlashCardApp_Project/data/words_to_learn.csv', index=False)


# Window
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flip Timer
flip_timer = window.after(3000, func=timer_and_flipper)

# Flash Card Canvas
front_card_img = PhotoImage(
    file=r'Day31_FlashCardApp_Project/images/card_front.png')
back_card_img = PhotoImage(
    file=r'Day31_FlashCardApp_Project/images/card_back.png')
flash_card_canvas = Canvas(width=800, height=526)
card_image = flash_card_canvas.create_image(400, 262, image=front_card_img)
flash_card_canvas.grid(column=0, row=0, columnspan=2)
flash_card_canvas.config(
    background=BACKGROUND_COLOR, highlightthickness=0)
card_title = flash_card_canvas.create_text(
    400, 150, text='', font=('Arial', 40, 'italic'))
card_word = flash_card_canvas.create_text(
    400, 263, text='', font=('Arial', 60, 'bold'))

# Wrong Button
unknown_img = PhotoImage(file=r'Day31_FlashCardApp_Project/images/wrong.png')
unknown_button = Button(image=unknown_img, highlightthickness=0)
unknown_button.config(border=0, command=random_word_picker)
unknown_button.grid(column=0, row=1)

# Check Button
check_img = PhotoImage(file=r'Day31_FlashCardApp_Project/images/right.png')
check_button = Button(image=check_img, highlightthickness=0)
check_button.config(border=0, command=data_was_known)
check_button.grid(column=1, row=1)

random_word_picker()

window.mainloop()
