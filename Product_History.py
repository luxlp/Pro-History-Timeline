
import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Timeline Example", layout="wide")

CDN_LOCAL = False
CDN_PATH = 'https://cdn.knightlab.com/libs/timeline3/latest'
CSS_PATH = 'timeline.css'
JS_PATH = 'timeline.js'

SOURCE_TYPE = 'gdocs'
GDOCS_PATH = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRVVm396-LKToqZ5lJNe9hj-8bbv3JHhdNDg5ddrHIDzTn9gvxY-cmLhi5aqW97R03vFq6xcxjQ01tz/pubhtml?gid=0&single=true'
JSON_PATH = 'timeline_nlp.json'

TL_HEIGHT = 800

json_text = ''

if SOURCE_TYPE == 'gdocs':
    source_param = f'"{GDOCS_PATH}"'
    source_block = ''


# load css + js
if CDN_LOCAL:
    with open(CSS_PATH, "r") as f:
        css_text = f.read()
        css_block = f'<head><style>{css_text}</style></head>'

    with open(JS_PATH, "r") as f:
        js_text = f.read()
        js_block  = f'<script type="text/javascript">{js_text}</script>'
else:
    css_block = f'<link title="timeline-styles" rel="stylesheet" href="{CDN_PATH}/css/timeline.css">'
    js_block  = f'<script src="{CDN_PATH}/js/timeline.js"></script>'


# write html block
htmlcode = css_block + ''' 
''' + js_block + '''
    <div id='timeline-embed' style="width: 95%; height: '''+str(TL_HEIGHT)+'''px; margin: 1px;"></div>
    <script type="text/javascript">
        var additionalOptions = {
            start_at_end: false, is_embed:true,
        }
        '''+source_block+'''
        timeline = new TL.Timeline('timeline-embed', '''+source_param+''', additionalOptions);
    </script>'''


# UI sections
data = 'Data'
code = 'HTML Code'
line = 'Visualization'
about = 'About'
view = st.sidebar.radio("View", (line, ), index=0) # code

if view == line:
    # render html
    components.html(htmlcode, height=TL_HEIGHT,)


elif view == code:
    st.subheader(code)
    st.markdown(htmlcode, unsafe_allow_html=False)

