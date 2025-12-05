import streamlit as st

# ==========================================
# 1. 頁面基礎設定
# ==========================================
st.set_page_config(
    page_title="數位行銷自動化解決方案 | Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed" 
)

# ==========================================
# 2. CSS 樣式：強制對齊與卡片優化
# ==========================================
st.markdown("""
<style>
    /* 1. 全局字型優化 */
    .main-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: #2c3e50;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 1rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 30px;
        font-weight: 400;
    }
    
    /* 2. 聯絡資訊區塊優化 (置中卡片) */
    .contact-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        margin-bottom: 25px;
        color: #475569;
        font-size: 1rem;
    }
    .contact-card a {
        color: #2563eb;
        font-weight: 600;
        text-decoration: none;
    }
    .contact-card a:hover {
        text-decoration: underline;
    }

    /* 3. 分類標題美化 */
    .category-header {
        font-size: 1.1rem;
        font-weight: 700;
        color: #334155;
        border-left: 5px solid #3b82f6;
        padding-left: 10px;
        margin-top: 30px;
        margin-bottom: 15px;
        background: linear-gradient(90deg, #f1f5f9 0%, #ffffff 100%);
        padding-top: 8px;
        padding-bottom: 8px;
    }

    /* 4. 工具卡片內容排版 (關鍵：高度對齊) */
    .tool-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 8px;
        white-space: nowrap; /* 標題不換行 */
        overflow: hidden;
        text-overflow: ellipsis;
    }
    
    .solution-badge {
        font-size: 0.8rem;
        color: #047857;
        background-color: #d1fae5;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-bottom: 12px;
        font-weight: 600;
        border: 1px solid #6ee7b7;
    }

    /* 關鍵 CSS：設定最小高度，確保左右兩邊的文字區塊一樣高，按鈕才會對齊 */
    .desc-text {
        font-size: 0.95rem;
        color: #475569;
        line-height: 1.5;
        margin-bottom: 15px;
        min-height: 85px; /* 強制文字區塊高度 */
    }
    
    .feature-list {
        font-size: 0.85rem;
        color: #64748b;
        margin-bottom: 15px;
        padding-left: 18px;
        min-height: 70px; /* 強制列表區塊高度 */
    }
    
    /* 5. 偽裝區域樣式 */
    .admin-zone {
        background-color: #fef2f2;
        padding: 15px;
        border-radius: 8px;
        border: 1px dashed #ef4444;
        min-height: 200px; /* 與左邊卡片等高 */
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 權限控制 (Demo Access)
# ==========================================
is_unlocked = False

with st.sidebar:
    st.title("🔐 Demo Access") # 修改：Client -> Demo
    st.info("部分進階分析模組需輸入 Demo Key 才能解鎖完整功能。")
    
    password = st.text_input("Enter Access Key", type="password", placeholder="請輸入 Demo Key")
    
    if password == "790420":
        is_unlocked = True
        st.success("✅ 驗證成功：Demo 功能已解鎖")
    elif password:
        st.error("❌ Key 錯誤")
    
    st.divider()
    # 修改：System Status -> Demo Environment
    st.caption("Demo Environment: 🟢 Online")

# ==========================================
# 4. 標題與簡介
# ==========================================
st.markdown('<div class="main-header">數位行銷自動化解決方案中心</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Strategic Automation Hub: Enhancing Efficiency & Decision Quality</div>', unsafe_allow_html=True)

# 聯絡資訊卡片
st.markdown("""
<div class="contact-card">
    👋 專案負責人：<strong>Rh K</strong>
    &nbsp;&nbsp;<span style="color:#cbd5e1">|</span>&nbsp;&nbsp;
    📧 Email：<a href="mailto:rhk9903@gmail.com">rhk9903@gmail.com</a>
</div>
""", unsafe_allow_html=True)

# --- 關於此平台 (包含核心免責聲明) ---
with st.expander("ℹ️ 關於此平台 (About this Portfolio)", expanded=True):
    # ⚠️ 這裡加入了您指定的免責聲明
    st.warning("""
    **⚠️ 免責聲明 (Disclaimer)**
    
    本平台為個人 Portfolio Demo，所有邏輯以泛用模型 (Generic Models) 與模擬數據 (Synthetic Data) 設計，
    **不涉及任何實際客戶或前公司機密資料**。僅供技術展示與邏輯驗證使用。
    """)
    
    st.markdown("""
    此平台整合了我開發的五套自動化工具，旨在解決數位行銷工作中常見的**「重複性作業」**與**「數據盲點」**問題。
    透過這些工具，我能夠：
    1.  **大幅縮短** 市場研究與報表製作的工時。
    2.  **量化決策**，減少憑直覺判斷的風險。
    3.  **即時監控** 預算使用效率，防止無效花費。
    
    *(註：部分核心功能需解鎖 Demo Access 才能操作)*
    """)

# ==========================================
# 5. 工具連結設定
# ==========================================
TOOLS = {
    "market_miner": "https://market-miner-ptfhq6qjq8vhuzaf4nkhre.streamlit.app/",
    "prompt_gen": "https://8wiqqppginsnnhexjv6chv.streamlit.app/",
    "ads_analytics": "https://adsanalyticsforcourse-7vi6zvnjeautmk4qg2s2tl.streamlit.app/",
    "traffic_audit": "https://jfhcpyfqfqp7pwhc6yx2aw.streamlit.app/",
    "web_scraper": "https://competitive-intelligence-snapshot-b5sbxe3kqndxgb89782ofb.streamlit.app/",
    "system_core": "https://dennisisgod-dihjnspatfsqmks2w4me2n.streamlit.app/"
}

# ---------------------------------------------
# 核心邏輯：防右鍵偷看 (Security Logic)
# ---------------------------------------------
def render_secure_btn(url, btn_key, label="🚀 開啟工具 (Launch)"):
    """
    如果解鎖：渲染 st.link_button (帶有 href)
    如果鎖定：渲染 st.button (無 href)，防止右鍵複製網址
    """
    if is_unlocked:
        st.link_button(
            label=label, 
            url=url, 
            type="primary", 
            use_container_width=True
        )
    else:
        # 普通 button 沒有 href 屬性，最安全
        if st.button("🔒 Demo Restricted", key=btn_key, type="secondary", use_container_width=True):
            st.toast("🚫 請輸入 Demo Key 以解鎖試用功能", icon="🔒")

# ==========================================
# 6. 儀表板佈局 (卡片式整齊排版)
# ==========================================

# --- Phase 1: 市場決策 ---
st.markdown('<div class="category-header">Phase 1: 市場決策與策略制定</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown('<div class="tool-title">💎 Market Insight Miner</div>', unsafe_allow_html=True)
        st.markdown('<div class="solution-badge">解決：市場調查耗時且缺乏量化標準</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="desc-text">
        將繁雜的搜尋量數據轉化為可視化的「紅藍海策略地圖」。協助團隊在投入預算前，快速識別高需求但低競爭的利基市場。
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <ul class="feature-list">
            <li>機會點發現：計算競爭指數</li>
            <li>消費者洞察：分析意圖與痛點</li>
            <li>預算規劃：科學化分配預算</li>
        </ul>
        """, unsafe_allow_html=True)
        render_secure_btn(TOOLS["market_miner"], "btn_market")

