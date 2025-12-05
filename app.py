import streamlit as st

# ==========================================
# 1. 頁面基礎設定
# ==========================================
st.set_page_config(
    page_title="數位行銷戰略總部",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CSS 美化樣式
# ==========================================
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3D59;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 3rem;
    }
    .category-label {
        font-size: 1.1rem;
        font-weight: 600;
        color: #444;
        border-left: 5px solid #FF4B4B;
        padding-left: 10px;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    .card-desc {
        font-size: 0.95rem;
        color: #555;
        margin-bottom: 15px;
        height: 60px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 標題區
# ==========================================
st.markdown('<div class="main-header">🚀 數位行銷戰略總部</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Central Command for Marketing Intelligence & Analytics</div>', unsafe_allow_html=True)

# ==========================================
# 4. 工具連結設定 (URL Configuration)
# ==========================================
TOOLS = {
    "market_miner": "https://market-miner-ptfhq6qjq8vhuzaf4nkhre.streamlit.app/",
    "prompt_gen": "https://8wiqqppginsnnhexjv6chv.streamlit.app/",
    "ads_analytics": "https://adsanalyticsforcourse-7vi6zvnjeautmk4qg2s2tl.streamlit.app/",
    "traffic_audit": "https://jfhcpyfqfqp7pwhc6yx2aw.streamlit.app/",
    "web_scraper": "https://competitive-intelligence-snapshot-b5sbxe3kqndxgb89782ofb.streamlit.app/",
    # 這是偽裝目標的連結 (Dennis AI)
    "system_core": "https://dennisisgod-dihjnspatfsqmks2w4me2n.streamlit.app/"
}

# ==========================================
# 5. 儀表板佈局
# ==========================================

# --- 區域 A: 洞察與策略 (Strategy & Insight) ---
st.markdown('<div class="category-label">🧠 策略與洞察 (Strategy & Insight)</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.info("💎 **Market Insight Miner**")
    st.markdown("""
    <div class="card-desc">
    Google Ads 關鍵字數據挖掘、NLP 詞頻分析、藍海紅海市場判讀。<br>
    <small>核心功能：種子關鍵字生成、五維度數據拆解</small>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 前往工具", TOOLS["market_miner"], use_container_width=True, type="primary")

with col2:
    st.info("🎯 **廣告策略 Prompt 生成器**")
    st.markdown("""
    <div class="card-desc">
    競品廣告逆向工程，生成差異化策略與素材 Canvas。<br>
    <small>核心功能：競品分析、差異比對、素材產出指令</small>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 前往工具", TOOLS["prompt_gen"], use_container_width=True, type="primary")

st.markdown("---")

# --- 區域 B: 數據與成效 (Analytics & Audit) ---
st.markdown('<div class="category-label">📊 數據與成效 (Analytics & Audit)</div>', unsafe_allow_html=True)
col3, col4 = st.columns(2)

with col3:
    st.warning("📊 **廣告成效全能分析 (Excel詳盡版)**")
    st.markdown("""
    <div class="card-desc">
    上傳單一 Excel 報表，自動進行 P1D/P7D 雙重監控與趨勢診斷。<br>
    <small>核心功能：緊急異常警示、週環比衰退分析</small>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("📈 前往分析", TOOLS["ads_analytics"], use_container_width=True)

with col4:
    st.warning("⚖️ **流量異常鑑識儀表板**")
    st.markdown("""
    <div class="card-desc">
    偵測幽靈點擊 (Ghost Clicks) 與展示灌水 (Flooding)，建立帳戶正常基準。<br>
    <small>核心功能：異常流量判定、IQR 統計門檻</small>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("🛡️ 前往鑑識", TOOLS["traffic_audit"], use_container_width=True)

st.markdown("---")

# --- 區域 C: 戰略工具 (Tactical Tools) ---
st.markdown('<div class="category-label">🛠️ 戰略工具 (Tactical Tools)</div>', unsafe_allow_html=True)
col5, col6 = st.columns(2)

with col5:
    st.success("🛡️ **網頁情資擷取助手 (Pro+)**")
    st.markdown("""
    <div class="card-desc">
    針對無限捲動網站 (如 FB 廣告檔案庫) 進行深度截圖與 PDF 歸檔。<br>
    <small>核心功能：Playwright 自動滾動、智慧展開、批量截圖</small>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("📥 啟動工具", TOOLS["web_scraper"], use_container_width=True)

with col6:
    # --- 偽裝區域 ---
    # 使用 st.error (紅色) 營造一種 "後台/警告/核心" 的嚴肅感
    # 文字描述非常技術性，讓人以為只是參數設定或日誌
    
    st.error("🔒 **System Kernel Logs (Admin)**")
    st.markdown("""
    <div class="card-desc">
    查看系統核心運行日誌與 API 響應延遲校正。非管理人員請勿操作。<br>
    <small>System Status: 🟢 Stable | Latency: 12ms</small>
    </div>
    """, unsafe_allow_html=True)
    
    # 按鈕文字也很技術性，但連結指向 Dennis AI
    st.link_button("🔧 進入維護終端", TOOLS["system_core"], use_container_width=True, help="點擊進入隱藏入口")

# ==========================================
# 6. 頁尾
# ==========================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #aaa; font-size: 0.8rem;">
    © 2024 Digital Marketing Strategy Hub | Centralized Access Portal
</div>
""", unsafe_allow_html=True)
