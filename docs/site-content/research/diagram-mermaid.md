## Diagram (Mermaid) — Horizontal (LR)

```mermaid
flowchart LR
  subgraph Drivers["🧭 External Drivers & Standards"]
    A1["TOGAF"]:::fw
    A2["COBIT 2019"]:::fw
    A3["NIST AI RMF"]:::fw
    A4["UU PDP"]:::reg
    A5["POJK"]:::reg
    A6["STRANAS AI"]:::reg
  end
  subgraph DPPT["🧩 DPPT Core"]
    D["📊 DATA"]:::pill
    PR["⚙️ PROCESS"]:::pill
    P["👥 PEOPLE"]:::pill
    T["🖥️ TECHNOLOGY"]:::pill
    PO["📜 POLICY"]:::pill
  end
  subgraph Eval["📐 Evaluation"]
    E["NIST Metrics · COBIT Maturity · TOGAF Fit"]:::eval
  end
  subgraph Out["🏁 Outcomes"]
    O1["AI Governance Maturity"]:::out
    O2["Compliance Roadmap"]:::out
    O3["Business Impact"]:::out
  end
  A1 --> D & PR & P & T & PO
  A2 --> D & PR & P & T & PO
  A3 --> D & PR & P & T & PO
  A4 --> D & PO
  A5 --> PR & T & PO
  A6 --> P & PO
  D & PR & P & T & PO --> E
  E --> O1 & O2 & O3
  classDef fw  fill:#e8f1ff,stroke:#2f7de1,stroke-width:1.5px,color:#173b6b;
  classDef reg fill:#fff1e6,stroke:#e18a2f,stroke-width:1.5px,color:#5a3410;
  classDef pill fill:#eef8ef,stroke:#2ea44f,stroke-width:1.5px,color:#0f4d1f;
  classDef eval fill:#f5f0ff,stroke:#6e40c9,stroke-width:1.5px,color:#3b1d91;
  classDef out fill:#f0fbff,stroke:#0aa2c0,stroke-width:1.5px,color:#035766;
  style Drivers rx:8, ry:8
  style DPPT    rx:8, ry:8
  style Eval    rx:8, ry:8
  style Out     rx:8, ry:8

