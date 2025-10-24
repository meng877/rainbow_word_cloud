from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ====== 可改动点 ======
font_path = 'C:/Windows/Fonts/msyh.ttc'      # Win 雅黑
# font_path = '/System/Library/Fonts/PingFang.ttc'  # mac 苹黑
bg_color  = 'black'
color_map = 'prism'
width_px  = 1080
height_px = 720
# ======================

with open('keywords.txt', encoding='utf-8') as f:
    text = f.read()

wc = WordCloud(
    width=width_px,
    height=height_px,
    background_color=bg_color,
    colormap=color_map,
    font_path=font_path,
    relative_scaling=0.5,
    prefer_horizontal=0.8
).generate(text)

plt.figure(figsize=(width_px/100, height_px/100))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.savefig('rainbow_wallpaper.png', dpi=300)
print('✅ 彩虹弹幕图已生成:rainbow_wallpaper.png')
