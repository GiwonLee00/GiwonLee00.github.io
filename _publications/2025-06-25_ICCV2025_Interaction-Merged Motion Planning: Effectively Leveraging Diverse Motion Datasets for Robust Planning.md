---
title: "Interaction-Merged Motion Planning: Effectively Leveraging Diverse Motion Datasets for Robust Planning"
collection: publications
category: conferences
# permalink: /publication/2025-06-18-CVPR2025_Multi-modal Knowledge Distillation-based Human Trajectory Forecasting.md
excerpt: 'Giwon Lee\*, Wooseong Jeong\*, Daehee Park, Jaewoo Jeong, Kuk-Jin Yoon (\* denotes equal contribution)'
date: 2025-06-25
venue: 'International Conference on Computer Vision (ICCV)'
# slidesurl: 'http://academicpages.github.io/files/slides1.pdf'
# paperurl: 'https://openaccess.thecvf.com/content/CVPR2025/papers/Jeong_Multi-modal_Knowledge_Distillation-based_Human_Trajectory_Forecasting_CVPR_2025_paper.pdf'
# bibtexurl: 'http://academicpages.github.io/files/bibtex1.bib'
# citation: 'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
---
Motion planning is a crucial component of autonomous robot driving. While various trajectory datasets exist, effectively utilizing them for a target domain remains challenging due to differences in agent interactions and environmental characteristics. Conventional approaches, such as domain adaptation or ensemble learning, leverage multiple source datasets but suffer from domain imbalance, catastrophic forgetting, and high computational costs. To address these challenges, we propose Interaction-Merged Motion Planning (IMMP), a novel approach that leverages parameter checkpoints trained on different domains during adaptation to the target domain. IMMP follows a two-step process: pre-merging to capture agent behaviors and interactions, sufficiently extracting diverse information from the source domain, followed by merging to construct an adaptable model that efficiently transfers diverse interactions to the target domain. Our method is evaluated on various planning benchmarks and models, demonstrating superior performance compared to conventional approaches.
