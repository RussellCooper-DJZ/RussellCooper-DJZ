<h1 align="center">Russell Cooper (DJZ)</h1>

<p align="center"><strong>Embedded Systems · Edge AI · Autonomous Agents</strong></p>

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

> Building reliable systems where **embedded intelligence**, **autonomous agents**, and **practical developer tooling** meet.

<p align="center">
  <a href="https://russellcooper.me"><img src="https://img.shields.io/badge/Portfolio-russellcooper.me-0F172A?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio" /></a>
  <a href="https://github.com/RussellCooper-DJZ"><img src="https://img.shields.io/badge/GitHub-RussellCooper--DJZ-0F172A?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://github.com/RussellCooper-DJZ?tab=repositories"><img src="https://img.shields.io/badge/Focus-Embedded%20%2B%20AI-0F766E?style=for-the-badge" alt="Focus" /></a>
</p>

---

## Profile at a Glance

| Area | Current focus |
|---|---|
| **Embedded & edge systems** | STM32, ARM Cortex-M/A, Renesas, RTOS, bare-metal C/C++, PCB design and hardware-in-the-loop testing |
| **AI agents & retrieval** | LangGraph, MCP, human-in-the-loop workflows, RAG, hybrid retrieval, VLM-assisted automation |
| **Developer systems** | Python, Rust, FastAPI, Docker, CI/CD, browser automation and observability tooling |
| **Product interfaces** | React, TypeScript and Tailwind CSS |

<p>
  <img src="https://img.shields.io/badge/C-0F766E?style=flat-square&logo=c&logoColor=white" alt="C" />
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=c%2B%2B&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust" />
  <img src="https://img.shields.io/badge/STM32-03234B?style=flat-square&logo=stmicroelectronics&logoColor=white" alt="STM32" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/KiCad-314CB0?style=flat-square&logo=kicad&logoColor=white" alt="KiCad" />
</p>

## Original Projects

> This section intentionally highlights only projects confirmed as original work or user-authored extensions. Repositories that GitHub identifies as forks, mirrors, or reference copies are excluded.

<p align="center">
  <a href="https://github.com/RussellCooper-DJZ/RCclaw"><img src="https://img.shields.io/badge/RCclaw-Agent%20Integration%20Layer-4338CA?style=for-the-badge&logo=typescript&logoColor=white" alt="RCclaw" /></a>
  <a href="https://github.com/RussellCooper-DJZ/manbo-robot-dog"><img src="https://img.shields.io/badge/manbo--robot--dog-STM32%20Robotics-0F766E?style=for-the-badge&logo=stmicroelectronics&logoColor=white" alt="manbo robot dog" /></a>
  <a href="https://github.com/RussellCooper-DJZ/OfficeMind-New"><img src="https://img.shields.io/badge/OfficeMind--New-Local%20AI%20Automation-4338CA?style=for-the-badge&logo=fastapi&logoColor=white" alt="OfficeMind New" /></a>
  <a href="https://github.com/RussellCooper-DJZ/c-hacks-library"><img src="https://img.shields.io/badge/c--hacks--library-C%20Systems%20Tools-0F766E?style=for-the-badge&logo=c&logoColor=white" alt="c hacks library" /></a>
</p>

