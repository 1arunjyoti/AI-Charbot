import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
   api_key="<YOUR_API_KEY>",
)

def is_last_message_from_sender(chat_log, sender_name="person name"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

# Step 1: Click on the chrome icon at coordinates (796, 746)
pyautogui.click(796, 746)
time.sleep(1)

while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (438, 169) to (1335, 644) to select the text
    pyautogui.moveTo(438, 169)
    pyautogui.dragTo(1335, 644, duration=1.0, button='left')

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    # Step 3: Copy the selected text to the clipboard
    time.sleep(1)
    pyautogui.click(1327, 196)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chatHistory = pyperclip.paste()

    # Step 5: Print the text to the console
    print(chatHistory)

    if is_last_message_from_sender(chatHistory):

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Naruto who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das: "},
            {"role": "user", "content": chatHistory}
        ]
        )

        response =completion.choices[0].message.content
        pyperclip.copy(response)

        #click at the position to deselect the text
        pyautogui.click(628, 693)
        time.sleep(1)

        #paste the response
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        
        pyautogui.press('enter')