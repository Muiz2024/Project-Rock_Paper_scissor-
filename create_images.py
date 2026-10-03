import os
from PIL import Image, ImageDraw, ImageFont

IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(IMG_DIR, exist_ok=True)

SIZE = 200


def get_font(size):
    for path in [
        "C:\\Windows\\Fonts\\arialbd.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\segoeui.ttf",
    ]:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()


def make_rock():
    img = Image.new("RGBA", (SIZE, SIZE), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    d.ellipse([20, 40, 180, 170], fill=(120, 120, 130), outline=(60, 60, 70), width=4)
    d.ellipse([40, 30, 80, 70], fill=(120, 120, 130), outline=(60, 60, 70), width=3)
    d.ellipse([85, 25, 125, 65], fill=(120, 120, 130), outline=(60, 60, 70), width=3)
    d.ellipse([130, 30, 170, 70], fill=(120, 120, 130), outline=(60, 60, 70), width=3)
    img.save(os.path.join(IMG_DIR, "rock.png"))


def make_paper():
    img = Image.new("RGBA", (SIZE, SIZE), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([40, 20, 160, 180], fill=(245, 245, 245), outline=(80, 80, 80), width=4)
    for y in range(55, 170, 25):
        d.line([55, y, 145, y], fill=(120, 120, 120), width=3)
    img.save(os.path.join(IMG_DIR, "paper.png"))


def make_scissor():
    img = Image.new("RGBA", (SIZE, SIZE), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    d.ellipse([20, 110, 90, 180], outline=(80, 80, 80), width=6)
    d.ellipse([110, 110, 180, 180], outline=(80, 80, 80), width=6)
    d.line([75, 115, 170, 20], fill=(80, 80, 80), width=6)
    d.line([125, 115, 30, 20], fill=(80, 80, 80), width=6)
    d.line([75, 115, 100, 100], fill=(80, 80, 80), width=6)
    d.line([125, 115, 100, 100], fill=(80, 80, 80), width=6)
    img.save(os.path.join(IMG_DIR, "scissor.png"))


def make_question():
    img = Image.new("RGBA", (SIZE, SIZE), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    d.ellipse([10, 10, 190, 190], fill=(240, 240, 240), outline=(150, 150, 150), width=4)
    f = get_font(110)
    d.text((70, 35), "?", fill=(80, 80, 80), font=f)
    img.save(os.path.join(IMG_DIR, "question.png"))


def make_logo():
    size = 256
    img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    d.ellipse([4, 4, size - 4, size - 4], fill=(41, 128, 185), outline=(31, 97, 141), width=6)
    d.ellipse([55, 45, 115, 105], fill=(120, 120, 130), outline=(70, 70, 80), width=3)
    d.rectangle([140, 50, 205, 115], fill=(245, 245, 245), outline=(80, 80, 80), width=3)
    for y in range(62, 110, 12):
        d.line([148, y, 197, y], fill=(120, 120, 120), width=2)
    d.ellipse([55, 140, 95, 180], outline=(80, 80, 80), width=4)
    d.ellipse([155, 140, 195, 180], outline=(80, 80, 80), width=4)
    d.line([85, 145, 165, 120], fill=(80, 80, 80), width=4)
    d.line([165, 145, 85, 120], fill=(80, 80, 80), width=4)
    f = get_font(34)
    d.text((78, 195), "RPS", fill=(255, 255, 255), font=f)
    img.save(os.path.join(IMG_DIR, "logo.png"))
    img.resize((32, 32), Image.LANCZOS).save(os.path.join(IMG_DIR, "logo.ico"), format="ICO")


make_rock()
make_paper()
make_scissor()
make_question()
make_logo()
print("Images created in:", IMG_DIR)