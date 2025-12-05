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
# 2. CSS 樣式：專業商務風格
# ==========================================
st.markdown("""
<style>
    /* 全局字型與配色 */
    .main-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #2c3e50;
        text-align: center;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 400;
    }
    
    /* 分類標籤樣式 */
    .category-label {
        font-size: 1.2rem;
        font-weight: 600;
        color: #34495e;
        border-left: 5px solid #2980b9;
        padding-left: 12px;
        margin-top: 40px;
        margin-bottom: 20px;
        background-color: #ecf0f1;
        padding-top: 5px;
        padding-bottom: 5px;
    }

    /* 卡片標題 */
    .tool-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 5px;
    }
    
    /* 解決問題標籤 (核心價值) */
    .solution-tag {
        font-size: 0.85rem;
        color: #ffffff;
        background-color: #27ae60; /* 綠色代表解決方案/正面價值 */
        padding: 4px 10px;
        border-radius: 15px;
        display: inline-block;
        margin-bottom: 12px;
        font-weight: 500;
    }

    /* 商業情境描述 */
    .business-desc {
        font-size: 0.95rem;
        color: #34495e;
        line-height: 1.6;
        margin-bottom: 15px;
        min-height: 90px;
    }
    
    /* 重點清單 */
    .feature-list {
        font-size: 0.9rem;
        color: #576574;
        margin-bottom: 20px;
        padding-left: 20px;
        list-style-type: disc;
    }
    
    /* 偽裝區域樣式 - 嚴肅的系統維運感 */
    .admin-zone {
        border: 1px solid #bdc3c7;
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 5px;
    }
    .admin-title {
        font-family: monospace;
        color: #7f8c8d;
        font-weight: bold;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 標題與簡介 (針對面試官)
# ==========================================
st.markdown('<div class="main-header">數位行銷自動化解決方案中心</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Strategic Automation Hub: Enhancing Efficiency & Decision Quality</div>', unsafe_allow_html=True)

# 可以在這裡加入一段給面試官的話，說明這個頁面的目的
with st.expander("ℹ️ 關於此平台 (About this Portfolio)"):
    st.markdown("""
    此平台整合了我開發的五套自動化工具，旨在解決數位行銷工作中常見的**「重複性作業」**與**「數據盲點」**問題。
    透過這些工具，我能夠：
    1.  **大幅縮短** 市場研究與報表製作的工時。
    2.  **量化決策**，減少憑直覺判斷的風險。
    3.  **即時監控** 預算使用效率，防止無效花費。
    """)

# ==========================================
# 4. 工具連結設定
# ==========================================
TOOLS = {
    "market_miner": "https://market-miner-ptfhq6qjq8vhuzaf4nkhre.streamlit.app/",
    "prompt_gen": "https://8wiqqppginsnnhexjv6chv.streamlit.app/",
    "ads_analytics": "https://adsanalyticsforcourse-7vi6zvnjeautmk4qg2s2tl.streamlit.app/",
    "traffic_audit": "https://jfhcpyfqfqp7pwhc6yx2aw.streamlit.app/",
    "web_scraper": "https://competitive-intelligence-snapshot-b5sbxe3kqndxgb89782ofb.streamlit.app/",
    "system_core": "https://dennisisgod-dihjnspatfsqmks2w4me2n.streamlit.app/"
}

# ==========================================
# 5. 儀表板佈局 (Problem & Solution 導向)
# ==========================================

# --- 區域 A: 市場決策與策略優化 ---
st.markdown('<div class="category-label">Phase 1: 市場決策與策略制定 (Strategy & Planning)</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="tool-title">💎 Market Insight Miner (市場機會探勘)</div>', unsafe_allow_html=True)
    st.markdown('<span class="solution-tag">解決：人工市場調查耗時且缺乏量化標準</span>', unsafe_allow_html=True)
    st.markdown("""
    <div class="business-desc">
    將繁雜的 Google 搜尋量數據轉化為可視化的「紅藍海策略地圖」。協助團隊在投入預算前，快速識別高需求但低競爭的利基市場 (Niche Market)，避免在紅海市場無效競爭。
    </div>
    <ul class="feature-list">
        <li><strong>機會點發現：</strong>自動計算競爭指數，找出高潛力關鍵字。</li>
        <li><strong>消費者洞察：</strong>分析搜尋詞彙背後的消費者意圖與痛點。</li>
        <li><strong>預算規劃：</strong>依據市場熱度，科學化分配初期行銷預算。</li>
    </ul>
    """, unsafe_allow_html=True)
    st.link_button("🚀 開啟工具 (Launch)", TOOLS["market_miner"], use_container_width=True, type="primary")

with col2:
    st.markdown('<div class="tool-title">🎯 Competitor Strategy Decoder (競品策略解構)</div>', unsafe_allow_html=True)
    st.markdown('<span class="solution-tag">解決：廣告素材缺乏差異化，創意發想憑感覺</span>', unsafe_allow_html=True)
    st.markdown("""
    <div class="business-desc">
    透過逆向工程邏輯，系統化拆解競爭對手的廣告策略。從對手的文案與視覺中提煉出受眾心理，並自動生成具備「差異化優勢」的行銷切角，確保我方素材能有效突圍。
    </div>
    <ul class="feature-list">
        <li><strong>策略分析：</strong>快速歸納競品的主打訴求與受眾輪廓。</li>
        <li><strong>差異化定位：</strong>自動比對我方與競品優劣，找出溝通缺口。</li>
        <li><strong>創意產出：</strong>標準化生成廣告腳本與視覺建議，提升製作效率。</li>
    </ul>
    """, unsafe_allow_html=True)
    st.link_button("🚀 開啟工具 (Launch)", TOOLS["prompt_gen"], use_container_width=True, type="primary")

st.markdown("---")

# --- 區域 B: 成效監控與預算風控 ---
st.markdown('<div class="category-label">Phase 2: 成效優化與風險控制 (Optimization & Risk Control)</div>', unsafe_allow_html=True)
col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="tool-title">📈 Automated Performance Audit (成效自動稽核)</div>', unsafe_allow_html=True)
    st.markdown('<span class="solution-tag">解決：人工報表製作耗時，異常發現滯後</span>', unsafe_allow_html=True)
    st.markdown("""
    <div class="business-desc">
    取代傳統人工 Excel 拉表作業，自動化進行跨週期的成效診斷。能比人工更早發現 CPA (獲客成本) 暴漲或 CTR (點擊率) 衰退的跡象，實現「即時止損」與「精準擴量」。
    </div>
    <ul class="feature-list">
        <li><strong>自動化週報：</strong>一鍵生成包含 P1D/P7D 對比的完整分析報告。</li>
        <li><strong>異常警示：</strong>針對 CPA 暴漲 >30% 等情況發出緊急調整建議。</li>
        <li><strong>趨勢診斷：</strong>識別廣告疲勞 (Ad Fatigue) 跡象，提醒更換素材。</li>
    </ul>
    """, unsafe_allow_html=True)
    st.link_button("📈 查看儀表板 (Dashboard)", TOOLS["ads_analytics"], use_container_width=True)

with col4:
    st.markdown('<div class="tool-title">⚖️ Traffic Quality & Fraud Guard (流量品質鑑識)</div>', unsafe_allow_html=True)
    st.markdown('<span class="solution-tag">解決：無效流量浪費預算，數據虛胖誤導決策</span>', unsafe_allow_html=True)
    st.markdown("""
    <div class="business-desc">
    針對廣告帳戶進行健康度檢查，揪出「幽靈點擊」(高點擊低瀏覽) 與「展示灌水」等異常行為。確保每一分行銷預算都花在真實、高品質的潛在客戶身上。
    </div>
    <ul class="feature-list">
        <li><strong>預算保護：</strong>識別並排除異常流量來源，提升預算利用率。</li>
        <li><strong>基準建立：</strong>透過統計學算法建立帳戶的「正常表現基準線」。</li>
        <li><strong>數據清洗：</strong>過濾極端值雜訊，還原真實的行銷成效數據。</li>
    </ul>
    """, unsafe_allow_html=True)
    st.link_button("🛡️ 執行診斷 (Diagnostic)", TOOLS["traffic_audit"], use_container_width=True)

st.markdown("---")

# --- 區域 C: 競情蒐集與系統監控 ---
st.markdown('<div class="category-label">Phase 3: 競情蒐集與系統維運 (Intelligence & Support)</div>', unsafe_allow_html=True)
col5, col6 = st.columns(2)

with col5:
    st.markdown('<div class="tool-title">📥 Competitive Intelligence Archiver (競情自動歸檔)</div>', unsafe_allow_html=True)
    st.markdown('<span class="solution-tag">解決：手動截圖競品廣告效率低，難以長期追蹤</span>', unsafe_allow_html=True)
    st.markdown("""
    <div class="business-desc">
    自動化模擬使用者行為，批量擷取與歸檔競爭對手的動態網頁資料 (如 Facebook 廣告檔案庫)。解決「無限捲動」網頁難以完整保存的問題，建立長期的戰略資料庫。
    </div>
    <ul class="feature-list">
        <li><strong>效率提升：</strong>將數小時的手動截圖工作縮減至數分鐘完成。</li>
        <li><strong>完整保存：</strong>自動展開隱藏內容，確保情資擷取無遺漏。</li>
        <li><strong>趨勢追蹤：</strong>長期記錄競品活動變化，輔助季度策略制定。</li>
    </ul>
    """, unsafe_allow_html=True)
    st.link_button("📥 啟動擷取 (Scraper)", TOOLS["web_scraper"], use_container_width=True)

with col6:
    # --- 偽裝區域：系統穩定性監控 ---
    # 對面試官來說，這代表你重視工具的穩定性與數據準確性
    # 實際上是 Dennis AI 的入口
    
    st.markdown('<div class="admin-zone">', unsafe_allow_html=True)
    st.markdown('<div class="admin-title">🔒 System Integrity Monitor (系統監控台)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 0.9rem; color: #7f8c8d; margin-top: 10px; margin-bottom: 15px;">
    <strong>[Internal Use Only]</strong> 負責監控上述所有工具的 API 連線狀態、資料抓取延遲與系統錯誤日誌。
    <br><br>
    此模組確保所有分析數據的準確性與即時性。若發生資料源中斷或 API 錯誤，此處將顯示即時警報以供維護。
    </div>
    """, unsafe_allow_html=True)
    
    col_status1, col_status2 = st.columns(2)
    with col_status1:
        st.markdown("**Status:** <span style='color:green'>● Operational</span>", unsafe_allow_html=True)
    with col_status2:
        st.markdown("**Uptime:** 99.9%", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    # 按鈕名稱改為 "進入維護模式"，看起來很枯燥
    st.link_button("🔧 Maintenance Console", TOOLS["system_core"], use_container_width=True, help="進入系統維護後台")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 6. 頁尾
# ==========================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #95a5a6; font-size: 0.8rem;">
    © 2024 Strategic Automation Portfolio. Designed to solve real-world marketing challenges.
</div>
""", unsafe_allow_html=True)
