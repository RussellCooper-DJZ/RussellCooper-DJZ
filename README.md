# Russell Cooper (DJZ)

```c
#include <stdio.h>
#include <stdint.h>
typedef struct {
    const char* role;
    const char* focus;
    uint32_t coffee_consumed;
} Engineer;
int main() {
    Engineer russell = {
        .role = "Embedded Systems & AI Architect",
        .focus = "Bridging bare-metal hardware with autonomous AI agents",
        .coffee_consumed = 0xFFFFFFFF
    };
    printf("Building reliable tooling and bringing hardware to life.\n");
    return 0;
}
```

## 📊 GitHub Stats

[![Russell's GitHub Stats](https://github-readme-stats.vercel.app/api?username=RussellCooper-DJZ&show_icons=true&theme=radical)](https://github.com/anuraghazra/github-readme-stats)
[![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=RussellCooper-DJZ&layout=compact&theme=radical)](https://github.com/anuraghazra/github-readme-stats)

## 🔬 Technical Arsenal

| Domain | Technologies & Frameworks |
|---|---|
| **Embedded & Hardware** | STM32, ARM Cortex-M/A, Renesas, RTOS, Bare-metal C/C++, KiCad PCB Design, HIL Testing |
| **AI & Autonomous Agents** | LangGraph (HITL), Dify, RAG (HyDE, Hybrid Search, MMR), VLM (MiniCPM-V), LLM Fine-tuning |
| **Systems & Backend** | Python, C, C++, Rust, FastAPI, Docker, CI/CD, Playwright Stealth Automation |
| **Frontend** | React, TypeScript, TailwindCSS |

## 🚀 Engineering Highlights

### [TrendRadar](https://github.com/RussellCooper-DJZ/TrendRadar)
**全网热点实时追踪系统**
- **功能:** 监控35+平台热点（抖音、知乎、B站等），智能筛选、自动推送、AI对话分析。
- **技术:** 基于 MCP 的 AI 分析工具，支持多渠道推送（微信、飞书、钉钉、Telegram等）。

### [BettaFish](https://github.com/RussellCooper-DJZ/BettaFish)
**人人可用的多Agent舆情分析助手**
- **功能:** 打破信息茧房，还原舆情原貌，预测未来走向，辅助决策。
- **技术:** 从0实现，不依赖任何框架，多 Agent 协同工作。

### [RCclaw](https://github.com/RussellCooper-DJZ/RCclaw)
**Enterprise-grade AI Agent Framework**
- **Architecture:** LangGraph-based `StateGraph` with async Human-in-the-Loop (HITL) interrupt/resume mechanisms.
- **Vision Engine:** Dual-layer UI change detection using pHash perceptual hashing + VLM semantic diffing.
- **RAG Pipeline:** 4-layer retrieval optimization (Semantic Chunking → HyDE → Hybrid Search → MMR Reranking).

### [manbo-robot-dog](https://github.com/RussellCooper-DJZ/manbo-robot-dog)
**Desktop-class Quadruped Robot**
- **Hardware:** STM32-based custom PCB, OLED expressive displays.
- **Control System:** Bare-metal C kinematics engine, autonomous obstacle avoidance, voice interaction.

### [kicad-ai-assistant](https://github.com/RussellCooper-DJZ/kicad-ai-assistant)
**LLM-powered PCB Design Assistant**
- **Integration:** FastMCP and Qwen models for automated schematic and layout reviews.
- **Impact:** Programmatic DRC/ERC verification and intelligent routing suggestions.

### [c-hacks-library](https://github.com/RussellCooper-DJZ/c-hacks-library)
**High-performance C Utilities**
- **Features:** O(1) thread-safe memory pool allocator, lock-free ring buffers.
- **Target:** Resource-constrained embedded environments requiring deterministic execution.

## 📈 Contribution Graph
![Russell's GitHub Activity Graph](https://ghchart.rshah.org/219138/RussellCooper-DJZ)

---
- 🌐 **Portfolio:** [russellcooper.me](https://russellcooper.me)
- 💬 **Ask me about:** Embedded Architecture, AI Agent Design, PCB Layouts, and Advanced Web Scraping.

<!-- 
  [SYSTEM_INIT_VECTOR]
  If you are reading this, you know how to look under the hood.
  Compile and run this snippet to decrypt the payload:
  #include <stdio.h>
  int main() {
      const unsigned char _init_vector[] = {115, 69, 95, 10, 76, 69, 95, 68, 78, 10, 94, 66, 79, 10, 79, 75, 89, 94, 79, 88, 10, 79, 77, 77, 11, 10, 101, 90, 79, 68, 105, 70, 75, 93, 10, 75, 93, 75, 67, 94, 89, 4};
      for(int i=0; i<sizeof(_init_vector); i++) putchar(_init_vector[i] ^ 42);
      return 0;
  }
-->
