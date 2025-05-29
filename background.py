import ctypes
import os
import time
import random
from PIL import Image, ImageDraw, ImageFont, ImageColor
import requests
from datetime import date
import dotenv

base_dir = f"C://path/to/your/folder"

quotes = [
    {"text": "Those who cannot remember the past are condemned to repeat it.", "attribution": "George Santayana"},
    {"text": "Injustice anywhere is a threat to justice everywhere.", "attribution": "Martin Luther King Jr."},
    {"text": "The only thing we have to fear is fear itself.", "attribution": "Franklin D. Roosevelt"},
    {"text": "Praise be to The LORD,\nThe God of Heaven and Earth", "attribution": ""},
    {"text": "Fear not, for I am with you;\nbe not dismayed, for I am your God;", "attribution": "Isaiah 41:10"},
    {"text": "Do not conform to the patterns of this world,\nbut be transformed by the renewing of your mind", "attribution": "Romans 12:2"},
    {"text": "The LORD is my shepherd", "attribution": "Psalm 23:1"},
    {"text": "Set your mind on things above", "attribution": "Colossians 3:2"},
    {"text": "The grass withers, the flower fades\nbut the Word of our God will stand forever", "attribution": "Isaiah 40:8"},
    {"text": "I lift up mine eyes to the mountains\nwhere does my help come from?\nmy help comes from The LORD\nthe Maker of heaven and earth", "attribution": "Psalm 121:1-2"},
    {"text": "For God so loved the world, He gave his one\nand only Son\nthat whoever believes in Him shall not perish\nbut have eternal life", "attribution": "John 3:16"},
    {"text": "Trust in The Lord with all your heart\nand lean not on your own understanding.", "attribution": "Proverbs 3:5-6"},
    {"text": "Seek first the Kingdom of Heaven and His righteousness\nand all this will be added unto you", "attribution": "Matthew 6:33"},
    {"text": "The word of the Lord is eternal,\nit stands firm in the heavens", "attribution": "Psalm 119:89"},
    {"text": "Our hearts are restless, Lord, until they find their rest in You.", "attribution": "St. Augustine"},
    
    # Sample quotes, add your own
    
]

dotenv.load_dotenv()
canvas_token = os.getenv("CANVAS_KEY")
chat_id = os.getenv("CHAT_ID")
TOKEN = os.getenv("TELEGRAM_TOKEN")
date_output_format_string = "%A, %B %d"

# define Course
class Course:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        
    def __str__(self):
        return f"{self.name}"

def assignments_message():
    message_body = """"""

    message_body += "Upcoming assignments:\n"
    message_body += "\n"

    for course in courses:
        #replace with the URL of your Canvas domain.
        response = requests.get(f"https://canvas.auckland.ac.nz/api/v1/courses/{course.id}/assignments", headers={"Authorization": canvas_token}, params={"order_by": "due_at", "bucket": "upcoming"})

        message_body += str(course)
        message_body += "\n"

        
        response_dictionary = response.json()                    
        for assignment in response_dictionary:

            if assignment['due_at']:
                due_date = date.fromisoformat(assignment['due_at'].split("T")[0])
                message_body += f"    {assignment['name']} - {due_date.strftime(date_output_format_string)}\n"
            
        message_body += "\n"
        message_body += "\n"
        
    return message_body
            
#list courses
courses = [
    Course(120882, "ENGSCI 211"),
    Course(122116, "SOFTENG 281"),
    Course(122117, "SOFTENG 282"),
    Course(121181, "COMPSYS 201")
]
 
class Main:
    def __init__(self) -> None:
        path = base_dir + "\images"
        modified_path = r"\modified_images"
        
        file_index = random.randint(0, len(os.listdir(path)) - 1)
        filename = os.listdir(path)[file_index]
            
        for file in os.listdir(modified_path):
            os.remove(os.path.join(modified_path, file))
            
        quote_index = random.randint(0, len(quotes) - 1)
            
        text = quotes[quote_index]["text"]
        attribution = quotes[quote_index]["attribution"]
        text_overlay = text + "\n" + attribution
            
        f = os.path.join(path, filename)
                    
        if os.path.isfile(f): 
            font = ImageFont.truetype(r"C:\Users\stapp\Downloads\Ancizar_Serif\AncizarSerif-VariableFont_wght.ttf", 100)
            font2 = ImageFont.truetype(r"C:\Users\stapp\Downloads\Ancizar_Serif\AncizarSerif-VariableFont_wght.ttf", 55)

            img = Image.open(f)
            draw = ImageDraw.Draw(img, "RGBA")
            offset = (2, 2)
            
            side_margin = 40
            
            lines = text_overlay.split("\n")
            
            lines.sort(key=lambda x: len(x), reverse=True)
            
            # Calculate bounding box for the quote
            bbox = font.getbbox(lines[0])
            t_height = (bbox[3] - bbox[1] + 20) * (text_overlay.count("\n") + 1)
            t_width = bbox[2] - bbox[0] + side_margin
            draw.rectangle((300 - side_margin/2, 1000, 300 + t_width, 1000 + t_height), fill=(0, 0, 0, 100))

            assignments = assignments_message()
            assignment_lines = assignments.strip().split("\n")
            if assignment_lines:
                assign_bbox = font2.getbbox(max(assignment_lines, key=len))
                assign_height = (assign_bbox[3] - assign_bbox[1] + 10) * len(assignment_lines)
                assign_width = assign_bbox[2] - assign_bbox[0] + side_margin
                draw.rectangle((3000 - side_margin/2, 300, 3000 + assign_width, 300 + assign_height), fill=(0, 0, 0, 100))
        
            draw.text((300 + offset[0], 1000 + offset[1]), text_overlay, font=font, fill="black")
            draw.text((3000 + offset[0], 300 + offset[1]), assignments, font=font2, fill="black")
                        
            draw.text((300, 1000), text_overlay, font=font, stroke_fill="white")
            draw.text((3000, 300), assignments, font=font2, stroke_fill="white")
                
            index = random.randint(0, 1000000)

            # replace with your own path
            img.save(base_dir + f"\\modified_images\\modified_image_{index}.png")
            img.close()
            ctypes.windll.user32.SystemParametersInfoW(20, 0, base_dir + f"\\modified_images\\modified_image_{index}.png", 1 | 2)
application = Main()  
