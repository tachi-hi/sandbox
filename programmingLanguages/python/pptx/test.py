import pptx
from pptx import Presentation
from pptx.util import Inches, Cm, Pt
import pptx.util
import glob
import scipy.misc
#from sympy import preview


# LaTeX rendering
# see http://stackoverflow.com/questions/9818279/render-equation-to-png-file-using-python
from io import StringIO, BytesIO
import matplotlib.pyplot as plt
def render_latex(formula, filename, fontsize=12, dpi=300, format_='svg'):
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, '${}$'.format(formula), fontsize=fontsize)
    buffer_ = BytesIO()
    fig.savefig(buffer_, dpi=dpi, transparent=True, format=format_, bbox_inches='tight', pad_inches=0.0)
    plt.close(fig)
    img_bytes = buffer_.getvalue()
    with open(filename, 'wb') as image_file:
        image_file.write(img_bytes)


prs = Presentation()

#-------
# title
slide = prs.slides.add_slide(prs.slide_layouts[0]) # 0 = title
slide.shapes.title.text = "Python-pptx テスト"
slide.placeholders[1].text = "テストテスト"

#-------
# ordinary page
slide = prs.slides.add_slide(prs.slide_layouts[1]) # 1 = bullet slide
slide.shapes.title.text = "普通のページ"
tf = slide.shapes.placeholders[1].text_frame
tf.text = "中身"
p = tf.add_paragraph()
p.text = "次"
p.level = 2
p = tf.add_paragraph()
txt = "ひたすら長い長文で埋めた場合プレースホルダーはどのように振る舞うのか？"
txt = txt + "+".join([str(i) for i in range(1,150)]) + "=??\nこのように、自動的には収まらない。（もっともバージョンアップで変わるかもしれない）"
p.text = txt
p.level = 2

#-------
# blank page
slide = prs.slides.add_slide(prs.slide_layouts[5]) # 5 = blank except title
slide.shapes.title.text = "空のページとテキストボックス"

tb = slide.shapes.add_textbox(left=Inches(1),top=Inches(3),height=Inches(2),width=Inches(5))
tb1 = tb.text_frame.add_paragraph()
tb1.text = "テキストボックス"
tb1.font.size = Pt(40)

tb = slide.shapes.add_textbox(left=Inches(5),top=Inches(5),height=Inches(2),width=Inches(5))
tb2 = tb.text_frame.add_paragraph()
tb2.text = "テキストボックスその2"
tb2.font.size = Pt(72)

#-------
# latex
slide = prs.slides.add_slide(prs.slide_layouts[5]) # 5 = blank except title
slide.shapes.title.text = "LaTeX img via matplotlib"

render_latex(
    r'\frac{1}{\sqrt{2 \pi \sigma^2}} \exp\left(- \frac{(x - \mu^2)}{2\sigma^2}\right)',
    "gaussian.png", fontsize=10, dpi=1000, format_='png')

img = 2.0
top, left = 1.5, 0.5
pic = slide.shapes.add_picture("gaussian.png",left=Inches(left), top=Inches(top), height=Inches(img))


render_latex(
    r'\frac{1}{(2 \pi)^{1/2} |\Sigma|^{d/2}} \exp\left(- \frac{1}{2}(\mathbf{x} - \mathbf{m})^T\Sigma^{-1}(\mathbf{x} - \mathbf{m})\right)',
    "gaussian.png", fontsize=10, dpi=1000, format_='png')

img = 1.0
top, left = 5.0, 0.5
pic = slide.shapes.add_picture("gaussian.png",left=Inches(left), top=Inches(top), height=Inches(img))

#-------
# save
prs.save('test.pptx')
