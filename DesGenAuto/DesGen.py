import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import concurrent.futures


def generateCertificate(name):
    certificate = Image.open('./Designs/CertOfPart_Testing.png')

    draw = ImageDraw.Draw(certificate)
    font = ImageFont.truetype('./Fonts/edwardian-script-itc-bold.ttf', size=100)

    text_width = font.getlength(name)
    # print(text_width)
    width, height = certificate.size
    # print(width)

    x = (width - text_width) / 2 # Centering the text
    # print(x)
    # x = 810
    y = 553

    draw.text((x, y), name, fill='black', font=font)

    # certificate.show()

    certificate.save(f'./Generated/{name}.png')
    return name

def main():
    try:
        # csv = pd.read_csv('../CSVs/volunteers.csv')
        csv = pd.read_csv('../CSVs/test.csv')


        nameList = csv['Name'].tolist()

        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = [executor.submit(generateCertificate, name) for name in nameList]
            for future in concurrent.futures.as_completed(futures):
                name = future.result()
                print(f'Certificate generated for {name}!')

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()