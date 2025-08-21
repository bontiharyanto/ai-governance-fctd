# 🧭 Research Framework (DPPT ↔ Frameworks ↔ Regulasi)

Dokumen ini menampilkan diagram visual kerangka penelitian yang menyelaraskan **DPPT** dengan **TOGAF, COBIT, NIST AI RMF** dan **UU PDP, POJK, STRANAS AI**.

## Diagram (Mermaid)

```mermaid
flowchart TD
  %% ====== Groups ======
  subgraph Drivers["External Drivers & Standards"]
    A1["TOGAF"]:::fw
    A2["COBIT 2019"]:::fw
    A3["NIST AI RMF"]:::fw
    A4["UU PDP"]:::reg
    A5["POJK"]:::reg
    A6["STRANAS AI"]:::reg
  end

  subgraph DPPT["DPPT Core"]
    D["DATA"]:::pill
    PR["PROCESS"]:::pill
    P["PEOPLE"]:::pill
    T["TECHNOLOGY"]:::pill
    PO["POLICY"]:::pill
  end

  subgraph Eval["Evaluation & Outcomes"]
    E["Evaluation<br/>(NIST Metrics • COBIT Maturity • TOGAF Fit)"]:::eval
    O["Outcomes<br/>• AI Governance Maturity<br/>• Compliance Roadmap<br/>• Business Impact"]:::out
  end

  %% ====== Mappings ======
  A1 --> D & PR & P & T & PO
  A2 --> D & PR & P & T & PO
  A3 --> D & PR & P & T & PO
  A4 --> D & PO
  A5 --> PR & T & PO
  A6 --> P & PO

  D & PR & P & T & PO --> E --> O

  %% ====== Styles ======
  classDef fw fill:#e8f1ff,stroke:#2f7de1,stroke-width:1.5px,color:#173b6b;
  classDef reg fill:#fff1e6,stroke:#e18a2f,stroke-width:1.5px,color:#5a3410;
  classDef pill fill:#eef8ef,stroke:#2ea44f,stroke-width:1.5px,color:#0f4d1f;
  classDef eval fill:#f5f0ff,stroke:#6e40c9,stroke-width:1.5px,color:#3b1d91;
  classDef out fill:#f0fbff,stroke:#0aa2c0,stroke-width:1.5px,color:#035766;
```

