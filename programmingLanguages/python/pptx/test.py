import pptx
from pptx import Presentation
from pptx.util import Inches, Cm, Pt
import pptx.util
import glob
import scipy.misc

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
# save
prs.save('test.pptx')