with col2:
    with st.container(border=True):
        st.markdown('<div class="tool-title">🎯 Competitor Strategy Decoder</div>', unsafe_allow_html=True)
        st.markdown('<div class="solution-badge">解決：廣告缺乏差異化，創意憑感覺</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="desc-text">
        透過逆向工程拆解競品策略。從對手文案中提煉受眾心理，自動生成具備「差異化優勢」的行銷切角，確保素材突圍。
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <ul class="feature-list">
            <li>策略分析：歸納主打訴求</li>
            <li>差異化定位：找出溝通缺口</li>
            <li>創意產出：標準化腳本建議</li>
        </ul>
        """, unsafe_allow_html=True)
        render_secure_btn(TOOLS["prompt_gen"], "btn_prompt")

# --- Phase 2: 成效監控 ---
st.markdown('<div class="category-header">Phase 2: 成效優化與風險控制</div>', unsafe_allow_html=True)
col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.markdown('<div class="tool-title">📈 Automated Performance Audit</div>', unsafe_allow_html=True)
        st.markdown('<div class="solution-badge">解決：人工報表製作耗時，異常滯後</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="desc-text">
        取代人工 Excel 拉表，自動進行成效診斷。能比人工更早發現 CPA 暴漲或 CTR 衰退跡象，實現「即時止損」。
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <ul class="feature-list">
            <li>自動化週報：生成 P1D/P7D 報告</li>
            <li>異常警示：偵測 CPA 異常暴漲</li>
            <li>趨勢診斷：識別廣告疲勞跡象</li>
        </ul>
        """, unsafe_allow_html=True)
        render_secure_btn(TOOLS["ads_analytics"], "btn_ads", label="📈 查看儀表板 (Dashboard)")

