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

# --- 模組 B: 系統中控台 (Dennis AI - 唯一的內建模組) ---
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
        .desc-text { font-size: 0.95rem; color: #475569; line-height: 1.5; margin-top: 10px; margin-bottom: 15px; min-height: 65px; }
        img { border-radius: 4px; border: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 10px; }
        .admin-zone { background-color: #fef2f2; padding: 15px; border-radius: 8px; border: 1px dashed #ef4444; }
    </style>
    """, unsafe_allow_html=True)

    # 標題區
    st.markdown('<div class="main-header">數位行銷自動化解決方案中心</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Strategic Automation Hub: Enhancing Efficiency & Decision Quality</div>', unsafe_allow_html=True)
    
    with st.expander("ℹ️ 關於此平台 (About)", expanded=True):
        st.info("本平台整合多項自動化工具。請點擊下方卡片按鈕前往各個模組。")

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
        "seo": "https://seo-prompt-builder-jamwdfnwpn36rwsyvznj5s.streamlit.app/", # 更新為您提供的外部網址
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
            st.markdown('<div class="solution-badge">解決：AI 寫作缺乏 SEO 架構</div>', unsafe_allow_html=True)
            show_img("seo")
            st.markdown('<div class="desc-text">全流程 SEO 戰略生成器，從意圖分析到大綱產出。</div>', unsafe_allow_html=True)
            st.link_button("🚀 開啟 (External)", URLS["seo"], use_container_width=True)

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
    
    # 使用 radio 按鈕作為導覽
    selection = st.radio(
        "前往模組：",
        ["🏠 首頁 (Dashboard)", "🔧 系統中控 (Dennis AI)"],
        index=["🏠 首頁 (Dashboard)", "🔧 系統中控 (Dennis AI)"].index(st.session_state.page_selection)
    )
    
    # 更新 session state
    if selection != st.session_state.page_selection:
        st.session_state.page_selection = selection
        st.rerun()
    
    st.divider()
    st.caption("System Status: Online 🟢")

# 根據選擇渲染頁面
if st.session_state.page_selection == "🏠 首頁 (Dashboard)":
    render_dashboard()
elif st.session_state.page_selection == "🔧 系統中控 (Dennis AI)":
    render_console_page()
