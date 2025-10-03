from PIL import Image

inp = "/mnt/giwon/GiwonLee00.github.io/assets/img/publication_preview/IROS2025_prev_original.png"
out = "/mnt/giwon/GiwonLee00.github.io/assets/img/publication_preview/IROS2025.png"

img = Image.open(inp).convert("RGBA")         # 원본 유지, 알파 포함
white_bg = Image.new("RGB", img.size, "white")# 원본과 같은 크기의 흰 배경
white_bg.paste(img, mask=img.split()[3])      # 알파 채널로 합성 (투명→흰색)
white_bg.save(out)                            # PNG/JPG 모두 OK (여기선 PNG)
print("saved to", out)