with col4:
    with st.container(border=True):
        st.markdown('<div class="tool-title">⚖️ Traffic Quality & Fraud Guard</div>', unsafe_allow_html=True)
        st.markdown('<div class="solution-badge">解決：無效流量浪費預算與誤導</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="desc-text">
        針對廣告帳戶進行健康度檢查，揪出「幽靈點擊」與「展示灌水」行為。確保預算花在真實的高品質潛在客戶身上。
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <ul class="feature-list">
            <li>預算保護：排除異常流量來源</li>
            <li>基準建立：統計算法建立基準線</li>
            <li>數據清洗：還原真實成效數據</li>
        </ul>
        """, unsafe_allow_html=True)
        render_secure_btn(TOOLS["traffic_audit"], "btn_traffic", label="🛡️ 執行診斷 (Diagnostic)")

# --- Phase 3: 競情與系統 ---
st.markdown('<div class="category-header">Phase 3: 競情蒐集與系統維運</div>', unsafe_allow_html=True)
col5, col6 = st.columns(2)

with col5:
    with st.container(border=True):
        st.markdown('<div class="tool-title">📥 Competitive Intelligence</div>', unsafe_allow_html=True)
        st.markdown('<div class="solution-badge">解決：手動截圖效率低，難以追蹤</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="desc-text">
        模擬使用者行為，自動擷取競爭對手的動態網頁資料 (如 FB 廣告檔案庫)。解決「無限捲動」問題，建立戰略資料庫。
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <ul class="feature-list">
            <li>效率提升：自動化批量歸檔</li>
            <li>完整保存：自動展開隱藏內容</li>
            <li>趨勢追蹤：輔助季度策略制定</li>
        </ul>
        """, unsafe_allow_html=True)
        render_secure_btn(TOOLS["web_scraper"], "btn_scraper", label="📥 啟動擷取 (Scraper)")

with col6:
    # 偽裝區域 (Dennis AI 入口)
    with st.container(border=True):
        st.markdown('<div class="admin-zone">', unsafe_allow_html=True)
        # 修改：Internal Only -> Demo Module
        st.markdown('<div class="tool-title" style="color:#991b1b;">🔒 System Integrity Monitor</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="font-size: 0.85rem; color: #7f8c8d; margin-bottom: 15px; line-height:1.5;">
        <strong>[Demo Module]</strong> 監控 API 連線狀態與錯誤日誌。<br>
        確保分析數據準確性。若發生資料源中斷，此處將顯示警報。
        </div>
        """, unsafe_allow_html=True)
        
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.markdown("**Status:** <span style='color:green'>● Operational</span>", unsafe_allow_html=True)
        with col_s2:
            st.markdown("**Latency:** 12ms", unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 修改：Maintenance Console -> Demo Console
        st.link_button("🔧 Demo Console", TOOLS["system_core"], use_container_width=True, help="System Admin")
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 7. 頁尾
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #94a3b8; font-size: 0.8rem;">
    © 2024 Strategic Automation Portfolio. Designed to solve real-world marketing challenges.
</div>
""", unsafe_allow_html=True)
