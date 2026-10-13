import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


keys = [
    list("QWERTYUIOP"),
    list("ASDFGHJKL"),
    list("ZXCVBNM")
]

key_width = 70
key_height = 60
gap = 10

start_y = 250


special_keys = [
    "SPACE",
    "BACKSPACE",
    "ENTER",
    "UP",
    "DOWN",
    "LEFT",
    "RIGHT"
]

last_key = None
last_press_time = 0
press_delay = 0.4


def get_key(x, y, frame_width):

    
    for row, key_row in enumerate(keys):

        row_width = (
            len(key_row) * key_width
            + (len(key_row) - 1) * gap
        )

        start_x = (frame_width - row_width) // 2

        for col, key in enumerate(key_row):

            key_x = start_x + col * (key_width + gap)
            key_y = start_y + row * (key_height + gap)

            if (
                key_x < x < key_x + key_width
                and key_y < y < key_y + key_height
            ):
                return key

    
    space_x = 250
    space_y = 475

    if (
        space_x < x < space_x + 450
        and space_y < y < space_y + key_height
    ):
        return "SPACE"


    
    back_x = 720

    if (
        back_x < x < back_x + 180
        and space_y < y < space_y + key_height
    ):
        return "BACKSPACE"


    
    enter_x = 920

    if (
        enter_x < x < enter_x + 180
        and space_y < y < space_y + key_height
    ):
        return "ENTER"

    

    arrow_y = 555


    
    if (
        520 < x < 590
        and arrow_y < y < arrow_y + key_height
    ):
        return "LEFT"

    
    if (
        600 < x < 670
        and arrow_y < y < arrow_y + key_height
    ):
        return "DOWN"

    
    if (
        680 < x < 750
        and arrow_y < y < arrow_y + key_height
    ):
        return "UP"

    
    if (
        760 < x < 830
        and arrow_y < y < arrow_y + key_height
    ):
        return "RIGHT"

    return None




def draw_keyboard(frame, selected_key):

    h, w, _ = frame.shape


    
    for row, key_row in enumerate(keys):

        row_width = (
            len(key_row) * key_width
            + (len(key_row) - 1) * gap
        )

        start_x = (w - row_width) // 2

        for col, key in enumerate(key_row):

            x = start_x + col * (key_width + gap)
            y = start_y + row * (key_height + gap)

            if key == selected_key:
                color = (0, 255, 0)
                thickness = -1
            else:
                color = (255, 255, 255)
                thickness = 2

            cv2.rectangle(
                frame,
                (x, y),
                (x + key_width, y + key_height),
                color,
                thickness
            )

            text_color = (
                (0, 0, 0)
                if key == selected_key
                else color
            )

            cv2.putText(
                frame,
                key,
                (x + 20, y + 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                text_color,
                2
            )


    
    space_x = 250
    space_y = 475

    draw_special_key(
        frame,
        "SPACE",
        space_x,
        space_y,
        450,
        selected_key
    )

   
    back_x = 720

    draw_special_key(
        frame,
        "BACK",
        back_x,
        space_y,
        180,
        selected_key
    )


    enter_x = 920

    draw_special_key(
        frame,
        "ENTER",
        enter_x,
        space_y,
        180,
        selected_key
    )


    arrow_y = 555

    draw_arrow_key(
        frame,
        "lt",
        520,
        arrow_y,
        "LEFT",
        selected_key
    )

    draw_arrow_key(
        frame,
        "dn",
        600,
        arrow_y,
        "DOWN",
        selected_key
    )

    draw_arrow_key(
        frame,
        "up",
        680,
        arrow_y,
        "UP",
        selected_key
    )

    draw_arrow_key(
        frame,
        "rt",
        760,
        arrow_y,
        "RIGHT",
        selected_key
    )



def draw_special_key(
    frame,
    text,
    x,
    y,
    width,
    selected_key
):

    if (
        (text == "SPACE" and selected_key == "SPACE")
        or
        (text == "BACK" and selected_key == "BACKSPACE")
        or
        (text == "ENTER" and selected_key == "ENTER")
    ):

        color = (0, 255, 0)
        thickness = -1

    else:

        color = (255, 255, 255)
        thickness = 2

    cv2.rectangle(
        frame,
        (x, y),
        (x + width, y + key_height),
        color,
        thickness
    )

    text_color = (
        (0, 0, 0)
        if thickness == -1
        else color
    )

    cv2.putText(
        frame,
        text,
        (x + 25, y + 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        text_color,
        2
    )




def draw_arrow_key(
    frame,
    symbol,
    x,
    y,
    key_name,
    selected_key
):

    if key_name == selected_key:

        color = (0, 255, 0)
        thickness = -1

    else:

        color = (255, 255, 255)
        thickness = 2

    cv2.rectangle(
        frame,
        (x, y),
        (x + 70, y + 60),
        color,
        thickness
    )

    text_color = (
        (0, 0, 0)
        if key_name == selected_key
        else color
    )

    cv2.putText(
        frame,
        symbol,
        (x + 20, y + 43),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        text_color,
        2
    )



cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


while True:

    ret, frame = cap.read()

    if not ret:

        print("Camera not found!")
        break

    
    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape

   
    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    results = hands.process(rgb)

    selected_key = None

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

    
        index = hand.landmark[8]

    
        thumb = hand.landmark[4]

        index_x = int(index.x * w)
        index_y = int(index.y * h)

        thumb_x = int(thumb.x * w)
        thumb_y = int(thumb.y * h)

        
        selected_key = get_key(
            index_x,
            index_y,
            w
        )

        
        cv2.circle(
            frame,
            (index_x, index_y),
            10,
            (0, 255, 255),
            -1
        )

      
        distance = np.sqrt(
            (index_x - thumb_x) ** 2 +
            (index_y - thumb_y) ** 2
        )

        if distance < 40:

            current_time = time.time()

            if (
                selected_key is not None
                and selected_key != last_key
                and current_time - last_press_time > press_delay
            ):

              

                if selected_key == "SPACE":

                    pyautogui.press("space")

                elif selected_key == "BACKSPACE":

                    pyautogui.press("backspace")

                elif selected_key == "ENTER":

                    pyautogui.press("enter")

                elif selected_key == "UP":

                    pyautogui.press("up")

                elif selected_key == "DOWN":

                    pyautogui.press("down")

                elif selected_key == "LEFT":

                    pyautogui.press("left")

                elif selected_key == "RIGHT":

                    pyautogui.press("right")

                else:

                    pyautogui.press(
                        selected_key.lower()
                    )

                print("Pressed:", selected_key)

                last_key = selected_key
                last_press_time = current_time

        else:

            last_key = None


    draw_keyboard(
        frame,
        selected_key
    )

   
    cv2.putText(
        frame,
        "Move finger + Pinch to press",
        (420, 650),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "ESC = Exit",
        (550, 690),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.imshow(
        "Air Keyboard",
        frame
    )

    
    if cv2.waitKey(1) & 0xFF == 27:
        break



cap.release()
cv2.destroyAllWindows()
hands.close()