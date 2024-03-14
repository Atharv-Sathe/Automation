import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import concurrent.futures


def generateCertificate(name, regNo):
    # certificate = Image.open('./Designs/CertOfPart_Testing.png')
    certificate = Image.open('./Designs/HashTech_Certificate_of_Appriciation.png')

    draw = ImageDraw.Draw(certificate)
    # font = ImageFont.truetype('./Fonts/edwardian-script-itc-bold.ttf', size=100)
    font = ImageFont.truetype('./Fonts/tahomabd.ttf', size=60)

    text = f"Mr./Ms. {name}"
    text_width = font.getlength(text)
    # print(text_width)
    width, height = certificate.size
    # print(width)

    x = (width - text_width) / 2 # Centering the text
    # print(x)
    # x = 810
    y = 785

    draw.text((x, y), text, fill='black', font=font)

    # certificate.show()

    certificate.save(f'./Generated/{regNo}.png')
    certificate.save(f'../SendEmails/Attachments/{regNo}.png')
    certificate.close()
    return name

def main():
    try:
        # csv = pd.read_csv('../CSVs/volunteers.csv')
        csv = pd.read_csv('../CSVs/test.csv')


        nameList = csv['Name'].tolist()
        regList = csv['Registration Number'].tolist()

        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = [executor.submit(generateCertificate, name, regNo) for name, regNo in zip(nameList, regList)]
            for future in concurrent.futures.as_completed(futures):
                name = future.result()
                print(f'Certificate generated for {name}!')

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()