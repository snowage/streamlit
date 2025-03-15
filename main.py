import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit Hello World') # タイトル

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
}) # データフレームの作成

st.write(df)  # データフレームの表示
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100) # データフレームの表示（スタイル付き）

#公式ドキュメントを見に行くと、いろんな表示形式があるので確認する（display data）

st.table(df.style.highlight_max(axis=0)) # データフレームの表示（スタイル付き）

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

st.write('DataFrame') # テキストの表示

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)   # データフレームの作成

st.line_chart(df) # 折れ線グラフの表示
st.area_chart(df) # エリアグラフの表示

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)


st.map(df) # 地図の表示

st.write('Display Image') #画像の表示

img = Image.open('pic/img031.jpg') # 画像の読み込み
st.image(img, caption='sample', use_container_width=True) # 画像の表示



st.write('Interactive Widgets') # ウィジェットの表示

text = st.sidebar.text_input('あなたの趣味を教えてください。') # テキスト入力
'あなたの趣味は', text, 'です。' # テキスト表示

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50) # スライダー
'コンディション：', condition # テキスト表示