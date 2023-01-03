from PIL import Image, ImageFont, ImageDraw
import pandas as pd

template_path = "Final Lanyard EECS.png"


font = ImageFont.truetype(r"FontsFree-Net-norwester.ttf", 50)

#load name list
data = pd.read_csv('./data/student list - CMED.csv')
data_name = data[['Name']]

for i in range(len(data_name)):
    word = data_name['Name'][i].split()
    num_words = len(word)

    if num_words > 3:
        new_name = word[:2]
        combine_name = " ".join(new_name)

        template = Image.open(template_path)
    
        # Create an ImageDraw object to draw on the template
        draw = ImageDraw.Draw(template)

        # Measure the size of the text
        text_width, text_height = draw.textsize(combine_name, font=font)

        # Calculate the position of the text
        text_x = (template.width - text_width) / 2
        text_y = (720 - text_height) / 2

        # Draw the name on the template
        draw.text((text_x, text_y), combine_name, font=font, fill=(255, 255, 255))

        # Save the modified template as a new image
        output_path = "./output/cmed/lanyard_{}.png".format(i+1)
        template.save(output_path)

    else:
      
        template = Image.open(template_path)
    
        # Create an ImageDraw object to draw on the template
        draw = ImageDraw.Draw(template)

        # Measure the size of the text
        text_width, text_height = draw.textsize(data_name['Name'][i], font=font)

        # Calculate the position of the text
        text_x = (template.width - text_width) / 2
        text_y = (720 - text_height) / 2

        # Draw the name on the template
        draw.text((text_x, text_y), data_name['Name'][i], font=font, fill=(255, 255, 255))

        # Save the modified template as a new image
        output_path = "./output/CMED/lanyard_{}.png".format(i+1)
        template.save(output_path)

      







