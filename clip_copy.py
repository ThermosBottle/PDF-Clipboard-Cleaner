import pyperclip as clp
import keyboard as kb
import re
import time

def replace_char(text_lists):
    repl = ''
    pattern = '(?<=[^A-Za-z])[\r\n\s\u2022\u2013\uf06c\uf070\u27a2\uf0d8\uf645]' 
    for i in range(len(text_lists)):
        text_lists[i] = re.sub(r'[\r\n]',' ', text_lists[i])
        text_lists[i] = re.sub(pattern, repl, text_lists[i])

def clean_clp(texts):
    pattern = '(\r\n..?\r\n.*?)(?=(?:\r\n..?\r\n)|$)' 
    text_lists = re.split(pattern, texts, flags=re.DOTALL)
    #delete None and ''
    text_lists = [text for text in text_lists if text]
    replace_char(text_lists)
    texts = '\r\n'.join(text_lists)
    return texts

if __name__ == '__main__':
    try:
        print(__name__)
        origin_text = ''
        flag = True
        while True:
            event = kb.read_event()
            if event.event_type == kb.KEY_DOWN and event.name == 'esc':
                raise KeyboardInterrupt
            elif event.event_type == kb.KEY_DOWN and event.name == 'up':
                clp.copy('\u2191')
            elif event.event_type == kb.KEY_DOWN and event.name == 'down':
                clp.copy('\u2193')
            elif event.event_type == kb.KEY_DOWN and event.name == 'caps lock':
                flag = not flag 
                if flag:
                    print('Resume...')
                else:
                    print('Pause...') 
            elif flag:
                current_text = clp.paste() 
                #return '' when content of clipboard is image or other binary file 
                if current_text and origin_text != current_text:
                    origin_text = clean_clp(current_text)
                    clp.copy(origin_text)
            time.sleep(0.01)
    finally:
        print('Exiting...')
        time.sleep(0.5)
        exit()