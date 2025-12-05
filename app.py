import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches # 引入 patches 以防萬一
import numpy as np
import io

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
# 2. 核心技術：動態模擬畫面生成器 (Mockup Generator)
# ==========================================
@st.cache_data
def create_mockup(tool_type):
    """
    根據工具類型，動態繪製一張模擬圖表
    """
    # 設定繪圖風格
    plt.style.use('bmh') 
    fig, ax = plt.subplots(figsize=(6, 3.5))
    fig.patch.set_facecolor('#f8fafc') # 背景色與卡片一致
    ax.set_facecolor('#ffffff')
    
    # -------------------------------------------
    # A. 市場探勘 (紅藍海散佈圖)
    # -------------------------------------------
    if tool_type == "market":
        np.random.seed(42)
        x = np.random.randint(100, 5000, 30) # 搜尋量
        y = np.random.randint(10, 100, 30)   # 競爭度
        colors = ['#ef4444' if i > 60 else '#3b82f6' for i in y]
        
        ax.scatter(x, y, c=colors, s=x/10, alpha=0.6, edgecolors='white')
        ax.set_title("Market Opportunity Map (Red vs Blue Ocean)", fontsize=10, color='#334155')
        ax.set_xlabel("Search Volume (Monthly)", fontsize=8)
        ax.set_ylabel("Competition Index", fontsize=8)
        ax.grid(True, linestyle='--', alpha=0.3)
        ax.text(4000, 20, "Blue Ocean\nOpportunity", fontsize=9, color='#2563eb', ha='center')

    # -------------------------------------------
    # B. 策略解構 (文字雲/架構圖模擬) -> [修復點]
    # -------------------------------------------
    elif tool_type == "strategy":
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        # 定義方塊：(x, y, w, h, color, text)
        rects = [
            (1, 6, 8, 3, "#dbeafe", "Competitor Analysis\n(Angle / Hook)"),
            (1, 3.5, 3.5, 2, "#d1fae5", "Gap\nDiscovery"),
            (5.5, 3.5, 3.5, 2, "#fee2e2", "Psychological\nTrigger"),
            (1, 0.5, 8, 2.5, "#f3f4f6", "Generated Script Canvas\n[Headline] [Body] [CTA]")
        ]
        
        for x, y, w, h, c, t in rects:
            # [修復]: 移除了 rx=0.5 參數，確保舊版 matplotlib 也能執行
            rect = patches.Rectangle((x, y), w, h, facecolor=c, edgecolor='#94a3b8', alpha=0.8)
            ax.add_patch(rect)
            ax.text(x + w/2, y + h/2, t, ha='center', va='center', fontsize=9, color='#475569', weight='bold')
        
        ax.set_title("Strategy Reverse Engineering Framework", fontsize=10, color='#334155')

    # -------------------------------------------
    # C. 成效監控 (趨勢折線圖)
    # -------------------------------------------
    elif tool_type == "ads":
        days = np.arange(1, 8)
        cpa = [150, 145, 160, 280, 290, 155, 140]
        ctr = [1.2, 1.3, 1.2, 0.8, 0.7, 1.1, 1.3]
        
        ax2 = ax.twinx()
        ax.plot(days, cpa, color='#ef4444', marker='o', label='CPA', linewidth=2)
        ax2.plot(days, ctr, color='#3b82f6', marker='s', linestyle='--', label='CTR', linewidth=2)
        
        ax.annotate('Anomaly Alert!', xy=(4, 280), xytext=(2.5, 320),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1), fontsize=8, color='#991b1b')
        
        ax.set_title("Performance Trend: CPA Spike Detection", fontsize=10, color='#334155')
        ax.set_xlabel("Day (Past 7 Days)", fontsize=8)
        ax.set_ylabel("CPA ($)", color='#ef4444', fontsize=8)
        ax2.set_ylabel("CTR (%)", color='#3b82f6', fontsize=8)
        
    # -------------------------------------------
    # D. 流量鑑識 (IQR 離群值圖)
    # -------------------------------------------
    elif tool_type == "audit":
        x_norm = np.random.normal(50, 10, 50)
        y_norm = np.random.normal(3, 0.5, 50)
        x_ghost = np.random.normal(80, 5, 5)
        y_ghost = np.random.normal(0.5, 0.1, 5)
        
        ax.scatter(x_norm, y_norm, c='#10b981', alpha=0.5, label='Normal')
        ax.scatter(x_ghost, y_ghost, c='#ef4444', marker='x', s=100, label='Ghost Clicks')
        
        ax.axhline(y=1.0, color='#f59e0b', linestyle='--', alpha=0.7)
        ax.text(20, 1.1, "Threshold (IQR Limit)", fontsize=7, color='#d97706')
        
        ax.set_title("Traffic Quality Forensics (Ghost Clicks)", fontsize=10, color='#334155')
        ax.set_xlabel("Impressions", fontsize=8)
        ax.set_ylabel("CTR (%)", fontsize=8)

    # -------------------------------------------
    # E. 網頁擷取 (流程示意圖)
    # -------------------------------------------
    elif tool_type == "scraper":
        ax.axis('off')
        nodes = [
            (1.5, 5, "Target URLs\n(List)", '#f1f5f9'),
            (4, 5, "Auto-Scroll\nEngine", '#3b82f6'),
            (6.5, 5, "PDF/ZIP\nArchive", '#fcd34d')
        ]
        
        ax.arrow(2.5, 5, 0.5, 0, head_width=0.3, head_length=0.2, fc='#94a3b8', ec='#94a3b8')
        ax.arrow(5, 5, 0.5, 0, head_width=0.3, head_length=0.2, fc='#94a3b8', ec='#94a3b8')
        
        for x, y, t, c in nodes:
            circle = patches.Circle((x, y), 1, color=c, alpha=0.8)
            ax.add_patch(circle)
            ax.text(x, y, t, ha='center', va='center', fontsize=8, weight='bold', color='#334155')
            
        ax.set_ylim(2, 8)
        ax.set_xlim(0, 8)
        ax.set_title("Automated Archiving Process Workflow", fontsize=10, color='#334155')

    # -------------------------------------------
    # F. 系統終端 (黑底綠字)
    # -------------------------------------------
    elif tool_type == "console":
        ax.set_facecolor('#0f172a')
        fig.patch.set_facecolor('#0f172a')
        ax.axis('off')
        
        terminal_text = """
> SYSTEM_DIAGNOSTIC_TOOL v2.4
-----------------------------
[INFO] API Connection .... OK (12ms)
[INFO] Data Pipeline ..... STABLE
[WARN
