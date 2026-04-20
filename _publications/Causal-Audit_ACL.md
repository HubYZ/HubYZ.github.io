---
title: "Causal-Audit: Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction"
collection: publications
author: Su LAN and Xuefei Yin and Yanming Zhu and Alan Wee-Chung Liew
booktitle: Findings of the Association for Computational Linguistics, ACL 2026
abstract: Causal and intervention-based question answering is fundamental to advancing large language models (LLMs) toward reasoning beyond surface-level correlations and understanding underlying causal mechanisms. However, existing LLM-based methods often rely on implicit language-level reasoning, resulting in opaque causal assumptions, unverifiable reasoning paths, and fragile predictions under complex interventions, particularly in context-free settings. In this paper, we propose an explicit and auditable causal reasoning framework for context-free intervention-based question answering. Our method formulates causal inference as structured reasoning over an explicit causal graph through four modular stages, rather than implicit end-to-end prediction. A key innovation is a target-aware causal graph construction strategy that treats the target variable as a core constraint during graph expansion, effectively suppressing irrelevant variables, spurious causal relations, and reasoning noise. We further introduce a path-level causal evidence aggregation mechanism that combines multiple causal paths while modeling both reinforcing and counteracting effects, enabling robust decision-making beyond single-chain reasoning. Extensive experiments on three benchmarks demonstrate that our framework consistently outperforms existing LLM-based methods while providing interpretable and auditable causal reasoning traces.
permalink: /publication/Causal-Audit_ACL
date: 2026-4-15
citation: '@inproceedings{Su2026findings, title={Findings of the Association for Computational Linguistics: ACL 2025}, author={Su LAN and Xuefei Yin and Yanming Zhu and Alan Wee-Chung Liew}, booktitle={Findings of the Association for Computational Linguistics: ACL 2026}, year={2026} }'
---
[[PDF]](https://HubYZ.github.io/files/Causal-Audit_ACL.pdf)
