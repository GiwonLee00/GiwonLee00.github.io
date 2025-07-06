---
title: "Multi-modal Knowledge Distillation-based Human Trajectory Forecasting"
collection: publications
category: conferences
# permalink: /publication/2025-06-18-CVPR2025_Multi-modal Knowledge Distillation-based Human Trajectory Forecasting.md
excerpt: 'Jaewoo Jeong, Seohee Lee, Daehee Park, Giwon Lee, Kuk-Jin Yoon'
date: 2025-06-18
venue: 'IEEE / CVF Computer Vision and Pattern Recognition Conference (CVPR)'
# slidesurl: 'http://academicpages.github.io/files/slides1.pdf'
# paperurl: 'https://openaccess.thecvf.com/content/CVPR2025/papers/Jeong_Multi-modal_Knowledge_Distillation-based_Human_Trajectory_Forecasting_CVPR_2025_paper.pdf'
# bibtexurl: 'http://academicpages.github.io/files/bibtex1.bib'
# citation: 'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
---
Pedestrian trajectory forecasting is crucial in various applications such as autonomous driving and mobile robot navigation. In such applications, camera-based perception enables the extraction of additional modalities (human pose, text) to enhance prediction accuracy. Indeed, we find that textual descriptions play a crucial role in integrating additional modalities into a unified understanding. However, online extraction of text requires the use of VLM, which may not be feasible for resource-constrained systems. To address this challenge, we propose a multimodal knowledge distillation framework: a student model with limited modality is distilled from a teacher model trained with full range of modalities. The comprehensive knowledge of a teacher model trained with trajectory, human pose, and text is distilled into a student model using only trajectory or human pose as a sole supplement. In doing so, we separately distill the core locomotion insights from intra-agent multi-modality and inter-agent interaction. Our generalizable framework is validated with two state-of-the-art models across three datasets on both ego-view (JRDB, SIT) and BEV-view (ETH/UCY) setups, utilizing both annotated and VLM-generated text captions. Distilled student models show consistent improvement in all prediction metrics for both full and instantaneous observations, improving up to ∼13%. The code is available at github.com/Jaewoo97/KDTF.