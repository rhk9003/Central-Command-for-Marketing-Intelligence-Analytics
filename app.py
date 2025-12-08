import streamlit as st
import os
import requests
import time

# ==========================================
# 1. 全局設定 (必須在第一行)
# ==========================================
st.set_page_config(
    page_title="數位行銷自動化解決方案 | Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. 核心功能模組
# ==========================================

# --- 模組 A: SEO Prompt 生成器 (內建版) ---
def render_seo_page():
    # 局部樣式
    st.markdown("""
    <style>
        .stTextArea textarea { font-family: monospace; }
        .main-title { font-size: 2rem; font-weight: 700; color: #1e293b; margin-bottom: 10px; }
        .step-header { color: #334155; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-title">📑 SEO 文章戰略：全流程 Prompt 生成器</div>', unsafe_allow_html=True)
    st.markdown("""
    **使用說明：**
    1. 依照順序在**左側**欄位填入你的資訊（或貼上 AI 上一步的回覆）。
    2. **右側**會即時組裝好 Prompt。
    3. 即使欄位留空，右側也會顯示帶有 `[佔位符]` 的 Prompt，方便你直接複製格式。
    """)
    st.divider()

    # 輔助函式
    def get_value(input_val, placeholder_text):
        if input_val.strip():
            return input_val
        return f"[{placeholder_text}]"

    # Step 1
    st.header("Step 1: 產品/計畫解析")
    col1, col2 = st.columns(2)
    with col1:
        p1_input = st.text_area("在此輸入產品/計畫頁面內容：", height=200, placeholder="貼上你的網站文案、產品介紹或是計畫書內容...", key="p1_in")
    with col2:
        st.caption("🚀 複製下方的 Prompt 給 AI：")
        p1_content = get_value(p1_input, "請在此處貼上您的產品/計畫內容")
        prompt1 = f"""幫我解析，這個計畫/產品頁中，提供了什麼?解決了什麼問題?

內容如下：
{p1_content}"""
        st.code(prompt1, language="markdown")

    st.divider()

    # Step 2
    st.header("Step 2: 設定目標 & 主題發想")
    col1, col2 = st.columns(2)
    with col1:
        p2_input = st.text_area("在此輸入 SEO 任務目標：", height=150, placeholder="例如：我想讓找『自動化行銷』的中小企業主看到這篇文章...", key="p2_in")
    with col2:
        st.caption("🚀 複製下方的 Prompt 給 AI：")
        p2_goal = get_value(p2_input, "請在此處描述您的 SEO 任務目標")
        prompt2 = f"""現在我有個任務目標，我要撰寫一篇SEO為目的的文章，利用搜尋結果達成以下目的:

{p2_goal}

為了這個目的，你認為我選關鍵字該鎖定哪些主題?"""
        st.code(prompt2, language="markdown")

    st.divider()

    # Step 3
    st.header("Step 3: 核心關鍵字篩選")
    col1, col2 = st.columns(2)
    with col1:
        p3_input = st.text_area("在此貼上 AI (在 Step 2) 建議的關鍵字/主題清單：", height=150, placeholder="貼上 AI 剛剛產生的主題列表...", key="p3_in")
    with col2:
        st.caption("🚀 複製下方的 Prompt 給 AI：")
        p3_context = get_value(p3_input, "請在此處貼上 AI 建議的關鍵字主題清單")
        prompt3 = f"""根據這些關鍵字，你認為哪些字最適合作為這篇文章操作的核心關鍵字

參考清單：
{p3_context}"""
        st.code(prompt3, language="markdown")

    st.divider()

    # Step 4
    st.header("Step 4: 搜尋意圖 Deep Research")
    col1, col2 = st.columns(2)
    with col1:
        p4_input = st.text_area("在此輸入決定要操作的「核心關鍵字」：", height=150, placeholder="例如：\n關鍵字A\n關鍵字B", key="p4_in")
    with col2:
        st.caption("🚀 複製下方的 Prompt 給 AI：")
        p4_keywords = get_value(p4_input, "請在此處輸入您選定的核心關鍵字清單")
        prompt4 = f"""幫我針對下列關鍵字進行研究(deep research)
我需要知道的事情有，這些關鍵字在搜尋結果中，排名前兩頁的搜尋結果標題都是些什麼?進而幫我推論，搜尋我給的這些字的使用者具有什麼樣的搜尋意圖與資訊需求?

請研究後，幫我彙整每個關鍵字對應的搜尋意圖。

關鍵字清單:
{p4_keywords}"""
        st.code(prompt4, language="markdown")

    st.divider()

    # Step 5
    st.header("Step 5: 文章標題建議")
    col1, col2 = st.columns(2)
    with col1:
        p5_input = st.text_area("在此貼上 AI (在 Step 4) 分析的搜尋意圖/資訊需求：", height=150, placeholder="貼上 AI 分析的意圖結果...", key="p5_in")
    with col2:
        st.caption("🚀 複製下方的 Prompt 給 AI：")
        p5_intent = get_value(p5_input, "請在此處貼上搜尋意圖分析結果")
        prompt5 = f"""請幫我根據我給的資訊/搜尋意圖，給我這篇文章能符合搜尋意圖的標題建議清單

資訊/搜尋意圖參考：
{p5_intent}"""
        st.code(prompt5, language="markdown")

    st.divider()

    # Step 6
    st.header("Step 6: 擬定文章大綱")
    col1, col2 = st.columns(2)
    with col1:
        p6_input = st.text_input("在此輸入您最終選擇的「文章標題」：", placeholder="例如：如何使用 AI 提升工作效率？", key="p6_in")
    with col2:
        st.caption("🚀 複製下方的 Prompt 給 AI：")
        p6_title = get_value(p6_input, "請在此處填入您選擇的文章標題")
        prompt6 = f"""我選擇的標題如下，請根據這個標題幫我擬定這篇文章的大綱
我希望標題能夠都以問題導向呈現。

文章標題: {p6_title}"""
        st.code(prompt6, language="markdown")

    st.divider()

    # Step 7
    st.header("Step 7: 撰寫文章內容")
    col1, col2 = st.columns(2)
    with col1:
        p7_word = st.text_input("文章字數需求：", value="1500字", key="p7_w")
        p7_cta = st.text_input("文章 CTA 連結：", value="https://example.com", key="p7_cta")
        p7_outline = st.text_area("在此貼上確認後的「文章大綱」：", height=200, placeholder="貼上 AI 擬定的大綱...", key="p7_out")
    with col2:
        st.caption("🚀 複製下方的 Prompt 給 AI：")
        p7_content = get_value(p7_outline, "請在此處貼上文章大綱")
        prompt7 = f"""請幫我根據前面訂好的大鋼與標題，撰寫文章內容

文章字數需求: {p7_word}

文章CTA 連結: {p7_cta}

大綱:
{p7_content}"""
        st.code(prompt7, language="markdown")

    st.divider()
    if st.button("🗑️ 清空所有輸入欄位"):
        st.rerun()

# --- 模組 B: 系統中控台 (Dennis AI) ---
def render_console_page():
    # 注入終端機樣式
    st.markdown("""
    <style>
        .stApp { font-family: 'Consolas', 'Monaco', monospace; }
        .stChatMessage { background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
        .badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 700; margin-right: 8px; }
        .badge-sys { background-color: #cbd5e1; color: #334155; }
        .badge-err { background-color: #fee2e2; color: #991b1b; }
        .badge-ok  { background-color: #dcfce7; color: #166534; }
        .badge-ai  { background-color: #dbeafe; color: #1e40af; }
    </style>
    """, unsafe_allow_html=True)

    st.title("🔧 AI Neural Core Console")
    st.caption("System v4.2.0 | Status: 🟡 Standby (Safe Mode)")
    st.divider()

    # 雲端計數邏輯
    COUNTER_NAMESPACE = "dennis_handsome_project" 
    COUNTER_KEY = "handsome_clicks"
    API_URL = "https://api.counterapi.dev/v1"

    def get_count():
        try:
            r = requests.get(f"{API_URL}/{COUNTER_NAMESPACE}/{COUNTER_KEY}/", timeout=1)
            return r.json().get("count", 0) if r.status_code == 200 else 0
        except: return 0

    def inc_count():
        try: requests.get(f"{API_URL}/{COUNTER_NAMESPACE}/{COUNTER_KEY}/up", timeout=1)
        except: pass

    col1, col2 = st.columns(2)
    col1.metric("Latency", "12ms", "-1.4ms")
    col2.metric("Total Restores", f"{get_count()}")

    # 對話邏輯
    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant", 
            "content": """<span class="badge badge-sys">SYSTEM</span> **Initializing...**<br>> Verifying Admin Privileges... <span style="color:#b91c1c;">[FAILED]</span><br><br><span class="badge badge-warn">WARNING</span> System is in Safe Mode. Input **Root Authorization Command** to unlock."""
        }]

    for msg in st.session_state.messages:
        avatar = "🔧" if msg["role"] == "assistant" else "👤"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"], unsafe_allow_html=True)

    if prompt := st.chat_input("Enter system command..."):
        user_msg = f"<span style='color:#64748b;'>$ user@admin:</span> <code>{prompt}</code>"
        st.chat_message("user", avatar="👤").markdown(user_msg, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": user_msg})

        if prompt == "丹尼斯好帥":
            response = """<span class="badge badge-ok">SUCCESS</span> **Authorization Accepted**<br>> Decrypting Core... 100%<br><br><span class="badge badge-ai">AI OUTPUT</span><br>### "謝謝我知道 😎"<br><hr><span class="badge badge-sys">LOG</span> *Session closed.*"""
            st.session_state.messages.append({"role": "assistant", "content": response})
            inc_count()
            st.balloons()
            time.sleep(2)
            st.rerun()
        else:
            response = f"""<span class="badge badge-err">ERROR 403</span> **Command Not Recognized**<br>Hint: **"丹尼斯好帥"**"""
            with st.chat_message("assistant", avatar="🔧"):
                st.markdown(response, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- 模組 C: Portfolio 首頁 (Dashboard) ---
def render_dashboard():
    # CSS 樣式
    st.markdown("""
    <style>
        .main-header { font-size: 2.2rem; font-weight: 700; color: #2c3e50; text-align: center; margin-top: 10px; }
        .sub-header { font-size: 1rem; color: #7f8c8d; text-align: center; margin-bottom: 30px; }
        .category-header { font-size: 1.1rem; font-weight: 700; color: #334155; border-left: 5px solid #3b82f6; padding-left: 10px; margin-top: 30px; margin-bottom: 15px; background: linear-gradient(90deg, #f1f5f9 0%, #ffffff 100%); padding-top: 8px; padding-bottom: 8px; }
        .tool-title { font-size: 1.2rem; font-weight: 700; color: #1e293b; margin-bottom: 8px; }
        .solution-badge { font-size: 0.8rem; color: #047857; background-color: #d1fae5; padding: 4px 8px; border-radius: 4px; display: inline-block; margin-bottom: 12px; font-weight: 600; border: 1px solid #6ee7b7; }
        .solution-badge-blue { font-size: 0.8rem; color: #1e40af; background-color: #dbeafe; padding: 4px 8px; border-radius: 4px; display: inline-block; margin-bottom: 12px; font-weight: 600; border: 1px solid #93c5fd; }
        .desc-text { font-size: 0.95rem; color: #475569; line-height: 1.5; margin-top: 10px; margin-bottom: 15px; min-height: 65px; }
        img { border-radius: 4px; border: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 10px; }
        .admin-zone { background-color: #fef2f2; padding: 15px; border-radius: 8px; border: 1px dashed #ef4444; }
    </style>
    """, unsafe_allow_html=True)

    # 標題區
    st.markdown('<div class="main-header">數位行銷自動化解決方案中心</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Strategic Automation Hub: Enhancing Efficiency & Decision Quality</div>', unsafe_allow_html=True)
    
    with st.expander("ℹ️ 關於此平台 (About)", expanded=True):
        st.info("本平台整合多項自動化工具。請透過左側選單切換至「內建工具」或點擊下方卡片前往「外部模組」。")

    # 圖片與連結設定
    IMG_FILES = {
        "market": "demo_market.png",
        "strategy": "demo_strategy.png",
        "seo": "demo_seo.png", # 必須使用此檔名
        "ads": "demo_ads.png",
        "traffic": "demo_traffic.png",
        "scraper": "demo_scraper.png",
        "console": "demo_console.png"
    }
    
    def show_img(key):
        if IMG_FILES.get(key) and os.path.exists(IMG_FILES.get(key)):
            st.image(IMG_FILES.get(key), use_container_width=True)
        else:
            st.info(f"🖼️ 待上傳截圖：{IMG_FILES.get(key)}")

    # 外部連結
    URLS = {
        "market": "https://market-miner-ptfhq6qjq8vhuzaf4nkhre.streamlit.app/",
        "strategy": "https://8wiqqppginsnnhexjv6chv.streamlit.app/",
        "seo": "https://seo-prompt-builder-jamwdfnwpn36rwsyvznj5s.streamlit.app/", # 更新網址
        "ads": "https://adsanalyticsforcourse-7vi6zvnjeautmk4qg2s2tl.streamlit.app/",
        "traffic": "https://jfhcpyfqfqp7pwhc6yx2aw.streamlit.app/",
        "scraper": "https://competitive-intelligence-snapshot-b5sbxe3kqndxgb89782ofb.streamlit.app/"
    }

    # --- Phase 1: 策略 ---
    st.markdown('<div class="category-header">Phase 1: 市場決策與策略制定</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown('<div class="tool-title">💎 Market Miner</div>', unsafe_allow_html=True)
            st.markdown('<div class="solution-badge">解決：市場調查缺乏量化標準</div>', unsafe_allow_html=True)
            show_img("market")
            st.markdown('<div class="desc-text">將搜尋量轉化為紅藍海策略地圖，識別利基市場。</div>', unsafe_allow_html=True)
            st.link_button("🚀 開啟 (External)", URLS["market"], use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown('<div class="tool-title">🎯 Strategy Decoder</div>', unsafe_allow_html=True)
            st.markdown('<div class="solution-badge">解決：文案缺乏差異化</div>', unsafe_allow_html=True)
            show_img("strategy")
            st.markdown('<div class="desc-text">逆向工程拆解競品策略，生成差異化行銷切角。</div>', unsafe_allow_html=True)
            st.link_button("🚀 開啟 (External)", URLS["strategy"], use_container_width=True)

    with col3:
        with st.container(border=True):
            st.markdown('<div class="tool-title">📑 SEO Prompt Gen</div>', unsafe_allow_html=True)
            st.markdown('<div class="solution-badge-blue">✨ 內建模組 (Built-in)</div>', unsafe_allow_html=True)
            show_img("seo")
            st.markdown('<div class="desc-text">全流程 SEO 戰略生成器，從意圖分析到大綱產出。</div>', unsafe_allow_html=True)
            
            # 兩個按鈕並排
            b_col1, b_col2 = st.columns(2)
            with b_col1:
                if st.button("📂 內建", key="btn_open_seo", use_container_width=True):
                    st.session_state.page_selection = "📑 SEO 戰略生成"
                    st.rerun()
            with b_col2:
                st.link_button("🔗 連結", URLS["seo"], use_container_width=True)

    # --- Phase 2: 成效 ---
    st.markdown('<div class="category-header">Phase 2: 成效優化與風險控制</div>', unsafe_allow_html=True)
    col4, col5 = st.columns(2)
    
    with col4:
        with st.container(border=True):
            st.markdown('<div class="tool-title">📈 Performance Audit</div>', unsafe_allow_html=True)
            show_img("ads")
            st.markdown('<div class="desc-text">自動化成效診斷，比人工更早發現 CPA 異常。</div>', unsafe_allow_html=True)
            st.link_button("📈 查看儀表板", URLS["ads"], use_container_width=True)

    with col5:
        with st.container(border=True):
            st.markdown('<div class="tool-title">⚖️ Traffic Guard</div>', unsafe_allow_html=True)
            show_img("traffic")
            st.markdown('<div class="desc-text">針對廣告帳戶進行健康度檢查，揪出無效流量。</div>', unsafe_allow_html=True)
            st.link_button("🛡️ 執行診斷", URLS["traffic"], use_container_width=True)

    # --- Phase 3: 競情與中控 ---
    st.markdown('<div class="category-header">Phase 3: 競情蒐集與系統維運</div>', unsafe_allow_html=True)
    col6, col7 = st.columns(2)

    with col6:
        with st.container(border=True):
            st.markdown('<div class="tool-title">📥 Web Scraper</div>', unsafe_allow_html=True)
            show_img("scraper")
            st.markdown('<div class="desc-text">自動擷取競品動態資料庫，解決無限捲動難題。</div>', unsafe_allow_html=True)
            st.link_button("📥 啟動擷取", URLS["scraper"], use_container_width=True)

    with col7:
        with st.container(border=True):
            st.markdown('<div class="admin-zone">', unsafe_allow_html=True)
            st.markdown('<div class="tool-title" style="color:#991b1b;">🔒 System Console</div>', unsafe_allow_html=True)
            show_img("console")
            st.markdown('<div class="desc-text">監控 API 連線狀態與錯誤日誌 (偽裝後台)。</div>', unsafe_allow_html=True)
            if st.button("🔧 連線至中控台", key="btn_open_console", use_container_width=True):
                st.session_state.page_selection = "🔧 系統中控 (Dennis AI)"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br><div style='text-align: center; color: #94a3b8; font-size: 0.8rem;'>© 2024 Strategic Automation Portfolio.</div>", unsafe_allow_html=True)

# ==========================================
# 3. 主程式邏輯 (導覽控制器)
# ==========================================

# 初始化頁面狀態
if "page_selection" not in st.session_state:
    st.session_state.page_selection = "🏠 首頁 (Dashboard)"

# 側邊欄導覽
with st.sidebar:
    st.title("🎛️ 導覽中心")
    
    # 使用 radio 按鈕作為導覽，並與 session_state 同步
    selection = st.radio(
        "前往模組：",
        ["🏠 首頁 (Dashboard)", "📑 SEO 戰略生成", "🔧 系統中控 (Dennis AI)"],
        index=["🏠 首頁 (Dashboard)", "📑 SEO 戰略生成", "🔧 系統中控 (Dennis AI)"].index(st.session_state.page_selection)
    )
    
    # 更新 session state
    if selection != st.session_state.page_selection:
        st.session_state.page_selection = selection
        st.rerun()
    
    st.divider()
    st.info("💡 提示：SEO 工具與系統中控台已整合為內建模組，可直接點擊切換。")

# 根據選擇渲染頁面
if st.session_state.page_selection == "🏠 首頁 (Dashboard)":
    render_dashboard()
elif st.session_state.page_selection == "📑 SEO 戰略生成":
    render_seo_page()
elif st.session_state.page_selection == "🔧 系統中控 (Dennis AI)":
    render_console_page()