| Project | Original work focus | Core stack |
|---|---|---|
| [RCclaw](https://github.com/RussellCooper-DJZ/RCclaw) | User-authored multi-channel agent integration layer and messaging extensions, built around the OpenClaw ecosystem. | TypeScript · AI agents |
| [manbo-robot-dog](https://github.com/RussellCooper-DJZ/manbo-robot-dog) | STM32 quadruped robot with voice, sensor safety and DWT profiling compiled out of production firmware by default. | C · STM32 · Resource-aware firmware |
| [OfficeMind-New](https://github.com/RussellCooper-DJZ/OfficeMind-New) | Local office automation with a single-model lite runtime, bounded token budget and fail-closed browser approval gates. | Python · FastAPI · Local AI |
| [c-hacks-library](https://github.com/RussellCooper-DJZ/c-hacks-library) | Low-level C utilities with documented numeric-boundary semantics, GCC/Clang regression checks and sanitizer validation. | C · Systems programming · Testing |

## Engineering Doctrine: Software Efficiency First

> **Extreme capability should come from disciplined software, not compulsory hardware escalation.**
>
> The maintained projects expose resource budgets, eliminate unnecessary resident work, and separate diagnostics from production paths. Claims are tied to source, tests, or board-side measurement protocols rather than decorative badges.

| Repository | Verifiable maintenance outcome |
|---|---|
| [manbo-robot-dog](https://github.com/RussellCooper-DJZ/manbo-robot-dog) | DWT `CYCCNT` instrumentation is compiled out in the default production build (`PERF_PROBE_ENABLE=0`), so performance diagnostics do not reserve runtime resources; a separate measurement build produces board-side evidence. |
| [OfficeMind-New](https://github.com/RussellCooper-DJZ/OfficeMind-New) | A lite profile starts without LangGraph or RAG, uses one configurable local model endpoint, defaults to a bounded 1,024-token response budget, and routes high-risk browser actions to human review before model execution. |
| [c-hacks-library](https://github.com/RussellCooper-DJZ/c-hacks-library) | Numeric boundary defects were corrected and the repository gained a reproducible `make demo test sanitize` quality gate validated locally with GCC and Clang. |
| [RCclaw](https://github.com/RussellCooper-DJZ/RCclaw) | A zero-dependency `check:lite-profile` guard now verifies the existing skip-channel gateway, startup-memory, performance-budget and hotspot checks remain available; the runtime guide treats channels and heavy capabilities as explicit opt-ins. |
| [OfficeMind-Hackathon](https://github.com/RussellCooper-DJZ/OfficeMind-Hackathon) | The router now has a `lite` profile that selects a configurable small text model and fails closed for vision/OCR rather than silently loading an optional large model; its selection rules are shell-tested. |
| [Browser Operator](https://github.com/RussellCooper-DJZ/openclaw-my-browser-operator) | A zero-third-party diagnostic path now isolates `--help`/`check`/`tabs` from Click, aiohttp, Playwright and OpenAI. In 7 cold-process median runs, root help fell from **275.312 ms / 28,076 KB RSS** to **87.031 ms / 14,496 KB RSS** (−68.39% / −48.37%); [raw samples, tests and method](https://github.com/RussellCooper-DJZ/openclaw-my-browser-operator/blob/main/docs/performance.md) are versioned with the code. |
| [manus-skills](https://github.com/RussellCooper-DJZ/manus-skills) | Added a standard-library skill preflight, a resource-budget workflow and a report template, so capability modules are selected and installed individually instead of being loaded wholesale. |
| [fate-symphony](https://github.com/RussellCooper-DJZ/fate-symphony) | A `--lite` renderer bounds preview buffers, caps output at 11,025 Hz and skips optional reverb; the output WAV contract is regression-tested. |
| [fried-chicken-manager](https://github.com/RussellCooper-DJZ/fried-chicken-manager) | Profit and sensitivity calculations now have a standard-library CLI that runs without Tkinter or Matplotlib; input validation and 25-scenario analysis are regression-tested. |

## Original Project Catalogue

### 1. AI Agents, Automation & Developer Workflows

[![RCclaw](https://img.shields.io/badge/RCclaw-Agent%20Integration%20Layer-4338CA?style=flat-square&logo=typescript&logoColor=white)](https://github.com/RussellCooper-DJZ/RCclaw)
[![OfficeMind-New](https://img.shields.io/badge/OfficeMind--New-Office%20Agent-4338CA?style=flat-square&logo=python&logoColor=white)](https://github.com/RussellCooper-DJZ/OfficeMind-New)
[![OfficeMind-Hackathon](https://img.shields.io/badge/OfficeMind--Hackathon-Automation%20Agent-4338CA?style=flat-square&logo=python&logoColor=white)](https://github.com/RussellCooper-DJZ/OfficeMind-Hackathon)
[![manus-skills](https://img.shields.io/badge/manus--skills-Reusable%20AI%20Skills-4338CA?style=flat-square&logo=python&logoColor=white)](https://github.com/RussellCooper-DJZ/manus-skills)
[![Browser Operator](https://img.shields.io/badge/Browser%20Operator-CDP%20Integration-4338CA?style=flat-square&logo=googlechrome&logoColor=white)](https://github.com/RussellCooper-DJZ/openclaw-my-browser-operator)

This group presents user-authored agent integrations, office-automation experiments, reusable AI skills and browser-session tooling. Each showcased project now defines an explicit capability budget rather than treating all models, browsers, channels or retrieval components as mandatory runtime work.

### 2. Embedded Systems, Robotics & Systems Programming

[![manbo-robot-dog](https://img.shields.io/badge/manbo--robot--dog-STM32%20Robotics-0F766E?style=flat-square&logo=stmicroelectronics&logoColor=white)](https://github.com/RussellCooper-DJZ/manbo-robot-dog)
[![c-hacks-library](https://img.shields.io/badge/c--hacks--library-C%20Systems%20Tools-0F766E?style=flat-square&logo=c&logoColor=white)](https://github.com/RussellCooper-DJZ/c-hacks-library)

This group focuses on original work in microcontroller-based robotics and C-oriented systems tooling.

### 3. Product Experiments & Creative Computing

[![fate-symphony](https://img.shields.io/badge/fate--symphony-Generative%20Audio-B45309?style=flat-square&logo=python&logoColor=white)](https://github.com/RussellCooper-DJZ/fate-symphony)
[![fried-chicken-manager](https://img.shields.io/badge/fried--chicken--manager-Profit%20Analytics-B45309?style=flat-square&logo=python&logoColor=white)](https://github.com/RussellCooper-DJZ/fried-chicken-manager)

These repositories showcase original experiments in generative computing and practical analytics, each with a functional low-resource path that avoids external libraries or graphical processing when it is not required.

## Live Metrics

<p align="center">
  <a href="https://github.com/RussellCooper-DJZ"><img src="https://visitor-badge.laobi.icu/badge?page_id=RussellCooper-DJZ.RussellCooper-DJZ&left_text=Profile%20Views&left_color=0F172A&right_color=0F766E" alt="Profile views" /></a>
</p>

> The visitor badge records profile-page requests. It is a page-view counter rather than a unique-visitor measure.

## GitHub Activity

<p align="center">
  <a href="https://github.com/RussellCooper-DJZ">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=RussellCooper-DJZ&amp;show_icons=true&amp;hide_border=true&amp;bg_color=0F172A&amp;title_color=5EEAD4&amp;text_color=CBD5E1&amp;icon_color=2DD4BF" />
      <source media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)" srcset="https://github-readme-stats.vercel.app/api?username=RussellCooper-DJZ&amp;show_icons=true&amp;hide_border=true&amp;bg_color=FFFFFF&amp;title_color=0F766E&amp;text_color=334155&amp;icon_color=0F766E" />
      <img height="165" src="https://github-readme-stats.vercel.app/api?username=RussellCooper-DJZ&amp;show_icons=true&amp;hide_border=true&amp;bg_color=FFFFFF&amp;title_color=0F766E&amp;text_color=334155&amp;icon_color=0F766E" alt="Russell's GitHub statistics" />
    </picture>
  </a>
  <a href="https://git.io/streak-stats">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com/?user=RussellCooper-DJZ&amp;hide_border=true&amp;background=0F172A&amp;ring=2DD4BF&amp;fire=FBBF24&amp;currStreakNum=F8FAFC&amp;sideNums=F8FAFC&amp;currStreakLabel=CBD5E1&amp;sideLabels=CBD5E1&amp;dates=94A3B8" />
      <source media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)" srcset="https://streak-stats.demolab.com/?user=RussellCooper-DJZ&amp;hide_border=true&amp;background=FFFFFF&amp;ring=0F766E&amp;fire=F59E0B&amp;currStreakNum=0F172A&amp;sideNums=0F172A&amp;currStreakLabel=475569&amp;sideLabels=475569&amp;dates=94A3B8" />
      <img height="165" src="https://streak-stats.demolab.com/?user=RussellCooper-DJZ&amp;hide_border=true&amp;background=FFFFFF&amp;ring=0F766E&amp;fire=F59E0B&amp;currStreakNum=0F172A&amp;sideNums=0F172A&amp;currStreakLabel=475569&amp;sideLabels=475569&amp;dates=94A3B8" alt="GitHub contribution streak" />
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://github.com/RussellCooper-DJZ?tab=repositories">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=RussellCooper-DJZ&amp;layout=compact&amp;hide_border=true&amp;bg_color=0F172A&amp;title_color=5EEAD4&amp;text_color=CBD5E1" />
      <source media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=RussellCooper-DJZ&amp;layout=compact&amp;hide_border=true&amp;bg_color=FFFFFF&amp;title_color=0F766E&amp;text_color=334155" />
      <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=RussellCooper-DJZ&amp;layout=compact&amp;hide_border=true&amp;bg_color=FFFFFF&amp;title_color=0F766E&amp;text_color=334155" alt="Top languages" />
    </picture>
  </a>
</p>

![Russell's GitHub activity graph](https://ghchart.rshah.org/219138/RussellCooper-DJZ)

---

**Portfolio:** [russellcooper.me](https://russellcooper.me)  
**Ask me about:** embedded architecture, AI agent design, PCB layouts and advanced web automation.

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
