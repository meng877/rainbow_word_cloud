from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

# ====== 可改动点 ======
font_path = 'C:/Windows/Fonts/msyh.ttc'      # Win 雅黑
# font_path = '/System/Library/Fonts/PingFang.ttc'  # mac 苹黑
bg_color  = 'white'
color_map = 'RdPu'
width_px  = 1080
height_px = 720
mask_path = 'mask.png'  # 把你的白色底 mask 放在工作目录，或修改为实际路径
# ======================

with open('keywords.txt', encoding='utf-8') as f:
    text = f.read()

# 如果存在 mask，则加载并处理，使文字只出现在 mask 的白色部分
mask = None
if os.path.exists(mask_path):
    try:
        img = Image.open(mask_path).convert('L')
        # 调整为目标尺寸（最近邻避免抗锯齿改变边界）
        img = img.resize((width_px, height_px), Image.NEAREST)
        arr = np.array(img)
        # 二值化：把亮色 (白色) 部分设为 255（允许绘字），暗色设为 0
        bin_mask = np.where(arr > 127, 255, 0).astype(np.uint8)
        mask = bin_mask
        print(f'ℹ️ 使用 mask: {mask_path}（已调整到 {width_px}x{height_px} 并二值化）')
    except Exception as e:
        print('⚠️ 无法加载或处理 mask，已忽略：', e)
        mask = None

wc_kwargs = dict(
    width=width_px,
    height=height_px,
    background_color=bg_color,
    colormap=color_map,
    font_path=font_path,
    relative_scaling=0.5,
    prefer_horizontal=0.8
)
if mask is not None:
    wc_kwargs['mask'] = mask

wc = WordCloud(**wc_kwargs).generate(text)

plt.figure(figsize=(width_px/100, height_px/100))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.savefig('rainbow_wallpaper.png', dpi=300)
print('✅ 彩虹弹幕图已生成：rainbow_wallpaper.png')
